import json
from pathlib import Path

from app.config.paths import ROOT_DIR
from app.services.who_is_here.check_different_seconds import check_different_seconds
from app.services.who_is_here.get_day_seconds_now import get_day_seconds_now
from app.services.who_is_here.save_and_return_astro_file import save_and_return_astro_file


def check_astros_file() -> None:
    try:
        with Path(ROOT_DIR / "files_output/astros.json").open("r") as file:
            data_from_json = json.load(file)
            seconds_today = get_day_seconds_now()
            time, change = check_different_seconds(check_seconds=10,
                                                   time_for_check=data_from_json["save_time"],
                                                   time_now=seconds_today)
            if change:
                return save_and_return_astro_file()
            return data_from_json
    except FileNotFoundError:
        return save_and_return_astro_file()