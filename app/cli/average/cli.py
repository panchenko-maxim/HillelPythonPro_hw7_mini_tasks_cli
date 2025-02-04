import typer

from app.cli.average.main import average

app_cli = typer.Typer()

@app_cli.command(help="Get average weight and height of people. Create drawing in the file.")
def run() -> None:
    average()