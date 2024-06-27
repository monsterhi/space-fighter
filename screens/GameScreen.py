import random
import time
from tkinter import Canvas
from screens.BaseScreeen import BaseScreen
from items.Alien import Alien
from items.Asteroid import Asteroid
from items.Bullet import Bullet, OurBullet, TheirBullet
from items.SpaceShip import SpaceShip

class GameScreen(BaseScreen):
    """
    Represents the game screen where the gameplay takes place.
    Inherits from the BaseScreen class.

    Attributes:
    - game_items: A list to store all the game items (spaceship, bullets, asteroids, aliens).
    - ship: The player's spaceship object.
    - bullet_created_time: The time when the last bullet was created.
    - asteroid_created_time: The time when the last asteroid was created.
    - alien_created_time: The time when the last alien was created.
    - up_pressed: A boolean indicating if the up arrow key is pressed.
    - down_pressed: A boolean indicating if the down arrow key is pressed.
    - left_pressed: A boolean indicating if the left arrow key is pressed.
    - right_pressed: A boolean indicating if the right arrow key is pressed.
    - score: The player's score.
    - game_over: A callback function to be called when the game is over.

    Methods:
    - __init__(self, canvas, game_over): Initializes the GameScreen object.
    - draw(self): Draws the game items on the canvas.
    - update(self): Updates the game state.
    - on_arrow_press(self, event): Handles the arrow key press events.
    - on_arrow_release(self, event): Handles the arrow key release events.
    - on_space_press(self, event): Handles the space key press event.
    - bind_keys(self): Binds the keyboard events to the canvas.
    - unbind_keys(self): Unbinds the keyboard events from the canvas.
    """
    game_items = []
    ship: SpaceShip
    bullet_created_time = time.time()
    asteroid_created_time = time.time()
    alien_created_time = time.time()

    up_pressed = False
    down_pressed = False
    left_pressed = False
    right_pressed = False

    score = 0
    game_over = None

    def __init__(self, canvas, game_over):
        """
        Initializes the GameScreen object.

        Parameters:
        - canvas: The tkinter Canvas object where the game will be displayed.
        - game_over: A callback function to be called when the game is over.
        - score: The player's score.
        - game_items: A list to store all the game items (spaceship, bullets, asteroids, aliens).
        - ship: The player's spaceship object.
        """
        super().__init__(canvas)
        self.game_over = game_over
        self.game_items.clear()
        self.score = 0        
        
        self.ship = SpaceShip(self.game_items, 400, 500, 50, 50)
        self.game_items.append(self.ship)


    def draw(self):
        """
        Draws the game items on the canvas. Specifically draws the score and lives.
        """
        if self.ship.is_alive():
            for item in self.game_items:
                if item.is_alive():
                    item.draw(self.canvas)

            self.canvas.create_text(700, 50, text=f"Score: {self.score}", font=("Helvetica", 16))
            self.canvas.create_text(700, 100, text=f"Lives: {self.ship.lives}", font=("Helvetica", 16))

    
    def update(self):
        """
        Updates the game state.

        This method is called every frame to update the game state.

        The method checks for collisions between game items, creates new game items and deletes the game items that are not alive.
        The method also checks if the player has pressed the arrow keys or the space key and moves the spaceship accordingly.

        The method also checks if the player's spaceship is alive and if not, calls the game over callback function.
        """
        x_speed = 2
        y_speed = 2

        if not self.ship.is_alive():
            return

        if self.up_pressed:
            self.ship.y -= y_speed
        if self.down_pressed:
            self.ship.y += y_speed
        if self.left_pressed:
            self.ship.x -= x_speed
        if self.right_pressed:
            self.ship.x += x_speed

        for item in self.game_items:
            if not item.is_alive():
                self.game_items.remove(item)
            elif isinstance(item, Bullet) or isinstance(item, Asteroid):
                if item.y < 0 or item.y > 600 or item.x < 0 or item.x > 800:
                    self.game_items.remove(item)

        for i in range(len(self.game_items)-1, -1, -1):
            for j in range(i-1, -1, -1):
                item1 = self.game_items[i]
                item2 = self.game_items[j]
                if not item1.is_alive() or not item2.is_alive():
                    continue
                distance = ((item1.center_x() - item2.center_x())**2 + (item1.center_y() - item2.center_y())**2)**0.5
                if distance < 20:
                    if isinstance(item1, SpaceShip) and (isinstance(item2, Asteroid) or isinstance(item2, TheirBullet)) or (isinstance(item1, Asteroid) or isinstance(item1, TheirBullet)) and isinstance(item2, SpaceShip):
                        item1.kill()
                        item2.kill()
                        if self.ship.is_alive() == False:
                            self.game_over(self.score)
                    if isinstance(item1, OurBullet) and (isinstance(item2, Asteroid) or isinstance(item2, Alien)) or (isinstance(item1, Asteroid) or isinstance(item1, Alien)) and isinstance(item2, OurBullet):
                        item1.kill()
                        item2.kill()
                        self.score += 10                        

        for item in self.game_items:
            if item.is_alive():
                item.move()

        if time.time() - self.bullet_created_time > 1:
            for item in self.game_items:
                if item.is_alive() and isinstance(item, Alien):
                    item.attack()
            self.bullet_created_time = time.time()

        if time.time() - self.asteroid_created_time > 3:
            asteroid = Asteroid(self.game_items, random.randint(0, self.canvas.winfo_width()), 0, 1)
            self.game_items.append(asteroid)
            self.asteroid_created_time = time.time()

        if time.time() - self.alien_created_time > 5 and len([item for item in self.game_items if isinstance(item, Alien)]) < 5:
            alien = Alien(self.game_items, random.randint(0, self.canvas.winfo_width()), 0, "Alien")
            self.game_items.append(alien)
            self.alien_created_time = time.time()


    def on_arrow_press(self, event):
        """
        Handles the arrow key press events.

        Parameters:
        - event: The key press event object.
        """
        if event.keysym == "Up":
            self.up_pressed = True
        elif event.keysym == "Down":
            self.down_pressed = True
        elif event.keysym == "Left":
            self.left_pressed = True
        elif event.keysym == "Right":
            self.right_pressed = True


    def on_arrow_release(self, event):
        """
        Handles the arrow key release events.

        Parameters:
        - event: The key release event object.
        """
        if event.keysym == "Up":
            self.up_pressed = False
        elif event.keysym == "Down":
            self.down_pressed = False
        elif event.keysym == "Left":
            self.left_pressed = False
        elif event.keysym == "Right":
            self.right_pressed = False


    def on_space_press(self, event):
        """
        Handles the space key press event.

        Parameters:
        - event: The key press event object.
        """
        if (self.ship.is_alive()):
            self.ship.attack()


    def bind_keys(self):
        """
        Binds the keyboard events to the canvas.
        """
        self.canvas.bind("<KeyPress>", self.on_arrow_press)
        self.canvas.bind("<KeyRelease>", self.on_arrow_release)
        self.canvas.bind("<space>", self.on_space_press)


    def unbind_keys(self):
        """
        Unbinds the keyboard events from the canvas.
        """
        self.canvas.unbind("<KeyPress>")
        self.canvas.unbind("<KeyRelease>")
        self.canvas.unbind("<space>")
