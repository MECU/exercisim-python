class HighScores(object):
    def __init__(self, scores: list):
        self.scores = scores
        pass

    def latest(self) -> int:
        return self.scores[-1]

    def personal_best(self) -> int:
        return max(self.scores)

    def personal_top(self) -> list:
        self.scores.sort()
        self.scores.reverse()
        return self.scores[:3]

    def report(self) -> str:
        latest = f'Your latest score was {self.latest()}. '

        if self.latest() == self.personal_best():
            best = "That's your personal best!"
        else:
            short = self.personal_best() - self.latest()
            best = f"That's {short} short of your personal best!"

        return latest + best
