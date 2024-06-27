from HighScores import HighScores
from screens.BaseScreeen import BaseScreen

class GameOverScreen(BaseScreen):
    """
    Represents the game over screen. 

    Inherits from BaseScreen class.

    Attributes:
    - score (int): The player's score.
    - name (str): The player's name.
    - high_scores (HighScores): An instance of the HighScores class.

    Methods:
    - __init__(self, canvas, score, show_high_scores): Initializes the GameOverScreen object.
    - draw(self): Draws the game over screen.
    - on_key_press(self, event): Handles key press events.
    - bind_keys(self): Binds key events to the canvas.
    - unbind_keys(self): Unbinds key events from the canvas.
    """

    score = 0
    name = ""
    high_scores = HighScores()

    def __init__(self, canvas, score, show_high_scores):
        """
        Initializes the GameOverScreen object.

        Parameters:
        - canvas: The canvas on which to draw the screen.
        - score (int): The player's score.
        - show_high_scores (function): A function to show the high scores screen.
        """
        super().__init__(canvas)
        self.score = score
        self.show_high_scores = show_high_scores


    def draw(self):
        """
        Draws the game over screen.
        """
        center_x = self.canvas.winfo_width() / 2
        game_over_y = 100
        game_over_gap = 50
        enter_your_name_y = 300
        enter_your_name_gap = 40

        self.canvas.create_text(center_x, game_over_y + 0 * game_over_gap, text="Game Over", font=("Helvetica", 30))
        self.canvas.create_text(center_x, game_over_y + 1 * game_over_gap, text=f"Your score is {self.score}", font=("Helvetica", 20))

        self.canvas.create_text(center_x, enter_your_name_y + 0 * enter_your_name_gap, text="Please enter your name and press Enter", font=("Helvetica", 15))

        box_font_size = 20
        box_width = 300
        box_height = 40
        box_left = center_x - box_width / 2
        box_right = center_x + box_width / 2
        box_top = enter_your_name_y + 1 * enter_your_name_gap - box_font_size
        box_bottom = enter_your_name_y + 1 * enter_your_name_gap + box_height - box_font_size

        self.canvas.create_polygon(box_left, box_top, box_right, box_top, box_right, box_bottom, box_left, box_bottom, fill="white", outline="black")
        self.canvas.create_text(center_x, enter_your_name_y + 1 * enter_your_name_gap, text=self.name, font=("Helvetica", box_font_size, "bold"))


    def on_key_press(self, event):
        """
        Handles key press events. 
        Loads the high scores, adds the new player's score, saves the high scores, and shows the high scores screen.

        Parameters:
        - event: The key press event.
        """
        if event.keysym == "BackSpace":
            self.name = self.name[:-1]
        elif event.keysym == "Return":
            if len(self.name) > 0:
                self.high_scores.load()
                self.high_scores.add_score(self.name, self.score)
                self.high_scores.save()
                self.show_high_scores()
        else:
            self.name += event.char


    def bind_keys(self):
        """
        Binds key events to the canvas.
        """
        self.canvas.bind_all("<Key>", self.on_key_press)


    def unbind_keys(self):
        """
        Unbinds key events from the canvas.
        """
        self.canvas.unbind_all("<Key>")
       
