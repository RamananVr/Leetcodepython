"""
LeetCode Problem #353: Design Snake Game

Problem Statement:
Design a Snake game that is played on a rectangular grid of size width x height. The game starts with a 
snake of length 1 at the top-left corner (0, 0) with a score of 0. The snake moves in one of four directions 
('U' = Up, 'L' = Left, 'R' = Right, 'D' = Down). The game also includes a list of food positions that the 
snake can eat to grow its length and increase its score.

The game ends if the snake runs into the wall or into itself.

Implement the SnakeGame class:
- SnakeGame(width: int, height: int, food: List[List[int]]) Initializes the object with a grid of size width x height and the food positions.
- move(direction: str) -> int: Moves the snake in the given direction. Returns the game's score after the move. If the game is over, return -1.

Constraints:
- 1 <= width, height <= 10^4
- 0 <= food.length <= 50
- food[i].length == 2
- 0 <= food[i][0] < height
- 0 <= food[i][1] < width
- direction is one of ['U', 'L', 'R', 'D'].
- At most 10^4 calls will be made to move.
"""

from collections import deque

class SnakeGame:
    def __init__(self, width: int, height: int, food: list[list[int]]):
        """
        Initialize the game with the grid dimensions and food positions.
        """
        self.width = width
        self.height = height
        self.food = deque(food)  # Use deque for efficient food management
        self.snake = deque([(0, 0)])  # Snake starts at the top-left corner
        self.directions = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}
        self.score = 0

    def move(self, direction: str) -> int:
        """
        Move the snake in the given direction and return the score.
        """
        # Calculate the new head position
        current_head = self.snake[0]
        dx, dy = self.directions[direction]
        new_head = (current_head[0] + dx, current_head[1] + dy)

        # Check if the new head position is out of bounds
        if not (0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width):
            return -1  # Game over

        # Check if the new head position collides with the snake's body
        if new_head in self.snake and new_head != self.snake[-1]:
            return -1  # Game over

        # Check if the new head position is on a food cell
        if self.food and self.food[0] == list(new_head):
            self.food.popleft()  # Remove the food
            self.score += 1  # Increase the score
        else:
            self.snake.pop()  # Remove the tail (move forward)

        # Add the new head to the snake
        self.snake.appendleft(new_head)

        return self.score


# Example Test Cases
if __name__ == "__main__":
    # Initialize the game
    game = SnakeGame(3, 3, [[1, 2], [0, 1]])

    # Test moves
    print(game.move("R"))  # Output: 0
    print(game.move("D"))  # Output: 0
    print(game.move("R"))  # Output: 1 (food eaten)
    print(game.move("U"))  # Output: 1
    print(game.move("L"))  # Output: 2 (food eaten)
    print(game.move("U"))  # Output: -1 (game over)

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `move` method runs in O(1) for most operations (e.g., updating the snake's position, checking collisions).
- Accessing food and updating the snake's deque are O(1) operations due to the use of deque.

Space Complexity:
- The space complexity is O(F + S), where F is the number of food items and S is the maximum length of the snake.

Topic: Design, Queue, Simulation
"""