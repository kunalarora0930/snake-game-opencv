# Snake Game with Hand Tracking using OpenCV

This project is a simple implementation of the classic Snake Game using Python and OpenCV, enhanced with hand tracking capabilities. The snake is controlled by hand movements, and the objective is to eat the food to grow longer while avoiding collisions.

## Features

- Hand tracking to control the snake's movements.
- Dynamic food placement on the screen.
- Score tracking and game over conditions.
- Collision detection for the snake.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- cvzone

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kunalarora0930/snake-game.git
    ```

2. Install dependencies:

    ```bash
    pip install opencv-python numpy cvzone
    ```

## How to Play

1. Run the game:

    ```bash
    python snake_game.py
    ```

2. Use your hand to control the snake's movements. The snake will follow the movement of your index finger.
3. Try to eat the food to increase your score.
4. Be cautious not to collide with the snake's own body.
5. Press 'r' to restart the game after a game over.
