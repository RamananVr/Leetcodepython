"""
LeetCode Problem #1729: Find Followers Count

Problem Statement:
You are given a table `Followers` with the following structure:

| Column Name | Type    |
|-------------|---------|
| user_id     | int     |
| follower_id | int     |

(user_id, follower_id) is the primary key for this table.
Each row of this table indicates that the user with ID `follower_id` is following the user with ID `user_id`.

Write an SQL query to find the number of followers for each user. The result table should have the following structure:

| Column Name | Type    |
|-------------|---------|
| user_id     | int     |
| followers   | int     |

The result table should be sorted by `user_id` in ascending order.

Note: Since this is an SQL problem, we will provide a Python solution to simulate the behavior of the query using Python data structures.

"""

# Python Solution
from collections import defaultdict

def find_followers_count(followers):
    """
    Simulates the SQL query to find the number of followers for each user.

    :param followers: List of tuples where each tuple represents (user_id, follower_id)
    :return: List of tuples where each tuple represents (user_id, followers_count)
    """
    # Dictionary to count followers for each user
    followers_count = defaultdict(int)

    # Count the followers for each user
    for user_id, follower_id in followers:
        followers_count[user_id] += 1

    # Convert the dictionary to a sorted list of tuples
    result = sorted(followers_count.items())

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    followers = [
        (1, 3),
        (2, 3),
        (3, 1),
        (3, 2),
        (4, 1)
    ]
    print(find_followers_count(followers))
    # Expected Output: [(1, 1), (2, 1), (3, 2), (4, 1)]

    # Test Case 2
    followers = [
        (1, 2),
        (1, 3),
        (2, 1),
        (2, 3),
        (3, 1),
        (3, 2)
    ]
    print(find_followers_count(followers))
    # Expected Output: [(1, 2), (2, 2), (3, 2)]

    # Test Case 3
    followers = []
    print(find_followers_count(followers))
    # Expected Output: []

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting followers involves iterating through the `followers` list, which takes O(n), where n is the number of rows in the input.
- Sorting the dictionary keys takes O(k log k), where k is the number of unique users.

Overall Time Complexity: O(n + k log k)

Space Complexity:
- The `followers_count` dictionary stores up to k entries, where k is the number of unique users.
- The result list also stores up to k entries.

Overall Space Complexity: O(k)
"""

# Topic: Hash Table, Sorting