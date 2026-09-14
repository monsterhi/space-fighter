# Space Fighters

A small arcade shooter written in Python with `tkinter`. You fly a spaceship at
the bottom of the screen, shoot down alien saucers and falling asteroids, and
try to survive with three lives. Every hit is worth 10 points, and the ten best
results are kept in a local leaderboard.

Everything is drawn with plain canvas shapes — no images, no game engine and no
third-party libraries.

## Requirements

- Python 3.10 or newer
- `tkinter`, which ships with the standard Python installers (on Debian/Ubuntu
  install it separately with `sudo apt install python3-tk`)

## Running the game

From the project folder:

```bash
python main.py
```

Optionally, install it as a package and use the command or the module:

```bash
pip install -e .
space-fighter          # console script
python -m space_fighter # same thing
```

## Controls

| Screen     | Key             | Action                        |
|------------|-----------------|-------------------------------|
| Menu       | `s`             | Start a new game              |
| Menu       | `h`             | Show the leaderboard          |
| Menu       | `c`             | Show the credits              |
| Game       | arrow keys      | Move the ship                 |
| Game       | `space`         | Shoot                         |
| Game over  | letters, `⌫`    | Type your name                |
| Game over  | `Enter`         | Save the score                |
| Scores     | `b`             | Back to the menu              |
| Credits    | `b`             | Back to the menu              |

## Project layout

```
space-fighter/
├── main.py                  # launcher: puts src/ on the path and starts the game
├── pyproject.toml           # packaging metadata (optional install)
└── src/
    └── space_fighter/
        ├── app.py           # MainFrame: the window, the loops, screen switching
        ├── high_scores.py   # reading, writing and sorting the leaderboard
        ├── items/           # everything that lives in the game world
        │   ├── base_item.py # shared position, lives and collision interface
        │   ├── space_ship.py
        │   ├── alien.py
        │   ├── asteroid.py
        │   └── bullet.py    # Bullet + OurBullet / TheirBullet
        └── screens/         # one class per state of the game
            ├── base_screen.py
            ├── welcome_screen.py
            ├── game_screen.py
            ├── game_over_screen.py
            ├── high_scores_screen.py
            └── credits_screen.py
```

The game code sits under `src/` so that it is imported as one package,
`space_fighter`, instead of as a pile of top-level modules.

## How it works

### Screens

The window (`MainFrame`) owns a single `tkinter` canvas and shows exactly one
screen at a time. Screens never switch themselves: each one receives callbacks
from the frame and calls them when the player presses a key or when the round
ends.

```
WelcomeScreen ──s──► GameScreen ──ship dies──► GameOverScreen
      │                                             │ Enter
      ├──h──► HighScoresScreen ◄────────────────────-┘
      └──c──► CreditsScreen
```

Each screen implements what it needs from `BaseScreen`:

| Method                        | Called by                    | Purpose                          |
|-------------------------------|------------------------------|----------------------------------|
| `draw()`                      | frame, every 16 ms           | Paint the freshly cleared canvas |
| `update()`                    | frame, every 10 ms           | Move things, run the game logic  |
| `bind_keys()` / `unbind_keys()` | frame, on screen change    | Claim and release the keyboard   |

### The two loops

Drawing runs on the Tk event loop through `after(16, ...)`, which is about 60
frames per second. Game logic runs in a separate thread that calls `update()`
every 10 ms. Splitting them keeps the window responsive while the game state
keeps advancing.

### Items and collisions

Ship, aliens, asteroids and bullets all derive from `BaseItem`, so the game
screen can keep them in one list and treat them the same way: ask each item to
draw itself, to move itself, and to report the center point used for
collisions. Items also carry a number of lives — `kill()` takes one away, and
the game screen removes an item once it has none left.

Collision detection is deliberately simple. Every update, each pair of items is
measured center to center, and a distance below 20 pixels counts as a hit:

- ship vs. asteroid or alien bullet → the ship loses one of its three lives;
- player bullet vs. asteroid or alien → both are destroyed and the score grows
  by 10 points.

When the last life is gone, the game screen calls back into the frame, which
shows the game over screen.

### Spawning

Three timers drive the action: every alien shoots once per second, an asteroid
falls from the top edge every 3 seconds, and a new alien appears every
5 seconds while fewer than five of them are on screen.

### The leaderboard

`HighScores` stores one `name,score` pair per line in `high_scores.txt`, created
in the folder the game was started from. Only a player's best score is kept, the
list is sorted from best to worst, and it is trimmed to ten entries. The file is
plain text, so deleting it simply resets the leaderboard.

## Good to know

- The window is 800×600, and the playfield edges are fixed to that size: items
  that leave it are discarded. Resizing the window does not enlarge the
  playfield.
- Aliens patrol the left 600 pixels of the screen and wrap around at its edges.
- The leaderboard path is relative, so starting the game from a different
  working directory gives you a different leaderboard file.

## About

Project for the PPY course at PJATK (semester 4, 2024) by Anna Glushchenko
(s28602), group 13c.
