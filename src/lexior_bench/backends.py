"""Model backends: Ollama (default), OpenAI, Anthropic, Hugging Face local.

Backends are selected by spec string "provider:model"; a bare model name
defaults to Ollama. OpenAI/Anthropic/HF SDKs are optional extras and imported
lazily.
"""

from __future__ import annotations

import os
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

import httpx

DEFAULT_OLLAMA_BASE_URL = "http://localhost:11434"


@dataclass
class ModelResponse:
    text: str
    latency_s: float
    raw: dict = field(default_factory=dict, repr=False)


class ModelBackend(ABC):
    """A model that turns a prompt into a completion."""

    spec: str = ""

    @abstractmethod
    def generate(self, prompt: str, *, temperature: float = 0.0, max_tokens: int = 512) -> ModelResponse:
        """Generate a completion for the prompt."""


class OllamaBackend(ModelBackend):
    def __init__(self, model: str, base_url: str | None = None, timeout: float = 240.0):
        self.model = model
        self.base_url = (
            base_url or os.environ.get("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL)
        ).rstrip("/")
        self.timeout = timeout
        self.spec = f"ollama:{model}"

    def _post(self, payload: dict) -> dict:
        response = httpx.post(
            f"{self.base_url}/api/chat", json=payload, timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()

    def generate(self, prompt: str, *, temperature: float = 0.0, max_tokens: int = 512) -> ModelResponse:
        t0 = time.perf_counter()
        data = self._post(
            {
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}],
                "stream": False,
                "options": {"temperature": temperature, "num_predict": max_tokens},
            }
        )
        return ModelResponse(
            text=data["message"]["content"].strip(),
            latency_s=round(time.perf_counter() - t0, 3),
            raw=data,
        )


class OpenAIBackend(ModelBackend):
    def __init__(self, model: str):
        try:
            import openai
        except ImportError as e:
            raise ImportError(
                "The openai SDK is not installed. Run: uv sync --extra openai"
            ) from e
        self.client = openai.OpenAI()  # OPENAI_API_KEY from env
        self.model = model
        self.spec = f"openai:{model}"

    def generate(self, prompt: str, *, temperature: float = 0.0, max_tokens: int = 512) -> ModelResponse:
        t0 = time.perf_counter()
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=temperature,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
        )
        return ModelResponse(
            text=(response.choices[0].message.content or "").strip(),
            latency_s=round(time.perf_counter() - t0, 3),
            raw=response.model_dump(),
        )


class AnthropicBackend(ModelBackend):
    def __init__(self, model: str):
        try:
            import anthropic
        except ImportError as e:
            raise ImportError(
                "The anthropic SDK is not installed. Run: uv sync --extra anthropic"
            ) from e
        self.client = anthropic.Anthropic()  # ANTHROPIC_API_KEY from env
        self.model = model
        self.spec = f"anthropic:{model}"

    def generate(self, prompt: str, *, temperature: float = 0.0, max_tokens: int = 512) -> ModelResponse:
        # Current Claude models (Opus 4.7+) reject sampling params with a 400,
        # so temperature is intentionally not passed.
        t0 = time.perf_counter()
        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
        )
        if response.stop_reason == "refusal":
            text = ""
        else:
            text = "".join(
                block.text for block in response.content if block.type == "text"
            ).strip()
        return ModelResponse(
            text=text,
            latency_s=round(time.perf_counter() - t0, 3),
            raw=response.model_dump(),
        )


class HuggingFaceBackend(ModelBackend):
    """Local transformers inference (loads the model from the Hub once)."""

    def __init__(self, model: str):
        try:
            import torch  # noqa: F401
            from transformers import AutoModelForCausalLM, AutoTokenizer
        except ImportError as e:
            raise ImportError(
                "transformers/torch are not installed. Run: uv sync --extra hf"
            ) from e
        token = os.environ.get("HF_TOKEN")  # for private repos
        self.tokenizer = AutoTokenizer.from_pretrained(model, token=token)
        self.model = AutoModelForCausalLM.from_pretrained(
            model, device_map="auto", torch_dtype="auto", token=token
        )
        self.model_name = model
        self.spec = f"hf:{model}"

    def generate(self, prompt: str, *, temperature: float = 0.0, max_tokens: int = 512) -> ModelResponse:
        t0 = time.perf_counter()
        messages = [{"role": "user", "content": prompt}]
        inputs = self.tokenizer.apply_chat_template(
            messages, add_generation_prompt=True, return_tensors="pt"
        ).to(self.model.device)
        if temperature == 0:
            sampling = {"do_sample": False}
        else:
            sampling = {"do_sample": True, "temperature": temperature}
        outputs = self.model.generate(
            inputs,
            max_new_tokens=max_tokens,
            pad_token_id=self.tokenizer.eos_token_id,
            **sampling,
        )
        # decode only the newly generated tokens
        new_tokens = outputs[0][inputs.shape[-1]:]
        text = self.tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
        return ModelResponse(
            text=text, latency_s=round(time.perf_counter() - t0, 3), raw={}
        )


PROVIDERS = {
    "ollama": OllamaBackend,
    "openai": OpenAIBackend,
    "anthropic": AnthropicBackend,
    "hf": HuggingFaceBackend,
}


def parse_spec(spec: str) -> tuple[str, str]:
    """Split "provider:model" (bare model name defaults to ollama)."""
    provider, sep, model = spec.partition(":")
    if not sep:
        return "ollama", spec.strip()
    provider = provider.strip()
    model = model.strip()
    if provider not in PROVIDERS:
        raise ValueError(
            f"unknown provider {provider!r} (available: {', '.join(PROVIDERS)})"
        )
    if not model:
        raise ValueError(f"spec {spec!r} has no model name")
    return provider, model


def create_backend(spec: str) -> ModelBackend:
    provider, model = parse_spec(spec)
    return PROVIDERS[provider](model)
