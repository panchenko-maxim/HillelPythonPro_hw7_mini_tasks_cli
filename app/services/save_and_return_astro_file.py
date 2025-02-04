import json
from pathlib import Path

import requests

from app.config.paths import ROOT_DIR
from app.services.get_day_seconds_now import get_day_seconds_now


def save_and_return_astro_file() -> None:
    with requests.Session() as session, session.get(url="http://api.open-notify.org/astros.json") as response:
        astros_data = response.json()
        astros_data["save_time"] = get_day_seconds_now()
        with Path(ROOT_DIR / "files_output/astros.json").open("w") as file:
            json.dump(astros_data, file, indent=4)
        return astros_data