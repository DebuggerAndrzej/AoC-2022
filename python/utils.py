def get_input(type: str) -> str:
    with open(f"../input/day_3/{type}.txt") as f:
        data = f.read()
    return data
