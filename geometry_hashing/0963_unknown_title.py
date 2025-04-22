"""
LeetCode Problem #963: Minimum Area Rectangle II

Problem Statement:
Given a set of points in the plane, find the minimum area of a rectangle formed from these points, 
with sides parallel to the x and y axes. If no rectangle can be formed, return 0.

A rectangle is defined as a set of four points that form the vertices of a rectangle. 
The sides of the rectangle must be parallel to the x and y axes.

Input:
- points: List[List[int]] - A list of points where each point is represented as [x, y].

Output:
- float - The minimum area of a rectangle formed by the points. If no rectangle can be formed, return 0.

Constraints:
- 1 <= len(points) <= 500
- points[i].length == 2
- 0 <= points[i][0], points[i][1] <= 10^4
- All the points are unique.
"""

# Python Solution
from itertools import combinations
import math

def minAreaFreeRect(points):
    """
    Finds the minimum area of a rectangle formed by the given points.
    
    :param points: List[List[int]] - List of points in the plane.
    :return: float - Minimum area of a rectangle formed by the points, or 0 if no rectangle can be formed.
    """
    point_set = set(map(tuple, points))
    min_area = float('inf')
    
    # Iterate through all pairs of points to find diagonals
    for p1, p2 in combinations(points, 2):
        # Calculate the center and the squared length of the diagonal
        center = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        diagonal_length_squared = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        
        # Iterate through all other points to find rectangles
        for p3 in points:
            if p3 == p1 or p3 == p2:
                continue
            
            # Calculate the fourth point of the rectangle
            p4 = (2 * center[0] - p3[0], 2 * center[1] - p3[1])
            
            # Check if the fourth point exists in the set
            if p4 in point_set:
                # Calculate the area of the rectangle
                side1 = math.sqrt((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2)
                side2 = math.sqrt((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2)
                area = side1 * side2
                min_area = min(min_area, area)
    
    return min_area if min_area != float('inf') else 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [[1, 2], [2, 1], [1, 0], [0, 1]]
    print(minAreaFreeRect(points1))  # Expected Output: 2.0

    # Test Case 2
    points2 = [[0, 0], [1, 1], [1, 0], [0, 1]]
    print(minAreaFreeRect(points2))  # Expected Output: 1.0

    # Test Case 3
    points3 = [[0, 0], [1, 1], [2, 2], [3, 3]]
    print(minAreaFreeRect(points3))  # Expected Output: 0.0

    # Test Case 4
    points4 = [[3, 1], [1, 1], [0, 1], [2, 1], [3, 3], [3, 2]]
    print(minAreaFreeRect(points4))  # Expected Output: 2.0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through all pairs of points (O(n^2)) and checks for rectangles involving other points (O(n)).
- Thus, the overall complexity is O(n^3), where n is the number of points.

Space Complexity:
- The algorithm uses a set to store the points (O(n)) and additional variables for calculations.
- Thus, the space complexity is O(n).
"""

# Topic: Geometry, Hashing