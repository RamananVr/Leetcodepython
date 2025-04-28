"""
LeetCode Problem #1050: Actors and Directors Who Cooperated At Least Three Times

Problem Statement:
Table: ActorDirector

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| actor_id    | int     |
| director_id | int     |
| timestamp   | int     |
+-------------+---------+
(actor_id, director_id) is the primary key for this table.

Write an SQL query for a report that provides the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

Return the result table in any order.
"""

# Note: Since this is an SQL problem, we will provide the SQL query as part of the solution.
# However, we will also include a Python simulation of the solution for testing purposes.

# SQL Solution:
"""
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;
"""

# Python Simulation of the SQL Solution:
from collections import defaultdict

def actors_and_directors(data):
    """
    Simulates the SQL query for finding actor-director pairs who cooperated at least three times.

    :param data: List of tuples representing the ActorDirector table. Each tuple is (actor_id, director_id, timestamp).
    :return: List of tuples (actor_id, director_id) where the actor and director cooperated at least three times.
    """
    cooperation_count = defaultdict(int)

    # Count the number of cooperations for each (actor_id, director_id) pair
    for actor_id, director_id, _ in data:
        cooperation_count[(actor_id, director_id)] += 1

    # Filter pairs with at least three cooperations
    result = [(actor_id, director_id) for (actor_id, director_id), count in cooperation_count.items() if count >= 3]

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    data1 = [
        (1, 1, 100),
        (1, 1, 200),
        (1, 1, 300),
        (2, 1, 400),
        (2, 1, 500),
        (3, 2, 600),
        (3, 2, 700),
        (3, 2, 800),
        (3, 2, 900)
    ]
    print(actors_and_directors(data1))  # Expected Output: [(1, 1), (3, 2)]

    # Test Case 2
    data2 = [
        (1, 2, 100),
        (1, 2, 200),
        (2, 3, 300),
        (2, 3, 400),
        (2, 3, 500),
        (3, 4, 600),
        (3, 4, 700),
        (3, 4, 800),
        (4, 5, 900)
    ]
    print(actors_and_directors(data2))  # Expected Output: [(2, 3), (3, 4)]

    # Test Case 3
    data3 = [
        (1, 1, 100),
        (1, 1, 200),
        (2, 2, 300),
        (2, 2, 400),
        (3, 3, 500)
    ]
    print(actors_and_directors(data3))  # Expected Output: []

# Time and Space Complexity Analysis:
# Time Complexity: O(n), where n is the number of rows in the input data. We iterate through the data once to count cooperations.
# Space Complexity: O(k), where k is the number of unique (actor_id, director_id) pairs. We store these pairs in a dictionary.

# Topic: SQL, Hash Table