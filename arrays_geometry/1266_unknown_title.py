"""
LeetCode Problem #1266: Minimum Time Visiting All Points

Problem Statement:
On a 2D plane, there are `n` points, where the `i-th` point is given as `points[i] = [xi, yi]`. 
Return the minimum time in seconds to visit all the points in the order given by `points`.

You can move according to these rules:
1. In 1 second, you can either:
   - Move vertically by 1 unit,
   - Move horizontally by 1 unit, or
   - Move diagonally by 1 unit.
2. You have to visit the points in the same order as they appear in the array.
3. You are allowed to pass through points that appear later in the order, but these do not count as visits.

Constraints:
- `points.length == n`
- `1 <= n <= 100`
- `points[i].length == 2`
- `-1000 <= points[i][0], points[i][1] <= 1000`

"""

def minTimeToVisitAllPoints(points):
    """
    Calculate the minimum time to visit all points in the given order.

    :param points: List[List[int]] - A list of points on a 2D plane.
    :return: int - The minimum time to visit all points.
    """
    total_time = 0
    for i in range(1, len(points)):
        # Calculate the time to move from points[i-1] to points[i]
        x_diff = abs(points[i][0] - points[i-1][0])
        y_diff = abs(points[i][1] - points[i-1][1])
        # The time is the maximum of the x and y differences (diagonal movement is optimal)
        total_time += max(x_diff, y_diff)
    return total_time

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [[1, 1], [3, 4], [-1, 0]]
    print(minTimeToVisitAllPoints(points1))  # Expected Output: 7

    # Test Case 2
    points2 = [[3, 2], [-2, 2]]
    print(minTimeToVisitAllPoints(points2))  # Expected Output: 5

    # Test Case 3
    points3 = [[0, 0], [1, 1], [1, 2]]
    print(minTimeToVisitAllPoints(points3))  # Expected Output: 2

    # Test Case 4
    points4 = [[0, 0]]
    print(minTimeToVisitAllPoints(points4))  # Expected Output: 0

"""
Time Complexity Analysis:
- The function iterates through the list of points once, calculating the time to move between consecutive points.
- Let `n` be the number of points. The time complexity is O(n).

Space Complexity Analysis:
- The function uses a constant amount of extra space for variables like `total_time`, `x_diff`, and `y_diff`.
- The space complexity is O(1).

Topic: Arrays, Geometry
"""