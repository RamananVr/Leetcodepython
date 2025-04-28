"""
LeetCode Problem #1127: User Activity for the Past 30 Days I

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
There is no primary key for this table, it may have duplicate rows.
The activity_type column is an ENUM of type ('open_session', 'end_session', 'scroll_down', 'send_message').

Write an SQL query to find the user_id and the number of times a user performed any activity in the past 30 days (from the current date).

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Activity table:
+---------+-------------+---------------+---------------+
| user_id | session_id  | activity_date | activity_type |
+---------+-------------+---------------+---------------+
| 1       | 1           | 2023-10-01    | open_session  |
| 1       | 1           | 2023-10-01    | scroll_down   |
| 1       | 1           | 2023-10-02    | end_session   |
| 2       | 2           | 2023-10-01    | open_session  |
| 2       | 2           | 2023-10-01    | send_message  |
| 3       | 3           | 2023-09-30    | scroll_down   |
+---------+-------------+---------------+---------------+

Output:
+---------+--------------+
| user_id | activity_count|
+---------+--------------+
| 1       | 3            |
| 2       | 2            |
+---------+--------------+

Explanation:
User 1 has 3 activities in the past 30 days: open_session, scroll_down, and end_session.
User 2 has 2 activities in the past 30 days: open_session and send_message.
User 3's activity on 2023-09-30 is outside the 30-day window, so it is not included.
"""

# Python Solution:
# Since this is an SQL problem, we will write the SQL query as the solution.

"""
SQL Query:
SELECT 
    user_id,
    COUNT(*) AS activity_count
FROM 
    Activity
WHERE 
    activity_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
GROUP BY 
    user_id;
"""

# Example Test Cases:
# The test cases are based on the example provided in the problem statement.

"""
Input:
Activity table:
+---------+-------------+---------------+---------------+
| user_id | session_id  | activity_date | activity_type |
+---------+-------------+---------------+---------------+
| 1       | 1           | 2023-10-01    | open_session  |
| 1       | 1           | 2023-10-01    | scroll_down   |
| 1       | 1           | 2023-10-02    | end_session   |
| 2       | 2           | 2023-10-01    | open_session  |
| 2       | 2           | 2023-10-01    | send_message  |
| 3       | 3           | 2023-09-30    | scroll_down   |
+---------+-------------+---------------+---------------+

Output:
+---------+--------------+
| user_id | activity_count|
+---------+--------------+
| 1       | 3            |
| 2       | 2            |
+---------+--------------+
"""

# Time and Space Complexity Analysis:
# Time Complexity: O(N), where N is the number of rows in the Activity table. The query scans the table once to filter rows and count activities.
# Space Complexity: O(U), where U is the number of unique user_ids. This is the space required to store the grouped results.

# Topic: SQL