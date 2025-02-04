import matplotlib.pyplot as plt

from app.config.paths import ROOT_DIR


def draw_and_save_people_dependence_of_weight_on_height(heights: list, weights: list) -> None:
    plt.figure(figsize=(8, 6))
    plt.scatter(heights, weights, color="b", label="People's data")
    plt.xlabel("Height (sm)")
    plt.ylabel("Weight (kg)")
    plt.title("Dependence of weight on height")
    plt.legend()
    plt.grid(True)
    plt.savefig(ROOT_DIR / "files_output/weight_vs_height.png", dpi=300)