import os
import json


RAW_FILES = [
    "data/raw/customers.json",
    "data/raw/payments.json",
    "data/raw/tickets.json"
]


def test_raw_files_exist():
    """Check whether raw JSON files exist."""
    for file in RAW_FILES:
        assert os.path.exists(file), f"{file} does not exist"


def test_raw_json_valid():
    """Check whether JSON files are valid."""
    for file in RAW_FILES:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data is not None
        assert isinstance(data, (list, dict))