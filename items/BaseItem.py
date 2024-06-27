from tkinter import Canvas

class BaseItem:
    """
    Represents a base item in the game.

    Attributes:
        items (list): A list of items in the game.
        x (int): The x-coordinate of the item.
        y (int): The y-coordinate of the item.
        lives (int): The number of lives the item has.
    """

    items: list
    x: int
    y: int
    lives: int

    def __init__(self, items: list, x: int, y: int, lives: int):
        """
        Initializes a new instance of the BaseItem class.

        Args:
            items (list): A list of items in the game.
            x (int): The x-coordinate of the item.
            y (int): The y-coordinate of the item.
            lives (int): The number of lives the item has.
        """
        self.x = x
        self.y = y
        self.items = items
        self.lives = lives

    def draw(self, canvas: Canvas):
        """
        Draws the item on the canvas.

        Args:
            canvas (Canvas): The canvas object to draw on.

        Raises:
            NotImplementedError: This method must be implemented in derived classes.
        """
        raise NotImplementedError("Draw method must be implemented in derived classes")
    
    def center_x(self) -> int:
        """
        Calculates the x-coordinate of the center of the item.

        Returns:
            int: The x-coordinate of the center of the item.

        Raises:
            NotImplementedError: This method must be implemented in derived classes.
        """
        raise NotImplementedError("center_x method must be implemented in derived classes")
    
    def center_y(self) -> int:
        """
        Calculates the y-coordinate of the center of the item.

        Returns:
            int: The y-coordinate of the center of the item.

        Raises:
            NotImplementedError: This method must be implemented in derived classes.
        """
        raise NotImplementedError("center_y method must be implemented in derived classes")
    
    def is_alive(self) -> bool:
        """
        Checks if the item is alive.

        Returns:
            bool: True if the item is alive, False otherwise.
        """
        return self.lives > 0
    
    def kill(self):
        """
        Decreases the number of lives of the item by 1.
        """
        self.lives -= 1