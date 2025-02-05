import json
from pathlib import Path

from app.config.paths import ROOT_DIR


def load_json_file(name_json: str) -> json:
    with Path(ROOT_DIR / f"files_output/{name_json}", encoding="utf-8").open("r") as file_json:
         return json.load(file_json)