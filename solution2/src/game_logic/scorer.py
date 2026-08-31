class Scorer:
    def __init__(self, initial_score=100):
        self.score = initial_score

    def decrease_score(self, penalty=10):
        self.score -= penalty
        self.score = max(0, self.score)

    def get_score(self):
        return self.score