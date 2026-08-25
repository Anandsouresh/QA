"""QAGen -- generate QA test cases and a navigation graph from a live URL."""

__version__ = "0.1.0"

from .config import RunConfig
from .orchestrator import Orchestrator

__all__ = ["RunConfig", "Orchestrator", "__version__"]
