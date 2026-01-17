from pathlib import Path
import pandas as pd


# -----------------------------
# Public API
# -----------------------------


def prepare_conn_data(raw_csv_path: str | Path, output_dir: str | Path):
    """
    Load, clean, and store Zeek conn.log CSV as parquet.

    Parameters
    ----------
    raw_csv_path : str | Path
        Path to raw Zeek conn CSV
    output_dir : str | Path
        Directory to store cleaned parquet

    Returns
    -------
    pd.DataFrame
        Cleaned conn dataframe
    Path
        Path to saved parquet file
    """


# -----------------------------
# Internal helpers
# -----------------------------


def _clean_conn_schema(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize Zeek conn.log schema and compute base timing features.
    """

    # Normalize column names
