"""
LeetCode Question #452: Minimum Number of Arrows to Burst Balloons

Problem Statement:
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [x_start, x_end]` denotes a balloon whose horizontal diameter stretches between `x_start` and `x_end`. You don't know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with `x_start` and `x_end` is burst by an arrow shot at `x` if `x_start <= x <= x_end`. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array `points`, return the minimum number of arrows that must be shot to burst all balloons.

Constraints:
- `1 <= points.length <= 10^5`
- `points[i].length == 2`
- `-2^31 <= x_start < x_end <= 2^31 - 1`
"""

# Solution
def findMinArrowShots(points):
    """
    Function to find the minimum number of arrows required to burst all balloons.

    :param points: List[List[int]] - List of intervals representing balloons
    :return: int - Minimum number of arrows required
    """
    if not points:
        return 0

    # Sort the balloons by their ending points
    points.sort(key=lambda x: x[1])

    arrows = 1  # At least one arrow is needed
    current_end = points[0][1]  # Track the end of the first balloon

    for x_start, x_end in points[1:]:
        # If the current balloon starts after the end of the previous balloon, we need a new arrow
        if x_start > current_end:
            arrows += 1
            current_end = x_end  # Update the end to the current balloon's end

    return arrows

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print(findMinArrowShots(points1))  # Expected Output: 2

    # Test Case 2
    points2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    print(findMinArrowShots(points2))  # Expected Output: 4

    # Test Case 3
    points3 = [[1, 2], [2, 3], [3, 4], [4, 5]]
    print(findMinArrowShots(points3))  # Expected Output: 2

    # Test Case 4
    points4 = [[1, 10], [2, 3], [4, 5], [6, 7], [8, 9]]
    print(findMinArrowShots(points4))  # Expected Output: 1

    # Test Case 5
    points5 = [[1, 2]]
    print(findMinArrowShots(points5))  # Expected Output: 1

    # Test Case 6
    points6 = [[2, 3], [2, 3]]
    print(findMinArrowShots(points6))  # Expected Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the `points` array takes O(n log n), where n is the number of balloons.
- Iterating through the sorted array takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation uses O(n) space in the worst case for the sorting algorithm.
- No additional space is used apart from a few variables.
- Overall space complexity: O(n).

Topic: Greedy Algorithm
"""