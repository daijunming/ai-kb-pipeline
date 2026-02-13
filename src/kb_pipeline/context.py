from dataclasses import dataclass
from pathlib import Path


@dataclass
class RunContext:
    run_id: str
    run_dir: Path
