#!/usr/bin/env python
"""Bootstrap repository structure for ai-kb-pipeline."""

from pathlib import Path

if __name__ == "__main__":
    for p in [
        "data/raw",
        "data/fixtures",
        "data/runs",
        "prompts/stages",
        "schemas",
    ]:
        Path(p).mkdir(parents=True, exist_ok=True)
    print("Repository scaffold ensured.")
