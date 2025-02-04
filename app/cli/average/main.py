import csv
from pathlib import Path

import pandas

import requests

from app.config.paths import ROOT_DIR


def save_csv_file() -> None:
    data = pandas.read_csv("https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt")
    print(data[:50])

    # with Path(ROOT_DIR / "files_output/average_data.csv").open("w") as file:
    #     csv.writer(file).writerows(data)

save_csv_file()