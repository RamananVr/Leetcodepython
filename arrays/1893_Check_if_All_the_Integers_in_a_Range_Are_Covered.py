"""
LeetCode Problem #1893: Check if All the Integers in a Range Are Covered

Problem Statement:
You are given a 2D integer array `ranges` and two integers `left` and `right`. Each `ranges[i] = [start_i, end_i]` represents an inclusive interval.

Return `true` if every integer in the inclusive range `[left, right]` is covered by at least one interval in `ranges`. Otherwise, return `false`.

An integer `x` is covered by an interval `[a, b]` if `a <= x <= b`.

Constraints:
- 1 <= ranges.length <= 50
- 1 <= start_i <= end_i <= 50
- 1 <= left <= right <= 50
"""

def isCovered(ranges, left, right):
    """
    Check if all integers in the range [left, right] are covered by at least one interval in ranges.

    :param ranges: List[List[int]] - List of intervals [start, end]
    :param left: int - Start of the target range
    :param right: int - End of the target range
    :return: bool - True if all integers in [left, right] are covered, False otherwise
    """
    # Create a boolean array to track coverage for numbers 1 to 50
    covered = [False] * 51

    # Mark all numbers covered by the intervals in ranges
    for start, end in ranges:
        for i in range(start, end + 1):
            covered[i] = True

    # Check if all numbers in the range [left, right] are covered
    for i in range(left, right + 1):
        if not covered[i]:
            return False

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    ranges = [[1, 2], [3, 4], [5, 6]]
    left = 2
    right = 5
    print(isCovered(ranges, left, right))  # Expected: True

    # Test Case 2
    ranges = [[1, 10], [10, 20]]
    left = 21
    right = 21
    print(isCovered(ranges, left, right))  # Expected: False

    # Test Case 3
    ranges = [[1, 50]]
    left = 1
    right = 50
    print(isCovered(ranges, left, right))  # Expected: True

    # Test Case 4
    ranges = [[1, 2], [3, 4], [6, 7]]
    left = 5
    right = 6
    print(isCovered(ranges, left, right))  # Expected: False

"""
Time Complexity:
- Marking the covered array: O(n * m), where n is the number of intervals in `ranges` and m is the average length of each interval.
- Checking the range [left, right]: O(k), where k = right - left + 1.
- Overall: O(n * m + k).

Space Complexity:
- The `covered` array has a fixed size of 51, so the space complexity is O(1) (constant space).

Topic: Arrays
"""