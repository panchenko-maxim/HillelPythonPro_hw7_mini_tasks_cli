import typer

from app.cli.average.main import average

app_cli = typer.Typer()

@app_cli.command()
def run() -> None:
    average()