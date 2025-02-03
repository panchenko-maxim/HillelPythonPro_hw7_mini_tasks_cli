from typing import Annotated

import typer

from app.cli.user_generator.main import user_generator

app_cli = typer.Typer()


@app_cli.command()
def run(
        amount: Annotated[int, typer.Option(help="Amount users for get list")]=10,
        format_file: Annotated[str | None, typer.Option(help="Name file for reading ('csv', 'json', 'txt')")]=None,
    ) -> None:
    user_generator(amount_of_users=amount, format_file=format_file)