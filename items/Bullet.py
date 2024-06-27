from tkinter import Canvas
from items.BaseItem import BaseItem


class Bullet(BaseItem):
    """
    Represents a bullet in the game.

    Inherits from the BaseItem class.

    Attributes:
    - items (list): A list of all items in the game.
    - x (int): The x-coordinate of the bullet.
    - y (int): The y-coordinate of the bullet.
    - radius (int): The radius of the bullet.
    - speed (int): The speed at which the bullet moves.

    Methods:
    - move(): Moves the bullet vertically.
    - draw(canvas: Canvas): Draws the bullet on the canvas.
    - center_x() -> int: Returns the x-coordinate of the center of the bullet.
    - center_y() -> int: Returns the y-coordinate of the center of the bullet.
    """

    def __init__(self, items: list, x: int, y: int, radius: int, speed: int):
        """
        Initializes a new instance of the Bullet class.

        Parameters:
        - items (list): A list of all items in the game.
        - x (int): The x-coordinate of the bullet.
        - y (int): The y-coordinate of the bullet.
        - radius (int): The radius of the bullet.
        - speed (int): The speed at which the bullet moves.
        """
        super().__init__(items, x, y, 1)
        self.radius = radius
        self.speed = speed

    def move(self):
        """
        Moves the bullet vertically.
        """
        self.y += self.speed

    def draw(self, canvas: Canvas):
        """
        Draws the bullet on the canvas.

        Parameters:
        - canvas (Canvas): The canvas on which to draw the bullet.
        """
        canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill="red")

    def center_x(self) -> int:
        """
        Returns the x-coordinate of the center of the bullet.

        Returns:
        - int: The x-coordinate of the center of the bullet.
        """
        return self.x
    
    def center_y(self) -> int:
        """
        Returns the y-coordinate of the center of the bullet.

        Returns:
        - int: The y-coordinate of the center of the bullet.
        """
        return self.y
    
class OurBullet(Bullet):
    """
    Represents a bullet fired by the player.

    Inherits from the Bullet class.
    """

    def __init__(self, items: list, x: int, y: int, radius: int, speed: int):
        """
        Initializes a new instance of the OurBullet class.

        Parameters:
        - items (list): A list of all items in the game.
        - x (int): The x-coordinate of the bullet.
        - y (int): The y-coordinate of the bullet.
        - radius (int): The radius of the bullet.
        - speed (int): The speed at which the bullet moves.
        """
        super().__init__(items, x, y, radius, speed)

class TheirBullet(Bullet):
    """
    Represents a bullet fired by the enemy.

    Inherits from the Bullet class.
    """

    def __init__(self, items: list, x: int, y: int, radius: int, speed: int):
        """
        Initializes a new instance of the TheirBullet class.

        Parameters:
        - items (list): A list of all items in the game.
        - x (int): The x-coordinate of the bullet.
        - y (int): The y-coordinate of the bullet.
        - radius (int): The radius of the bullet.
        - speed (int): The speed at which the bullet moves.
        """
        super().__init__(items, x, y, radius, speed)
