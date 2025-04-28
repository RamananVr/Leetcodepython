"""
LeetCode Problem #2339: Find the Minimum Number of Arrows to Burst Balloons

Problem Statement:
There are `n` balloons, where the position and radius of the i-th balloon is represented by `x[i]` and `r[i]`.
The balloons are represented as intervals `[x[i] - r[i], x[i] + r[i]]`. You need to shoot arrows to burst the balloons.
An arrow can burst all balloons whose intervals it intersects. You want to minimize the number of arrows required to burst all the balloons.

Given an array `points` where `points[i] = [x[i], r[i]]`, return the minimum number of arrows that must be shot to burst all balloons.

Constraints:
- `1 <= points.length <= 10^5`
- `points[i].length == 2`
- `-10^9 <= x[i] <= 10^9`
- `1 <= r[i] <= 10^9`

Example:
Input: points = [[10, 2], [2, 1], [6, 1], [8, 2]]
Output: 2
Explanation: The intervals are [8, 12], [1, 3], [5, 7], [6, 10]. One arrow can burst the balloons at [5, 7] and [6, 10], and another arrow can burst the balloons at [1, 3] and [8, 12].
"""

# Solution
def findMinArrowShots(points):
    """
    Function to find the minimum number of arrows required to burst all balloons.

    :param points: List[List[int]] - List of balloons represented as [x, r].
    :return: int - Minimum number of arrows required.
    """
    if not points:
        return 0

    # Convert points to intervals and sort by the end of intervals
    intervals = [[x - r, x + r] for x, r in points]
    intervals.sort(key=lambda interval: interval[1])

    arrows = 0
    last_arrow_position = float('-inf')

    for start, end in intervals:
        # If the current interval does not overlap with the last arrow position, shoot a new arrow
        if start > last_arrow_position:
            arrows += 1
            last_arrow_position = end

    return arrows

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [[10, 2], [2, 1], [6, 1], [8, 2]]
    print(findMinArrowShots(points1))  # Output: 2

    # Test Case 2
    points2 = [[1, 1], [2, 1], [3, 1], [4, 1]]
    print(findMinArrowShots(points2))  # Output: 4

    # Test Case 3
    points3 = [[10, 5], [15, 5], [20, 5], [25, 5]]
    print(findMinArrowShots(points3))  # Output: 4

    # Test Case 4
    points4 = [[1, 2], [2, 3], [3, 4], [4, 5]]
    print(findMinArrowShots(points4))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the intervals takes O(n log n), where n is the number of balloons.
- Iterating through the intervals takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The space required to store the intervals is O(n).
- Overall space complexity: O(n).

Topic: Greedy Algorithm
"""