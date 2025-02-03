from datetime import datetime

import json
from pathlib import Path

import requests

from app.config.paths import ROOT_DIR


def save_and_return_file() -> None:
    with requests.Session() as session, session.get(url="https://api.open-notify.org/astros.json") as response:
        astros_data = response.json()
        now = datetime.now()
        seconds_today = now.hour * 3600 + now.minute * 60 + now.second
        astros_data["save_time"] = seconds_today
        with Path(ROOT_DIR / "files_output/astros.json").open("w") as file:
            json.dump(astros_data, file, indent=4)
        return astros_data


def check_astros_file() -> None:
    try:
        with Path(ROOT_DIR / "files_output/astros.json").open("r") as file:
            data_from_json = json.load(file)
            # if (datetime.now() - data_from_json["save_time"]).second > 15:
            #     return save_and_return_file()
            return data_from_json
    except FileNotFoundError:
        return save_and_return_file()

def who_is_here() -> None:
    astros_data = check_astros_file()
    print(astros_data)

who_is_here()


