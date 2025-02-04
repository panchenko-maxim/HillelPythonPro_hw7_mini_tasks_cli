import typer
from faker import Faker

from app.services.save_file import save_file

faker = Faker()

def user_generator(amount_of_users: int, format_file: str|None) -> None:
    users = [[faker.first_name(), faker.email()] for el in range(amount_of_users)]
    users_text = "".join([f"{user[0]} {user[1]}\n" for user in users]).rstrip("\n")
    if format_file:
        save_file(name_file="user_generator",
                  format_file=format_file,
                  data_for_save=users_text if "txt" in format_file else users)
    else:
        typer.echo(users_text)


