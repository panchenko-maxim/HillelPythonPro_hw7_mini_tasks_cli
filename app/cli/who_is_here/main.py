import typer

from app.services.who_is_here.return_text_for_who_is_here import return_text_for_who_is_here


def who_is_here() -> None:
    # astros_data = check_astros_file()
    typer.echo(return_text_for_who_is_here())


