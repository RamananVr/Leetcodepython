"""
LeetCode Question #184: Department Highest Salary

Problem Statement:
The `Employee` table holds all employees, and the `Department` table holds all departments. Write a SQL query to find employees who have the highest salary in each of the departments. In case of a tie, include all employees with the highest salary.

The `Employee` table contains the following columns:
- `Id`: Employee ID
- `Name`: Employee Name
- `Salary`: Employee Salary
- `DepartmentId`: The ID of the department the employee belongs to

The `Department` table contains the following columns:
- `Id`: Department ID
- `Name`: Department Name

Return the result table in any order. The result table should contain the following columns:
- `Department`: The name of the department
- `Employee`: The name of the employee with the highest salary in that department

Example:
Input:
Employee table:
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
+----+-------+--------+--------------+

Department table:
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+

Output:
+------------+----------+
| Department | Employee |
+------------+----------+
| IT         | Max      |
| Sales      | Henry    |
+------------+----------+
"""

# Python Solution:
# Since this is a SQL-based problem, we will write the SQL query to solve it.

"""
SQL Query:
SELECT d.Name AS Department, e.Name AS Employee
FROM Employee e
JOIN Department d ON e.DepartmentId = d.Id
WHERE e.Salary = (
    SELECT MAX(Salary)
    FROM Employee
    WHERE DepartmentId = e.DepartmentId
);
"""

# Example Test Cases:
"""
Input:
Employee table:
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
+----+-------+--------+--------------+

Department table:
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+

Output:
+------------+----------+
| Department | Employee |
+------------+----------+
| IT         | Max      |
| Sales      | Henry    |
+------------+----------+
"""

# Time and Space Complexity Analysis:
"""
Time Complexity:
- The query involves a join operation between the `Employee` and `Department` tables, which is O(n * m) where n is the number of rows in the `Employee` table and m is the number of rows in the `Department` table.
- Additionally, for each row in the `Employee` table, we perform a subquery to find the maximum salary in the department, which is O(n) in the worst case. Thus, the overall complexity is O(n^2).

Space Complexity:
- The space complexity is O(n + m) for storing the tables in memory during the join operation.

Note: The actual performance depends on the database engine's optimization techniques.
"""

# Topic: SQL