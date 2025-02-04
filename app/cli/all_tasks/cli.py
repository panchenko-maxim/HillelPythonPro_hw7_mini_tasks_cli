import typer

from app.cli.all_tasks.main import all_tasks

app_cli = typer.Typer()

@app_cli.command(help="Run all cli commands")
def run() -> None:
    all_tasks()