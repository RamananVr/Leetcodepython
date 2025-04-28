"""
LeetCode Question #1075: Project Employees I

Problem Statement:
Table: Project
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key of this table.

Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
+-------------+---------+
employee_id is the primary key of this table.

Write an SQL query that reports all the projects and the employees working on them.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
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

Employee table:
+-------------+--------+
| employee_id | name   |
+-------------+--------+
| 1           | Khaled |
| 2           | Ali    |
| 3           | John   |
| 4           | Doe    |
+-------------+--------+

Output:
+-------------+--------+
| project_id  | name   |
+-------------+--------+
| 1           | Khaled |
| 1           | Ali    |
| 1           | John   |
| 2           | Khaled |
| 2           | Doe    |
+-------------+--------+
"""

# Python Solution
# Since this is an SQL problem, we will write the SQL query as the solution.

"""
SQL Query:
SELECT 
    p.project_id,
    e.name
FROM 
    Project p
JOIN 
    Employee e
ON 
    p.employee_id = e.employee_id;
"""

# Example Test Cases
"""
Input:
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

Employee table:
+-------------+--------+
| employee_id | name   |
+-------------+--------+
| 1           | Khaled |
| 2           | Ali    |
| 3           | John   |
| 4           | Doe    |
+-------------+--------+

Output:
+-------------+--------+
| project_id  | name   |
+-------------+--------+
| 1           | Khaled |
| 1           | Ali    |
| 1           | John   |
| 2           | Khaled |
| 2           | Doe    |
+-------------+--------+
"""

# Time and Space Complexity Analysis
"""
Time Complexity:
The time complexity of the SQL query depends on the size of the `Project` and `Employee` tables. 
Assuming `n` is the number of rows in the `Project` table and `m` is the number of rows in the `Employee` table, 
the JOIN operation typically has a time complexity of O(n * m) in the worst case. However, with proper indexing, 
the query can be optimized to O(n + m).

Space Complexity:
The space complexity is O(n + m) for storing the tables in memory during the JOIN operation.

Note: The actual complexity depends on the database engine and indexing used.
"""

# Topic: SQL, Database Query