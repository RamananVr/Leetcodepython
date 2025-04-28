"""
LeetCode Problem #2731: Movement of Robots

Problem Statement:
There are `n` robots, each initially at a unique position on a 1D number line. You are given two integer arrays, `positions` and `directions`, both of length `n`:
- `positions[i]` represents the initial position of the i-th robot.
- `directions[i]` is either 1 (indicating the robot moves to the right) or -1 (indicating the robot moves to the left).

Each robot moves at the same speed of 1 unit per second. If two robots collide, they both stop moving.

Return the positions of all robots after all collisions have occurred, sorted in ascending order.

Constraints:
- `1 <= n <= 10^5`
- `-10^9 <= positions[i] <= 10^9`
- All values in `positions` are unique.
- `directions[i]` is either 1 or -1.

Example:
Input: positions = [5, 3, 8, 2], directions = [1, -1, -1, 1]
Output: [2, 3, 8]
Explanation:
- Robot at position 5 moves right, robot at position 3 moves left, and they collide at position 4.
- Robot at position 8 moves left, robot at position 2 moves right, and they collide at position 5.
- After all collisions, the remaining robots are at positions 2, 3, and 8.

"""

# Python Solution
from typing import List

def survivedRobots(positions: List[int], directions: List[int]) -> List[int]:
    # Combine positions and directions into a single list and sort by position
    robots = sorted(zip(positions, directions), key=lambda x: x[0])
    stack = []  # Stack to simulate collisions

    for pos, dir in robots:
        if dir == 1:  # Moving right
            stack.append((pos, dir))
        else:  # Moving left
            while stack and stack[-1][1] == 1:  # Check for collision
                right_pos, _ = stack.pop()
                if right_pos < pos:  # Collision happens
                    break
            else:
                stack.append((pos, dir))  # No collision, add to stack

    # Extract the positions of the surviving robots and sort them
    return sorted(pos for pos, _ in stack)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    positions = [5, 3, 8, 2]
    directions = [1, -1, -1, 1]
    print(survivedRobots(positions, directions))  # Output: [2, 3, 8]

    # Test Case 2
    positions = [1, 4, 6, 8]
    directions = [1, 1, -1, -1]
    print(survivedRobots(positions, directions))  # Output: [1, 8]

    # Test Case 3
    positions = [10, 20, 30]
    directions = [1, 1, 1]
    print(survivedRobots(positions, directions))  # Output: [10, 20, 30]

    # Test Case 4
    positions = [10, 20, 30]
    directions = [-1, -1, -1]
    print(survivedRobots(positions, directions))  # Output: [10, 20, 30]

    # Test Case 5
    positions = [5, 10, 15, 20]
    directions = [1, -1, 1, -1]
    print(survivedRobots(positions, directions))  # Output: [5, 20]

"""
Time Complexity:
- Sorting the robots by position takes O(n log n).
- Simulating the collisions using a stack takes O(n) since each robot is pushed and popped from the stack at most once.
- Extracting and sorting the surviving positions takes O(n log n).
- Overall time complexity: O(n log n).

Space Complexity:
- The stack used for collision simulation takes O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Simulation, Stack
"""