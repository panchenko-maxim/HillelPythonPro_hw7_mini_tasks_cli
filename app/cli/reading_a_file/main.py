from pathlib import Path

import typer

from app.services.reading_a_file.try_to_read_file import try_to_read_file


def reading_a_file(file: str) -> None:
    typer.echo(try_to_read_file(file=file))

