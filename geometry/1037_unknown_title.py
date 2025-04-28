"""
LeetCode Problem #1037: Valid Boomerang

Problem Statement:
A boomerang is a set of three points that are all distinct and not in a straight line.

Given a list of three points in the plane, return true if and only if they form a boomerang.

You can represent the points as a list of two-element lists, where each list represents a point in a 2D plane.

Example 1:
Input: points = [[1,1],[2,3],[3,2]]
Output: true

Example 2:
Input: points = [[1,1],[2,2],[3,3]]
Output: false

Note:
- points.length == 3
- points[i].length == 2
- 0 <= points[i][j] <= 100
"""

def isBoomerang(points):
    """
    Determines if three points form a boomerang (not in a straight line).

    Args:
    points (List[List[int]]): A list of three points in the 2D plane.

    Returns:
    bool: True if the points form a boomerang, False otherwise.
    """
    # Extract the points
    (x1, y1), (x2, y2), (x3, y3) = points

    # Check if the points are distinct
    if (x1, y1) == (x2, y2) or (x1, y1) == (x3, y3) or (x2, y2) == (x3, y3):
        return False

    # Check if the points are collinear using the slope formula
    # Instead of calculating the slope directly (to avoid division by zero),
    # we use the cross product to determine collinearity:
    # (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)
    return (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Points form a boomerang
    points1 = [[1, 1], [2, 3], [3, 2]]
    print(isBoomerang(points1))  # Output: True

    # Test Case 2: Points are collinear
    points2 = [[1, 1], [2, 2], [3, 3]]
    print(isBoomerang(points2))  # Output: False

    # Test Case 3: Two points are the same
    points3 = [[1, 1], [1, 1], [2, 2]]
    print(isBoomerang(points3))  # Output: False

    # Test Case 4: Points form a boomerang
    points4 = [[0, 0], [1, 1], [1, 0]]
    print(isBoomerang(points4))  # Output: True

    # Test Case 5: Points are collinear
    points5 = [[0, 0], [0, 1], [0, 2]]
    print(isBoomerang(points5))  # Output: False

"""
Time Complexity:
- Extracting the points takes O(1).
- Checking if the points are distinct takes O(1).
- The collinearity check using the cross product takes O(1).
Overall, the time complexity is O(1).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables.
Overall, the space complexity is O(1).

Topic: Geometry
"""