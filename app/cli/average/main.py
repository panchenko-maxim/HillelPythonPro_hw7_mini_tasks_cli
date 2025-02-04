import logging

import typer

from app.services.average.draw_and_save_people_dependence_of_weight_on_height import (
    draw_and_save_people_dependence_of_weight_on_height,
)
from app.services.average.get_heights_weights_count_from_json_file import get_heights_weights_count_from_json_file
from app.services.average.open_json_file import open_json_file
from app.services.average.return_text_for_average_result import return_text_for_average_result


def average() -> None:
    logging.info("Run task: average:")
    json_file = open_json_file(name_json="average.json")
    heights, weights, count = get_heights_weights_count_from_json_file(json_file=json_file)
    draw_and_save_people_dependence_of_weight_on_height(heights=heights, weights=weights)
    typer.echo(return_text_for_average_result(heights=heights, weights=weights, count=count))







