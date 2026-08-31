import random


def generate_number(start: int, end: int) -> int:
    """Generate a random integer between start and end."""
    if start > end:
        raise ValueError("Start must be less than or equal to end.")

    return random.randint(start, end)