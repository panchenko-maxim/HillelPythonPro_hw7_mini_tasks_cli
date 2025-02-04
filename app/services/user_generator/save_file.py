import csv
import json
from pathlib import Path

from app.config.paths import ROOT_DIR


def save_file(name_file: str, format_file: str, data_for_save: list[list[str]]|str) -> None:
    with Path(ROOT_DIR / f"files_output/{name_file}.{format_file}").open("w") as file:
        if format_file == "csv":
            csv.writer(file).writerows(data_for_save)
        elif format_file == "json":
            json.dump(data_for_save, file, indent=4)
        elif format_file == "txt":
            file.write(data_for_save)