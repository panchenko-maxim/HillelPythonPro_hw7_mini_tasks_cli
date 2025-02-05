import json

from app.services.average.download_csv_file import download_csv_file
from app.services.average.from_csv_in_json import from_csv_in_json
from app.services.average.load_json_file import load_json_file


def open_json_file(name_json: str) -> json:
    json_file: json = None
    try:
        json_file = load_json_file(name_json=name_json)
    except FileNotFoundError:
        result = download_csv_file(name_csv="average.csv")
        if result:
            from_csv_in_json(name_csv="average.csv", name_json=name_json)
            json_file = load_json_file(name_json=name_json)
    return json_file