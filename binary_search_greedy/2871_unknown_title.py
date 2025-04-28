"""
LeetCode Problem #2871: Maximum Number of Tasks You Can Assign

Problem Statement:
You are given two integer arrays `tasks` and `workers` of length `n` and `m` respectively, where `tasks[i]` is the strength required to complete the i-th task, and `workers[j]` is the strength of the j-th worker. Each worker can complete at most one task, and a task can only be assigned to a worker if the worker's strength is greater than or equal to the task's strength.

Additionally, you are given an integer `pills` and an integer `strength`. You can give a worker a pill to temporarily increase their strength by `strength`. Each worker can be given at most one pill.

Return the maximum number of tasks that can be assigned to workers.

Constraints:
- `1 <= tasks.length, workers.length <= 10^5`
- `1 <= tasks[i], workers[j], strength <= 10^9`
- `0 <= pills <= 10^5`
"""

from collections import deque

def max_tasks_assigned(tasks, workers, pills, strength):
    """
    Function to calculate the maximum number of tasks that can be assigned to workers.
    
    :param tasks: List[int] - Strength required for each task
    :param workers: List[int] - Strength of each worker
    :param pills: int - Number of pills available
    :param strength: int - Strength added by each pill
    :return: int - Maximum number of tasks that can be assigned
    """
    def can_assign(mid):
        """
        Helper function to check if `mid` tasks can be assigned.
        """
        task_queue = deque(sorted(tasks[:mid]))
        worker_queue = deque(sorted(workers))
        remaining_pills = pills

        while task_queue:
            task = task_queue.pop()
            # Assign task to the strongest worker who can handle it without a pill
            while worker_queue and worker_queue[-1] >= task:
                worker_queue.pop()
                break
            else:
                # If no worker can handle it without a pill, try with a pill
                while worker_queue and worker_queue[0] + strength < task:
                    worker_queue.popleft()
                if worker_queue and remaining_pills > 0:
                    worker_queue.popleft()
                    remaining_pills -= 1
                else:
                    return False
        return True

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
    print(max_tasks_assigned(tasks, workers, pills, strength))  # Output: 3

    # Test Case 2
    tasks = [10, 15, 20]
    workers = [5, 10, 15]
    pills = 2
    strength = 5
    print(max_tasks_assigned(tasks, workers, pills, strength))  # Output: 2

    # Test Case 3
    tasks = [1, 2, 3]
    workers = [1, 1, 1]
    pills = 1
    strength = 2
    print(max_tasks_assigned(tasks, workers, pills, strength))  # Output: 2

"""
Time Complexity:
- Sorting the `tasks` and `workers` arrays takes O(n log n + m log m), where n is the length of `tasks` and m is the length of `workers`.
- The binary search runs in O(log(min(n, m))) iterations.
- Each iteration of the binary search involves a linear scan of the `tasks` and `workers` arrays, which takes O(n + m).
- Overall complexity: O((n + m) log(n + m)).

Space Complexity:
- The space complexity is O(n + m) due to the sorted arrays and queues used in the helper function.

Topic: Binary Search, Greedy
"""