from tkinter import Canvas

from space_fighter.items.base_item import BaseItem
from space_fighter.items.bullet import OurBullet

BULLET_RADIUS = 3
BULLET_SPEED = -5  # negative: the shot flies up the screen


class SpaceShip(BaseItem):
    """The player's ship. Starts with 3 lives.

    `x` and `y` are the bottom left corner of the hull, and the ship is drawn
    upwards from there. The ship has no movement of its own: the game screen
    changes `x` and `y` while the arrow keys are held down.
    """

    width: int
    height: int

    def __init__(self, items: list, x: int, y: int, width: int, height: int):
        super().__init__(items, x, y, 3)
        self.width = width
        self.height = height

    def draw(self, canvas: Canvas):
        # Hull: a triangle pointing up.
        canvas.create_polygon(self.x, self.y, self.x + self.width // 2, self.y - self.height, self.x + self.width, self.y, fill='grey')

        # Cockpit: a small oval halfway up the hull.
        cockpit_width = self.width // 4
        cockpit_height = self.height // 4
        cockpit_x = self.x + self.width // 2 - cockpit_width // 2
        cockpit_y = self.y - self.height // 2
        canvas.create_oval(cockpit_x, cockpit_y, cockpit_x + cockpit_width, cockpit_y + cockpit_height, fill='blue')

        # Two wings and the engine flame below the hull.
        canvas.create_polygon(self.x, self.y, self.x - self.width // 2, self.y + self.height // 2, self.x, self.y + self.height // 2, fill='red')
        canvas.create_polygon(self.x + self.width, self.y, self.x + self.width * 1.5, self.y + self.height // 2, self.x + self.width, self.y + self.height // 2, fill='red')
        canvas.create_polygon(self.x + self.width // 4, self.y, self.x + 3 * self.width // 4, self.y, self.x + self.width // 2, self.y + self.height // 2, fill='orange')

    def move(self):
        """Nothing to do: the player moves the ship with the arrow keys."""
        pass

    def attack(self):
        """Fire a bullet upwards from the nose of the ship."""
        bullet = OurBullet(self.items, self.x + self.width / 2 - BULLET_RADIUS / 2, self.y - BULLET_RADIUS / 2, BULLET_RADIUS, BULLET_SPEED)
        self.items.append(bullet)

    def center_x(self) -> int:
        return self.x + self.width / 2

    def center_y(self) -> int:
        return self.y + self.height / 2 - 50
