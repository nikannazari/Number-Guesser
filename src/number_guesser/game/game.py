from dataclasses import dataclass

from .hint_generator import GuessResult, evaluate_guess
from .number_generator import generate_number
from .scorer import Scorer


@dataclass
class GuessResponse:
    result: GuessResult
    score: int
    attempts: int
    finished: bool


class NumberGuessingGame:
    """Core game engine for the Number Guesser game."""

    def __init__(
        self,
        start: int = 1,
        end: int = 100,
        initial_score: int = 100,
        penalty: int = 10,
    ):
        if start > end:
            raise ValueError("Start must be less than or equal to end.")

        self.start = start
        self.end = end
        self.target = generate_number(start, end)
        self.scorer = Scorer(initial_score, penalty)
        self.attempts = 0
        self.finished = False

    def make_guess(self, guess: int) -> GuessResponse:
        """Process a player's guess."""
        if self.finished:
            raise RuntimeError("The game has already finished.")

        if not self.start <= guess <= self.end:
            raise ValueError(
                f"Guess must be between {self.start} and {self.end}."
            )

        self.attempts += 1

        result = evaluate_guess(self.target, guess)

        if result == GuessResult.CORRECT:
            self.finished = True
        else:
            self.scorer.apply_penalty()

            if self.scorer.score == 0:
                self.finished = True

        return GuessResponse(
            result=result,
            score=self.scorer.score,
            attempts=self.attempts,
            finished=self.finished,
        )

    def reset(self) -> None:
        """Start a new game."""
        self.target = generate_number(self.start, self.end)
        self.scorer.reset()
        self.attempts = 0
        self.finished = False