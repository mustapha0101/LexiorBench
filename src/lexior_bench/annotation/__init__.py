"""Annotation provider registry."""

from __future__ import annotations

from .base import AnnotationProvider


def get_provider(name: str) -> AnnotationProvider:
    if name == "argilla":
        from .argilla_provider import ArgillaProvider

        return ArgillaProvider()
    if name == "labelstudio":
        from .labelstudio_provider import LabelStudioProvider

        return LabelStudioProvider()
    raise ValueError(f"unknown annotation provider {name!r} (available: argilla, labelstudio)")


__all__ = ["AnnotationProvider", "get_provider"]
