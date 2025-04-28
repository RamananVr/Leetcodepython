"""
LeetCode Question #2432: The Employee That Worked on the Longest Task

Problem Statement:
There is a company with `n` employees, each with a unique ID from `0` to `n - 1`. The company 
is running a project, and the work is divided among the employees. You are given a 2D integer 
array `logs` where `logs[i] = [id_i, leaveTime_i]` indicates that the employee with ID `id_i` 
worked from the time they were assigned the task until `leaveTime_i`.

The tasks are assigned sequentially, so the next task for an employee starts exactly when the 
previous task for that employee ends. The first task starts at time `0`.

Return the ID of the employee that worked on the task with the longest time. If there is a tie, 
return the smallest ID.

Constraints:
- 2 <= n <= 500
- 1 <= logs.length <= 500
- logs[i].length == 2
- 0 <= id_i <= n - 1
- 1 <= leaveTime_i <= 500
- leaveTime_i is strictly increasing.

"""

# Python Solution
def hardestWorker(n, logs):
    """
    Finds the employee ID who worked on the longest task. If there is a tie, returns the smallest ID.

    :param n: int - Number of employees
    :param logs: List[List[int]] - Logs containing employee ID and leave time
    :return: int - ID of the employee who worked the longest
    """
    max_duration = 0
    hardest_worker_id = float('inf')
    prev_time = 0

    for log in logs:
        employee_id, leave_time = log
        duration = leave_time - prev_time
        if duration > max_duration or (duration == max_duration and employee_id < hardest_worker_id):
            max_duration = duration
            hardest_worker_id = employee_id
        prev_time = leave_time

    return hardest_worker_id


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 10
    logs1 = [[0, 3], [2, 5], [0, 9], [1, 15]]
    print(hardestWorker(n1, logs1))  # Expected Output: 1

    # Test Case 2
    n2 = 2
    logs2 = [[0, 10], [1, 20]]
    print(hardestWorker(n2, logs2))  # Expected Output: 1

    # Test Case 3
    n3 = 3
    logs3 = [[0, 5], [1, 5], [2, 5]]
    print(hardestWorker(n3, logs3))  # Expected Output: 0

    # Test Case 4
    n4 = 4
    logs4 = [[0, 2], [1, 4], [2, 6], [3, 8]]
    print(hardestWorker(n4, logs4))  # Expected Output: 0


# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `logs` list once, performing constant-time operations for each log.
- Let `m` be the length of the `logs` list. The time complexity is O(m).

Space Complexity:
- The function uses a constant amount of extra space for variables (`max_duration`, `hardest_worker_id`, `prev_time`).
- The space complexity is O(1).
"""

# Topic: Arrays