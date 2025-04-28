"""
LeetCode Question #2580: Count Ways to Group Overlapping Ranges

Problem Statement:
You are given a 2D integer array `ranges` where `ranges[i] = [start_i, end_i]` represents an inclusive interval.
You need to count the number of ways to group the intervals such that:
1. Each interval is in exactly one group.
2. If two intervals overlap (i.e., they share at least one common point), they must be in the same group.

Return the number of ways to group the intervals.

Constraints:
- 1 <= ranges.length <= 10^5
- 0 <= start_i <= end_i <= 10^9
"""

# Python Solution
def countWays(ranges):
    """
    Count the number of ways to group overlapping ranges.

    :param ranges: List[List[int]] - List of intervals [start, end].
    :return: int - Number of ways to group the intervals.
    """
    # Step 1: Sort the ranges by their start points
    ranges.sort()

    # Step 2: Merge overlapping intervals
    merged_intervals = []
    for start, end in ranges:
        if not merged_intervals or merged_intervals[-1][1] < start:
            merged_intervals.append([start, end])
        else:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], end)

    # Step 3: Count the number of groups (merged intervals)
    num_groups = len(merged_intervals)

    # Step 4: Calculate the number of ways to group the intervals
    # Each group can either be included or excluded, so there are 2^num_groups ways
    return pow(2, num_groups, 10**9 + 7)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    ranges1 = [[1, 3], [2, 4], [5, 6]]
    print(countWays(ranges1))  # Output: 4

    # Test Case 2
    ranges2 = [[1, 2], [3, 4], [5, 6]]
    print(countWays(ranges2))  # Output: 8

    # Test Case 3
    ranges3 = [[1, 10], [2, 3], [4, 5], [6, 7]]
    print(countWays(ranges3))  # Output: 2

    # Test Case 4
    ranges4 = [[1, 2]]
    print(countWays(ranges4))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the ranges takes O(n log n), where n is the number of intervals.
- Merging the intervals takes O(n), as we iterate through the sorted list once.
- Calculating the number of ways to group the intervals is O(1).
Overall, the time complexity is O(n log n).

Space Complexity:
- The space complexity is O(n) for storing the merged intervals.
- No additional space is used apart from the input and output.
Overall, the space complexity is O(n).

Topic: Arrays, Sorting, Interval Merging
"""