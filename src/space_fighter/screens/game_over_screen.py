from space_fighter.high_scores import HighScores
from space_fighter.screens.base_screen import BaseScreen


class GameOverScreen(BaseScreen):
    """Final score plus a text box where the player types a name.

    Every key press is collected into `name`; Backspace deletes a character and
    Enter saves the score to the leaderboard and opens it.
    """

    score = 0
    name = ""
    high_scores = HighScores()

    def __init__(self, canvas, score, show_high_scores):
        super().__init__(canvas)
        self.score = score
        self.show_high_scores = show_high_scores

    def draw(self):
        center_x = self.canvas.winfo_width() / 2
        game_over_y = 100
        game_over_gap = 50
        enter_your_name_y = 300
        enter_your_name_gap = 40

        self.canvas.create_text(center_x, game_over_y + 0 * game_over_gap, text="Game Over", font=("Helvetica", 30))
        self.canvas.create_text(center_x, game_over_y + 1 * game_over_gap, text=f"Your score is {self.score}", font=("Helvetica", 20))

        self.canvas.create_text(center_x, enter_your_name_y + 0 * enter_your_name_gap, text="Please enter your name and press Enter", font=("Helvetica", 15))

        # The input field is drawn by hand: a white rectangle with the typed
        # name centered inside it.
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
        """Edit the name, or save the score and show the leaderboard on Enter."""
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
        self.canvas.bind_all("<Key>", self.on_key_press)

    def unbind_keys(self):
        self.canvas.unbind_all("<Key>")
