def return_text_for_average_result(heights: list[float], weights: list[float], count: int) -> str:
    return (
        f"Hello! We counted {count} people.\n"
        f"---\n"
        f"Average height: {sum(heights) / count} centimeters\n"
        f"Average weight: {sum(weights) / count} kilograms\n"
        f"---\n"
        f"Drawing in the file: files_output/weight_vs_height.png"
    )