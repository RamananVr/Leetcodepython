"""
LeetCode Problem #1610: Maximum Number of Visible Points

Problem Statement:
You are given an array `points`, an integer `angle`, and your location `location`, where:
- `points[i] = [xi, yi]` represents a point located at (xi, yi).
- `location = [x, y]` represents your position.

You can rotate your viewing angle counterclockwise starting from the positive x-axis. You are tasked to find the maximum number of points you can see within the viewing angle.

Constraints:
1. 1 <= points.length <= 10^5
2. points[i].length == 2
3. location.length == 2
4. 0 <= angle < 360
5. 0 <= xi, yi, x, y <= 10^9

Note:
- Points that are exactly at your location are always visible, regardless of the viewing angle.
"""

from math import atan2, degrees
from bisect import bisect_right

def visiblePoints(points, angle, location):
    """
    Function to calculate the maximum number of visible points within a given angle.
    
    :param points: List[List[int]] - List of points on the 2D plane.
    :param angle: int - Viewing angle in degrees.
    :param location: List[int] - Your location on the 2D plane.
    :return: int - Maximum number of visible points.
    """
    x, y = location
    angles = []
    same_location_count = 0

    # Calculate angles for all points relative to the location
    for px, py in points:
        if px == x and py == y:
            same_location_count += 1
        else:
            dx, dy = px - x, py - y
            angles.append(degrees(atan2(dy, dx)))

    # Sort the angles
    angles.sort()

    # Duplicate the angles to handle the circular nature of the problem
    angles += [a + 360 for a in angles]

    # Sliding window to find the maximum number of points within the angle
    max_visible = 0
    for i in range(len(angles) // 2):
        max_visible = max(max_visible, bisect_right(angles, angles[i] + angle) - i)

    return max_visible + same_location_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points = [[2, 1], [2, 2], [3, 3]]
    angle = 90
    location = [1, 1]
    print(visiblePoints(points, angle, location))  # Output: 3

    # Test Case 2
    points = [[2, 1], [2, 2], [3, 4], [1, 1]]
    angle = 90
    location = [1, 1]
    print(visiblePoints(points, angle, location))  # Output: 4

    # Test Case 3
    points = [[1, 0], [2, 1]]
    angle = 13
    location = [1, 1]
    print(visiblePoints(points, angle, location))  # Output: 1

"""
Time Complexity:
- Calculating angles for all points: O(n), where n is the number of points.
- Sorting the angles: O(n log n).
- Sliding window using binary search: O(n log n).
Overall: O(n log n).

Space Complexity:
- Storing angles: O(n).
- Duplicating angles for circular handling: O(n).
Overall: O(n).

Topic: Geometry, Sliding Window, Sorting
"""