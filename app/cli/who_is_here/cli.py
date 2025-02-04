import typer

from app.cli.who_is_here.main import who_is_here

app_cli = typer.Typer()

@app_cli.command(help="Who is here? Get info about astronauts in space.")
def run() -> None:
    who_is_here()