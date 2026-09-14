from tkinter import Canvas


class BaseItem:
    """An object that lives in the game world: ship, alien, asteroid, bullet.

    Subclasses say how the item looks (`draw`) and where its center is
    (`center_x`, `center_y`); the game screen uses the center to measure
    distances between items and detect collisions.
    """

    items: list  # all items of the running game, so an item can spawn bullets
    x: int
    y: int
    lives: int

    def __init__(self, items: list, x: int, y: int, lives: int):
        self.x = x
        self.y = y
        self.items = items
        self.lives = lives

    def draw(self, canvas: Canvas):
        """Draw the item on the canvas."""
        raise NotImplementedError("Draw method must be implemented in derived classes")

    def center_x(self) -> int:
        """Return the x coordinate of the item's center."""
        raise NotImplementedError("center_x method must be implemented in derived classes")

    def center_y(self) -> int:
        """Return the y coordinate of the item's center."""
        raise NotImplementedError("center_y method must be implemented in derived classes")

    def is_alive(self) -> bool:
        """Return True while the item still has lives left."""
        return self.lives > 0

    def kill(self):
        """Take one life away; the game screen removes items with none left."""
        self.lives -= 1
