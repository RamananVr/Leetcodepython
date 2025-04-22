"""
LeetCode Question #197: Rising Temperature

Problem Statement:
Table: Weather
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the primary key for this table.
This table contains information about the temperature on a certain day.

Write an SQL query to find all dates' Ids with higher temperatures compared to the previous day (yesterday).

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2023-03-01 | 10          |
| 2  | 2023-03-02 | 25          |
| 3  | 2023-03-03 | 20          |
| 4  | 2023-03-04 | 30          |
+----+------------+-------------+

Output:
+----+
| id |
+----+
| 2  |
| 4  |
+----+

Explanation:
- On 2023-03-02, the temperature (25) is higher than the previous day (10), so id = 2 is included.
- On 2023-03-03, the temperature (20) is not higher than the previous day (25), so id = 3 is not included.
- On 2023-03-04, the temperature (30) is higher than the previous day (20), so id = 4 is included.
"""

# Python Solution:
# Since this is an SQL problem, we will write the SQL query as the solution.

"""
SQL Query:
SELECT W1.id
FROM Weather W1
JOIN Weather W2
ON DATEDIFF(W1.recordDate, W2.recordDate) = 1
WHERE W1.temperature > W2.temperature;
"""

# Example Test Cases:
# The test cases are based on the Weather table provided in the problem statement.

"""
Input:
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2023-03-01 | 10          |
| 2  | 2023-03-02 | 25          |
| 3  | 2023-03-03 | 20          |
| 4  | 2023-03-04 | 30          |
+----+------------+-------------+

Output:
+----+
| id |
+----+
| 2  |
| 4  |
+----+
"""

# Time and Space Complexity Analysis:
# Time Complexity: O(n), where n is the number of rows in the Weather table. The JOIN operation compares each row with its previous day's row, which is linear in nature.
# Space Complexity: O(1), as no additional space is used apart from the result set.

# Topic: SQL, Joins