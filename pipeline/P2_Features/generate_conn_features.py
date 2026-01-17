from pathlib import Path
import pandas as pd


# -----------------------------
# Public API
# -----------------------------


def generate_conn_features(
    df: pd.DataFrame,
    window: str = "5min",
    output_path: str | Path | None = None,
) -> pd.DataFrame:
    """
    Generate time-windowed behavioral features from cleaned Zeek conn data.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned conn dataframe (output of ingest phase)
    window : str
        Pandas time window (default: "5min")
    output_path : str | Path | None
        Optional path to save parquet artifact

    Returns
    -------
    pd.DataFrame
        Feature dataframe indexed by (src_ip, window)
    """

    pass


def compute_feature_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute mean and standard deviation for numeric features only.

    Parameters
    ----------
    df : pd.DataFrame
        Feature dataframe

    Returns
    -------
    pd.DataFrame
        Summary statistics dataframe
    """


# -----------------------------
# Internal helpers
# -----------------------------


def _validate_input(df: pd.DataFrame):
    pass


def _window_seconds(window: str) -> int:
    """
    Convert pandas window string to seconds.
    """
    pass
