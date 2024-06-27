import time
from tkinter import BOTH, Canvas, Frame
import threading

from HighScores import HighScores
from screens.CreditScreen import CreditScreen
from screens.HighScoresScreen import HighScoresScreen
from screens.BaseScreeen import BaseScreen
from screens.GameOverScreen import GameOverScreen
from screens.GameScreen import GameScreen
from screens.WelcomeScreen import WelcomeScreen

class MainFrame(Frame):
    """
    The MainFrame class represents the main window of the Space Fighters game.

    Inherits from the tkinter Frame class.

    Attributes:
    - canvas (Canvas): The canvas widget used for drawing game elements.
    - screen (BaseScreen): The current screen being displayed.
    - high_scores (HighScores): An instance of the HighScores class for managing high scores.

    Methods:
    - __init__(): Initializes the MainFrame object and sets up the window.
    - set_screen(screen): Sets the current screen to the specified screen.
    - draw(): Clears the canvas and redraws the current screen.
    - show_welcome(event): Displays the welcome screen.
    - show_credit(event): Displays the credit screen.
    - start_game(event): Starts the game. Displays the game screen.
    - game_over(score): Displays the game over screen with the final score.
    - show_high_scores(event): Displays the high scores screen.
    - update(): Updates the current screen at regular intervals.
    """

    canvas: Canvas
    screen: BaseScreen = None
    high_scores = HighScores()

    def __init__(self):
        """
        Initializes the MainFrame object and sets up the window.

        Displays the welcome screen.
        Sets up the canvas and starts the game loop. 

        Attributes:
        - canvas (Canvas): The canvas widget used for drawing game elements.
        - screen (BaseScreen): The current screen being displayed.
        - high_scores (HighScores): An instance of the HighScores class for managing high scores.
        """
        super().__init__()

        self.master.title("Space Fighters")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)

        threading.Thread(target=self.update).start()

        self.show_welcome()

        self.draw()
        self.canvas.focus_set()


    def set_screen(self, screen):
        """
        Sets the current screen to the specified screen.

        Parameters:
        - screen (BaseScreen): The screen to be set as the current screen.
        """
        if self.screen is not None:
            self.screen.unbind_keys()
        self.screen = screen
        if self.screen is not None:
            self.screen.bind_keys()


    def draw(self):
        """
        Clears the canvas and redraws the current screen.
        """
        self.canvas.delete('all')

        if self.screen is not None:
            self.screen.draw()

        self.after(16, self.draw)


    def show_welcome(self, event = None):
        """
        Displays the welcome screen.
        """
        self.set_screen(WelcomeScreen(self.canvas, self.start_game, self.show_high_scores, self.show_credit))


    def show_credit(self, event = None):
        """
        Displays the credit screen.
        """
        self.set_screen(CreditScreen(self.canvas, self.show_welcome))


    def start_game(self, event = None):
        """
        Starts the game. Displays the game screen.
        """
        self.set_screen(GameScreen(self.canvas, self.game_over))


    def game_over(self, score):
        """
        Displays the game over screen with the final score.

        Parameters:
        - score (int): The final score of the game.
        """
        self.set_screen(GameOverScreen(self.canvas, score, self.show_high_scores))


    def show_high_scores(self, event = None):
        """
        Displays the high scores screen.
        """
        self.high_scores.load()
        self.set_screen(HighScoresScreen(self.canvas, self.high_scores.get_scores(), self.show_welcome))


    def update(self):
        """
        Updates the current screen at regular intervals.
        """
        while True:
            if self.screen is not None:
                self.screen.update()
            time.sleep(0.01)

    
