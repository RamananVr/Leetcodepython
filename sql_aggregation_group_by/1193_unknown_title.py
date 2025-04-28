"""
LeetCode Problem #1193: Monthly Transactions I

Problem Statement:
Table: Transactions
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| id             | int     |
| country        | varchar |
| state          | enum    |
| amount         | int     |
| trans_date     | date    |
+----------------+---------+
id is the primary key for this table.
The table has information about incoming transactions in a financial institution.
The state column is an enum that takes one of the three values ('approved', 'declined', 'pending').

Write an SQL query to find the total number of transactions and their total amount grouped by each month and country.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 101  | US      | approved | 1000   | 2019-01-01 |
| 102  | US      | declined | 2000   | 2019-01-02 |
| 103  | US      | approved | 3000   | 2019-02-01 |
| 104  | US      | approved | 4000   | 2019-02-01 |
| 105  | UK      | approved | 5000   | 2019-03-01 |
| 106  | UK      | declined | 6000   | 2019-03-01 |
+------+---------+----------+--------+------------+

Output:
+----------+---------+----------------+--------------+
| month    | country | trans_count    | total_amount |
+----------+---------+----------------+--------------+
| 2019-01  | US      | 2              | 3000         |
| 2019-02  | US      | 2              | 7000         |
| 2019-03  | UK      | 2              | 11000        |
+----------+---------+----------------+--------------+

Explanation:
In January 2019, there are 2 transactions in the US, and the total amount is 1000 + 2000 = 3000.
In February 2019, there are 2 transactions in the US, and the total amount is 3000 + 4000 = 7000.
In March 2019, there are 2 transactions in the UK, and the total amount is 5000 + 6000 = 11000.
"""

# Python Solution:
# Since this is an SQL problem, we will write the SQL query as the solution.

"""
SQL Query:
SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(amount) AS total_amount
FROM 
    Transactions
GROUP BY 
    DATE_FORMAT(trans_date, '%Y-%m'), country;
"""

# Example Test Cases:
# The test cases are based on the example provided in the problem statement.

"""
Input:
Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 101  | US      | approved | 1000   | 2019-01-01 |
| 102  | US      | declined | 2000   | 2019-01-02 |
| 103  | US      | approved | 3000   | 2019-02-01 |
| 104  | US      | approved | 4000   | 2019-02-01 |
| 105  | UK      | approved | 5000   | 2019-03-01 |
| 106  | UK      | declined | 6000   | 2019-03-01 |
+------+---------+----------+--------+------------+

Output:
+----------+---------+----------------+--------------+
| month    | country | trans_count    | total_amount |
+----------+---------+----------------+--------------+
| 2019-01  | US      | 2              | 3000         |
| 2019-02  | US      | 2              | 7000         |
| 2019-03  | UK      | 2              | 11000        |
+----------+---------+----------------+--------------+
"""

# Time and Space Complexity Analysis:
# Time Complexity: O(n), where n is the number of rows in the Transactions table. The query involves a GROUP BY operation, which processes each row once.
# Space Complexity: O(k), where k is the number of unique (month, country) pairs. This is the size of the result set.

# Topic: SQL, Aggregation, Group By