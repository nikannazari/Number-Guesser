from enum import Enum


class GuessResult(Enum):
    TOO_LOW = "too_low"
    TOO_HIGH = "too_high"
    CORRECT = "correct"


def evaluate_guess(number: int, guess: int) -> GuessResult:
    """Evaluate a guess against the target number."""
    if guess < number:
        return GuessResult.TOO_LOW

    if guess > number:
        return GuessResult.TOO_HIGH

    return GuessResult.CORRECT