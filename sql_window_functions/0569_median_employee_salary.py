"""
LeetCode Question #569: Median Employee Salary

Problem Statement:
The `Employee` table holds all employees. Every employee has an Id, and there is also a column for the department Id and the salary.

+----+-------+--------+--------+
| Id | Name  | Salary | DeptId |
+----+-------+--------+--------+
| 1  | Joe   | 70000  | 1      |
| 2  | Henry | 80000  | 2      |
| 3  | Sam   | 60000  | 2      |
| 4  | Max   | 90000  | 1      |
| 5  | Janet | 69000  | 1      |
| 6  | Randy | 85000  | 1      |
+----+-------+--------+--------+

Write an SQL query to find the median salary of each department. The median salary is the value separating the higher half from the lower half of a data sample. If there is an even number of salaries, the median is the average of the two middle values.

The result table should contain the department Id and the median salary. Order the result by department Id.

+--------+-------------+
| DeptId | MedianSalary|
+--------+-------------+
| 1      | 74500       |
| 2      | 70000       |
+--------+-------------+

Note:
- The median salary for department 1 is (70000 + 69000) / 2 = 74500.
- The median salary for department 2 is 70000 because it is the middle value.

Solution:
Since this is an SQL problem, we will not write Python code for it. Instead, we will provide the SQL query to solve the problem.
"""

# SQL Solution:
"""
WITH RankedSalaries AS (
    SELECT
        DeptId,
        Salary,
        ROW_NUMBER() OVER (PARTITION BY DeptId ORDER BY Salary) AS RowAsc,
        ROW_NUMBER() OVER (PARTITION BY DeptId ORDER BY Salary DESC) AS RowDesc,
        COUNT(*) OVER (PARTITION BY DeptId) AS TotalCount
    FROM Employee
)
SELECT
    DeptId,
    CASE
        WHEN TotalCount % 2 = 1 THEN
            CAST(Salary AS FLOAT)
        ELSE
            CAST((SELECT Salary FROM RankedSalaries WHERE DeptId = RS.DeptId AND RowAsc = TotalCount / 2) AS FLOAT) +
            CAST((SELECT Salary FROM RankedSalaries WHERE DeptId = RS.DeptId AND RowAsc = TotalCount / 2 + 1) AS FLOAT) / 2
    END AS MedianSalary
FROM RankedSalaries RS
WHERE RowAsc = (TotalCount + 1) / 2 OR RowAsc = TotalCount / 2 + 1
GROUP BY DeptId
ORDER BY DeptId;
"""

"""
Example Test Cases:
Input:
+----+-------+--------+--------+
| Id | Name  | Salary | DeptId |
+----+-------+--------+--------+
| 1  | Joe   | 70000  | 1      |
| 2  | Henry | 80000  | 2      |
| 3  | Sam   | 60000  | 2      |
| 4  | Max   | 90000  | 1      |
| 5  | Janet | 69000  | 1      |
| 6  | Randy | 85000  | 1      |
+----+-------+--------+--------+

Output:
+--------+-------------+
| DeptId | MedianSalary|
+--------+-------------+
| 1      | 74500       |
| 2      | 70000       |
+--------+-------------+

Time and Space Complexity Analysis:
- Time Complexity: O(N log N), where N is the number of employees. Sorting the salaries for each department is the most expensive operation.
- Space Complexity: O(N), as we need to store the intermediate results for the ranked salaries.

Topic: SQL, Window Functions
"""