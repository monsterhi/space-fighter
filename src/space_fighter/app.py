import threading
import time
from tkinter import BOTH, Canvas, Frame, Tk

from space_fighter.high_scores import HighScores
from space_fighter.screens.base_screen import BaseScreen
from space_fighter.screens.credits_screen import CreditsScreen
from space_fighter.screens.game_over_screen import GameOverScreen
from space_fighter.screens.game_screen import GameScreen
from space_fighter.screens.high_scores_screen import HighScoresScreen
from space_fighter.screens.welcome_screen import WelcomeScreen

DRAW_INTERVAL_MS = 16  # ~60 frames per second
UPDATE_INTERVAL_S = 0.01


class MainFrame(Frame):
    """The game window.

    It owns the single canvas that everything is drawn on and keeps exactly one
    screen active at a time. Screens never switch themselves: each one gets a
    callback (`start_game`, `game_over`, ...) that asks the frame to swap in the
    next screen.

    Two loops run side by side:
      - `draw` redraws the active screen on the Tk event loop;
      - `update` advances the game state on a background thread.
    """

    canvas: Canvas
    screen: BaseScreen = None
    high_scores = HighScores()

    def __init__(self):
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
        """Make `screen` the active one and hand the keyboard over to it."""
        if self.screen is not None:
            self.screen.unbind_keys()
        self.screen = screen
        if self.screen is not None:
            self.screen.bind_keys()

    def draw(self):
        """Clear the canvas, redraw the active screen, repeat on a timer."""
        self.canvas.delete('all')

        if self.screen is not None:
            self.screen.draw()

        self.after(DRAW_INTERVAL_MS, self.draw)

    def update(self):
        """Advance the active screen forever (runs on a background thread)."""
        while True:
            if self.screen is not None:
                self.screen.update()
            time.sleep(UPDATE_INTERVAL_S)

    def show_welcome(self, event=None):
        """Show the main menu."""
        self.set_screen(WelcomeScreen(self.canvas, self.start_game, self.show_high_scores, self.show_credits))

    def show_credits(self, event=None):
        """Show the scrolling credits."""
        self.set_screen(CreditsScreen(self.canvas, self.show_welcome))

    def start_game(self, event=None):
        """Start a new round."""
        self.set_screen(GameScreen(self.canvas, self.game_over))

    def game_over(self, score):
        """Show the game over screen so the player can save `score`."""
        self.set_screen(GameOverScreen(self.canvas, score, self.show_high_scores))

    def show_high_scores(self, event=None):
        """Reload the scores from disk and show the leaderboard."""
        self.high_scores.load()
        self.set_screen(HighScoresScreen(self.canvas, self.high_scores.get_scores(), self.show_welcome))


def run():
    """Open the window and run the game until it is closed."""
    root = Tk()
    root.geometry("800x600+300+300")
    MainFrame()
    root.mainloop()
