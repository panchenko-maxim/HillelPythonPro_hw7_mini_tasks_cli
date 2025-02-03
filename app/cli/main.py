from typer import Typer

from app.cli.reading_a_file import app_cli as reading_a_file
from app.cli.user_generator import app_cli as user_generator
from app.cli.who_is_here import app_cli as who_is_here

app = Typer()

app.add_typer(reading_a_file, name="reading_a_file")
app.add_typer(user_generator, name="user_generator")
app.add_typer(who_is_here, name="who_is_here")