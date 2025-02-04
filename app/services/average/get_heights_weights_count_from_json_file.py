import json


def get_heights_weights_count_from_json_file(json_file: json) -> tuple[list[float], list[float], int]:
    heights = []
    weights = []
    count = 0
    for el in json_file:
        heights.append(float(el["Height(Inches)"]) * 2.54)
        weights.append(float(el["Weight(Pounds)"]) * 0.45359237)
        count += 1
    return heights, weights, count