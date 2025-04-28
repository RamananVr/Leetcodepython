"""
LeetCode Problem #1779: Find Nearest Point That Has the Same X or Y Coordinate

Problem Statement:
You are given two integers, `x` and `y`, which represent your current location on a Cartesian grid. 
You are also given an array `points` where each `points[i] = [xi, yi]` represents that a point exists at `(xi, yi)` on the grid. 
A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-based) of the valid point with the smallest Manhattan distance from your current location. 
If there are multiple valid points with the same smallest Manhattan distance, return the smallest index. 
If there are no valid points, return -1.

The Manhattan distance between two points `(x1, y1)` and `(x2, y2)` is `abs(x1 - x2) + abs(y1 - y2)`.

Example 1:
Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
Output: 2
Explanation: Of all the points, only [3,1], [2,4], and [4,4] are valid. 
The distances from (3,4) to these points are 3, 1, and 1, respectively.
The point [2,4] and [4,4] have the same distance, so return the smallest index 2.

Example 2:
Input: x = 3, y = 4, points = [[3,4]]
Output: 0
Explanation: The point [3,4] is the only valid point, so return its index.

Example 3:
Input: x = 3, y = 4, points = [[2,3]]
Output: -1
Explanation: There are no valid points.

Constraints:
- 1 <= points.length <= 10^4
- points[i].length == 2
- 1 <= x, y, xi, yi <= 10^4
"""

def nearestValidPoint(x: int, y: int, points: list[list[int]]) -> int:
    """
    Finds the index of the nearest valid point that shares the same x or y coordinate.
    If no valid point exists, returns -1.
    """
    min_distance = float('inf')
    result_index = -1

    for i, (xi, yi) in enumerate(points):
        # Check if the point is valid
        if xi == x or yi == y:
            # Calculate Manhattan distance
            distance = abs(x - xi) + abs(y - yi)
            # Update the result if this point is closer or has a smaller index
            if distance < min_distance:
                min_distance = distance
                result_index = i

    return result_index

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    x1, y1, points1 = 3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
    print(nearestValidPoint(x1, y1, points1))  # Output: 2

    # Test Case 2
    x2, y2, points2 = 3, 4, [[3, 4]]
    print(nearestValidPoint(x2, y2, points2))  # Output: 0

    # Test Case 3
    x3, y3, points3 = 3, 4, [[2, 3]]
    print(nearestValidPoint(x3, y3, points3))  # Output: -1

    # Test Case 4
    x4, y4, points4 = 5, 5, [[5, 6], [7, 5], [5, 5], [6, 6]]
    print(nearestValidPoint(x4, y4, points4))  # Output: 2

    # Test Case 5
    x5, y5, points5 = 1, 1, [[2, 2], [3, 3], [4, 4]]
    print(nearestValidPoint(x5, y5, points5))  # Output: -1

"""
Time Complexity Analysis:
- The function iterates through the `points` list once, performing constant-time operations for each point.
- Let `n` be the length of the `points` list.
- Time complexity: O(n)

Space Complexity Analysis:
- The function uses a constant amount of extra space, regardless of the input size.
- Space complexity: O(1)

Topic: Arrays
"""