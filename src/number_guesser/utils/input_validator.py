def validate_guess(guess: int, start: int, end: int) -> bool:
    """Validate that a guess is inside the allowed range."""
    return start <= guess <= end