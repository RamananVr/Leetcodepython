"""
LeetCode Problem #2365: Task Scheduler II

Problem Statement:
You are given a list of tasks that need to be completed in order, represented as an array `tasks` where `tasks[i]` is the type of the i-th task. Tasks of the same type must be separated by at least `space` units of time, where `space` is a non-negative integer. At any time, you can either complete a task or wait for one unit of time.

Return the minimum number of units of time required to complete all the tasks.

Example 1:
Input: tasks = [1, 2, 1, 2, 3, 1], space = 3
Output: 9
Explanation:
- At time 1, task 1 is completed.
- At time 2, task 2 is completed.
- At time 3, we wait.
- At time 4, task 1 is completed.
- At time 5, task 2 is completed.
- At time 6, task 3 is completed.
- At time 7, we wait.
- At time 8, we wait.
- At time 9, task 1 is completed.

Example 2:
Input: tasks = [5, 8, 8, 5], space = 2
Output: 6
Explanation:
- At time 1, task 5 is completed.
- At time 2, task 8 is completed.
- At time 3, we wait.
- At time 4, task 8 is completed.
- At time 5, we wait.
- At time 6, task 5 is completed.

Constraints:
- 1 <= tasks.length <= 10^5
- 1 <= tasks[i] <= 10^9
- 0 <= space <= tasks.length - 1
"""

# Python Solution
def taskSchedulerII(tasks, space):
    """
    Calculate the minimum time required to complete all tasks with the given constraints.

    :param tasks: List[int] - List of tasks to be completed in order.
    :param space: int - Minimum units of time required between two tasks of the same type.
    :return: int - Minimum time required to complete all tasks.
    """
    last_completed = {}  # Dictionary to store the last time a task was completed
    current_time = 0     # Tracks the current time

    for task in tasks:
        if task in last_completed and current_time - last_completed[task] < space:
            # Wait until the cooldown period is over
            current_time = last_completed[task] + space + 1
        else:
            # Complete the task immediately
            current_time += 1
        # Update the last completed time for the task
        last_completed[task] = current_time

    return current_time

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tasks1 = [1, 2, 1, 2, 3, 1]
    space1 = 3
    print(taskSchedulerII(tasks1, space1))  # Expected Output: 9

    # Test Case 2
    tasks2 = [5, 8, 8, 5]
    space2 = 2
    print(taskSchedulerII(tasks2, space2))  # Expected Output: 6

    # Test Case 3
    tasks3 = [1, 1, 1, 1]
    space3 = 2
    print(taskSchedulerII(tasks3, space3))  # Expected Output: 10

    # Test Case 4
    tasks4 = [1, 2, 3, 4]
    space4 = 0
    print(taskSchedulerII(tasks4, space4))  # Expected Output: 4

    # Test Case 5
    tasks5 = [1, 2, 1, 2, 1, 2]
    space5 = 1
    print(taskSchedulerII(tasks5, space5))  # Expected Output: 8

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the `tasks` list once, performing O(1) operations for each task.
- Therefore, the time complexity is O(n), where n is the length of the `tasks` list.

Space Complexity:
- The `last_completed` dictionary stores the last completed time for each unique task. In the worst case, it contains all unique tasks.
- Therefore, the space complexity is O(u), where u is the number of unique tasks in the `tasks` list.
"""

# Topic: Arrays, Hash Table