import json

from app.services.who_is_here.new_astros_data_format import new_astros_data_format


def text_processing_for_astro_data(astros_data: json) -> str:
    new_astros_data = {}
    for astros in astros_data["people"]:
        new_astros_data_format(new_astros_data=new_astros_data, craft=astros["craft"], name=astros["name"])
    text = ""
    for craft, names in new_astros_data.items():
        text += f"Craft '{craft}': {'; '.join(names)[:-1]}\n"
    return text.rstrip()