"""
LeetCode Problem #1496: Path Crossing

Problem Statement:
Given a string `path`, where `path[i]` represents the movement direction ('N', 'S', 'E', 'W') 
of a person starting at the origin (0, 0), determine if the path crosses itself at any point.

A path crosses itself if the person visits the same point more than once.

Return `True` if the path crosses itself, and `False` otherwise.

Example:
Input: path = "NES"
Output: False
Explanation: The path moves north, east, and south, forming a triangle without crossing.

Input: path = "NESWW"
Output: True
Explanation: The path moves north, east, south, west, and west again, crossing the origin.

Constraints:
- 1 <= path.length <= 10^4
- path[i] is either 'N', 'S', 'E', or 'W'.
"""

# Python Solution
def isPathCrossing(path: str) -> bool:
    # Initialize the starting point and a set to track visited positions
    x, y = 0, 0
    visited = {(x, y)}  # Start at the origin (0, 0)

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
    # Test Case 1: Path does not cross itself
    path1 = "NES"
    print(isPathCrossing(path1))  # Output: False

    # Test Case 2: Path crosses itself
    path2 = "NESWW"
    print(isPathCrossing(path2))  # Output: True

    # Test Case 3: Path crosses itself immediately
    path3 = "NNS"
    print(isPathCrossing(path3))  # Output: True

    # Test Case 4: Long path without crossing
    path4 = "NNNNSSSS"
    print(isPathCrossing(path4))  # Output: False

    # Test Case 5: Path crosses itself after several moves
    path5 = "NENWNESW"
    print(isPathCrossing(path5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the `path` string once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the `path`.

Space Complexity:
- The space complexity is determined by the `visited` set, which stores all unique positions visited during the traversal.
- In the worst case, the person never revisits a position, and the set contains all n positions. Each position is stored as a tuple (x, y), which takes constant space.
- Therefore, the space complexity is O(n).

Topic: Hashing
"""