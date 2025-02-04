from pathlib import Path

import typer

from app.config.paths import ROOT_DIR


def reading_a_file(file: str) -> None:
    try:
        with Path(ROOT_DIR / f"files_input/{file}").open("r") as file_for_read:
             text_from_file: str = file_for_read.read()
             typer.echo(text_from_file)
    except FileNotFoundError:
        typer.echo("File not found in the files_input directory.")



