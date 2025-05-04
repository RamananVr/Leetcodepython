"""
LeetCode Problem #1113: Reported as "Path Crossing"

Problem Statement:
You are given a string `path`, where `path[i]` represents the movement direction of a robot on an infinite grid:
- 'N' for north,
- 'S' for south,
- 'E' for east, and
- 'W' for west.

The robot starts at the origin point `(0, 0)`. Return `True` if the robot visits the same point at least twice, and `False` otherwise.

Example 1:
Input: path = "NES"
Output: False
Explanation: The robot moves north, then east, then south. It does not revisit any point.

Example 2:
Input: path = "NESWW"
Output: True
Explanation: The robot moves north, then east, then south, then west twice. The robot returns to the point `(0, 0)`.

Constraints:
- `1 <= path.length <= 10^4`
- `path` consists of only characters 'N', 'S', 'E', 'W'.
"""

def isPathCrossing(path: str) -> bool:
    """
    Determines if the robot crosses its own path.

    Args:
    path (str): A string representing the movement directions of the robot.

    Returns:
    bool: True if the robot crosses its path, False otherwise.
    """
    # Initialize the starting position and a set to track visited positions
    x, y = 0, 0
    visited = set()
    visited.add((x, y))  # Add the starting position to the set

    # Iterate through the path
    for direction in path:
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1

        # Check if the current position has been visited before
        if (x, y) in visited:
            return True
        visited.add((x, y))

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    path1 = "NES"
    print(isPathCrossing(path1))  # Output: False

    # Test Case 2
    path2 = "NESWW"
    print(isPathCrossing(path2))  # Output: True

    # Test Case 3
    path3 = "NENENENENW"
    print(isPathCrossing(path3))  # Output: True

    # Test Case 4
    path4 = "SSSS"
    print(isPathCrossing(path4))  # Output: False

    # Test Case 5
    path5 = "NSEW"
    print(isPathCrossing(path5))  # Output: True

"""
Time Complexity Analysis:
- The function iterates through the `path` string once, performing O(1) operations for each character.
- Checking and adding elements to the set is O(1) on average.
- Therefore, the time complexity is O(n), where n is the length of the `path`.

Space Complexity Analysis:
- The space complexity is determined by the size of the `visited` set, which can grow up to O(n) in the worst case (if no positions are revisited).

Topic: Hashing, Simulation
"""