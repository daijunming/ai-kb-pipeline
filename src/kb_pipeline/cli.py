"""CLI entrypoints for kb pipeline."""

from __future__ import annotations

import argparse

from .evals.harness import run_eval
from .runner import run_pipeline, run_stage


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="kb")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("run", help="Run full pipeline")

    stage = sub.add_parser("stage", help="Run single stage")
    stage.add_argument("--name", required=True)

    sub.add_parser("eval", help="Run evaluation suite")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "run":
        run_pipeline()
    elif args.command == "stage":
        run_stage(args.name)
    elif args.command == "eval":
        run_eval()


if __name__ == "__main__":
    main()
