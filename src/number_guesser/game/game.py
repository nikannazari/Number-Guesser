from dataclasses import dataclass

from .hint_generator import GuessResult, evaluate_guess
from .number_generator import generate_number
from .scorer import Scorer


@dataclass
class GuessResponse:
    """Represent the result of a player's guess."""

    result: GuessResult
    score: int
    attempts: int
    finished: bool
    remaining_attempts: int | None
    repeated: bool = False


class NumberGuessingGame:
    """Core game engine for the Number Guesser game."""

    def __init__(
        self,
        start: int = 1,
        end: int = 100,
        initial_score: int = 100,
        penalty: int = 10,
        max_attempts: int | None = 10,
    ):
        if start > end:
            raise ValueError("Start must be less than or equal to end.")

        if initial_score < 0:
            raise ValueError("Initial score cannot be negative.")

        if penalty < 0:
            raise ValueError("Penalty cannot be negative.")

        if max_attempts is not None and max_attempts <= 0:
            raise ValueError("Maximum attempts must be greater than zero.")

        self.start = start
        self.end = end
        self.max_attempts = max_attempts

        self.initial_score = initial_score
        self.penalty = penalty

        self.target = generate_number(start, end)
        self.scorer = Scorer(initial_score, penalty)

        self.attempts = 0
        self.guesses: list[int] = []

        self.finished = False
        self.won = False
        self.lost = False

    @property
    def remaining_attempts(self) -> int | None:
        """Return the number of attempts remaining."""

        if self.max_attempts is None:
            return None

        return max(0, self.max_attempts - self.attempts)

    @property
    def last_guess(self) -> int | None:
        """Return the latest guess, if available."""

        if not self.guesses:
            return None

        return self.guesses[-1]

    def make_guess(self, guess: int) -> GuessResponse:
        """Process a player's guess."""

        if self.finished:
            raise RuntimeError("The game has already finished.")

        if not isinstance(guess, int):
            raise TypeError("Guess must be an integer.")

        if not self.start <= guess <= self.end:
            raise ValueError(
                f"Guess must be between {self.start} and {self.end}."
            )

        if guess in self.guesses:
            result = evaluate_guess(self.target, guess)

            return GuessResponse(
                result=result,
                score=self.scorer.score,
                attempts=self.attempts,
                finished=self.finished,
                remaining_attempts=self.remaining_attempts,
                repeated=True,
            )

        self.guesses.append(guess)
        self.attempts += 1

        result = evaluate_guess(self.target, guess)

        if result == GuessResult.CORRECT:
            self.finished = True
            self.won = True
            self.lost = False

        else:
            self.scorer.apply_penalty()

            score_reached_zero = self.scorer.score == 0

            attempts_reached_limit = (
                self.max_attempts is not None
                and self.attempts >= self.max_attempts
            )

            if score_reached_zero or attempts_reached_limit:
                self.finished = True
                self.won = False
                self.lost = True

        return GuessResponse(
            result=result,
            score=self.scorer.score,
            attempts=self.attempts,
            finished=self.finished,
            remaining_attempts=self.remaining_attempts,
            repeated=False,
        )

    def reset(self) -> None:
        """Start a new game with the same configuration."""

        self.target = generate_number(self.start, self.end)

        self.scorer.reset()

        self.attempts = 0
        self.guesses.clear()

        self.finished = False
        self.won = False
        self.lost = False