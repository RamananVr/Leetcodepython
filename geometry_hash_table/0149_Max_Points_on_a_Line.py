"""
LeetCode Problem #149: Max Points on a Line

Problem Statement:
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.

Constraints:
- 1 <= points.length <= 300
- points[i].length == 2
- -10^4 <= xi, yi <= 10^4
- All the points are unique.
"""

from collections import defaultdict
from math import gcd

def maxPoints(points):
    """
    Function to find the maximum number of points that lie on the same straight line.

    :param points: List[List[int]] - List of points on the X-Y plane
    :return: int - Maximum number of points on the same line
    """
    if len(points) <= 1:
        return len(points)
    
    def get_slope(p1, p2):
        """
        Helper function to calculate the slope between two points.
        Returns a tuple (dy, dx) representing the reduced slope.
        """
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        if dx == 0:  # Vertical line
            return (float('inf'), 0)
        if dy == 0:  # Horizontal line
            return (0, float('inf'))
        g = gcd(dx, dy)
        return (dy // g, dx // g)
    
    max_points = 0
    
    for i in range(len(points)):
        slopes = defaultdict(int)
        duplicate = 1  # Count the current point itself
        for j in range(i + 1, len(points)):
            if points[i] == points[j]:
                duplicate += 1
            else:
                slope = get_slope(points[i], points[j])
                slopes[slope] += 1
        max_points = max(max_points, duplicate + max(slopes.values(), default=0))
    
    return max_points

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [[1,1],[2,2],[3,3]]
    print(maxPoints(points1))  # Output: 3

    # Test Case 2
    points2 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(maxPoints(points2))  # Output: 4

    # Test Case 3
    points3 = [[0,0],[0,0],[0,0]]
    print(maxPoints(points3))  # Output: 3

    # Test Case 4
    points4 = [[1,1],[1,1],[2,2],[3,3],[4,4]]
    print(maxPoints(points4))  # Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop iterates over all points, so it runs O(n) times.
- The inner loop iterates over all remaining points, so it runs O(n) times for each point.
- Calculating the slope and updating the dictionary takes O(1) for each pair of points.
- Overall, the time complexity is O(n^2).

Space Complexity:
- We use a dictionary to store slopes for each point, which can have at most O(n) entries.
- The space complexity is O(n).

Topic: Geometry, Hash Table
"""