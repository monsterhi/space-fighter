from tkinter import Canvas


class BaseScreen:
    """One state of the game, for example the menu or a round of play.

    The main frame calls `draw` on the Tk event loop and `update` on the
    background thread, and calls `bind_keys` / `unbind_keys` when the screen
    becomes active or is replaced. Subclasses override what they need.
    """

    canvas: Canvas

    def __init__(self, canvas: Canvas):
        self.canvas = canvas

    def update(self):
        """Advance the screen by one step (animation, game logic)."""
        pass

    def draw(self):
        """Draw the screen on the canvas, which has just been cleared."""
        pass

    def bind_keys(self):
        """Start listening for the keys this screen uses."""
        pass

    def unbind_keys(self):
        """Stop listening, so the next screen gets the keys."""
        pass
