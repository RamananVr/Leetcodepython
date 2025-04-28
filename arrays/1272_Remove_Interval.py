"""
LeetCode Problem #1272: Remove Interval

Problem Statement:
You are given a 2D array `intervals`, where each `intervals[i] = [start_i, end_i]` represents the interval [start_i, end_i) (inclusive of start_i and exclusive of end_i). 
You are also given an interval `toBeRemoved = [start_r, end_r]`, representing the interval to be removed from `intervals`.

Return a list of intervals after removing `toBeRemoved` from `intervals`. The intervals should be returned in the same order as they appear in the input.

An interval [a, b) is the part of the interval that satisfies `a <= x < b`.

Constraints:
- 1 <= intervals.length <= 10^4
- -10^9 <= start_i < end_i <= 10^9
- -10^9 <= start_r < end_r <= 10^9

Example:
Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]

Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]
"""

def removeInterval(intervals, toBeRemoved):
    """
    Removes the interval `toBeRemoved` from the list of intervals.

    Args:
    intervals (List[List[int]]): List of intervals [start, end).
    toBeRemoved (List[int]): Interval [start, end) to be removed.

    Returns:
    List[List[int]]: List of intervals after removing `toBeRemoved`.
    """
    result = []
    remove_start, remove_end = toBeRemoved

    for start, end in intervals:
        # If the current interval is completely outside the removal range
        if end <= remove_start or start >= remove_end:
            result.append([start, end])
        else:
            # If there's a left part of the interval that remains
            if start < remove_start:
                result.append([start, remove_start])
            # If there's a right part of the interval that remains
            if end > remove_end:
                result.append([remove_end, end])

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    intervals = [[0, 2], [3, 4], [5, 7]]
    toBeRemoved = [1, 6]
    print(removeInterval(intervals, toBeRemoved))  # Expected Output: [[0, 1], [6, 7]]

    # Test Case 2
    intervals = [[0, 5]]
    toBeRemoved = [2, 3]
    print(removeInterval(intervals, toBeRemoved))  # Expected Output: [[0, 2], [3, 5]]

    # Test Case 3
    intervals = [[0, 10]]
    toBeRemoved = [3, 7]
    print(removeInterval(intervals, toBeRemoved))  # Expected Output: [[0, 3], [7, 10]]

    # Test Case 4
    intervals = [[0, 2], [3, 5], [6, 8]]
    toBeRemoved = [4, 7]
    print(removeInterval(intervals, toBeRemoved))  # Expected Output: [[0, 2], [3, 4], [7, 8]]

    # Test Case 5
    intervals = [[0, 1], [2, 3], [4, 5]]
    toBeRemoved = [1, 4]
    print(removeInterval(intervals, toBeRemoved))  # Expected Output: [[0, 1], [4, 5]]

"""
Time Complexity Analysis:
- Let `n` be the number of intervals in the input list `intervals`.
- For each interval, we perform constant-time operations to check overlap and potentially split the interval.
- Therefore, the time complexity is O(n).

Space Complexity Analysis:
- The space complexity is O(n) for the result list, as we store at most `n` intervals in the output.

Topic: Arrays
"""