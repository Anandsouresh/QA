"""Generation layer: summarize, call an LLM adapter, validate the result."""

from .adapter import LLMAdapter, build_adapter
from .summarizer import summarize
from .validator import ValidationReport, Validator

__all__ = ["LLMAdapter", "build_adapter", "summarize", "Validator", "ValidationReport"]
