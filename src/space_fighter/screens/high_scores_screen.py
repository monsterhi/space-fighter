from space_fighter.screens.base_screen import BaseScreen


class HighScoresScreen(BaseScreen):
    """The leaderboard. Pressing 'b' goes back to the menu."""

    high_scores = []
    back_to_welcome = None

    def __init__(self, canvas, high_scores, back_to_welcome):
        """Show `high_scores`, a list of `(name, score)` tuples, best first."""
        super().__init__(canvas)
        self.high_scores = high_scores
        self.back_to_welcome = back_to_welcome

    def draw(self):
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
        self.canvas.bind_all("<b>", self.back_to_welcome)

    def unbind_keys(self):
        self.canvas.unbind_all("<b>")
