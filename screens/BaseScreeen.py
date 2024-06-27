from tkinter import Canvas


class BaseScreen:
    """
    Represents a base screen for a game.

    Attributes:
        canvas (Canvas): The canvas object to draw on.
    """

    canvas: Canvas

    def __init__(self, canvas: Canvas):
        """
        Initializes a new instance of the BaseScreen class.

        Args:
            canvas (Canvas): The canvas object to draw on.
        """
        self.canvas = canvas

    def update(self):
        """
        Updates the screen state.
        """
        pass

    def draw(self):
        """
        Draws the screen.
        """
        pass

    def bind_keys(self):
        """
        Binds the necessary keys for the screen.
        """
        pass
    
    def unbind_keys(self):
        """
        Unbinds the keys bound to the screen.
        """
        pass