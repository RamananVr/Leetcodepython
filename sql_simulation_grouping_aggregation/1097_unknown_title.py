"""
LeetCode Problem #1097: Game Play Analysis V

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
This table shows the activity of players of some games. Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on some date using some device.

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
+-----------+----------------+
| player_id | first_login    |
+-----------+----------------+
| 1         | 2016-03-01     |
| 2         | 2017-06-25     |
| 3         | 2016-03-02     |
+-----------+----------------+

Explanation:
The first login date for each player is:
- player 1: 2016-03-01
- player 2: 2017-06-25
- player 3: 2016-03-02
"""

# Python Solution:
# Since this is a SQL problem, we will simulate the solution using pandas in Python.

import pandas as pd

def first_login(activity: pd.DataFrame) -> pd.DataFrame:
    """
    Function to find the first login date for each player.
    
    Args:
    activity (pd.DataFrame): A DataFrame containing the activity table with columns:
                             'player_id', 'device_id', 'event_date', 'games_played'.
                             
    Returns:
    pd.DataFrame: A DataFrame with columns 'player_id' and 'first_login', where
                  'first_login' is the earliest event_date for each player_id.
    """
    # Group by player_id and find the minimum event_date for each player
    result = activity.groupby('player_id', as_index=False)['event_date'].min()
    # Rename the column to match the expected output
    result.rename(columns={'event_date': 'first_login'}, inplace=True)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Input Data
    data = {
        "player_id": [1, 1, 2, 3, 3],
        "device_id": [2, 2, 3, 1, 4],
        "event_date": ["2016-03-01", "2016-05-02", "2017-06-25", "2016-03-02", "2018-07-03"],
        "games_played": [5, 6, 1, 0, 5]
    }
    activity = pd.DataFrame(data)
    
    # Convert event_date to datetime for proper comparison
    activity['event_date'] = pd.to_datetime(activity['event_date'])
    
    # Call the function
    result = first_login(activity)
    
    # Expected Output
    expected_data = {
        "player_id": [1, 2, 3],
        "first_login": ["2016-03-01", "2017-06-25", "2016-03-02"]
    }
    expected = pd.DataFrame(expected_data)
    expected['first_login'] = pd.to_datetime(expected['first_login'])
    
    # Print Results
    print("Result:")
    print(result)
    print("\nExpected:")
    print(expected)

# Time and Space Complexity Analysis:
# Time Complexity:
# - Grouping by `player_id` takes O(n), where n is the number of rows in the DataFrame.
# - Finding the minimum event_date for each group is O(g), where g is the number of unique player_ids.
# Overall: O(n + g), which simplifies to O(n) since g <= n.

# Space Complexity:
# - The space required for the output DataFrame is O(g), where g is the number of unique player_ids.
# - The input DataFrame is not modified, so no additional space is used.
# Overall: O(g).

# Topic: SQL Simulation, Grouping, Aggregation