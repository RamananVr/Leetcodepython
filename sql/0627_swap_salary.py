"""
LeetCode Question #627: Swap Salary

Problem Statement:
Table: Employee

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| name        | varchar  |
| sex         | char     |
| salary      | int      |
+-------------+----------+
id is the primary key column for this table.
The sex column has values 'm' and 'f'.
Write an SQL query to swap all 'm' and 'f' values (i.e., change all 'm' values to 'f' and vice versa) with a single update statement and no intermediate temp table.
Note that you must write a single update statement and not two separate statements.

The query result format is in the following example.

Example:
Input:
Employee table:
+----+-------+------+--------+
| id | name  | sex  | salary |
+----+-------+------+--------+
| 1  | A     | m    | 2500   |
| 2  | B     | f    | 1500   |
| 3  | C     | m    | 5500   |
| 4  | D     | f    | 500    |
+----+-------+------+--------+

Output:
+----+-------+------+--------+
| id | name  | sex  | salary |
+----+-------+------+--------+
| 1  | A     | f    | 2500   |
| 2  | B     | m    | 1500   |
| 3  | C     | f    | 5500   |
| 4  | D     | m    | 500    |
+----+-------+------+--------+

Explanation:
'sex' column values are swapped from 'm' to 'f' and 'f' to 'm'.
"""

# Solution:
"""
Since this is an SQL problem, the solution is written as an SQL query.
"""

# SQL Query:
"""
UPDATE Employee
SET sex = CASE
            WHEN sex = 'm' THEN 'f'
            WHEN sex = 'f' THEN 'm'
          END;
"""

# Example Test Cases:
"""
Input:
Employee table:
+----+-------+------+--------+
| id | name  | sex  | salary |
+----+-------+------+--------+
| 1  | A     | m    | 2500   |
| 2  | B     | f    | 1500   |
| 3  | C     | m    | 5500   |
| 4  | D     | f    | 500    |
+----+-------+------+--------+

Output:
+----+-------+------+--------+
| id | name  | sex  | salary |
+----+-------+------+--------+
| 1  | A     | f    | 2500   |
| 2  | B     | m    | 1500   |
| 3  | C     | f    | 5500   |
| 4  | D     | m    | 500    |
+----+-------+------+--------+
"""

# Time and Space Complexity Analysis:
"""
Time Complexity:
The query performs a single update operation on the `Employee` table. The complexity depends on the number of rows in the table, denoted as `n`. 
Thus, the time complexity is O(n), where `n` is the number of rows in the table.

Space Complexity:
The query does not use any additional space apart from the space required to store the table itself. 
Thus, the space complexity is O(1).
"""

# Topic: SQL