from pathlib import Path
import json
import pandas as pd
from .feature_definitions import FEATURE_DEFINITIONS


def generate_feature_catalog(
    features_df: pd.DataFrame,
    stats_df: pd.DataFrame | None = None,
    feature_set: str = "conn_v1",
    window: str = "5min",
    output_dir: str | Path = "../data/catalog",
):
    """
    Auto-generate feature catalog documentation.
    """

    return


# -----------------------------
# Writers
# -----------------------------


def _write_markdown(catalog: list[dict], path: Path):
    pass
