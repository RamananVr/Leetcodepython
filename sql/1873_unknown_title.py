"""
LeetCode Problem #1873: Calculate Special Bonus

Problem Statement:
Table: Employees

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id is the primary key for this table.
Each row of this table indicates the ID, name, and salary of an employee.

Write an SQL query to calculate the bonus of each employee. The bonus of an employee is:
- 0 if the employee's name starts with the prefix 'M' (case-insensitive).
- Otherwise, 2 times their salary.

Return the result table ordered by employee_id.

The query result format is in the following example.

Example:
Input:
Employees table:
+-------------+--------+--------+
| employee_id | name   | salary |
+-------------+--------+--------+
| 1           | John   | 1000   |
| 2           | MARY   | 2000   |
| 3           | Alice  | 3000   |
| 4           | Mark   | 4000   |
+-------------+--------+--------+

Output:
+-------------+-------+
| employee_id | bonus |
+-------------+-------+
| 1           | 2000  |
| 2           | 0     |
| 3           | 6000  |
| 4           | 0     |
+-------------+-------+
"""

# Python Solution
# Since this is an SQL problem, we will write the SQL query as the solution.

def calculate_special_bonus():
    """
    Returns the SQL query to calculate the special bonus for employees.
    """
    query = """
    SELECT 
        employee_id,
        CASE 
            WHEN LOWER(name) LIKE 'm%' THEN 0
            ELSE salary * 2
        END AS bonus
    FROM Employees
    ORDER BY employee_id;
    """
    return query

# Example Test Cases
"""
Input:
Employees table:
+-------------+--------+--------+
| employee_id | name   | salary |
+-------------+--------+--------+
| 1           | John   | 1000   |
| 2           | MARY   | 2000   |
| 3           | Alice  | 3000   |
| 4           | Mark   | 4000   |
+-------------+--------+--------+

Output:
+-------------+-------+
| employee_id | bonus |
+-------------+-------+
| 1           | 2000  |
| 2           | 0     |
| 3           | 6000  |
| 4           | 0     |
+-------------+-------+
"""

# Time and Space Complexity Analysis
"""
Time Complexity:
- The query scans all rows in the Employees table, so the time complexity is O(n), where n is the number of rows in the table.

Space Complexity:
- The query does not use any additional space beyond the result set, so the space complexity is O(1).

Note: The actual complexity depends on the database engine's implementation of the query execution plan.

Topic: SQL
"""