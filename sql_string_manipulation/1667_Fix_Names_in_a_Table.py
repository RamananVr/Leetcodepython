"""
LeetCode Problem #1667: Fix Names in a Table

Problem Statement:
You are given a table `Users` with the following structure:

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| name        | varchar |
+-------------+---------+
user_id is the primary key for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.

Write an SQL query to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by `user_id`.

The query result format is in the following example:

Input:
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+

Output:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+
"""

# Python Solution:
# Since this is an SQL problem, we will write the SQL query as the solution.

"""
SQL Query Solution:

SELECT 
    user_id,
    CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM 
    Users
ORDER BY 
    user_id;
"""

# Example Test Cases:
# Input:
# Users table:
# +---------+-------+
# | user_id | name  |
# +---------+-------+
# | 1       | aLice |
# | 2       | bOB   |
# +---------+-------+

# Output:
# +---------+-------+
# | user_id | name  |
# +---------+-------+
# | 1       | Alice |
# | 2       | Bob   |
# +---------+-------+

# Time and Space Complexity Analysis:
# Time Complexity: O(n), where n is the number of rows in the `Users` table. The query processes each row once to transform the name.
# Space Complexity: O(1), as the query does not use any additional space that scales with the input size.

# Topic: SQL, String Manipulation