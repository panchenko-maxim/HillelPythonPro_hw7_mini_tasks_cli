from pathlib import Path

import requests

from app.config.paths import ROOT_DIR


def download_csv_file(name_csv: str) -> bool:
    url = "https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt"
    response = requests.get(url=url)
    if response.status_code == 200:
        with Path(ROOT_DIR / f"files_output/{name_csv}").open("wb") as file:
            file.write(response.content)
        return True
    return False