"""
LeetCode Problem #1633: Percentage of Users Attended a Contest

Problem Statement:
SQL Schema:
Table: Users
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| user_name      | varchar |
+----------------+---------+
user_id is the primary key for this table.
Each row of this table contains the ID and the name of a user.

Table: Register
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| contest_id     | int     |
| user_id        | int     |
+----------------+---------+
(contest_id, user_id) is the primary key for this table.
Each row of this table indicates that a user with user_id registered for a contest with contest_id.

Write an SQL query to find the percentage of the users registered for at least one contest rounded to two decimal places.

The query result format is in the following example:

Users table:
+---------+-----------+
| user_id | user_name |
+---------+-----------+
| 6       | Alice     |
| 2       | Bob       |
| 7       | Alex      |
+---------+-----------+

Register table:
+------------+---------+
| contest_id | user_id |
+------------+---------+
| 215        | 6       |
| 209        | 2       |
+------------+---------+

Result table:
+------------+
| percentage |
+------------+
| 66.67      |
+------------+
Alice and Bob have registered for at least one contest out of 3 users. The percentage is (2/3) * 100 = 66.67.
"""

# Note: Since this is an SQL problem, we cannot directly write a Python solution for it.
# However, we can simulate the logic in Python for educational purposes.

# Python Simulation of the SQL Problem
def percentage_of_users_attended(users, register):
    """
    Simulates the SQL query to calculate the percentage of users who registered for at least one contest.

    :param users: List of dictionaries representing the Users table.
    :param register: List of dictionaries representing the Register table.
    :return: Float representing the percentage of users who registered for at least one contest.
    """
    # Extract all user_ids from the Users table
    total_users = {user['user_id'] for user in users}
    
    # Extract all user_ids from the Register table who registered for at least one contest
    registered_users = {entry['user_id'] for entry in register}
    
    # Calculate the percentage of users who registered
    percentage = (len(registered_users) / len(total_users)) * 100 if total_users else 0
    return round(percentage, 2)

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    users = [
        {"user_id": 6, "user_name": "Alice"},
        {"user_id": 2, "user_name": "Bob"},
        {"user_id": 7, "user_name": "Alex"}
    ]
    register = [
        {"contest_id": 215, "user_id": 6},
        {"contest_id": 209, "user_id": 2}
    ]
    print(percentage_of_users_attended(users, register))  # Output: 66.67

    # Example 2
    users = [
        {"user_id": 1, "user_name": "John"},
        {"user_id": 2, "user_name": "Jane"}
    ]
    register = []
    print(percentage_of_users_attended(users, register))  # Output: 0.0

    # Example 3
    users = []
    register = []
    print(percentage_of_users_attended(users, register))  # Output: 0.0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Extracting user_ids from the Users table: O(U), where U is the number of users.
- Extracting user_ids from the Register table: O(R), where R is the number of registrations.
- Calculating the percentage: O(1).
Overall: O(U + R).

Space Complexity:
- Storing user_ids from the Users table: O(U).
- Storing user_ids from the Register table: O(R).
Overall: O(U + R).
"""

# Topic: SQL Simulation, Set Operations