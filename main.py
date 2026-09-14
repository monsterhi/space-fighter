"""Launcher for the Space Fighters game: `python main.py`.

The game code lives in `src/space_fighter`, so this file puts `src` on the
import path first. After `pip install -e .` you can also run the installed
`space-fighter` command or `python -m space_fighter`.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from space_fighter.app import run  # noqa: E402  (needs the path set above)

if __name__ == "__main__":
    run()
