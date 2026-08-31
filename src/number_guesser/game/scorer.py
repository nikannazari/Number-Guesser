class Scorer:
    """Manage the player's score."""

    def __init__(self, initial_score: int = 100, penalty: int = 10):
        if initial_score < 0:
            raise ValueError("Initial score cannot be negative.")

        if penalty < 0:
            raise ValueError("Penalty cannot be negative.")

        self._initial_score = initial_score
        self._score = initial_score
        self._penalty = penalty

    @property
    def score(self) -> int:
        return self._score

    def apply_penalty(self) -> None:
        """Decrease the score by the configured penalty."""
        self._score = max(0, self._score - self._penalty)

    def reset(self) -> None:
        """Reset the score to its initial value."""
        self._score = self._initial_score