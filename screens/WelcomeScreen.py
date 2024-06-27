from screens.BaseScreeen import BaseScreen

class WelcomeScreen(BaseScreen):
    """
    The WelcomeScreen class represents the screen that is displayed when the game starts.
    It inherits from the BaseScreen class.

    Attributes:
    - start_game (function): The function to be called when the 's' key is pressed.
    - show_high_scores (function): The function to be called when the 'h' key is pressed.
    - show_credits (function): The function to be called when the 'c' key is pressed.

    Methods:
    - __init__(self, canvas, start_game, show_high_scores, show_credits): Initializes a WelcomeScreen object.
    - draw(self): Draws the welcome screen on the canvas.
    - bind_keys(self): Binds the keyboard keys to their respective functions.
    - unbind_keys(self): Unbinds the keyboard keys.
    """

    start_game = None
    show_high_scores = None
    show_credits = None

    def __init__(self, canvas, start_game, show_high_scores, show_credits):
        """
        Initializes a WelcomeScreen object.

        Parameters:
        - canvas (Tkinter.Canvas): The canvas on which the screen will be drawn.
        - start_game (function): The function to be called when the 's' key is pressed.
        - show_high_scores (function): The function to be called when the 'h' key is pressed.
        - show_credits (function): The function to be called when the 'c' key is pressed.
        """
        super().__init__(canvas)
        self.start_game = start_game
        self.show_high_scores = show_high_scores
        self.show_credits = show_credits

    def draw(self):
        """
        Draws the welcome screen on the canvas.
        """
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
        """
        Binds the keyboard keys to their respective functions.
        """
        self.canvas.bind_all("<s>", self.start_game)
        self.canvas.bind_all("<h>", self.show_high_scores)
        self.canvas.bind_all("<c>", self.show_credits)
    
    def unbind_keys(self):
        """
        Unbinds the keyboard keys.
        """
        self.canvas.unbind_all("<s>")
        self.canvas.unbind_all("<h>")
        self.canvas.unbind_all("<c>")
