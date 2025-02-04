import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import requests
import typer

from app.config.paths import ROOT_DIR
from app.services.average.draw_and_save_people_dependence_of_weight_on_height import (
    draw_and_save_people_dependence_of_weight_on_height,
)
from app.services.average.get_heights_weights_count_from_json_file import get_heights_weights_count_from_json_file
from app.services.average.load_json_file import load_json_file
from app.services.average.open_json_file import open_json_file

# def load_json_file(name_json: str) -> None:
#     with Path(ROOT_DIR / f"files_output/{name_json}", encoding="utf-8").open("r") as file_json:
#          return json.load(file_json)

# def open_json_file(name_json: str) -> None:
#     json_file: json = None
#     try:
#         json_file = load_json_file(name_json=name_json)
#     except FileNotFoundError:
#         result = download_csv_file(name_csv="average.csv")
#         if result:
#             from_csv_in_json(name_csv="average.csv", name_json=name_json)
#             json_file = load_json_file(name_json=name_json)
#     return json_file


# def from_csv_in_json(name_csv: str, name_json: str) -> None:
#     with Path(ROOT_DIR / f"files_output/{name_csv}", encoding="utf-8").open("r") as file:
#         reader = csv.DictReader(file)
#         with Path(ROOT_DIR / f"files_output/{name_json}", encoding="utf-8").open("w") as file_json:
#             json.dump([dict(el) for el in reader], file_json, indent=4)

# def download_csv_file(name_csv: str) -> bool:
#     url = "https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt"
#     response = requests.get(url=url)
#     if response.status_code == 200:
#         with Path(ROOT_DIR / f"files_output/{name_csv}").open("wb") as file:
#             file.write(response.content)
#         return True
#     return False

# def draw_and_save_people_dependence_of_weight_on_height(heights: list, weights: list) -> None:
#     plt.figure(figsize=(8, 6))
#     plt.scatter(heights, weights, color="b", label="People's data")
#     plt.xlabel("Height (sm)")
#     plt.ylabel("Weight (kg)")
#     plt.title("Dependence of weight on height")
#     plt.legend()
#     plt.grid(True)
#     plt.savefig(ROOT_DIR / "files_output/weight_vs_height.png", dpi=300)

# def get_heights_weights_count_from_json_file(json_file: json) -> tuple[list[float], list[float], int]:
#     heights = []
#     weights = []
#     count = 0
#     for el in json_file:
#         heights.append(float(el["Height(Inches)"]) * 2.54)
#         weights.append(float(el["Weight(Pounds)"]) * 0.45359237)
#         count += 1
#     return heights, weights, count

def average() -> None:
    json_file = open_json_file("average.json")
    heights, weights, count = get_heights_weights_count_from_json_file(json_file=json_file)
    draw_and_save_people_dependence_of_weight_on_height(heights, weights)
    typer.echo(
        f"Hello! We counted {count} people.\n"
        f"---\n"
        f"Average height: {sum(heights) / count} centimeters\n"
        f"Average weight: {sum(weights) / count} kilograms\n"
        f"---\n"
        f"Drawing in the file: files_output/weight_vs_height.png")







