"""Browser layer: session, extraction, classification, crawling."""

from .analyzer import PageAnalyzer
from .budgets import Budgets
from .crawler import CrawlResult, Crawler
from .fingerprint import compute_fingerprint, interactive_signature, normalize_url
from .policy import InteractionPolicy, ScopeRules
from .session import AuthError, Session, load_storage_state

__all__ = [
    "PageAnalyzer",
    "Budgets",
    "Crawler",
    "CrawlResult",
    "compute_fingerprint",
    "interactive_signature",
    "normalize_url",
    "InteractionPolicy",
    "ScopeRules",
    "Session",
    "AuthError",
    "load_storage_state",
]
