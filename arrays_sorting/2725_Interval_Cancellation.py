"""
LeetCode Problem #2725: Interval Cancellation

Problem Statement:
You are given a list of intervals where each interval is represented as a pair of integers [start, end]. 
An interval [start, end] represents all the integers from start to end inclusive. 
Your task is to return a list of intervals after removing all overlapping intervals.

Two intervals [a, b] and [c, d] are considered overlapping if they share at least one integer, 
i.e., max(a, c) <= min(b, d).

The output list should be sorted in ascending order by the start of the intervals. 
If two intervals have the same start, sort them by their end.

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- -10^6 <= intervals[i][0] <= intervals[i][1] <= 10^6
"""

# Python Solution
def removeOverlappingIntervals(intervals):
    """
    Removes overlapping intervals from the given list of intervals.

    Args:
    intervals (List[List[int]]): A list of intervals where each interval is represented as [start, end].

    Returns:
    List[List[int]]: A list of non-overlapping intervals sorted by start and end.
    """
    # Sort intervals by start time, and by end time if start times are the same
    intervals.sort(key=lambda x: (x[0], x[1]))
    
    result = []
    for interval in intervals:
        # If the result list is empty or the current interval does not overlap with the last interval in result
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            # Merge the intervals by updating the end of the last interval in result
            result[-1][1] = max(result[-1][1], interval[1])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(removeOverlappingIntervals(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]

    # Test Case 2
    intervals = [[1, 4], [4, 5]]
    print(removeOverlappingIntervals(intervals))  # Output: [[1, 5]]

    # Test Case 3
    intervals = [[1, 2], [3, 4], [5, 6]]
    print(removeOverlappingIntervals(intervals))  # Output: [[1, 2], [3, 4], [5, 6]]

    # Test Case 4
    intervals = [[1, 10], [2, 3], [4, 5], [6, 7], [8, 9]]
    print(removeOverlappingIntervals(intervals))  # Output: [[1, 10]]

    # Test Case 5
    intervals = [[1, 4], [0, 2], [3, 5]]
    print(removeOverlappingIntervals(intervals))  # Output: [[0, 5]]

# Time Complexity Analysis:
# Sorting the intervals takes O(n log n), where n is the number of intervals.
# The for loop iterates through the intervals once, which takes O(n).
# Therefore, the overall time complexity is O(n log n).

# Space Complexity Analysis:
# The space complexity is O(n) for the result list, where n is the number of intervals.
# Sorting the intervals in-place does not require additional space.
# Therefore, the overall space complexity is O(n).

# Topic: Arrays, Sorting