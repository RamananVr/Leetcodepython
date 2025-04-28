"""
LeetCode Problem #1141: User Activity for the Past 30 Days I

Problem Statement:
Table: Activity
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |
+---------------+---------+
(user_id, session_id, activity_date) is the primary key for this table.
This table shows the user activities for a social media website. 
It includes information about the user, their session, the date of the activity, 
and the activity type.

Write an SQL query to find the number of active users in the past 30 days 
(30 days before the current date).

An active user is defined as a user who has performed at least one activity 
in the past 30 days.

Return the result table with a single column named active_users.

The query result format is in the following example.

Example:
Input:
Activity table:
+---------+------------+---------------+---------------+
| user_id | session_id | activity_date | activity_type |
+---------+------------+---------------+---------------+
| 1       | 1          | 2023-10-01    | post          |
| 2       | 2          | 2023-10-02    | comment       |
| 3       | 3          | 2023-09-30    | like          |
| 1       | 4          | 2023-09-29    | post          |
| 2       | 5          | 2023-09-28    | comment       |
+---------+------------+---------------+---------------+

Output:
+--------------+
| active_users |
+--------------+
| 3            |
+--------------+

Explanation:
In the past 30 days (from 2023-10-01 to 2023-10-30), there are three unique users 
(1, 2, and 3) who have performed at least one activity.
"""

# Python Solution:
# Since this is an SQL problem, we will write the SQL query as the solution.

"""
SQL Query Solution:
SELECT COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);
"""

# Example Test Cases:
# The test cases for this problem would be run in an SQL environment, not Python.
# However, we can describe the expected behavior based on the input table.

"""
Test Case 1:
Input:
Activity table:
+---------+------------+---------------+---------------+
| user_id | session_id | activity_date | activity_type |
+---------+------------+---------------+---------------+
| 1       | 1          | 2023-10-01    | post          |
| 2       | 2          | 2023-10-02    | comment       |
| 3       | 3          | 2023-09-30    | like          |
| 1       | 4          | 2023-09-29    | post          |
| 2       | 5          | 2023-09-28    | comment       |
+---------+------------+---------------+---------------+

Output:
+--------------+
| active_users |
+--------------+
| 3            |
+--------------+

Test Case 2:
Input:
Activity table:
+---------+------------+---------------+---------------+
| user_id | session_id | activity_date | activity_type |
+---------+------------+---------------+---------------+
| 1       | 1          | 2023-10-01    | post          |
| 1       | 2          | 2023-09-15    | comment       |
| 2       | 3          | 2023-09-10    | like          |
+---------+------------+---------------+---------------+

Output:
+--------------+
| active_users |
+--------------+
| 1            |
+--------------+

Explanation:
Only user 1 has activity in the past 30 days.

Test Case 3:
Input:
Activity table:
+---------+------------+---------------+---------------+
| user_id | session_id | activity_date | activity_type |
+---------+------------+---------------+---------------+
| 1       | 1          | 2023-08-01    | post          |
| 2       | 2          | 2023-08-02    | comment       |
| 3       | 3          | 2023-08-03    | like          |
+---------+------------+---------------+---------------+

Output:
+--------------+
| active_users |
+--------------+
| 0            |
+--------------+

Explanation:
No users have activity in the past 30 days.

Time and Space Complexity Analysis:
- Time Complexity: O(N), where N is the number of rows in the Activity table. 
  The query scans the table to filter rows based on the date and count distinct user IDs.
- Space Complexity: O(U), where U is the number of unique user IDs in the filtered rows. 
  This is because the DISTINCT operation requires storing unique user IDs.

Topic: SQL
"""