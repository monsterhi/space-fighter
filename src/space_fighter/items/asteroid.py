from space_fighter.items.base_item import BaseItem


class Asteroid(BaseItem):
    """A rock falling straight down. Destroys the ship and can be shot down."""

    diameter = 35

    def __init__(self, items: list, x: int, y: int, speed):
        super().__init__(items, x, y, 1)
        self.speed = speed

    def draw(self, canvas):
        # A grey circle with a smaller darker circle as a crater.
        canvas.create_oval(self.x, self.y, self.x + self.diameter, self.y + self.diameter, fill='grey')
        canvas.create_oval(self.x + self.diameter // 6, self.y + self.diameter // 6, self.x + self.diameter * 3 // 6, self.y + self.diameter * 3 // 6, fill='darkgrey')

    def move(self):
        self.y += self.speed

    def center_x(self) -> int:
        return self.x + 20

    def center_y(self) -> int:
        return self.y + 30
