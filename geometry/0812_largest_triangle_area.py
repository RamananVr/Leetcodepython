"""
LeetCode Question #812: Largest Triangle Area

Problem Statement:
You are given an array of points in the 2D plane, where points[i] = [xi, yi] represents a point on the plane. 
Return the area of the largest triangle that can be formed by any three of the points.

The area of a triangle with vertices (x1, y1), (x2, y2), and (x3, y3) is given by:
    Area = |x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)| / 2

You may assume that the given points are all distinct.

Constraints:
- 3 <= points.length <= 50
- points[i].length == 2
- -50 <= xi, yi <= 50
- All the given points are unique.
"""

# Solution
from typing import List

def largestTriangleArea(points: List[List[int]]) -> float:
    def calculate_area(p1, p2, p3):
        # Using the formula for the area of a triangle given three vertices
        return abs(
            p1[0] * (p2[1] - p3[1]) +
            p2[0] * (p3[1] - p1[1]) +
            p3[0] * (p1[1] - p2[1])
        ) / 2

    n = len(points)
    max_area = 0

    # Iterate through all combinations of three points
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                max_area = max(max_area, calculate_area(points[i], points[j], points[k]))

    return max_area

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    print(largestTriangleArea(points1))  # Expected Output: 2.0

    # Test Case 2
    points2 = [[1, 0], [0, 0], [0, 1]]
    print(largestTriangleArea(points2))  # Expected Output: 0.5

    # Test Case 3
    points3 = [[-50, -50], [50, -50], [50, 50], [-50, 50]]
    print(largestTriangleArea(points3))  # Expected Output: 5000.0

    # Test Case 4
    points4 = [[0, 0], [1, 1], [2, 2], [3, 3]]
    print(largestTriangleArea(points4))  # Expected Output: 0.0 (Collinear points)

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves iterating through all combinations of three points from the input list.
- The number of combinations is C(n, 3) = n * (n-1) * (n-2) / 6, where n is the number of points.
- Therefore, the time complexity is O(n^3).

Space Complexity:
- The space complexity is O(1) since we are only using a few variables to store intermediate results and no additional data structures.

Topic: Geometry
"""