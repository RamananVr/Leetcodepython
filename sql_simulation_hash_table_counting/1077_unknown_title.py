"""
LeetCode Problem #1077: Project Employees III

Problem Statement:
You are given a table `Employee` and a table `Project`.

Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
+-------------+---------+
employee_id is the primary key for this table.

Table: Project
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key for this table.

Write an SQL query to report all the projects that have the most employees.

The query result format is in the following example:

Employee table:
+-------------+----------+
| employee_id | name     |
+-------------+----------+
| 1           | Khaled   |
| 2           | Ali      |
| 3           | John     |
| 4           | Doe      |
+-------------+----------+

Project table:
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+

Result table:
+-------------+
| project_id  |
+-------------+
| 1           |
+-------------+
Project 1 has 3 employees while project 2 has 2 employees. Thus, project 1 has the most employees.
"""

# Clean, Correct Python Solution
def most_employees_projects(employee, project):
    """
    This function simulates the SQL query to find the project(s) with the most employees.
    It takes two inputs:
    - employee: A list of dictionaries representing the Employee table.
    - project: A list of dictionaries representing the Project table.

    Returns:
    - A list of project IDs that have the most employees.
    """
    from collections import Counter

    # Count the number of employees per project
    project_employee_count = Counter([p['project_id'] for p in project])

    # Find the maximum number of employees in any project
    max_employees = max(project_employee_count.values())

    # Find all project IDs with the maximum number of employees
    result = [project_id for project_id, count in project_employee_count.items() if count == max_employees]

    return result

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    employee = [
        {"employee_id": 1, "name": "Khaled"},
        {"employee_id": 2, "name": "Ali"},
        {"employee_id": 3, "name": "John"},
        {"employee_id": 4, "name": "Doe"}
    ]
    project = [
        {"project_id": 1, "employee_id": 1},
        {"project_id": 1, "employee_id": 2},
        {"project_id": 1, "employee_id": 3},
        {"project_id": 2, "employee_id": 1},
        {"project_id": 2, "employee_id": 4}
    ]
    print(most_employees_projects(employee, project))  # Output: [1]

    # Example 2
    employee = [
        {"employee_id": 1, "name": "Alice"},
        {"employee_id": 2, "name": "Bob"},
        {"employee_id": 3, "name": "Charlie"}
    ]
    project = [
        {"project_id": 1, "employee_id": 1},
        {"project_id": 1, "employee_id": 2},
        {"project_id": 2, "employee_id": 3},
        {"project_id": 2, "employee_id": 1},
        {"project_id": 3, "employee_id": 2},
        {"project_id": 3, "employee_id": 3}
    ]
    print(most_employees_projects(employee, project))  # Output: [1, 2, 3]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting employees per project: O(n), where n is the number of rows in the `project` table.
- Finding the maximum count: O(k), where k is the number of unique project IDs.
- Filtering projects with the maximum count: O(k).
Overall: O(n + k).

Space Complexity:
- Storing the count of employees per project: O(k), where k is the number of unique project IDs.
Overall: O(k).
"""

# Topic: SQL Simulation, Hash Table, Counting