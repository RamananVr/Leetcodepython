"""
LeetCode Problem #1453: Maximum Number of Darts Inside a Circular Dartboard

Problem Statement:
You are given an array `points` where `points[i] = [xi, yi]` represents the coordinates of a dart on a 2D plane. 
You are also given an integer `r` which represents the radius of a circular dartboard. 
Return the maximum number of darts that can fit inside or on the boundary of a single circular dartboard with radius `r`.

Constraints:
- 1 <= points.length <= 100
- points[i].length == 2
- -10^4 <= xi, yi <= 10^4
- 1 <= r <= 5000

Example:
Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
Output: 4
Explanation: All points are within the circle centered at (0, 0) with radius 2.

Input: points = [[-3,0],[3,0],[2,2],[2,-2]], r = 2
Output: 3

Input: points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
Output: 4
"""

from math import sqrt, isclose
from itertools import combinations

def numPoints(points, r):
    def distance(p1, p2):
        """Calculate the Euclidean distance between two points."""
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def find_circle_center(p1, p2):
        """Find the center of the circle passing through two points with radius r."""
        d = distance(p1, p2)
        if d > 2 * r:
            return []  # No valid circle can be formed
        mid_x = (p1[0] + p2[0]) / 2
        mid_y = (p1[1] + p2[1]) / 2
        offset = sqrt(r ** 2 - (d / 2) ** 2)
        dx = (p2[1] - p1[1]) / d
        dy = (p1[0] - p2[0]) / d
        return [
            [mid_x + offset * dx, mid_y + offset * dy],
            [mid_x - offset * dx, mid_y - offset * dy]
        ]

    def count_points_inside(center):
        """Count the number of points inside or on the boundary of the circle."""
        count = 0
        for p in points:
            if distance(center, p) <= r + 1e-7:  # Add a small tolerance for floating-point precision
                count += 1
        return count

    max_count = 1  # At least one point is always inside the circle
    for p1, p2 in combinations(points, 2):
        for center in find_circle_center(p1, p2):
            max_count = max(max_count, count_points_inside(center))
    return max_count


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points = [[-2, 0], [2, 0], [0, 2], [0, -2]]
    r = 2
    print(numPoints(points, r))  # Output: 4

    # Test Case 2
    points = [[-3, 0], [3, 0], [2, 2], [2, -2]]
    r = 2
    print(numPoints(points, r))  # Output: 3

    # Test Case 3
    points = [[1, 2], [3, 5], [1, -1], [2, 3], [4, 1], [1, 3]]
    r = 2
    print(numPoints(points, r))  # Output: 4

    # Test Case 4
    points = [[0, 0], [0, 1], [1, 0], [1, 1]]
    r = 1
    print(numPoints(points, r))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates over all pairs of points, which takes O(n^2) time.
- For each pair, it calculates the potential circle centers and counts the points inside the circle, which takes O(n) time.
- Thus, the overall time complexity is O(n^3), where n is the number of points.

Space Complexity:
- The space complexity is O(1) for storing intermediate variables and results, as we do not use any additional data structures that scale with input size.
- Thus, the space complexity is O(1).

Topic: Geometry
"""