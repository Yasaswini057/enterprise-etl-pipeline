import os
import pandas as pd


PROCESSED_FILES = [
    "data/processed/customers.csv",
    "data/processed/payments.csv",
    "data/processed/tickets.csv"
]


def test_processed_files_exist():
    """Check whether processed CSV files exist."""
    for file in PROCESSED_FILES:
        assert os.path.exists(file), f"{file} does not exist"


def test_processed_csv_not_empty():
    """Check whether processed CSV files contain records."""
    for file in PROCESSED_FILES:
        df = pd.read_csv(file)

        assert not df.empty, f"{file} is empty"
        assert len(df.columns) > 0