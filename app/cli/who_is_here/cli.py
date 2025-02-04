import typer

app_cli = typer.Typer()

@app_cli.command(help="Who is here?")
def run() -> None:
    typer.echo("Who is here!")