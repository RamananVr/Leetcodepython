"""
LeetCode Question #1353: Maximum Number of Events That Can Be Attended

Problem Statement:
You are given an array of `events` where `events[i] = [startDayi, endDayi]`. Every event `i` starts at `startDayi` and ends at `endDayi`.

You can attend an event `i` at any day `d` where `startDayi <= d <= endDayi`. You can only attend one event per day, and at most one event can be attended on each day.

Return the maximum number of events you can attend.

Constraints:
1. 1 <= events.length <= 10^5
2. 1 <= startDayi <= endDayi <= 10^5
"""

from heapq import heappop, heappush

def maxEvents(events):
    """
    Function to calculate the maximum number of events that can be attended.

    Args:
    events (List[List[int]]): A list of events where each event is represented as [startDay, endDay].

    Returns:
    int: The maximum number of events that can be attended.
    """
    # Sort events by their start day
    events.sort()
    
    # Min-heap to track the end days of events
    min_heap = []
    day = 0
    attended = 0
    i = 0
    n = len(events)
    
    while i < n or min_heap:
        # If the heap is empty, move to the next event's start day
        if not min_heap:
            day = events[i][0]
        
        # Add all events that start on the current day or earlier to the heap
        while i < n and events[i][0] <= day:
            heappush(min_heap, events[i][1])
            i += 1
        
        # Remove events from the heap that have already ended
        while min_heap and min_heap[0] < day:
            heappop(min_heap)
        
        # Attend the event that ends the earliest
        if min_heap:
            heappop(min_heap)
            attended += 1
            day += 1
    
    return attended

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    events1 = [[1, 2], [2, 3], [3, 4]]
    print(maxEvents(events1))  # Output: 3

    # Test Case 2
    events2 = [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]
    print(maxEvents(events2))  # Output: 4

    # Test Case 3
    events3 = [[1, 2], [2, 3], [3, 4], [1, 2]]
    print(maxEvents(events3))  # Output: 4

    # Test Case 4
    events4 = [[1, 10], [2, 2], [2, 2], [2, 2], [2, 2]]
    print(maxEvents(events4))  # Output: 2

"""
Time Complexity:
- Sorting the events takes O(n log n), where n is the number of events.
- Each event is pushed and popped from the heap at most once, and heap operations take O(log n).
- Therefore, the overall time complexity is O(n log n).

Space Complexity:
- The space complexity is O(n) due to the heap, which can store up to n events in the worst case.

Topic: Greedy, Heap (Priority Queue)
"""