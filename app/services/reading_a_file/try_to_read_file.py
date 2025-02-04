from pathlib import Path

from app.config.paths import ROOT_DIR


def try_to_read_file(file: str) -> str:
    try:
        with Path(ROOT_DIR / f"files_input/{file}").open("r") as file_for_read:
             text_from_file: str = file_for_read.read()
             return text_from_file
    except FileNotFoundError:
        return "File not found in the files_input directory(by default search 'file.txt' in folder 'files_input')."