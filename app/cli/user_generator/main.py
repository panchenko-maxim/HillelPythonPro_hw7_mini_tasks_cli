import typer

from app.services.user_generator.save_and_return_name_and_emails_of_users import (
    save_and_return_name_and_emails_of_users,
)


def user_generator(amount_of_users: int, format_file: str|None=None) -> None:
    typer.echo(save_and_return_name_and_emails_of_users(amount_of_users=amount_of_users, format_file=format_file))


