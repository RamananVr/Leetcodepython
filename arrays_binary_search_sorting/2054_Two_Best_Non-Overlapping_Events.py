"""
LeetCode Problem #2054: Two Best Non-Overlapping Events

Problem Statement:
You are given a 2D integer array `events` where `events[i] = [startTime_i, endTime_i, value_i]`. 
The `i-th` event starts at `startTime_i` and ends at `endTime_i`, and if you attend this event, 
you will receive a value of `value_i`. You can choose at most two non-overlapping events to attend 
such that the sum of their values is maximized.

Return the maximum sum of values that you can receive by attending at most two non-overlapping events.

Note that the start time and end time of one chosen event cannot overlap with the start time and 
end time of the other chosen event.

Constraints:
- 1 <= events.length <= 10^5
- events[i].length == 3
- 1 <= startTime_i < endTime_i <= 10^9
- 1 <= value_i <= 10^6
"""

from typing import List
import bisect

def maxTwoEvents(events: List[List[int]]) -> int:
    # Sort events by their end time
    events.sort(key=lambda x: x[1])
    
    # Precompute the maximum value up to each event
    max_value_up_to = [0] * len(events)
    max_value = 0
    for i, event in enumerate(events):
        max_value = max(max_value, event[2])
        max_value_up_to[i] = max_value
    
    result = 0
    for i, (start, end, value) in enumerate(events):
        # Find the latest event that ends before the current event starts
        idx = bisect.bisect_right(events, [start, float('inf'), float('inf')], hi=i) - 1
        if idx >= 0:
            result = max(result, value + max_value_up_to[idx])
        else:
            result = max(result, value)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    events1 = [[1, 3, 3], [3, 4, 4], [2, 5, 2]]
    print(maxTwoEvents(events1))  # Expected Output: 7

    # Test Case 2
    events2 = [[1, 3, 2], [4, 5, 2], [6, 7, 4]]
    print(maxTwoEvents(events2))  # Expected Output: 6

    # Test Case 3
    events3 = [[1, 3, 4], [2, 4, 3], [2, 3, 1]]
    print(maxTwoEvents(events3))  # Expected Output: 4

    # Test Case 4
    events4 = [[1, 3, 10], [2, 5, 5], [6, 9, 8]]
    print(maxTwoEvents(events4))  # Expected Output: 18

"""
Time Complexity:
- Sorting the events takes O(n log n), where n is the number of events.
- For each event, we perform a binary search using `bisect_right`, which takes O(log n).
- Thus, the overall time complexity is O(n log n).

Space Complexity:
- The space complexity is O(n) due to the `max_value_up_to` array.

Topic: Arrays, Binary Search, Sorting
"""