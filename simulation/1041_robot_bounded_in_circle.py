"""
LeetCode Question #1041: Robot Bounded In Circle

Problem Statement:
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:
- "G": go straight 1 unit.
- "L": turn 90 degrees to the left.
- "R": turn 90 degrees to the right.

The robot performs the instructions given in order, and repeats them forever. Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0, 0) to (0, 2), turns 180 degrees, and then returns to (0, 0).

Example 2:
Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.

Example 3:
Input: instructions = "GL"
Output: true
Explanation: The robot moves in a circle (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0).

Constraints:
- 1 <= instructions.length <= 100
- instructions[i] is 'G', 'L' or 'R'.
"""

# Python Solution
def isRobotBounded(instructions: str) -> bool:
    # Initial position and direction
    x, y = 0, 0
    # Directions: North, East, South, West
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Start facing North
    direction_index = 0

    for instruction in instructions:
        if instruction == 'G':
            dx, dy = directions[direction_index]
            x, y = x + dx, y + dy
        elif instruction == 'L':
            direction_index = (direction_index - 1) % 4
        elif instruction == 'R':
            direction_index = (direction_index + 1) % 4

    # The robot is bounded if:
    # 1. It returns to the origin (0, 0), or
    # 2. It does not face North after one cycle of instructions
    return (x == 0 and y == 0) or direction_index != 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    instructions = "GGLLGG"
    print(isRobotBounded(instructions))  # Output: True

    # Test Case 2
    instructions = "GG"
    print(isRobotBounded(instructions))  # Output: False

    # Test Case 3
    instructions = "GL"
    print(isRobotBounded(instructions))  # Output: True

    # Additional Test Case 4
    instructions = "GRGRGRGR"
    print(isRobotBounded(instructions))  # Output: True

    # Additional Test Case 5
    instructions = "GLLG"
    print(isRobotBounded(instructions))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm processes each instruction in the input string exactly once.
- Let n be the length of the input string `instructions`.
- Time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of space to store the robot's position, direction, and the directions array.
- Space complexity is O(1).

Topic: Simulation
"""