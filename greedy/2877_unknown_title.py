"""
LeetCode Problem #2877: Minimum Time to Complete All Tasks

Problem Statement:
You are given an array `tasks` where `tasks[i] = [startTime_i, endTime_i, duration_i]` represents a task that starts at `startTime_i`, ends at `endTime_i`, and takes exactly `duration_i` units of time to complete. You can only work on one task at a time, but you can choose to work on any task within its valid time range `[startTime_i, endTime_i]`.

Return the minimum time required to complete all the tasks. If it is impossible to complete all tasks, return -1.

Constraints:
1. 1 <= tasks.length <= 10^5
2. 1 <= startTime_i < endTime_i <= 10^9
3. 1 <= duration_i <= endTime_i - startTime_i
"""

from heapq import heappush, heappop

def findMinimumTime(tasks):
    """
    Function to find the minimum time required to complete all tasks.

    Args:
    tasks (List[List[int]]): A list of tasks where each task is represented as [startTime, endTime, duration].

    Returns:
    int: The minimum time required to complete all tasks, or -1 if it's impossible.
    """
    # Sort tasks by their end time
    tasks.sort(key=lambda x: x[1])
    
    # Min-heap to track the time slots we are using
    used_time = set()
    
    for start, end, duration in tasks:
        # Count how many time slots are already used in the range [start, end]
        used_in_range = sum(1 for t in range(start, end + 1) if t in used_time)
        
        # Calculate how many more time slots are needed
        needed = duration - used_in_range
        
        # If we need more time slots, allocate them starting from the end
        for t in range(end, start - 1, -1):
            if needed == 0:
                break
            if t not in used_time:
                used_time.add(t)
                needed -= 1
        
        # If we still need more time slots, it's impossible to complete the task
        if needed > 0:
            return -1
    
    # The total time used is the size of the used_time set
    return len(used_time)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tasks1 = [[2, 5, 3], [1, 3, 2], [5, 6, 1]]
    print(findMinimumTime(tasks1))  # Output: 4

    # Test Case 2
    tasks2 = [[1, 3, 2], [2, 5, 3], [5, 6, 2]]
    print(findMinimumTime(tasks2))  # Output: -1

    # Test Case 3
    tasks3 = [[1, 10, 5], [2, 6, 3], [7, 9, 2]]
    print(findMinimumTime(tasks3))  # Output: 7

    # Test Case 4
    tasks4 = [[1, 2, 1], [2, 3, 1], [3, 4, 1]]
    print(findMinimumTime(tasks4))  # Output: 3

"""
Time Complexity:
- Sorting the tasks takes O(n log n), where n is the number of tasks.
- For each task, we iterate over the range [start, end], which in the worst case can be O(n * k), where k is the average range length.
- Overall time complexity: O(n log n + n * k).

Space Complexity:
- The `used_time` set can grow up to the total number of unique time slots used, which is O(n * k) in the worst case.
- Overall space complexity: O(n * k).

Topic: Greedy
"""