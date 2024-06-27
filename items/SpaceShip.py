from tkinter import Canvas
from items.BaseItem import BaseItem
from items.Bullet import OurBullet

class SpaceShip(BaseItem):
    """
    Represents a spaceship(player) in the game.

    Inherits from the BaseItem class.

    Attributes:
    - width (int): The width of the spaceship.
    - height (int): The height of the spaceship.

    Methods:
    - __init__(items: list, x: int, y: int, width: int, height: int): Initializes a new instance of the SpaceShip class.
    - draw(canvas: Canvas): Draws the spaceship on the canvas.
    - move(): Moves the spaceship.
    - attack(): Performs an attack action by creating a bullet.
    - center_x() -> int: Returns the x-coordinate of the center of the spaceship.
    - center_y() -> int: Returns the y-coordinate of the center of the spaceship.
    """

    width: int
    height: int

    def __init__(self, items: list, x: int, y: int, width: int, height: int):
        """
        Initializes a new instance of the SpaceShip class.

        Parameters:
        - items (list): The list of items in the game.
        - x (int): The x-coordinate of the spaceship.
        - y (int): The y-coordinate of the spaceship.
        - width (int): The width of the spaceship.
        - height (int): The height of the spaceship.
        """
        super().__init__(items, x, y, 3)
        self.width = width
        self.height = height


    def draw(self, canvas: Canvas):
        """
        Draws the spaceship on the canvas.

        Parameters:
        - canvas (Canvas): The canvas to draw on.
        """
        canvas.create_polygon(self.x, self.y, self.x + self.width // 2, self.y - self.height, self.x + self.width, self.y, fill='grey')

        cockpit_width = self.width // 4
        cockpit_height = self.height // 4
        cockpit_x = self.x + self.width // 2 - cockpit_width // 2
        cockpit_y = self.y - self.height // 2
        canvas.create_oval(cockpit_x, cockpit_y, cockpit_x + cockpit_width, cockpit_y + cockpit_height, fill='blue')

        canvas.create_polygon(self.x, self.y, self.x - self.width // 2, self.y + self.height // 2, self.x, self.y + self.height // 2, fill='red')
        canvas.create_polygon(self.x + self.width, self.y, self.x + self.width * 1.5, self.y + self.height // 2, self.x + self.width, self.y + self.height // 2, fill='red')
        canvas.create_polygon(self.x + self.width // 4, self.y, self.x + 3 * self.width // 4, self.y, self.x + self.width // 2, self.y + self.height // 2, fill='orange')


    def move(self):
        """
        Moves the spaceship.
        """
        pass

    def attack(self):
        """
        Performs an attack action by creating a bullet.
        """
        bullet = OurBullet(self.items, self.x + self.width / 2 - 3/2, self.y - 3/2, 3, -5)
        self.items.append(bullet)

    def center_x(self) -> int:
        """
        Returns the x-coordinate of the center of the spaceship.

        Returns:
        - int: The x-coordinate of the center of the spaceship.
        """
        return self.x + self.width / 2
    
    def center_y(self) -> int:
        """
        Returns the y-coordinate of the center of the spaceship.

        Returns:
        - int: The y-coordinate of the center of the spaceship.
        """
        return self.y + self.height / 2 - 50

