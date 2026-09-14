import random

from dataclasses import dataclass


@dataclass
class CodeGuessResponse:
    """Represent the result of a four-digit code guess."""

    guess: str
    feedback: list[str]
    attempts: int
    finished: bool
    won: bool
    repeated: bool = False


class FourDigitCodeGame:
    """Game engine for guessing a four-digit code."""

    CODE_LENGTH = 4
    AVAILABLE_DIGITS = "123456789"

    def __init__(self, max_attempts: int | None = None) -> None:
        if max_attempts is not None and max_attempts <= 0:
            raise ValueError("Maximum attempts must be greater than zero.")

        self.max_attempts = max_attempts

        self.correct_code = self._create_random_code()
        self.attempts = 0
        self.guesses: list[str] = []

        self.finished = False
        self.won = False

    @property
    def remaining_attempts(self) -> int | None:
        """Return the number of remaining attempts."""

        if self.max_attempts is None:
            return None

        return max(0, self.max_attempts - self.attempts)

    @property
    def lost(self) -> bool:
        """Return True if the player lost the game."""

        return self.finished and not self.won

    def _create_random_code(self) -> str:
        """Create a random four-digit code without repeated digits."""

        return "".join(
            random.sample(
                self.AVAILABLE_DIGITS,
                self.CODE_LENGTH,
            )
        )

    def validate_guess(self, guess: str) -> bool:
        """Validate the player's guess."""

        if len(guess) != self.CODE_LENGTH:
            return False

        if not guess.isdigit():
            return False

        if "0" in guess:
            return False

        if len(set(guess)) != self.CODE_LENGTH:
            return False

        return True

    def get_validation_error(self, guess: str) -> str | None:
        """Return a validation error message, if any."""

        if len(guess) != self.CODE_LENGTH:
            return "Your guess must contain exactly 4 digits."

        if not guess.isdigit():
            return "Your guess must contain only digits."

        if "0" in guess:
            return "Zero is not allowed in this game."

        if len(set(guess)) != self.CODE_LENGTH:
            return "Your guess must not contain repeated digits."

        return None

    def _generate_feedback(self, guess: str) -> list[str]:
        """Generate color feedback for each digit."""

        feedback = []

        for index, digit in enumerate(guess):
            if digit == self.correct_code[index]:
                feedback.append("green")

            elif digit in self.correct_code:
                feedback.append("yellow")

            else:
                feedback.append("red")

        return feedback

    def make_guess(self, guess: str) -> CodeGuessResponse:
        """Process a player's code guess."""

        if self.finished:
            raise RuntimeError("The game has already finished.")

        guess = guess.strip()

        validation_error = self.get_validation_error(guess)

        if validation_error is not None:
            raise ValueError(validation_error)

        if guess in self.guesses:
            return CodeGuessResponse(
                guess=guess,
                feedback=[],
                attempts=self.attempts,
                finished=self.finished,
                won=self.won,
                repeated=True,
            )

        self.guesses.append(guess)
        self.attempts += 1

        if guess == self.correct_code:
            self.finished = True
            self.won = True

            return CodeGuessResponse(
                guess=guess,
                feedback=["green"] * self.CODE_LENGTH,
                attempts=self.attempts,
                finished=self.finished,
                won=self.won,
                repeated=False,
            )

        feedback = self._generate_feedback(guess)

        attempts_reached_limit = (
            self.max_attempts is not None
            and self.attempts >= self.max_attempts
        )

        if attempts_reached_limit:
            self.finished = True
            self.won = False

        return CodeGuessResponse(
            guess=guess,
            feedback=feedback,
            attempts=self.attempts,
            finished=self.finished,
            won=self.won,
            repeated=False,
        )

    def reset(self) -> None:
        """Start a new code game."""

        self.correct_code = self._create_random_code()
        self.attempts = 0
        self.guesses.clear()

        self.finished = False
        self.won = False