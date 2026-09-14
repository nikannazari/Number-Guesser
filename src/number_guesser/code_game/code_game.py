import random
from dataclasses import dataclass


@dataclass
class CodeGuessResponse:
    guess: str
    feedback: list[str]
    attempts: int
    finished: bool
    won: bool
    repeated: bool = False


class FourDigitCodeGame:
    """
    Four-Digit Code Guessing Game.

    Rules:
    - The secret code contains 4 digits.
    - Digits are from 1 to 9.
    - Digits cannot repeat.
    - Green: correct digit in the correct position.
    - Yellow: correct digit but wrong position.
    - Red: digit does not exist in the secret code.
    """

    CODE_LENGTH = 4
    AVAILABLE_DIGITS = "123456789"

    def __init__(self, max_attempts: int | None = None):
        self.max_attempts = max_attempts
        self.correct_code = self._create_random_code()
        self.attempts = 0
        self.finished = False
        self.won = False
        self.history: list[CodeGuessResponse] = []
        self._guessed_codes: set[str] = set()

    @property
    def remaining_attempts(self) -> int | None:
        if self.max_attempts is None:
            return None

        return max(0, self.max_attempts - self.attempts)

    @property
    def lost(self) -> bool:
        return self.finished and not self.won

    def _create_random_code(self) -> str:
        return "".join(
            random.sample(
                self.AVAILABLE_DIGITS,
                self.CODE_LENGTH,
            )
        )

    def validate_guess(self, guess: str) -> bool:
        if not isinstance(guess, str):
            return False

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
        if not isinstance(guess, str):
            return "Guess must be text."

        if len(guess) != self.CODE_LENGTH:
            return "Code must contain exactly 4 digits."

        if not guess.isdigit():
            return "Code must contain digits only."

        if "0" in guess:
            return "Digit 0 is not allowed."

        if len(set(guess)) != self.CODE_LENGTH:
            return "Digits cannot be repeated."

        return None

    def _generate_feedback(self, guess: str) -> list[str]:
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
        if self.finished:
            raise RuntimeError("The game has already finished.")

        guess = str(guess).strip()

        validation_error = self.get_validation_error(guess)

        if validation_error is not None:
            raise ValueError(validation_error)

        if guess in self._guessed_codes:
            response = CodeGuessResponse(
                guess=guess,
                feedback=[],
                attempts=self.attempts,
                finished=self.finished,
                won=self.won,
                repeated=True,
            )

            return response

        self._guessed_codes.add(guess)
        self.attempts += 1

        feedback = self._generate_feedback(guess)

        self.won = guess == self.correct_code

        if self.won:
            self.finished = True

        elif (
            self.max_attempts is not None
            and self.attempts >= self.max_attempts
        ):
            self.finished = True

        response = CodeGuessResponse(
            guess=guess,
            feedback=feedback,
            attempts=self.attempts,
            finished=self.finished,
            won=self.won,
        )

        self.history.append(response)

        return response

    def reset(self) -> None:
        self.correct_code = self._create_random_code()
        self.attempts = 0
        self.finished = False
        self.won = False
        self.history = []
        self._guessed_codes = set()