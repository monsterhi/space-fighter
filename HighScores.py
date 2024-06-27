import os

class HighScores:
    """
    A class to manage high scores for a game.

    Attributes:
    - filename (str): The name of the file to save the high scores to.
    - scores (list): A list of tuples containing the player names and scores.

    Methods:
    - __init__(): Initializes an instance of the HighScores class.
    - add_score(name, score): Adds a new score to the high scores list.
    - get_scores(): Returns the high scores list.
    - save(): Saves the high scores to a file.
    - load(): Loads the high scores from a file.
    """

    filename = "high_scores.txt"

    def __init__(self):
        """
        Initializes an instance of the HighScores class.

        Attributes:
        - scores (list): A list of tuples containing the player names and scores.
        """
        self.scores = []

    def add_score(self, name, score):
        """
        Adds a new score to the high scores list. 
        If the player already exists in the list, their score is updated. 
        The list is then sorted in descending order of scores.

        Parameters:
        - name (str): The name of the player.
        - score (int): The score achieved by the player.
        """
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
        self.scores = self.scores[:10]

    def get_scores(self):
        """
        Returns the high scores list.

        Returns:
        - list: A list of tuples containing the player names and scores.
        """
        return self.scores

    def save(self):
        """
        Saves the high scores to a file.
        """
        with open(self.filename, "w") as file:
            for name, score in self.scores:
                file.write(f"{name},{score}\n")

    def load(self):
        """
        Loads the high scores from a file.
        """
        self.scores = []
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                self.scores.append((name, int(score)))
        self.scores.sort(key=lambda x: x[1], reverse=True)
        self.scores = self.scores[:10]
