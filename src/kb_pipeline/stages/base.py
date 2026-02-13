from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class Stage:
    name: str
    output_name: str

    def execute(self, payload: Any, run_dir: Path) -> Any:
        data = {"stage": self.name, "payload": payload}
        (run_dir / self.output_name).write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        return data


STAGE_REGISTRY = {
    "segment": Stage("segment", "segments.json"),
    "evidence": Stage("evidence", "evidence.json"),
    "concepts": Stage("concepts", "concepts.json"),
    "claims": Stage("claims", "claims.json"),
    "assumptions": Stage("assumptions", "assumptions.json"),
    "tensions": Stage("tensions", "tensions.json"),
    "insights": Stage("insights", "insights.json"),
    "deliverable": Stage("deliverable", "deliverable.md"),
    "qa": Stage("qa", "qa_report.json"),
}
