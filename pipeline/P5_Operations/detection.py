"""
ZeekGuard – Phase 5
Final Detection Report Generation

Consumes artifacts from Phase 4 and produces a single
explainable JSON security report.

NO retraining
NO rescoring
NO feature engineering
"""

import json
import sys
from pathlib import Path
from datetime import datetime
import pandas as pd


# ================================
# Configuration
# ================================

PROJECT_NAME = "ZeekGuard"
VERSION = "0.1"

REQUIRED_COLUMNS = [
    "baseline_mean",
    "attack_mean",
    "baseline_tail_pct",
    "attack_tail_pct",
    "attack_baseline_ratio",
]

# Decision thresholds (locked & explainable)
RATIO_THRESHOLD = 1.05
TAIL_INCREASE_THRESHOLD = 0.25


# ================================
# Utility Functions
# ================================


def load_detection_summary(path: Path) -> pd.DataFrame:
    pass


def evaluate_signals(row: pd.Series) -> dict:
    pass


def determine_risk(signals: dict) -> tuple[str, float]:
    pass


def generate_explanations(signals: dict) -> list[str]:
    pass


def recommend_actions(risk_level: str) -> list[str]:
    pass


# ================================
# Main Report Generator
# ================================


def generate_report(
    detection_summary_path: Path,
    output_path: Path,
) -> None:
    pass


# ================================
# CLI Entry Point
# ================================

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage:\n"
            "  python phase5_generate_report.py "
            "<detection_summary.csv> <output_report.json>"
        )
        sys.exit(1)

    detection_summary = Path(sys.argv[1])
    output_report = Path(sys.argv[2])

    generate_report(detection_summary, output_report)
