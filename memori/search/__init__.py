r"""
 __  __                           _
|  \/  | ___ _ __ ___   ___  _ __(_)
| |\/| |/ _ \ '_ ` _ \ / _ \| '__| |
| |  | |  __/ | | | | | (_) | |  | |
|_|  |_|\___|_| |_| |_|\___/|_|  |_|
                  perfectam memoriam
                       memorilabs.ai

Search utilities for Memori.

Public entrypoints:
- parse_embedding
- find_similar_embeddings
- search_facts
- FactCandidate
- FactSearchResult
"""

from memori.search._api import search_facts
from memori.search._faiss import find_similar_embeddings
from memori.search._parsing import parse_embedding
from memori.search._types import FactCandidate, FactSearchResult

__all__ = [
    "find_similar_embeddings",
    "parse_embedding",
    "search_facts",
    "FactCandidate",
    "FactSearchResult",
]
