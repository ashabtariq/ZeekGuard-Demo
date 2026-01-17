import pandas as pd
import joblib
from pathlib import Path
import pickle


def phase4_detect(
    model_path: str,
    baseline_features_path: str,
    attack_features_path: str,
    feature_columns: list,
    output_dir: str,
    tail_quantile: float = 0.95,
) -> pd.DataFrame:
    """
    Phase 4: Score baseline and attack traffic and summarize separation.
    """

    pass


def separation_verdict(ratio: float) -> str:
    pass
