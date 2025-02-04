import typer

from app.services.check_astros_file import check_astros_file
from app.services.text_processing_for_astro_data import text_processing_for_astro_data

# def get_day_seconds_now() -> int:
#     time_now = datetime.now()
#     return time_now.hour * 3600 + time_now.minute * 60 + time_now.second

# def check_different_seconds(check_seconds: int, time_for_check: int, time_now: int) -> tuple[int, bool]:
#     if time_now - time_for_check > check_seconds:
#         return time_now, True
#     return time_for_check, False

# def save_and_return_astro_file() -> None:
#     with requests.Session() as session, session.get(url="http://api.open-notify.org/astros.json") as response:
#         astros_data = response.json()
#         astros_data["save_time"] = get_day_seconds_now()
#         with Path(ROOT_DIR / "files_output/astros.json").open("w") as file:
#             json.dump(astros_data, file, indent=4)
#         return astros_data


# def check_astros_file() -> None:
#     try:
#         with Path(ROOT_DIR / "files_output/astros.json").open("r") as file:
#             data_from_json = json.load(file)
#             seconds_today = get_day_seconds_now()
#             time, change = check_different_seconds(check_seconds=10,
#                                                    time_for_check=data_from_json["save_time"],
#                                                    time_now=seconds_today)
#             if change:
#                 return save_and_return_astro_file()
#             return data_from_json
#     except FileNotFoundError:
#         return save_and_return_astro_file()

# def new_astros_data_format(new_astros_data: dict, craft: str, name: str) -> None:
#     if craft not in new_astros_data:
#         new_astros_data[craft] = set()
#     new_astros_data[craft].add(name)

# def text_processing_for_astro_data(astros_data: json) -> str:
#     new_astros_data = {}
#     for astros in astros_data["people"]:
#         new_astros_data_format(new_astros_data=new_astros_data, craft=astros["craft"], name=astros["name"])
#     text = ""
#     for craft, names in new_astros_data.items():
#         text += f"Craft '{craft}': {'; '.join(names)[:-1]}\n"
#     return text.rstrip()

def who_is_here() -> None:
    astros_data = check_astros_file()
    typer.echo(f"Hello, now in space {astros_data['number']} astronauts\n"
               f"They have different crafts and names\n"
               f"Here information about these:\n"
               f"---\n"
               f"{text_processing_for_astro_data(astros_data=astros_data)}\n"
               f"---\n"
               f"They are good guys! Good luck them!")


