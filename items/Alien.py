import random
import time
from items.BaseItem import BaseItem
from items.Bullet import TheirBullet

class Alien(BaseItem):
    """
    Represents an alien object in the game.

    Inherits from the BaseItem class.

    Attributes:
        change_direction_time (float): The time when the alien changes its direction.
        direction (int): The direction in which the alien is moving (-1 for left, 1 for right).
        width (int): The width of the alien.
        height (int): The height of the alien.
        name (str): The name of the alien.

    Args:
        items (list): The list of items in the game.
        x (int): The initial x-coordinate of the alien.
        y (int): The initial y-coordinate of the alien.
        name (str): The name of the alien.
    """

    change_direction_time = 0
    direction = 1
    width = 50
    height = 50

    def __init__(self, items: list, x: int, y: int, name: str):
        """
        Initializes a new instance of the Alien class.

        Args:
            items (list): The list of items in the game.
            x (int): The initial x-coordinate of the alien.
            y (int): The initial y-coordinate of the alien.
            name (str): The name of the alien.
        """
        super().__init__(items, x, y, 1)
        self.name = name

    def draw(self, canvas):
        """
        Draws the alien on the canvas.

        Args:
            canvas: The canvas on which to draw the alien.
        """
        body_top = canvas.create_oval(self.x, self.y, self.x + self.width, self.y + self.height // 2, fill='silver')
        body_bottom = canvas.create_oval(self.x + self.width // 8, self.y + self.height // 4, self.x + self.width * 7 // 8, self.y + self.height * 3 // 4, fill='darkgrey')

        dome_width = self.width // 4
        dome_height = self.height // 4
        dome_x = self.x + self.width // 2 - dome_width // 2
        dome_y = self.y - dome_height // 2
        dome = canvas.create_oval(dome_x, dome_y, dome_x + dome_width, dome_y + dome_height, fill='lightblue')

        for i in range(5):
            light_x = self.x + self.width // 8 + (self.width * 3 // 4) * i // 5
            light_y = self.y + self.height // 2 - 5
            canvas.create_oval(light_x, light_y, light_x + 9, light_y + 11, fill='yellow')
        beam = canvas.create_polygon(self.x + self.width // 4, self.y + self.height // 2, self.x + self.width * 3 // 4, self.y + self.height // 2, self.x + self.width // 2, self.y + self.height * 1.5, fill='lightyellow', stipple='gray50')

    def attack(self):
        """
        Creates a bullet object and adds it to the list of items.

        The bullet is created at the top center of the alien.
        """
        bullet = TheirBullet(self.items, self.x + 20 - 3/2, self.y + 40, 3, 3)
        self.items.append(bullet)

    def move(self):
        """
        Moves the alien horizontally across the screen.

        The alien changes its direction randomly every 3 seconds.
        """
        if self.x > 600:
            self.x = 0
        if self.x < 0:
            self.x = 600

        if time.time() - self.change_direction_time > 3:
            self.direction = random.choice([-1, 1])
            self.change_direction_time = time.time()

        self.x += 1 * self.direction

    def center_x(self) -> int:
        """
        Returns the x-coordinate of the center of the alien.

        Returns:
            int: The x-coordinate of the center of the alien.
        """
        return self.x + 20
    
    def center_y(self) -> int:
        """
        Returns the y-coordinate of the center of the alien.

        Returns:
            int: The y-coordinate of the center of the alien.
        """
        return self.y