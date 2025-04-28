"""
LeetCode Problem #2798: Number of Employees Who Met the Target

Problem Statement:
There is a company with `n` employees, where each employee has a unique ID from `0` to `n - 1`. 
The company keeps track of the number of tasks completed by each employee in an integer array `tasks`, 
where `tasks[i]` is the number of tasks completed by the `i-th` employee.

The company has a target number of tasks that each employee should complete. You are given an integer `target`.

Return the number of employees who completed at least `target` tasks.

Example:
Input: tasks = [5, 1, 4, 2], target = 3
Output: 2
Explanation: The employees with IDs 0 and 2 completed at least 3 tasks.

Constraints:
- `1 <= tasks.length <= 100`
- `0 <= tasks[i], target <= 100`
"""

# Python Solution
def numberOfEmployeesWhoMetTarget(tasks, target):
    """
    Function to count the number of employees who completed at least the target number of tasks.

    :param tasks: List[int] - List of tasks completed by each employee.
    :param target: int - Target number of tasks.
    :return: int - Number of employees who met or exceeded the target.
    """
    return sum(task >= target for task in tasks)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tasks = [5, 1, 4, 2]
    target = 3
    print(numberOfEmployeesWhoMetTarget(tasks, target))  # Output: 2

    # Test Case 2
    tasks = [10, 20, 30, 40]
    target = 25
    print(numberOfEmployeesWhoMetTarget(tasks, target))  # Output: 2

    # Test Case 3
    tasks = [0, 0, 0, 0]
    target = 1
    print(numberOfEmployeesWhoMetTarget(tasks, target))  # Output: 0

    # Test Case 4
    tasks = [1, 2, 3, 4, 5]
    target = 5
    print(numberOfEmployeesWhoMetTarget(tasks, target))  # Output: 1

    # Test Case 5
    tasks = [100, 99, 98, 97]
    target = 100
    print(numberOfEmployeesWhoMetTarget(tasks, target))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `tasks` list once to check if each task meets the target.
- This results in a time complexity of O(n), where n is the length of the `tasks` list.

Space Complexity:
- The function uses a generator expression to calculate the sum, which does not require additional space.
- Therefore, the space complexity is O(1).
"""

# Topic: Arrays