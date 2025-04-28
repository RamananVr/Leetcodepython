"""
LeetCode Problem #593: Valid Square

Problem Statement:
Given the coordinates of four points in a 2D space, return whether the four points could construct a square.

The coordinate (x, y) of a point is represented by an integer array [x, y].

A valid square has four equal sides with positive length and four equal angles (90-degree angles).

Input: points are given as a list of four integer arrays, where each array represents a point in the form [x, y].
Output: Return True if the points form a valid square, otherwise return False.

Constraints:
- points.length == 4
- points[i].length == 2
- -10^4 <= points[i][j] <= 10^4
"""

from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance_squared(a: List[int], b: List[int]) -> int:
            """Calculate the squared distance between two points."""
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        # Store all pairwise distances in a set
        distances = {
            distance_squared(p1, p2),
            distance_squared(p1, p3),
            distance_squared(p1, p4),
            distance_squared(p2, p3),
            distance_squared(p2, p4),
            distance_squared(p3, p4),
        }

        # A valid square must have exactly two unique distances:
        # - One for the sides (shorter distance)
        # - One for the diagonals (longer distance)
        if len(distances) != 2:
            return False

        # Extract the two unique distances
        side, diagonal = sorted(distances)

        # Check that the diagonal is exactly twice the side (Pythagoras theorem)
        if diagonal != 2 * side:
            return False

        # Ensure that there are exactly four sides of equal length
        side_count = sum(
            1 for d in distances if d == side
        )
        return side_count == 4

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Valid square
    p1 = [0, 0]
    p2 = [1, 1]
    p3 = [1, 0]
    p4 = [0, 1]
    print(solution.validSquare(p1, p2, p3, p4))  # Expected: True

    # Test Case 2: Not a square (collinear points)
    p1 = [0, 0]
    p2 = [1, 1]
    p3 = [2, 2]
    p4 = [3, 3]
    print(solution.validSquare(p1, p2, p3, p4))  # Expected: False

    # Test Case 3: Not a square (rectangle)
    p1 = [0, 0]
    p2 = [2, 0]
    p3 = [2, 1]
    p4 = [0, 1]
    print(solution.validSquare(p1, p2, p3, p4))  # Expected: False

    # Test Case 4: Valid square with negative coordinates
    p1 = [-1, -1]
    p2 = [-1, 0]
    p3 = [0, -1]
    p4 = [0, 0]
    print(solution.validSquare(p1, p2, p3, p4))  # Expected: True

    # Test Case 5: All points are the same
    p1 = [0, 0]
    p2 = [0, 0]
    p3 = [0, 0]
    p4 = [0, 0]
    print(solution.validSquare(p1, p2, p3, p4))  # Expected: False

"""
Time Complexity:
- Calculating the squared distance between two points is O(1).
- There are 6 pairwise distances to calculate, so the total time complexity is O(1).
- Checking the conditions for a valid square is also O(1).
- Overall time complexity: O(1).

Space Complexity:
- We use a set to store the pairwise distances, which can hold at most 6 elements.
- Overall space complexity: O(1).

Topic: Geometry
"""