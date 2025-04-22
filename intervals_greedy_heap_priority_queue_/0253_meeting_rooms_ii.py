"""
LeetCode Question #253: Meeting Rooms II

Problem Statement:
Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, 
return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:
1. 1 <= intervals.length <= 10^4
2. 0 <= start_i < end_i <= 10^6
"""

from heapq import heappush, heappop

def minMeetingRooms(intervals):
    """
    Function to calculate the minimum number of meeting rooms required.
    
    Args:
    intervals (List[List[int]]): A list of meeting time intervals.
    
    Returns:
    int: The minimum number of meeting rooms required.
    """
    if not intervals:
        return 0

    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Min-heap to track the end times of meetings
    heap = []

    # Add the first meeting's end time to the heap
    heappush(heap, intervals[0][1])

    # Iterate over the remaining intervals
    for i in range(1, len(intervals)):
        # If the current meeting starts after the earliest ending meeting, reuse the room
        if intervals[i][0] >= heap[0]:
            heappop(heap)

        # Add the current meeting's end time to the heap
        heappush(heap, intervals[i][1])

    # The size of the heap is the number of rooms required
    return len(heap)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    intervals1 = [[0, 30], [5, 10], [15, 20]]
    print("Test Case 1 Output:", minMeetingRooms(intervals1))  # Expected Output: 2

    # Test Case 2
    intervals2 = [[7, 10], [2, 4]]
    print("Test Case 2 Output:", minMeetingRooms(intervals2))  # Expected Output: 1

    # Test Case 3
    intervals3 = [[1, 5], [2, 6], [8, 9], [8, 9]]
    print("Test Case 3 Output:", minMeetingRooms(intervals3))  # Expected Output: 3

    # Test Case 4
    intervals4 = [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]
    print("Test Case 4 Output:", minMeetingRooms(intervals4))  # Expected Output: 4

"""
Time Complexity:
- Sorting the intervals takes O(n log n), where n is the number of intervals.
- Inserting and removing elements from the heap takes O(log k), where k is the size of the heap.
- In the worst case, we perform these heap operations for all n intervals, resulting in O(n log n) for heap operations.
- Overall time complexity: O(n log n).

Space Complexity:
- The heap stores at most n end times, so the space complexity is O(n).

Topic: Intervals, Greedy, Heap (Priority Queue)
"""