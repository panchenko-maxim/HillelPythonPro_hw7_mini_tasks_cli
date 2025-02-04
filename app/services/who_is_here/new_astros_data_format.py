def new_astros_data_format(new_astros_data: dict, craft: str, name: str) -> None:
    if craft not in new_astros_data:
        new_astros_data[craft] = set()
    new_astros_data[craft].add(name)