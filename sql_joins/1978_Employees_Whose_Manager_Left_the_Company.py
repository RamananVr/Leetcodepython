"""
LeetCode Problem #1978: Employees Whose Manager Left the Company

Problem Statement:
Table: Employees

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| manager_id  | int     |
| salary      | int     |
+-------------+---------+
employee_id is the primary key for this table.
Each row of this table indicates the ID of an employee, their name, the ID of their manager, and their salary.

Write an SQL query to find the IDs of employees whose manager left the company.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Employees table:
+-------------+----------+------------+--------+
| employee_id | name     | manager_id | salary |
+-------------+----------+------------+--------+
| 1           | John     | 3          | 1000   |
| 2           | Alice    | 3          | 2000   |
| 3           | Bob      | NULL       | 4000   |
| 4           | Jerry    | 2          | 3000   |
+-------------+----------+------------+--------+

Output:
+-------------+
| employee_id |
+-------------+
| 1           |
| 2           |
+-------------+

Explanation:
- Employees with IDs 1 and 2 have a manager with ID 3.
- Employee with ID 3 does not have a manager (manager_id is NULL), meaning they left the company.
- Thus, employees 1 and 2 are included in the result.
"""

# Python Solution:
# Since this is an SQL problem, we will write the SQL query as the solution.

"""
SQL Query:
SELECT e.employee_id
FROM Employees e
LEFT JOIN Employees m
ON e.manager_id = m.employee_id
WHERE e.manager_id IS NOT NULL AND m.employee_id IS NULL;
"""

# Example Test Cases:
"""
Input:
Employees table:
+-------------+----------+------------+--------+
| employee_id | name     | manager_id | salary |
+-------------+----------+------------+--------+
| 1           | John     | 3          | 1000   |
| 2           | Alice    | 3          | 2000   |
| 3           | Bob      | NULL       | 4000   |
| 4           | Jerry    | 2          | 3000   |
+-------------+----------+------------+--------+

Output:
+-------------+
| employee_id |
+-------------+
| 1           |
| 2           |
+-------------+
"""

# Time and Space Complexity Analysis:
# Time Complexity: O(N), where N is the number of rows in the Employees table. The LEFT JOIN operation and filtering
#                  require scanning the table, which is linear in complexity.
# Space Complexity: O(1), as the query does not use any additional data structures.

# Topic: SQL, Joins