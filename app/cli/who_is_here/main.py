import logging

import typer

from app.services.who_is_here.return_text_for_who_is_here import return_text_for_who_is_here


def who_is_here() -> None:
    logging.info("Run task: who_is_here:")
    typer.echo(return_text_for_who_is_here())


