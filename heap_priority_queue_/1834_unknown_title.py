"""
LeetCode Problem #1834: Single-Threaded CPU

Problem Statement:
You are given n tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTime_i, processingTime_i] means that the i-th task will be available to process at enqueueTime_i and will take processingTime_i to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:
1. If the CPU is idle and there are no available tasks to process, the CPU remains idle.
2. If the CPU is idle and there are available tasks, it chooses the one with the shortest processing time. If multiple tasks have the same shortest processing time, it chooses the task with the smallest index.
3. Once a task is started, the CPU will process the entire task without stopping.
4. The CPU can finish a task then start a new one in the same unit of time.

Return the order in which the CPU will process the tasks.

Constraints:
- tasks.length == n
- 1 <= n <= 10^5
- 1 <= enqueueTime_i, processingTime_i <= 10^9
"""

from heapq import heappush, heappop
from typing import List

def getOrder(tasks: List[List[int]]) -> List[int]:
    # Add the index to each task for tracking
    indexed_tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
    # Sort tasks by enqueue time
    indexed_tasks.sort()

    result = []
    min_heap = []
    time = 0
    i = 0
    n = len(tasks)

    while len(result) < n:
        # Add all tasks that are available at the current time to the heap
        while i < n and indexed_tasks[i][0] <= time:
            enqueue_time, processing_time, index = indexed_tasks[i]
            heappush(min_heap, (processing_time, index))
            i += 1

        if min_heap:
            # Process the task with the shortest processing time (and smallest index if tie)
            processing_time, index = heappop(min_heap)
            time += processing_time
            result.append(index)
        else:
            # If no tasks are available, move time forward to the next task's enqueue time
            time = indexed_tasks[i][0]

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tasks1 = [[1, 2], [2, 4], [3, 2], [4, 1]]
    print(getOrder(tasks1))  # Output: [0, 2, 3, 1]

    # Test Case 2
    tasks2 = [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]
    print(getOrder(tasks2))  # Output: [4, 3, 2, 0, 1]

    # Test Case 3
    tasks3 = [[1, 2], [2, 2], [3, 2], [4, 2]]
    print(getOrder(tasks3))  # Output: [0, 1, 2, 3]

"""
Time Complexity:
- Sorting the tasks takes O(n log n).
- Each task is pushed and popped from the heap once, and heap operations take O(log n). Thus, the heap operations take O(n log n).
- Overall time complexity: O(n log n).

Space Complexity:
- The heap can contain up to n tasks in the worst case, so the space complexity is O(n).
- Additionally, we store the indexed tasks, which also takes O(n) space.
- Overall space complexity: O(n).

Topic: Heap (Priority Queue)
"""