"""
LeetCode Problem #2436: Minimum Time to Complete All Tasks

Problem Statement:
You are given an array tasks where tasks[i] = [startTime_i, endTime_i, duration_i] indicates that you can start a task at any time between startTime_i and endTime_i (inclusive) and must complete it within duration_i consecutive units of time. You can only work on one task at a time.

Return the minimum time required to complete all the tasks, or -1 if it is impossible to complete all the tasks.

Constraints:
- 1 <= tasks.length <= 10^5
- 1 <= startTime_i <= endTime_i <= 10^9
- 1 <= duration_i <= endTime_i - startTime_i + 1
"""

# Solution
from heapq import heappush, heappop

def minimumTime(tasks):
    # Sort tasks by their end time
    tasks.sort(key=lambda x: x[1])
    
    # Min-heap to track the time slots used
    used_time = []
    
    for start, end, duration in tasks:
        # Add the duration to the heap
        for _ in range(duration):
            heappush(used_time, end)
        
        # Remove time slots that are outside the valid range
        while used_time and used_time[0] < start:
            heappop(used_time)
        
        # If the heap size exceeds the duration, it's impossible to complete the tasks
        if len(used_time) > duration:
            return -1
    
    return len(used_time)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Simple case
    tasks1 = [[1, 3, 2], [2, 5, 3], [3, 6, 1]]
    print(minimumTime(tasks1))  # Expected output: 6

    # Test Case 2: Impossible case
    tasks2 = [[1, 2, 2], [2, 3, 2]]
    print(minimumTime(tasks2))  # Expected output: -1

    # Test Case 3: Large range
    tasks3 = [[1, 100, 50], [50, 150, 50], [100, 200, 50]]
    print(minimumTime(tasks3))  # Expected output: 150

    # Test Case 4: Single task
    tasks4 = [[1, 10, 5]]
    print(minimumTime(tasks4))  # Expected output: 5

    # Test Case 5: Overlapping tasks
    tasks5 = [[1, 5, 3], [2, 6, 2], [4, 8, 4]]
    print(minimumTime(tasks5))  # Expected output: 9

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the tasks takes O(n log n), where n is the number of tasks.
- Iterating through the tasks and managing the heap takes O(n log n) in the worst case.
- Overall time complexity: O(n log n).

Space Complexity:
- The heap can grow up to size n in the worst case, so the space complexity is O(n).
"""

# Topic: Greedy, Sorting, Heap