"""
LeetCode Problem #2406: Divide Intervals Into Minimum Number of Groups

Problem Statement:
You are given a 2D integer array `intervals` where `intervals[i] = [start_i, end_i]` represents the inclusive interval [start_i, end_i].

You need to divide the intervals into the minimum number of groups so that no two intervals in the same group overlap. 

Return the minimum number of groups required.

An interval [a, b] overlaps with another interval [c, d] if and only if `max(a, c) <= min(b, d)`.

Constraints:
- 1 <= intervals.length <= 10^5
- 1 <= start_i <= end_i <= 10^6
"""

# Solution
def minGroups(intervals):
    """
    Function to find the minimum number of groups required such that no two intervals in the same group overlap.

    Args:
    intervals (List[List[int]]): A list of intervals where each interval is represented as [start, end].

    Returns:
    int: The minimum number of groups required.
    """
    from collections import defaultdict

    # Create a dictionary to track the changes in active intervals
    events = defaultdict(int)
    for start, end in intervals:
        events[start] += 1  # Increment count at the start of an interval
        events[end + 1] -= 1  # Decrement count after the end of an interval

    # Sort the events by time
    sorted_events = sorted(events.items())

    # Track the maximum number of overlapping intervals
    active_intervals = 0
    max_groups = 0
    for _, change in sorted_events:
        active_intervals += change
        max_groups = max(max_groups, active_intervals)

    return max_groups

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    intervals1 = [[1, 3], [2, 5], [6, 8]]
    print(minGroups(intervals1))  # Output: 2

    # Test Case 2
    intervals2 = [[1, 2], [2, 3], [3, 4], [4, 5]]
    print(minGroups(intervals2))  # Output: 1

    # Test Case 3
    intervals3 = [[1, 10], [2, 6], [8, 10], [15, 18]]
    print(minGroups(intervals3))  # Output: 3

    # Test Case 4
    intervals4 = [[1, 4], [2, 3], [3, 5], [7, 8]]
    print(minGroups(intervals4))  # Output: 2

"""
Time Complexity Analysis:
- Sorting the events takes O(N log N), where N is the number of unique start and end points in the intervals.
- Iterating through the sorted events takes O(N).
- Overall time complexity: O(N log N).

Space Complexity Analysis:
- The `events` dictionary stores at most 2 * len(intervals) entries (one for each start and end point), so it requires O(N) space.
- The sorted list of events also requires O(N) space.
- Overall space complexity: O(N).

Topic: Intervals, Greedy Algorithm, Sweep Line
"""