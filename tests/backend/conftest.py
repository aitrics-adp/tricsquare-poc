"""pytest bootstrap for QTrics' backend regression suite.

The QTrics test tree (``tests/backend/``) lives in a sibling directory to the
backend code (``backend/app``). Prepend ``backend/`` to ``sys.path`` so tests
can import the FastAPI app via ``from app.main import app`` without requiring
the backend wheel to be installed in this environment.
"""

from __future__ import annotations

import sys
from pathlib import Path

_BACKEND_ROOT = Path(__file__).resolve().parents[2] / "backend"
if str(_BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(_BACKEND_ROOT))
