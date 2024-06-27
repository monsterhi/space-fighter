from screens.BaseScreeen import BaseScreen

class CreditScreen(BaseScreen):
    """
    A class representing the credit screen in a space fighters game.

    Inherits from the BaseScreen class.

    Attributes:
    - canvas: The canvas object on which the screen is drawn.
    - show_welcome: A function that shows the welcome screen.
    - title_y: The y-coordinate of the title text.

    Methods:
    - __init__(self, canvas, show_welcome): Initializes the CreditScreen object.
    - draw(self): Draws the credit screen on the canvas.
    - update(self): Updates the position of the title text.
    - bind_keys(self): Binds the 'b' key to the show_welcome function.
    - unbind_keys(self): Unbinds the 'b' key from the show_welcome function.
    """

    show_welcome = None
    title_y = 0

    def __init__(self, canvas, show_welcome):
        """
        Initializes the CreditScreen object.

        Parameters:
        - canvas: The canvas object on which the screen is drawn.
        - show_welcome: A function that shows the welcome screen.
        """
        super().__init__(canvas)
        self.show_welcome = show_welcome
        self.title_y = self.canvas.winfo_height()

    def draw(self):
        """
        Draws the credit screen on the canvas.
        """
        center_x = self.canvas.winfo_width() / 2        
        title_gap = 50
        self.canvas.create_text(center_x, self.title_y + 0 * title_gap, text="Developed by:", font=("Helvetica", 30))
        self.canvas.create_text(center_x, self.title_y + 1 * title_gap, text="Anna Glushchenko", font=("Helvetica", 30))

    def update(self):
        """
        Updates the position of the title text.
        """
        self.title_y -= 1
        if self.title_y < 0:
            self.show_welcome()

    def bind_keys(self):
        """
        Binds the 'b' key to the show_welcome function.
        """
        self.canvas.bind_all("<b>", self.show_welcome)

    def unbind_keys(self):
        """
        Unbinds the 'b' key from the show_welcome function.
        """
        self.canvas.unbind_all("<b>")