"""
LeetCode Problem #1270: All People Report to the Given Manager

Problem Statement:
We have a table `Employee` with the following structure:

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| manager_id  | int      |
+-------------+----------+
employee_id is the primary key for this table.
Each row of this table indicates that the employee with ID `employee_id` has a manager with ID `manager_id`.
If `manager_id` is null, it means this employee does not have a manager (i.e., they are the CEO).

Write an SQL query to find all employees who directly or indirectly report to a given manager with ID `manager_id`.

Return the result table in any order.

Example:
Input:
Employee table:
+-------------+----------+------------+
| employee_id | name     | manager_id |
+-------------+----------+------------+
| 1           | John     | Null       |
| 2           | Alice    | 1          |
| 3           | Bob      | 1          |
| 4           | Carol    | 2          |
| 5           | David    | 2          |
+-------------+----------+------------+

Given manager_id = 1.

Output:
+-------------+----------+
| employee_id | name     |
+-------------+----------+
| 2           | Alice    |
| 3           | Bob      |
| 4           | Carol    |
| 5           | David    |
+-------------+----------+

Explanation:
Employees Alice and Bob directly report to John (manager_id = 1).
Carol and David report to Alice, who reports to John.
Thus, all these employees report to John either directly or indirectly.
"""

# Python Solution:
# Since this is a database-related problem, we will simulate the solution using Python and a graph traversal approach.

from collections import defaultdict, deque

def find_employees_reporting_to_manager(employee_data, manager_id):
    """
    Function to find all employees who directly or indirectly report to a given manager.

    :param employee_data: List of tuples representing the Employee table.
                          Each tuple is (employee_id, name, manager_id).
    :param manager_id: The manager_id to find all reporting employees for.
    :return: List of tuples representing employees who report to the given manager.
    """
    # Build a graph where manager_id is the key and the value is a list of employees reporting to them
    manager_to_employees = defaultdict(list)
    for employee_id, name, mgr_id in employee_data:
        manager_to_employees[mgr_id].append((employee_id, name))
    
    # Perform BFS to find all employees reporting to the given manager
    result = []
    queue = deque(manager_to_employees[manager_id])  # Start with employees directly reporting to the manager
    
    while queue:
        employee_id, name = queue.popleft()
        result.append((employee_id, name))
        # Add employees who report to the current employee to the queue
        queue.extend(manager_to_employees[employee_id])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Example Employee table
    employee_data = [
        (1, "John", None),
        (2, "Alice", 1),
        (3, "Bob", 1),
        (4, "Carol", 2),
        (5, "David", 2)
    ]
    
    # Test Case 1
    manager_id = 1
    print("Employees reporting to manager_id =", manager_id)
    print(find_employees_reporting_to_manager(employee_data, manager_id))
    # Expected Output: [(2, "Alice"), (3, "Bob"), (4, "Carol"), (5, "David")]

    # Test Case 2
    manager_id = 2
    print("Employees reporting to manager_id =", manager_id)
    print(find_employees_reporting_to_manager(employee_data, manager_id))
    # Expected Output: [(4, "Carol"), (5, "David")]

    # Test Case 3
    manager_id = 3
    print("Employees reporting to manager_id =", manager_id)
    print(find_employees_reporting_to_manager(employee_data, manager_id))
    # Expected Output: []

# Time and Space Complexity Analysis:
# Time Complexity: O(N), where N is the number of employees. We traverse each employee at most once.
# Space Complexity: O(N), for storing the graph and the queue used in BFS.

# Topic: Graph Traversal (BFS)