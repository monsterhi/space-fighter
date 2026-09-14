import os

MAX_SCORES = 10


class HighScores:
    """The leaderboard, stored as one `name,score` line per player.

    The list is kept sorted from best to worst and never grows past
    `MAX_SCORES` entries.
    """

    filename = "high_scores.txt"

    def __init__(self):
        self.scores = []

    def add_score(self, name, score):
        """Add a result for `name`, keeping only their best score."""
        contains = False
        for i, (n, s) in enumerate(self.scores):
            if n == name:
                contains = True
                if s < score:
                    self.scores[i] = (name, score)
                break
        if not contains:
            self.scores.append((name, score))
        self.scores.sort(key=lambda x: x[1], reverse=True)
        self.scores = self.scores[:MAX_SCORES]

    def get_scores(self):
        """Return the leaderboard as a list of `(name, score)` tuples."""
        return self.scores

    def save(self):
        """Write the leaderboard to `filename`, replacing the old contents."""
        with open(self.filename, "w") as file:
            for name, score in self.scores:
                file.write(f"{name},{score}\n")

    def load(self):
        """Read the leaderboard from `filename`, or start empty if it is missing."""
        self.scores = []
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                self.scores.append((name, int(score)))
        self.scores.sort(key=lambda x: x[1], reverse=True)
        self.scores = self.scores[:MAX_SCORES]
