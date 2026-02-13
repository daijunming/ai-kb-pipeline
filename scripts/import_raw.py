#!/usr/bin/env python
"""Import raw files into data/raw with metadata."""

from pathlib import Path


def main() -> None:
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    print("Place source files into data/raw/<yyyy-mm>/.")


if __name__ == "__main__":
    main()
