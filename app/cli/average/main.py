import csv
import json
from pathlib import Path

import pandas
import requests
import urllib3

from app.config.paths import ROOT_DIR


def load_json_file(name_json: str) -> None:
    with open(ROOT_DIR / f"files_output/{name_json}", "r", encoding="utf-8") as file_json:
         return json.load(file_json)


def open_json_file(name_json: str) -> None:
    json_file: json = None
    try:
        json_file = load_json_file(name_json=name_json)
    except FileNotFoundError:
        result = download_csv_file(name_csv="average.csv")
        if result:
            from_csv_in_json(name_csv="average.csv", name_json=name_json)
            json_file = load_json_file(name_json=name_json)
    return json_file


def from_csv_in_json(name_csv: str, name_json: str) -> None:
    with open(ROOT_DIR / f"files_output/{name_csv}", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        with open(ROOT_DIR / f"files_output/{name_json}", "w", encoding="utf-8") as file_json:
            json.dump([dict(el) for el in reader], file_json, indent=4)

def download_csv_file(name_csv: str) -> bool:
    url = "https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt"
    response = requests.get(url=url)
    if response.status_code == 200:
        with open(ROOT_DIR / f"files_output/{name_csv}", "wb") as file:
            file.write(response.content)
        return True
    return False

def average() -> None:
    json_file = open_json_file("average.json")
    print(json_file)

average()


