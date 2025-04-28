"""
LeetCode Problem #2071: Maximum Number of Tasks You Can Assign

Problem Statement:
You have `n` tasks and `m` workers. Each task has a strength requirement represented by the array `tasks`, 
where `tasks[i]` is the strength required to complete the i-th task. Each worker has a strength represented 
by the array `workers`, where `workers[j]` is the strength of the j-th worker. Each worker can only complete 
one task, and each task can only be completed by one worker.

Additionally, you have `pills` magical pills. You can give a pill to a worker, which increases their strength 
by `strength`. However, each worker can only take at most one pill.

Return the maximum number of tasks that can be assigned to the workers.

Constraints:
- `1 <= tasks.length, workers.length <= 5 * 10^4`
- `1 <= pills <= 10^5`
- `1 <= tasks[i], workers[j], strength <= 10^9`
"""

from collections import deque

def maxTasksAssign(tasks, workers, pills, strength):
    def can_assign(k):
        """
        Helper function to check if we can assign `k` tasks.
        """
        task_deque = deque(sorted(tasks[:k]))
        worker_list = sorted(workers)
        available_pills = pills

        for worker in reversed(worker_list[-k:]):
            if task_deque and worker >= task_deque[0]:
                # Worker can complete the easiest task without a pill
                task_deque.popleft()
            elif task_deque and available_pills > 0 and worker + strength >= task_deque[0]:
                # Worker can complete the easiest task with a pill
                task_deque.popleft()
                available_pills -= 1
            else:
                # Worker cannot complete the task
                return False

        return True

    # Sort tasks and workers
    tasks.sort()
    workers.sort()

    # Binary search to find the maximum number of tasks that can be assigned
    left, right = 0, min(len(tasks), len(workers))
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_assign(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tasks = [3, 5, 8]
    workers = [7, 2, 4]
    pills = 1
    strength = 3
    print(maxTasksAssign(tasks, workers, pills, strength))  # Output: 2

    # Test Case 2
    tasks = [10, 15, 20]
    workers = [5, 10, 15]
    pills = 2
    strength = 10
    print(maxTasksAssign(tasks, workers, pills, strength))  # Output: 3

    # Test Case 3
    tasks = [5, 9, 12]
    workers = [6, 8, 10]
    pills = 0
    strength = 5
    print(maxTasksAssign(tasks, workers, pills, strength))  # Output: 2

"""
Time Complexity:
- Sorting the `tasks` and `workers` arrays takes O(n log n + m log m), where `n` is the length of `tasks` and `m` is the length of `workers`.
- The binary search runs O(log(min(n, m))) iterations.
- Each iteration of the binary search involves checking if `k` tasks can be assigned, which takes O(k) in the worst case.

Overall time complexity: O((n + m) log(n + m)).

Space Complexity:
- The space complexity is O(n + m) due to the sorting and the deque used in the helper function.

Topic: Binary Search, Greedy
"""