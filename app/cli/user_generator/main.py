import typer
from faker import Faker

from app.services.save_file import save_file

faker = Faker()

def get_users_and_emails_from_faker(amount_of_users: int) -> tuple[list[list[str]], str]:
    users_list = [[faker.first_name(), faker.email()] for el in range(amount_of_users)]
    users_text = "".join([f"{user[0]} {user[1]}\n" for user in users_list]).rstrip("\n")
    return users_list, users_text

def save_and_return_name_and_emails_of_users(amount_of_users: int, format_file: str|None) -> str:
    users_list, users_text = get_users_and_emails_from_faker(amount_of_users=amount_of_users)
    if format_file:
        save_file(name_file="user_generator",
                  format_file=format_file,
                  data_for_save=users_text if "txt" in format_file else users_list)
        return f"Saved {amount_of_users} users in 'files_output/{format_file}'"
    return users_text

def user_generator(amount_of_users: int, format_file: str|None) -> None:
    typer.echo(save_and_return_name_and_emails_of_users(amount_of_users=amount_of_users, format_file=format_file))


