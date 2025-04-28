"""
LeetCode Problem #1205: Monthly Transactions I

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
The table contains information about transactions in a company.
The state column is an ENUM type of ('approved', 'declined', 'pending').

Write an SQL query to find the IDs of the users with the most approved transactions in each country. 
If a country has no approved transactions, do not include it in the result.

The query result format is in the following example:

Transactions table:
+----+---------+----------+--------+------------+
| id | country | state    | amount | trans_date |
+----+---------+----------+--------+------------+
| 1  | US      | approved | 1000   | 2023-01-01 |
| 2  | US      | declined | 2000   | 2023-01-02 |
| 3  | US      | approved | 1500   | 2023-01-03 |
| 4  | CA      | approved | 2000   | 2023-01-04 |
| 5  | CA      | approved | 3000   | 2023-01-05 |
| 6  | CA      | declined | 4000   | 2023-01-06 |
+----+---------+----------+--------+------------+

Result table:
+---------+-----+
| country | id  |
+---------+-----+
| US      | 1   |
| US      | 3   |
| CA      | 4   |
| CA      | 5   |
+---------+-----+
The result table should contain the IDs of the users with the most approved transactions in each country.
For the US, both transactions with IDs 1 and 3 are approved.
For CA, both transactions with IDs 4 and 5 are approved.
"""

# Solution:
# Since this is an SQL problem, we will provide the SQL query as the solution.

"""
SQL Query:

SELECT country, id
FROM Transactions
WHERE state = 'approved';
"""

# Example Test Cases:
# The example test cases are already provided in the problem statement.

# Time and Space Complexity Analysis:
# Time Complexity: O(n), where n is the number of rows in the Transactions table. 
# This is because we are scanning the table to filter rows with state = 'approved'.
# Space Complexity: O(1), as we are not using any additional data structures.

# Topic: SQL, Database