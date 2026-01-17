from sklearn.ensemble import IsolationForest
from pathlib import Path
import pandas as pd
import joblib
import pickle


def train_baseline_model(
    baseline_features: pd.DataFrame,
    feature_columns: list[str],
    model_dir: str,
    MODEL_VERSION: str,
    contamination: float = 0.05,
):
    """
    Phase 3.5 — Train anomaly model on baseline traffic only.

    Parameters
    ----------
    baseline_features : pd.DataFrame
        Feature dataframe from Phase 2 (baseline only)
    feature_columns : list[str]
        Selected numeric feature columns
    model_dir : str
        Directory to save trained model
    contamination : float
        Expected max anomaly ratio in baseline

    Returns
    -------
    model : IsolationForest
    baseline_scored : pd.DataFrame
    score_summary : pd.DataFrame
    """


pass
