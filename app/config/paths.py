from pathlib import Path
from typing import Final

ROOT_DIR: Final[Path] = Path(__file__).parents[2]
FILES_INPUT_DIR: Final[Path] = ROOT_DIR.joinpath("files_input")
FILES_OUTPUT_DIR: Final[Path] = ROOT_DIR.joinpath("files_output")
LOGS_DIR: Final[Path] = ROOT_DIR.joinpath("logs")
