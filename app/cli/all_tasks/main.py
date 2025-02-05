from app.cli.average.main import average
from app.cli.reading_a_file.main import reading_a_file
from app.cli.user_generator.main import user_generator
from app.cli.who_is_here.main import who_is_here


def all_tasks() -> None:
    reading_a_file()
    user_generator(amount_of_users=10)
    who_is_here()
    average()

