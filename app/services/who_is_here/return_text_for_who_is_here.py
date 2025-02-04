from app.services.who_is_here.check_astros_file import check_astros_file
from app.services.who_is_here.text_processing_for_astro_data import text_processing_for_astro_data


def return_text_for_who_is_here() -> str:
    astros_data = check_astros_file()
    return (f"Hello, now in space {astros_data['number']} astronauts\n"
               f"They have different crafts and names\n"
               f"Here information about these:\n"
               f"---\n"
               f"{text_processing_for_astro_data(astros_data=astros_data)}\n"
               f"---\n"
               f"They are good guys! Good luck them!"
            )