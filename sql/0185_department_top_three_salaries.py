"""
LeetCode Question #185: Department Top Three Salaries

Problem Statement:
The `Employee` table holds all employees, and the `Department` table holds all departments. Write a SQL query to find the top three salaries for each department. If a department has fewer than three employees, then just display the salaries that are available.

The `Employee` table contains the following columns:
- Id: Employee ID
- Name: Employee Name
- Salary: Employee Salary
- DepartmentId: The ID of the department the employee belongs to

The `Department` table contains the following columns:
- Id: Department ID
- Name: Department Name

Return the result table in any order. The result table should contain the following columns:
- Department: The name of the department
- Employee: The name of the employee
- Salary: The salary of the employee

Example Input:
Employee table:
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+

Department table:
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+

Example Output:
+------------+--------+--------+
| Department | Employee | Salary |
+------------+--------+--------+
| IT         | Max     | 90000  |
| IT         | Joe     | 85000  |
| IT         | Randy   | 85000  |
| Sales      | Henry   | 80000  |
| Sales      | Sam     | 60000  |
+------------+--------+--------+

Solution:
Since this is a SQL problem, the solution is written in SQL.
"""

# SQL Solution:
"""
SELECT d.Name AS Department, e.Name AS Employee, e.Salary
FROM Employee e
JOIN Department d ON e.DepartmentId = d.Id
WHERE (
    SELECT COUNT(DISTINCT e2.Salary)
    FROM Employee e2
    WHERE e2.DepartmentId = e.DepartmentId AND e2.Salary >= e.Salary
) <= 3
ORDER BY d.Name, e.Salary DESC;
"""

"""
Test Cases:
Input:
Employee table:
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+

Department table:
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+

Output:
+------------+--------+--------+
| Department | Employee | Salary |
+------------+--------+--------+
| IT         | Max     | 90000  |
| IT         | Joe     | 85000  |
| IT         | Randy   | 85000  |
| Sales      | Henry   | 80000  |
| Sales      | Sam     | 60000  |
+------------+--------+--------+
"""

"""
Time and Space Complexity Analysis:
- Time Complexity: O(N^2), where N is the number of rows in the Employee table. This is because for each employee, we perform a subquery to count the number of distinct salaries greater than or equal to the current employee's salary.
- Space Complexity: O(N), where N is the number of rows in the Employee table. This is due to the space required for the intermediate results during the query execution.

Topic: SQL
"""