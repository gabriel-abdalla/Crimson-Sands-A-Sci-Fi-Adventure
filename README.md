# Crimson Sands: A Sci-Fi Adventure

A text-based adventure game written for ICS3U, set in a sci-fi desert world of ruins and abandoned tech. The player explores a derelict train station, fights robots, hacks terminals, and works toward getting a train powered up to escape to Venture Corp.

## Features

- Branching exploration across multiple locations (train station main floor, top floor, basement, a wooden shack, and the surrounding desert)
- Location behavior changes based on how many times the player has visited (first-visit descriptions, later encounters, item-gated options)
- Combat system: a mini-game where the player must type a randomly chosen letter within a time limit to land hits
- Hacking mini-game: memorize and re-enter sequences of numbers shown briefly on screen, under a time limit
- Inventory and item-gating (e.g. needing a weapon before certain fights are survivable)
- Health tracking, with game-over conditions on death
- A full boss fight sequence and win condition once the train is powered and boarded
- One area exists purely as a joke/troll dead-end with escalating flavor text

## Requirements

- Python 3 (uses only standard library: `os`, `random`, `time`, `sys`, `select`)
- A Unix-like terminal (the timed-input mechanics rely on `select.select` on `sys.stdin`, and screen clearing uses `os.system('clear')`) — this will not work as-is on Windows

## Running it

```bash
python U6_A2_adventure_game.py
```

## Development history

Built incrementally over 8 versions: starting from a basic location skeleton, then layering in items, restrictions, the robot fight, health/death handling, the basement area, and finally the hacking mini-game, with a last pass for cleanup, comments, and docstrings.
