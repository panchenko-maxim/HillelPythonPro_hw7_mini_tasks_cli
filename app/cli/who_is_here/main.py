import typer

from app.services.check_astros_file import check_astros_file
from app.services.text_processing_for_astro_data import text_processing_for_astro_data

def who_is_here() -> None:
    astros_data = check_astros_file()
    typer.echo(f"Hello, now in space {astros_data['number']} astronauts\n"
               f"They have different crafts and names\n"
               f"Here information about these:\n"
               f"---\n"
               f"{text_processing_for_astro_data(astros_data=astros_data)}\n"
               f"---\n"
               f"They are good guys! Good luck them!")


