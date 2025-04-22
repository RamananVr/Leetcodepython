"""
LeetCode Question #612: Shortest Distance in a Plane

Problem Statement:
Given a table `point` with the following schema:

    +----+-----+-----+
    | id | x   | y   |
    +----+-----+-----+
    | 1  | 0   | 0   |
    | 2  | 1   | 1   |
    | 3  | 2   | 2   |
    | 4  | 3   | 3   |
    +----+-----+-----+

Write an SQL query to find the shortest distance between any two points in the plane. 
The distance between two points (x1, y1) and (x2, y2) is calculated as:

    sqrt((x2 - x1)^2 + (y2 - y1)^2)

Return the result as a single number rounded to 4 decimal places.

Note:
- Each row of the table represents a point in a 2D plane.
- There will be at least two points in the table.

Example:
Input:
    point table:
    +----+-----+-----+
    | id | x   | y   |
    +----+-----+-----+
    | 1  | 0   | 0   |
    | 2  | 1   | 1   |
    | 3  | 2   | 2   |
    +----+-----+-----+

Output:
    1.4142

Explanation:
The shortest distance is between points (0, 0) and (1, 1), which is sqrt((1-0)^2 + (1-0)^2) = sqrt(2) = 1.4142.
"""

# Python Solution
import math
from itertools import combinations

def shortest_distance(points):
    """
    Function to calculate the shortest distance between any two points in a 2D plane.

    :param points: List of tuples, where each tuple represents a point (x, y).
    :return: The shortest distance rounded to 4 decimal places.
    """
    min_distance = float('inf')
    
    # Generate all combinations of two points
    for (x1, y1), (x2, y2) in combinations(points, 2):
        # Calculate the Euclidean distance
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        # Update the minimum distance
        min_distance = min(min_distance, distance)
    
    # Return the shortest distance rounded to 4 decimal places
    return round(min_distance, 4)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [(0, 0), (1, 1), (2, 2)]
    print(shortest_distance(points1))  # Output: 1.4142

    # Test Case 2
    points2 = [(0, 0), (3, 4), (5, 12), (8, 15)]
    print(shortest_distance(points2))  # Output: 5.0

    # Test Case 3
    points3 = [(1, 1), (4, 5), (13, 14), (7, 8)]
    print(shortest_distance(points3))  # Output: 5.0

    # Test Case 4
    points4 = [(0, 0), (0, 1), (1, 0), (1, 1)]
    print(shortest_distance(points4))  # Output: 1.0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Generating all combinations of two points takes O(n^2), where n is the number of points.
- Calculating the Euclidean distance for each pair is O(1).
- Overall, the time complexity is O(n^2).

Space Complexity:
- The space required to store the combinations is O(n^2) in the worst case.
- The space complexity is O(n^2).
"""

# Topic: Geometry, Math, Combinatorics