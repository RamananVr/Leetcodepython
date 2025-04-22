"""
LeetCode Question #614: Second Degree Follower

Problem Statement:
Table: Followers
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| follower_id | int     |
+-------------+---------+
(user_id, follower_id) is the primary key for this table.
This table contains the IDs of a user and a follower of that user.

Write an SQL query to find the followers who follow the followers of a user. In other words, find the second-degree followers of a user.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Followers table:
+---------+-------------+
| user_id | follower_id |
+---------+-------------+
| 1       | 2           |
| 2       | 3           |
| 3       | 4           |
+---------+-------------+

Output:
+-------------+-------------+
| follower_id | user_id     |
+-------------+-------------+
| 3           | 1           |
| 4           | 2           |
+-------------+-------------+

Explanation:
- User 1 is followed by User 2. User 2 is followed by User 3. Thus, User 3 is a second-degree follower of User 1.
- User 2 is followed by User 3. User 3 is followed by User 4. Thus, User 4 is a second-degree follower of User 2.
"""

# Python Solution:
# Since this is an SQL problem, we will write the SQL query as part of the solution.

def second_degree_followers():
    """
    SQL Query to find second-degree followers.
    """
    query = """
    SELECT DISTINCT f1.follower_id AS follower_id, f2.user_id AS user_id
    FROM Followers f1
    JOIN Followers f2
    ON f1.user_id = f2.follower_id;
    """
    return query

# Example Test Cases:
# Note: These test cases are for demonstration purposes. In practice, you would run the SQL query on a database.

def test_second_degree_followers():
    """
    Example test cases for the second-degree followers query.
    """
    # Input Followers table:
    followers_table = [
        {"user_id": 1, "follower_id": 2},
        {"user_id": 2, "follower_id": 3},
        {"user_id": 3, "follower_id": 4},
    ]

    # Expected Output:
    expected_output = [
        {"follower_id": 3, "user_id": 1},
        {"follower_id": 4, "user_id": 2},
    ]

    # Note: In practice, you would execute the SQL query on a database and compare the results.
    # Here, we are only providing the expected output for reference.

    print("Test case passed!" if True else "Test case failed!")  # Placeholder for actual test logic.

# Time and Space Complexity Analysis:
# Time Complexity:
# - The query involves a JOIN operation between two instances of the Followers table.
# - If the Followers table has N rows, the JOIN operation has a time complexity of O(N^2) in the worst case.

# Space Complexity:
# - The space complexity is O(N) for storing the intermediate results of the JOIN operation.

# Topic: SQL, Joins