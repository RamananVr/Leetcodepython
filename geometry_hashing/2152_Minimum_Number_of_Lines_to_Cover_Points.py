"""
LeetCode Problem #2152: Minimum Number of Lines to Cover Points

Problem Statement:
You are given an array `points` where `points[i] = [xi, yi]` represents a point on a 2D plane. 
A line is defined as a set of points that satisfy the equation `y = mx + b` for some constants `m` and `b`. 
A line can cover multiple points.

You need to find the minimum number of lines required to cover all the points in the array. 
Each line can cover any number of points, but all points on the line must satisfy the same equation.

Constraints:
- 1 <= points.length <= 100
- points[i].length == 2
- -10^4 <= xi, yi <= 10^4

Example:
Input: points = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]
Output: 1
Explanation: All points lie on the same line y = x.

Input: points = [[1,1],[2,2],[3,3],[4,5],[5,6],[6,7]]
Output: 2
Explanation: The points can be covered by two lines: y = x and y = x + 1.
"""

from collections import defaultdict
from math import gcd

def minLinesToCoverPoints(points):
    """
    Function to calculate the minimum number of lines required to cover all points.
    :param points: List[List[int]] - List of points on a 2D plane.
    :return: int - Minimum number of lines required.
    """
    def slope(p1, p2):
        """
        Helper function to calculate the slope between two points as a tuple (dy, dx).
        """
        dy = p2[1] - p1[1]
        dx = p2[0] - p1[0]
        if dx == 0:  # Vertical line
            return (float('inf'), 0)
        g = gcd(dy, dx)
        return (dy // g, dx // g)

    n = len(points)
    if n <= 1:
        return n

    lines = defaultdict(set)
    for i in range(n):
        for j in range(i + 1, n):
            s = slope(points[i], points[j])
            lines[s].add(tuple(points[i]))
            lines[s].add(tuple(points[j]))

    covered_points = set()
    line_count = 0

    while len(covered_points) < n:
        max_covered = 0
        best_line = None
        for line, pts in lines.items():
            if len(pts - covered_points) > max_covered:
                max_covered = len(pts - covered_points)
                best_line = line
        covered_points.update(lines[best_line])
        line_count += 1

    return line_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]
    print(minLinesToCoverPoints(points1))  # Output: 1

    # Test Case 2
    points2 = [[1, 1], [2, 2], [3, 3], [4, 5], [5, 6], [6, 7]]
    print(minLinesToCoverPoints(points2))  # Output: 2

    # Test Case 3
    points3 = [[1, 1], [2, 2], [3, 3], [4, 5], [5, 6], [6, 7], [7, 8]]
    print(minLinesToCoverPoints(points3))  # Output: 2

    # Test Case 4
    points4 = [[1, 1], [1, 2], [1, 3], [1, 4]]
    print(minLinesToCoverPoints(points4))  # Output: 1

"""
Time and Space Complexity Analysis:
- Time Complexity: O(n^3)
  - Calculating slopes between all pairs of points takes O(n^2).
  - Iterating through lines and updating covered points takes O(n^2) in the worst case.
  - Overall complexity is O(n^3) for small input sizes.

- Space Complexity: O(n^2)
  - The `lines` dictionary stores slopes and associated points, which can grow to O(n^2) in the worst case.

Topic: Geometry, Hashing
"""