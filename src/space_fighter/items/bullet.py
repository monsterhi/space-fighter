from tkinter import Canvas

from space_fighter.items.base_item import BaseItem


class Bullet(BaseItem):
    """A shot travelling straight up or down.

    `speed` is added to `y` on every step, so a negative speed flies up the
    screen and a positive one flies down.
    """

    def __init__(self, items: list, x: int, y: int, radius: int, speed: int):
        super().__init__(items, x, y, 1)
        self.radius = radius
        self.speed = speed

    def move(self):
        self.y += self.speed

    def draw(self, canvas: Canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill="red")

    def center_x(self) -> int:
        return self.x

    def center_y(self) -> int:
        return self.y


class OurBullet(Bullet):
    """A bullet fired by the player. Hits asteroids and aliens."""


class TheirBullet(Bullet):
    """A bullet fired by an alien. Hits the player."""
