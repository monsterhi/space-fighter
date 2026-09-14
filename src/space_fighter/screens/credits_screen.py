from space_fighter.screens.base_screen import BaseScreen


class CreditsScreen(BaseScreen):
    """Credits that scroll up from the bottom of the window.

    `title_y` is moved up one pixel per update; once the text has left the
    screen the player is sent back to the menu. Pressing 'b' skips the scroll.
    """

    show_welcome = None
    title_y = 0

    def __init__(self, canvas, show_welcome):
        super().__init__(canvas)
        self.show_welcome = show_welcome
        self.title_y = self.canvas.winfo_height()

    def draw(self):
        center_x = self.canvas.winfo_width() / 2
        title_gap = 50
        self.canvas.create_text(center_x, self.title_y + 0 * title_gap, text="Developed by:", font=("Helvetica", 30))
        self.canvas.create_text(center_x, self.title_y + 1 * title_gap, text="Anna Glushchenko", font=("Helvetica", 30))

    def update(self):
        self.title_y -= 1
        if self.title_y < 0:
            self.show_welcome()

    def bind_keys(self):
        self.canvas.bind_all("<b>", self.show_welcome)

    def unbind_keys(self):
        self.canvas.unbind_all("<b>")
