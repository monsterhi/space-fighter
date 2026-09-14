from space_fighter.screens.base_screen import BaseScreen


class WelcomeScreen(BaseScreen):
    """The main menu: 's' starts a game, 'h' shows scores, 'c' shows credits.

    The three callbacks are supplied by the main frame, which does the actual
    switching between screens.
    """

    start_game = None
    show_high_scores = None
    show_credits = None

    def __init__(self, canvas, start_game, show_high_scores, show_credits):
        super().__init__(canvas)
        self.start_game = start_game
        self.show_high_scores = show_high_scores
        self.show_credits = show_credits

    def draw(self):
        center_x = self.canvas.winfo_width() / 2
        welcome_y = 100
        keys_y = 200
        keys_gap = 30
        keys_font_size = 15
        self.canvas.create_text(center_x, welcome_y, text="Welcome to Space Fighters", font=("Helvetica", 30))
        self.canvas.create_text(center_x, keys_y + 0 * keys_gap, text="Press 's' to start the game", font=("Helvetica", keys_font_size))
        self.canvas.create_text(center_x, keys_y + 1 * keys_gap, text="Press 'h' to see high scores", font=("Helvetica", keys_font_size))
        self.canvas.create_text(center_x, keys_y + 2 * keys_gap, text="Press 'c' to see credits", font=("Helvetica", keys_font_size))

    def bind_keys(self):
        self.canvas.bind_all("<s>", self.start_game)
        self.canvas.bind_all("<h>", self.show_high_scores)
        self.canvas.bind_all("<c>", self.show_credits)

    def unbind_keys(self):
        self.canvas.unbind_all("<s>")
        self.canvas.unbind_all("<h>")
        self.canvas.unbind_all("<c>")
