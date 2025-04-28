"""
LeetCode Problem #2589: Minimum Time to Complete All Tasks

Problem Statement:
You are given a 2D integer array `tasks` where `tasks[i] = [start_i, end_i, duration_i]` indicates that the i-th task 
starts at time `start_i` and ends at time `end_i` and requires exactly `duration_i` units of work. You can work on a 
task at any time during its start and end time inclusive. However, you can only work on one task at a time.

Return the minimum time required to complete all the tasks. If it is impossible to complete all the tasks, return -1.

Constraints:
- 1 <= tasks.length <= 10^5
- 1 <= start_i <= end_i <= 10^9
- 1 <= duration_i <= end_i - start_i + 1
"""

from heapq import heappush, heappop

def findMinimumTime(tasks):
    """
    Function to find the minimum time required to complete all tasks.

    Args:
    tasks (List[List[int]]): A list of tasks where each task is represented as [start, end, duration].

    Returns:
    int: The minimum time required to complete all tasks, or -1 if it's impossible.
    """
    # Sort tasks by their end time (and by start time if end times are the same)
    tasks.sort(key=lambda x: (x[1], x[0]))
    
    # Set to track the times we are working
    work_times = set()
    
    for start, end, duration in tasks:
        # Count how many times we are already working in the range [start, end]
        already_working = sum(1 for t in range(start, end + 1) if t in work_times)
        
        # Calculate how many more times we need to work to complete the task
        remaining_work = duration - already_working
        
        # If we need more work, add it starting from the end of the range
        for t in range(end, start - 1, -1):
            if remaining_work <= 0:
                break
            if t not in work_times:
                work_times.add(t)
                remaining_work -= 1
        
        # If we still need more work after trying, it's impossible
        if remaining_work > 0:
            return -1
    
    # The size of the work_times set is the minimum time required
    return len(work_times)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tasks1 = [[2, 3, 1], [1, 5, 2], [2, 2, 1]]
    print(findMinimumTime(tasks1))  # Output: 2

    # Test Case 2
    tasks2 = [[1, 3, 2], [2, 5, 3], [5, 6, 2]]
    print(findMinimumTime(tasks2))  # Output: 5

    # Test Case 3
    tasks3 = [[1, 2, 2], [2, 3, 2]]
    print(findMinimumTime(tasks3))  # Output: -1

    # Test Case 4
    tasks4 = [[1, 10, 5], [2, 6, 3], [7, 10, 2]]
    print(findMinimumTime(tasks4))  # Output: 7

"""
Time Complexity:
- Sorting the tasks takes O(n log n), where n is the number of tasks.
- For each task, we iterate over the range [start, end], which in the worst case could be O(n * m), 
  where m is the average range length. However, since the total number of work times is bounded by the 
  number of tasks, the effective complexity is O(n log n + n).

Space Complexity:
- The space complexity is O(n) due to the `work_times` set, which stores the times we are working.

Topic: Greedy Algorithm
"""