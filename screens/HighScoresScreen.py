from screens.BaseScreeen import BaseScreen

class HighScoresScreen(BaseScreen):
    """
    Represents the screen that displays the high scores in the game.

    Inherits from the BaseScreen class.

    Attributes:
    - high_scores (list): A list of tuples representing the high scores of players.
    - back_to_welcome (function): A function to be called when the 'b' key is pressed.

    Methods:
    - __init__(self, canvas, high_scores, back_to_welcome): Initializes a new instance of the HighScoresScreen class.
    - draw(self): Draws the high scores screen on the canvas.
    - bind_keys(self): Binds the 'b' key to the back_to_welcome function.
    - unbind_keys(self): Unbinds the 'b' key from the back_to_welcome function.
    """

    high_scores = []
    back_to_welcome = None

    def __init__(self, canvas, high_scores, back_to_welcome):
        """
        Initializes a new instance of the HighScoresScreen class.

        Parameters:
        - canvas (Tkinter.Canvas): The canvas on which the screen is drawn.
        - high_scores (list): A list of tuples representing the high scores.
        - back_to_welcome (function): A function to be called when the 'b' key is pressed.
        """
        super().__init__(canvas)
        self.high_scores = high_scores
        self.back_to_welcome = back_to_welcome


    def draw(self):
        """
        Draws the high scores screen on the canvas.
        """
        center_x = self.canvas.winfo_width() / 2
        title_y = 100
        scores_y = 200
        scores_gap = 30
        scores_font_size = 15
        self.canvas.create_text(center_x, title_y, text="High Scores", font=("Helvetica", 30))
        for i, (name, score) in enumerate(self.high_scores):
            self.canvas.create_text(center_x, scores_y + i * scores_gap, text=f"{name}: {score}", font=("Helvetica", scores_font_size))

        self.canvas.create_text(center_x, scores_y + 7 * scores_gap, text="Press 'b' to go back to welcome screen", font=("Helvetica", scores_font_size))


    def bind_keys(self):
        """
        Binds the 'b' key to the back_to_welcome function.
        """
        self.canvas.bind_all("<b>", self.back_to_welcome)


    def unbind_keys(self):
        """
        Unbinds the 'b' key from the back_to_welcome function.
        """
        self.canvas.unbind_all("<b>")