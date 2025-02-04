import logging
import sys
from logging.handlers import RotatingFileHandler

from app.config.paths import LOGS_DIR


def init_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s.%(msecs)03d] "
        "[PROCESS %(process)d %(processName)s] "
        "[THREAD %(thread)d %(threadName)s] "
        "%(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
            RotatingFileHandler(
                filename=LOGS_DIR / "app.log",
                maxBytes=10 * 1024 * 1024,  # 10 MB
                backupCount=5,
            ),
        ],
    )