"""
LeetCode Problem #356: Line Reflection

Problem Statement:
Given n points on a 2D plane, find if there is such a line parallel to the y-axis that reflects the given points symmetrically.

In other words, answer whether or not if you fold the plane up along a line parallel to the y-axis, then the given set of points will coincide with itself.

Example 1:
Input: points = [[1,1],[-1,1]]
Output: true
Explanation: We can choose the line x = 0.

Example 2:
Input: points = [[1,1],[-1,-1]]
Output: false
Explanation: No line can make the points symmetric.

Constraints:
- n == points.length
- 1 <= n <= 10^4
- -10^8 <= points[i][0] <= 10^8
- -10^8 <= points[i][1] <= 10^8
"""

def isReflected(points):
    """
    Determines if there exists a vertical line of reflection such that the given points are symmetric.

    :param points: List[List[int]] - A list of points on a 2D plane.
    :return: bool - True if a line of reflection exists, False otherwise.
    """
    # Use a set to store unique points
    point_set = set(map(tuple, points))
    
    # Find the minimum and maximum x-coordinates
    min_x = min(x for x, y in points)
    max_x = max(x for x, y in points)
    
    # Calculate the potential line of reflection
    reflection_line = (min_x + max_x) / 2
    
    # Check if every point has its reflected counterpart
    for x, y in points:
        reflected_point = (2 * reflection_line - x, y)
        if reflected_point not in point_set:
            return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [[1, 1], [-1, 1]]
    print(isReflected(points1))  # Output: True

    # Test Case 2
    points2 = [[1, 1], [-1, -1]]
    print(isReflected(points2))  # Output: False

    # Test Case 3
    points3 = [[0, 0], [2, 0], [1, 1]]
    print(isReflected(points3))  # Output: True

    # Test Case 4
    points4 = [[1, 1], [2, 2], [3, 3]]
    print(isReflected(points4))  # Output: False

    # Test Case 5
    points5 = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
    print(isReflected(points5))  # Output: True

"""
Time Complexity:
- Calculating the min and max x-coordinates takes O(n).
- Checking each point for its reflected counterpart takes O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(n) due to the set used to store unique points.

Topic: Hashing, Geometry
"""