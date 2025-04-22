"""
LeetCode Question #511: Game Play Analysis I

Problem Statement:
Table: Activity
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key of this table.
This table shows the activity of players of some games.

Write an SQL query to report the first login date for each player.

Return the result table in any order.

The query result format is in the following example.

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
The first login date for player 1 is 2016-03-01.
The first login date for player 2 is 2017-06-25.
The first login date for player 3 is 2016-03-02.
"""

# Python Solution:
# Since this is an SQL problem, we will write the SQL query as part of the solution.

def leetcode_511_solution():
    """
    Returns the SQL query to solve LeetCode Question #511.
    """
    query = """
    SELECT 
        player_id, 
        MIN(event_date) AS first_login
    FROM 
        Activity
    GROUP BY 
        player_id;
    """
    return query

# Example Test Cases:
# Note: These test cases are for understanding the input-output format. 
# You would run the SQL query on a database to verify correctness.

example_input = [
    {"player_id": 1, "device_id": 2, "event_date": "2016-03-01", "games_played": 5},
    {"player_id": 1, "device_id": 2, "event_date": "2016-05-02", "games_played": 6},
    {"player_id": 2, "device_id": 3, "event_date": "2017-06-25", "games_played": 1},
    {"player_id": 3, "device_id": 1, "event_date": "2016-03-02", "games_played": 0},
    {"player_id": 3, "device_id": 4, "event_date": "2018-07-03", "games_played": 5},
]

expected_output = [
    {"player_id": 1, "first_login": "2016-03-01"},
    {"player_id": 2, "first_login": "2017-06-25"},
    {"player_id": 3, "first_login": "2016-03-02"},
]

# Time and Space Complexity Analysis:
# Time Complexity:
# - The query involves a GROUP BY operation and a MIN aggregation. 
#   Assuming there are N rows in the table, the complexity is O(N) for scanning the rows and O(K) for grouping, 
#   where K is the number of unique player_ids. Thus, the overall complexity is O(N).

# Space Complexity:
# - The space complexity is O(K), where K is the number of unique player_ids, as we need to store the grouped results.

# Topic: SQL, Aggregation