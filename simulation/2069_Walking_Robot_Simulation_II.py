"""
LeetCode Problem #2069: Walking Robot Simulation II

Problem Statement:
A robot is located on a grid with dimensions `width x height`. The robot starts at the top-left corner (0, 0) facing "East". 
The robot can move in four directions: "East", "North", "West", and "South". The robot moves in a cyclic order: 
East -> North -> West -> South -> East -> ...

You are tasked to implement a class `Robot` that simulates the movement of the robot. The class should support the following methods:

1. `__init__(self, width: int, height: int)`: Initializes the grid dimensions and the robot's starting position and direction.
2. `step(self, num: int) -> None`: Moves the robot `num` steps forward. If the robot reaches the boundary of the grid, it continues moving cyclically.
3. `getPos(self) -> List[int]`: Returns the current position of the robot as a list `[x, y]`.
4. `getDir(self) -> str`: Returns the current direction of the robot as a string: "East", "North", "West", or "South".

Constraints:
- 2 <= width, height <= 100
- 1 <= num <= 10^5
- At most 10^4 calls will be made to `step`, `getPos`, and `getDir`.

Example:
Input:
    robot = Robot(6, 3)  # Initializes a 6x3 grid
    robot.step(2)        # Moves 2 steps forward
    robot.getPos()       # Returns [2, 0]
    robot.getDir()       # Returns "East"
    robot.step(2)        # Moves 2 steps forward
    robot.getPos()       # Returns [4, 0]
    robot.getDir()       # Returns "East"
    robot.step(2)        # Moves 2 steps forward
    robot.getPos()       # Returns [0, 2]
    robot.getDir()       # Returns "North"

"""

from typing import List

class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.perimeter = 2 * (width + height) - 4  # Total steps in one full cycle
        self.x, self.y = 0, 0  # Starting position
        self.direction = "East"  # Starting direction
        self.directions = ["East", "North", "West", "South"]  # Order of directions

    def step(self, num: int) -> None:
        # Reduce the number of steps using modulo to avoid unnecessary cycles
        num %= self.perimeter
        for _ in range(num):
            if self.direction == "East":
                if self.x + 1 < self.width:
                    self.x += 1
                else:
                    self.direction = "North"
                    self.y += 1
            elif self.direction == "North":
                if self.y + 1 < self.height:
                    self.y += 1
                else:
                    self.direction = "West"
                    self.x -= 1
            elif self.direction == "West":
                if self.x > 0:
                    self.x -= 1
                else:
                    self.direction = "South"
                    self.y -= 1
            elif self.direction == "South":
                if self.y > 0:
                    self.y -= 1
                else:
                    self.direction = "East"
                    self.x += 1

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.direction


# Example Test Cases
if __name__ == "__main__":
    robot = Robot(6, 3)  # Initializes a 6x3 grid
    robot.step(2)        # Moves 2 steps forward
    print(robot.getPos())  # Output: [2, 0]
    print(robot.getDir())  # Output: "East"
    robot.step(2)        # Moves 2 steps forward
    print(robot.getPos())  # Output: [4, 0]
    print(robot.getDir())  # Output: "East"
    robot.step(2)        # Moves 2 steps forward
    print(robot.getPos())  # Output: [0, 2]
    print(robot.getDir())  # Output: "North"

# Time and Space Complexity Analysis:
# Time Complexity:
# - The `step` method reduces the number of steps using modulo, so it avoids unnecessary iterations. 
#   Each step is processed in O(1) time, so the overall complexity is O(num % perimeter).
# - The `getPos` and `getDir` methods run in O(1) time.

# Space Complexity:
# - The space complexity is O(1) since we only store a few variables (position, direction, and grid dimensions).

# Topic: Simulation