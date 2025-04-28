"""
LeetCode Problem #1407: Top Travellers

Problem Statement:
Table: Users
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| id             | int     |
| name           | varchar |
+----------------+---------+
id is the primary key for this table.
Each row of this table contains the name of a user.

Table: Rides
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| id             | int     |
| user_id        | int     |
| distance       | int     |
+----------------+---------+
id is the primary key for this table.
user_id is a foreign key (reference column id from Users table).
Each row of this table contains the distance traveled by a user in a ride.

Write an SQL query to report the distance traveled by each user, sorted by the distance traveled in descending order. If two users traveled the same distance, sort them by their name in ascending order.

The query result format is in the following example.

Example:
Users table:
+------+-----------+
| id   | name      |
+------+-----------+
| 1    | Alice     |
| 2    | Bob       |
| 3    | Alex      |
| 4    | Donald    |
| 5    | Lee       |
| 6    | Jonathan  |
+------+-----------+

Rides table:
+------+----------+----------+
| id   | user_id  | distance |
+------+----------+----------+
| 1    | 1        | 120      |
| 2    | 2        | 317      |
| 3    | 3        | 222      |
| 4    | 4        | 100      |
| 5    | 1        | 42       |
| 6    | 5        | 300      |
| 7    | 6        | 50       |
| 8    | 5        | 43       |
+------+----------+----------+

Result table:
+-----------+----------------+
| name      | travelled_distance |
+-----------+----------------+
| Bob       | 317            |
| Lee       | 343            |
| Alex      | 222            |
| Alice     | 162            |
| Donald    | 100            |
| Jonathan  | 50             |
+-----------+----------------+
"""

# Python Solution (Simulating SQL Query Execution)

# Note: Since this is an SQL problem, the solution is provided as an SQL query.
# Below is the SQL query that solves the problem.

"""
SQL Query:
SELECT u.name, 
       SUM(r.distance) AS travelled_distance
FROM Users u
JOIN Rides r
ON u.id = r.user_id
GROUP BY u.name
ORDER BY travelled_distance DESC, u.name ASC;
"""

# Example Test Cases
# Since this is an SQL problem, test cases would involve running the query on a database.
# Below is a Python simulation of the expected output based on the example data.

def test_top_travellers():
    # Input data
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Alex"},
        {"id": 4, "name": "Donald"},
        {"id": 5, "name": "Lee"},
        {"id": 6, "name": "Jonathan"},
    ]
    
    rides = [
        {"id": 1, "user_id": 1, "distance": 120},
        {"id": 2, "user_id": 2, "distance": 317},
        {"id": 3, "user_id": 3, "distance": 222},
        {"id": 4, "user_id": 4, "distance": 100},
        {"id": 5, "user_id": 1, "distance": 42},
        {"id": 6, "user_id": 5, "distance": 300},
        {"id": 7, "user_id": 6, "distance": 50},
        {"id": 8, "user_id": 5, "distance": 43},
    ]
    
    # Expected output
    expected_output = [
        {"name": "Bob", "travelled_distance": 317},
        {"name": "Lee", "travelled_distance": 343},
        {"name": "Alex", "travelled_distance": 222},
        {"name": "Alice", "travelled_distance": 162},
        {"name": "Donald", "travelled_distance": 100},
        {"name": "Jonathan", "travelled_distance": 50},
    ]
    
    # Simulate SQL query execution
    from collections import defaultdict
    
    # Aggregate distances by user_id
    user_distances = defaultdict(int)
    for ride in rides:
        user_distances[ride["user_id"]] += ride["distance"]
    
    # Map user_id to name
    user_names = {user["id"]: user["name"] for user in users}
    
    # Create result list
    result = [
        {"name": user_names[user_id], "travelled_distance": distance}
        for user_id, distance in user_distances.items()
    ]
    
    # Sort by travelled_distance DESC, name ASC
    result.sort(key=lambda x: (-x["travelled_distance"], x["name"]))
    
    # Assert the result matches the expected output
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Test passed!")

# Run the test
test_top_travellers()

# Time and Space Complexity Analysis
"""
Time Complexity:
- Aggregating distances: O(n), where n is the number of rides.
- Mapping user_id to name: O(m), where m is the number of users.
- Sorting the result: O(k log k), where k is the number of unique users.

Overall: O(n + m + k log k)

Space Complexity:
- Storage for user_distances: O(k), where k is the number of unique users.
- Storage for user_names: O(m), where m is the number of users.
- Storage for result: O(k).

Overall: O(n + m + k)

Note: In a real SQL execution, the database engine handles these complexities internally.

Topic: SQL
"""