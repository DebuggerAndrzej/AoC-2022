def get_input(day: int, type: str) -> str:
    with open(f"../input/day_{day}/{type}.txt") as f:
        data = f.read()
    return data
