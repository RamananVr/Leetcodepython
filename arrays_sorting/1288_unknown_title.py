"""
LeetCode Problem #1288: Remove Covered Intervals

Problem Statement:
You are given a list of `intervals` where `intervals[i] = [li, ri]` represent the interval [li, ri).
An interval [a, b) is covered by an interval [c, d) if and only if c <= a and b <= d.

After removing all covered intervals, return the number of remaining intervals.

Example 1:
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], so it is removed.

Example 2:
Input: intervals = [[1,4],[2,3]]
Output: 1

Constraints:
- 1 <= intervals.length <= 1000
- intervals[i].length == 2
- 0 <= li < ri <= 10^5
- All the given intervals are unique.
"""

def removeCoveredIntervals(intervals):
    """
    Removes covered intervals and returns the count of remaining intervals.

    :param intervals: List[List[int]] - List of intervals
    :return: int - Number of remaining intervals
    """
    # Step 1: Sort intervals by start point. If start points are the same, sort by end point in descending order.
    intervals.sort(key=lambda x: (x[0], -x[1]))
    
    # Step 2: Initialize variables to track the end of the current interval and the count of remaining intervals.
    remaining_intervals = 0
    current_end = 0

    # Step 3: Iterate through the sorted intervals.
    for _, end in intervals:
        # If the current interval is not covered by the previous one, increment the count.
        if end > current_end:
            remaining_intervals += 1
            current_end = end  # Update the current end to the end of this interval.

    return remaining_intervals

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    intervals1 = [[1, 4], [3, 6], [2, 8]]
    print(removeCoveredIntervals(intervals1))  # Output: 2

    # Test Case 2
    intervals2 = [[1, 4], [2, 3]]
    print(removeCoveredIntervals(intervals2))  # Output: 1

    # Test Case 3
    intervals3 = [[1, 2], [1, 4], [3, 4]]
    print(removeCoveredIntervals(intervals3))  # Output: 1

    # Test Case 4
    intervals4 = [[1, 10], [2, 9], [3, 8], [4, 7]]
    print(removeCoveredIntervals(intervals4))  # Output: 1

    # Test Case 5
    intervals5 = [[1, 2], [2, 3], [3, 4]]
    print(removeCoveredIntervals(intervals5))  # Output: 3

"""
Time Complexity Analysis:
1. Sorting the intervals takes O(n log n), where n is the number of intervals.
2. Iterating through the intervals takes O(n).
Overall time complexity: O(n log n).

Space Complexity Analysis:
1. The sorting operation uses O(1) additional space if done in-place.
2. No additional data structures are used.
Overall space complexity: O(1).

Topic: Arrays, Sorting
"""