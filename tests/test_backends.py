import pytest

from lexior_bench.backends import (
    DEFAULT_OLLAMA_BASE_URL,
    ModelResponse,
    OllamaBackend,
    create_backend,
    parse_spec,
)


def test_parse_spec_bare_name_defaults_to_ollama():
    assert parse_spec("lexiorgpt") == ("ollama", "lexiorgpt")


def test_parse_spec_provider_prefix():
    assert parse_spec("openai:gpt-4o-mini") == ("openai", "gpt-4o-mini")
    assert parse_spec("anthropic:claude-opus-4-8") == ("anthropic", "claude-opus-4-8")
    assert parse_spec("hf:intelliwork/lexiorgpt-qwen25-7b-v3-merged") == (
        "hf",
        "intelliwork/lexiorgpt-qwen25-7b-v3-merged",
    )


def test_parse_spec_model_name_with_colon():
    # Ollama tags contain colons; only the first colon splits provider/model
    assert parse_spec("ollama:mistral:7b-instruct-q4_K_M") == (
        "ollama",
        "mistral:7b-instruct-q4_K_M",
    )


def test_parse_spec_errors():
    with pytest.raises(ValueError, match="unknown provider"):
        parse_spec("vllm:foo")
    with pytest.raises(ValueError, match="no model name"):
        parse_spec("ollama:")


def test_ollama_backend_payload_and_response(monkeypatch):
    backend = OllamaBackend("lexiorgpt")
    assert backend.base_url == DEFAULT_OLLAMA_BASE_URL
    captured = {}

    def fake_post(payload):
        captured.update(payload)
        return {"message": {"content": " Vrai \n"}, "eval_count": 5}

    monkeypatch.setattr(backend, "_post", fake_post)
    result = backend.generate("Question?", temperature=0.0, max_tokens=64)
    assert isinstance(result, ModelResponse)
    assert result.text == "Vrai"
    assert result.raw["eval_count"] == 5
    assert captured["model"] == "lexiorgpt"
    assert captured["stream"] is False
    assert captured["options"] == {"temperature": 0.0, "num_predict": 64}
    assert captured["messages"] == [{"role": "user", "content": "Question?"}]


def test_ollama_base_url_env(monkeypatch):
    monkeypatch.setenv("OLLAMA_BASE_URL", "http://gpu-box:11434/")
    backend = OllamaBackend("lexiorgpt")
    assert backend.base_url == "http://gpu-box:11434"


def test_create_backend_ollama():
    backend = create_backend("ollama:lexiorgpt")
    assert isinstance(backend, OllamaBackend)
    assert backend.spec == "ollama:lexiorgpt"
