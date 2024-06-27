from items.BaseItem import BaseItem

class Asteroid(BaseItem):
    """
    Represents an asteroid in the game.

    Inherits from the BaseItem class.

    Attributes:
    - diameter: The diameter of the asteroid.
    - speed: The speed at which the asteroid moves.
    - x: The x-coordinate of the asteroid's position.
    - y: The y-coordinate of the asteroid's position.

    Methods:
    - __init__(items: list, x: int, y: int, speed): Initializes the Asteroid object.
    - draw(canvas): Draws the asteroid on the canvas.
    - move(): Moves the asteroid vertically.
    - center_x() -> int: Returns the x-coordinate of the center of the asteroid.
    - center_y() -> int: Returns the y-coordinate of the center of the asteroid.
    """

    diameter = 35

    def __init__(self, items: list, x: int, y: int, speed):
        """
        Initializes the Asteroid object.

        Parameters:
        - items: A list of items in the game.
        - x: The x-coordinate of the asteroid's position.
        - y: The y-coordinate of the asteroid's position.
        - speed: The speed at which the asteroid moves.
        """
        super().__init__(items, x, y, 1)
        self.speed = speed

    def draw(self, canvas):
        """
        Draws the asteroid on the canvas.

        Parameters:
        - canvas: The canvas on which the asteroid is drawn.
        """
        canvas.create_oval(self.x, self.y, self.x + self.diameter, self.y + self.diameter, fill='grey')
        canvas.create_oval(self.x + self.diameter // 6, self.y + self.diameter // 6, self.x + self.diameter * 3 // 6, self.y + self.diameter * 3 // 6, fill='darkgrey') 

    def move(self):
        """
        Moves the asteroid vertically.
        """
        self.y += self.speed

    def center_x(self) -> int:
        """
        Returns the x-coordinate of the center of the asteroid.

        Returns:
        - The x-coordinate of the center of the asteroid.
        """
        return self.x + 20
    
    def center_y(self) -> int:
        """
        Returns the y-coordinate of the center of the asteroid.

        Returns:
        - The y-coordinate of the center of the asteroid.
        """
        return self.y + 30