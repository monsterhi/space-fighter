import random
import time

from space_fighter.items.base_item import BaseItem
from space_fighter.items.bullet import TheirBullet

DIRECTION_CHANGE_INTERVAL_S = 3
PATROL_LIMIT = 600  # aliens wrap around when they pass this x coordinate
BULLET_RADIUS = 3
BULLET_SPEED = 3  # positive: the shot flies down towards the player


class Alien(BaseItem):
    """An enemy saucer that drifts left and right near the top of the screen.

    It flies in one direction until `DIRECTION_CHANGE_INTERVAL_S` passes, then
    picks a new direction at random. The game screen makes every alien shoot on
    its own timer.
    """

    change_direction_time = 0
    direction = 1  # -1 moves left, 1 moves right
    width = 50
    height = 50

    def __init__(self, items: list, x: int, y: int, name: str):
        super().__init__(items, x, y, 1)
        self.name = name

    def draw(self, canvas):
        # Saucer body: a wide oval with a darker one on top of it.
        canvas.create_oval(self.x, self.y, self.x + self.width, self.y + self.height // 2, fill='silver')
        canvas.create_oval(self.x + self.width // 8, self.y + self.height // 4, self.x + self.width * 7 // 8, self.y + self.height * 3 // 4, fill='darkgrey')

        # Glass dome sticking out above the body.
        dome_width = self.width // 4
        dome_height = self.height // 4
        dome_x = self.x + self.width // 2 - dome_width // 2
        dome_y = self.y - dome_height // 2
        canvas.create_oval(dome_x, dome_y, dome_x + dome_width, dome_y + dome_height, fill='lightblue')

        # A row of five lights along the rim.
        for i in range(5):
            light_x = self.x + self.width // 8 + (self.width * 3 // 4) * i // 5
            light_y = self.y + self.height // 2 - 5
            canvas.create_oval(light_x, light_y, light_x + 9, light_y + 11, fill='yellow')

        # Light beam shining down from the saucer.
        canvas.create_polygon(self.x + self.width // 4, self.y + self.height // 2, self.x + self.width * 3 // 4, self.y + self.height // 2, self.x + self.width // 2, self.y + self.height * 1.5, fill='lightyellow', stipple='gray50')

    def attack(self):
        """Fire a bullet downwards from the bottom of the saucer."""
        bullet = TheirBullet(self.items, self.x + 20 - BULLET_RADIUS / 2, self.y + 40, BULLET_RADIUS, BULLET_SPEED)
        self.items.append(bullet)

    def move(self):
        """Slide sideways, wrapping at the edges and turning now and then."""
        if self.x > PATROL_LIMIT:
            self.x = 0
        if self.x < 0:
            self.x = PATROL_LIMIT

        if time.time() - self.change_direction_time > DIRECTION_CHANGE_INTERVAL_S:
            self.direction = random.choice([-1, 1])
            self.change_direction_time = time.time()

        self.x += 1 * self.direction

    def center_x(self) -> int:
        return self.x + 20

    def center_y(self) -> int:
        return self.y
