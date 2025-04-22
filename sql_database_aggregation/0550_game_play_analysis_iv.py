"""
LeetCode Question #550: Game Play Analysis IV

Problem Statement:
SQL Problem - This is a database problem and not a Python coding problem. 
The problem involves analyzing a database table to find the first login date for each player.

The table `Activity` has the following structure:
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key of this table.
This table shows the activity of players of some games. Each row is a record of a player who logged in and played games on some date using some device.

Write an SQL query to report the first login date for each player.

The query result format is in the following example:

Example:
Input:
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

Output:
+-----------+-------------+
| player_id | first_login |
+-----------+-------------+
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |
+-----------+-------------+

Explanation:
The first login date for each player is the minimum event_date for that player.
"""

# Since this is an SQL problem, there is no Python solution to implement.
# However, we can provide the SQL query to solve the problem.

"""
SQL Query Solution:

SELECT 
    player_id,
    MIN(event_date) AS first_login
FROM 
    Activity
GROUP BY 
    player_id;
"""

# Example Test Cases:
# The test cases are based on the input and output provided in the problem statement.

"""
Input:
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

Output:
+-----------+-------------+
| player_id | first_login |
+-----------+-------------+
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |
+-----------+-------------+
"""

# Time and Space Complexity Analysis:
# Time Complexity: O(N), where N is the number of rows in the Activity table. 
# This is because we need to scan all rows to compute the minimum event_date for each player.
# Space Complexity: O(K), where K is the number of unique player_ids. 
# This is because we need to store the result for each player in memory.

# Topic: SQL, Database, Aggregation