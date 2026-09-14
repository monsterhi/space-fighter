import random
import time

from space_fighter.items.alien import Alien
from space_fighter.items.asteroid import Asteroid
from space_fighter.items.bullet import Bullet, OurBullet, TheirBullet
from space_fighter.items.space_ship import SpaceShip
from space_fighter.screens.base_screen import BaseScreen

SHIP_SPEED = 2
COLLISION_DISTANCE = 20  # items closer than this (center to center) collide
POINTS_PER_HIT = 10

ALIEN_SHOT_INTERVAL_S = 1
ASTEROID_SPAWN_INTERVAL_S = 3
ALIEN_SPAWN_INTERVAL_S = 5
MAX_ALIENS = 5
ASTEROID_SPEED = 1

WORLD_WIDTH = 800
WORLD_HEIGHT = 600


class GameScreen(BaseScreen):
    """A round of play: the ship, the enemies, the score and the lives.

    All moving objects live in one flat list, `game_items`, and `update` walks
    it to move things, spawn new enemies, resolve collisions and drop whatever
    is dead or off screen. When the ship runs out of lives the `game_over`
    callback ends the round.
    """

    game_items = []
    ship: SpaceShip

    # Timestamps of the last shot / spawn, used to pace the three timers below.
    bullet_created_time = time.time()
    asteroid_created_time = time.time()
    alien_created_time = time.time()

    # Which arrow keys are held down right now.
    up_pressed = False
    down_pressed = False
    left_pressed = False
    right_pressed = False

    score = 0
    game_over = None

    def __init__(self, canvas, game_over):
        """Start a fresh round; `game_over(score)` is called when the ship dies."""
        super().__init__(canvas)
        self.game_over = game_over
        self.game_items.clear()
        self.score = 0

        self.ship = SpaceShip(self.game_items, 400, 500, 50, 50)
        self.game_items.append(self.ship)

    def draw(self):
        """Draw every living item, plus the score and the remaining lives."""
        if self.ship.is_alive():
            for item in self.game_items:
                if item.is_alive():
                    item.draw(self.canvas)

            self.canvas.create_text(700, 50, text=f"Score: {self.score}", font=("Helvetica", 16))
            self.canvas.create_text(700, 100, text=f"Lives: {self.ship.lives}", font=("Helvetica", 16))

    def update(self):
        """Run one step of the game: input, clean up, collisions, moves, spawns."""
        if not self.ship.is_alive():
            return

        # Move the ship while the arrow keys are held down.
        if self.up_pressed:
            self.ship.y -= SHIP_SPEED
        if self.down_pressed:
            self.ship.y += SHIP_SPEED
        if self.left_pressed:
            self.ship.x -= SHIP_SPEED
        if self.right_pressed:
            self.ship.x += SHIP_SPEED

        # Forget dead items, and bullets or asteroids that left the window.
        for item in self.game_items:
            if not item.is_alive():
                self.game_items.remove(item)
            elif isinstance(item, Bullet) or isinstance(item, Asteroid):
                if item.y < 0 or item.y > WORLD_HEIGHT or item.x < 0 or item.x > WORLD_WIDTH:
                    self.game_items.remove(item)

        # Compare every pair of items once and resolve the pairs that touch:
        # the ship loses a life to asteroids and alien bullets, and our bullets
        # score points against asteroids and aliens.
        for i in range(len(self.game_items)-1, -1, -1):
            for j in range(i-1, -1, -1):
                item1 = self.game_items[i]
                item2 = self.game_items[j]
                if not item1.is_alive() or not item2.is_alive():
                    continue
                distance = ((item1.center_x() - item2.center_x())**2 + (item1.center_y() - item2.center_y())**2)**0.5
                if distance < COLLISION_DISTANCE:
                    if isinstance(item1, SpaceShip) and (isinstance(item2, Asteroid) or isinstance(item2, TheirBullet)) or (isinstance(item1, Asteroid) or isinstance(item1, TheirBullet)) and isinstance(item2, SpaceShip):
                        item1.kill()
                        item2.kill()
                        if self.ship.is_alive() == False:
                            self.game_over(self.score)
                    if isinstance(item1, OurBullet) and (isinstance(item2, Asteroid) or isinstance(item2, Alien)) or (isinstance(item1, Asteroid) or isinstance(item1, Alien)) and isinstance(item2, OurBullet):
                        item1.kill()
                        item2.kill()
                        self.score += POINTS_PER_HIT

        for item in self.game_items:
            if item.is_alive():
                item.move()

        # All aliens shoot together, once per interval.
        if time.time() - self.bullet_created_time > ALIEN_SHOT_INTERVAL_S:
            for item in self.game_items:
                if item.is_alive() and isinstance(item, Alien):
                    item.attack()
            self.bullet_created_time = time.time()

        # New asteroid at a random x along the top edge.
        if time.time() - self.asteroid_created_time > ASTEROID_SPAWN_INTERVAL_S:
            asteroid = Asteroid(self.game_items, random.randint(0, self.canvas.winfo_width()), 0, ASTEROID_SPEED)
            self.game_items.append(asteroid)
            self.asteroid_created_time = time.time()

        # New alien, as long as the screen is not full of them already.
        if time.time() - self.alien_created_time > ALIEN_SPAWN_INTERVAL_S and len([item for item in self.game_items if isinstance(item, Alien)]) < MAX_ALIENS:
            alien = Alien(self.game_items, random.randint(0, self.canvas.winfo_width()), 0, "Alien")
            self.game_items.append(alien)
            self.alien_created_time = time.time()

    def on_arrow_press(self, event):
        """Remember that an arrow key went down."""
        if event.keysym == "Up":
            self.up_pressed = True
        elif event.keysym == "Down":
            self.down_pressed = True
        elif event.keysym == "Left":
            self.left_pressed = True
        elif event.keysym == "Right":
            self.right_pressed = True

    def on_arrow_release(self, event):
        """Remember that an arrow key came back up."""
        if event.keysym == "Up":
            self.up_pressed = False
        elif event.keysym == "Down":
            self.down_pressed = False
        elif event.keysym == "Left":
            self.left_pressed = False
        elif event.keysym == "Right":
            self.right_pressed = False

    def on_space_press(self, event):
        """Fire a bullet from the ship."""
        if (self.ship.is_alive()):
            self.ship.attack()

    def bind_keys(self):
        self.canvas.bind("<KeyPress>", self.on_arrow_press)
        self.canvas.bind("<KeyRelease>", self.on_arrow_release)
        self.canvas.bind("<space>", self.on_space_press)

    def unbind_keys(self):
        self.canvas.unbind("<KeyPress>")
        self.canvas.unbind("<KeyRelease>")
        self.canvas.unbind("<space>")
