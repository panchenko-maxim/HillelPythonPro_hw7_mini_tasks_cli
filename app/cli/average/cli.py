import typer

app_cli = typer.Typer()

@app_cli.command()
def run() -> None:
    typer.echo("Hello pidor!")