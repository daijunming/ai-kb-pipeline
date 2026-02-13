"""Pipeline runner with manifest output."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from .stages.base import STAGE_REGISTRY


def _new_run_dir() -> Path:
    run_id = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    run_dir = Path("data/runs") / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir


def run_pipeline() -> None:
    run_dir = _new_run_dir()
    outputs: dict[str, str] = {}
    payload = None
    for name, stage in STAGE_REGISTRY.items():
        payload = stage.execute(payload, run_dir)
        outputs[name] = stage.output_name
    manifest = {
        "run_dir": str(run_dir),
        "stages": outputs,
        "timestamp": datetime.now().isoformat(),
    }
    (run_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def run_stage(name: str) -> None:
    run_dir = _new_run_dir()
    stage = STAGE_REGISTRY[name]
    stage.execute(None, run_dir)
