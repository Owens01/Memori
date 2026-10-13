r"""
 __  __                           _
|  \/  | ___ _ __ ___   ___  _ __(_)
| |\/| |/ _ \ '_ ` _ \ / _ \| '__| |
| |  | |  __/ | | | | | (_) | |  | |
|_|  |_|\___|_| |_| |_|\___/|_|  |_|
                  perfectam memoriam
                       memorilabs.ai

Embeddings utilities.

The public entrypoints are:
- embed_texts
- format_embedding_for_db
"""

from memori.embeddings._api import embed_texts
from memori.embeddings._format import format_embedding_for_db
from memori.embeddings._tei import TEI

__all__ = ["TEI", "embed_texts", "format_embedding_for_db"]
