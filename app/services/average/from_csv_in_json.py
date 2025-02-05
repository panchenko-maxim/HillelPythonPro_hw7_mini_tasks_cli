import csv
import json
from pathlib import Path

from app.config.paths import ROOT_DIR


def from_csv_in_json(name_csv: str, name_json: str) -> None:
    with Path(ROOT_DIR / f"files_output/{name_csv}", encoding="utf-8").open("r") as file:
        reader = csv.DictReader(file)
        with Path(ROOT_DIR / f"files_output/{name_json}", encoding="utf-8").open("w") as file_json:
            json.dump([dict(el) for el in reader], file_json, indent=4)