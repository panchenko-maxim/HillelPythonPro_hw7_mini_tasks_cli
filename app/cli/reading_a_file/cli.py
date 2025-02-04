from typing import Annotated

import typer

from app.cli.reading_a_file.main import reading_a_file

app_cli = typer.Typer()

@app_cli.command()
def run(
        file: Annotated[str, typer.Option(help="Name file for reading.")]="file.txt") -> None:
    reading_a_file(file=file)