"""
LeetCode Question #620: Not Boring Movies

Problem Statement:
Table: Cinema

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| id             | int      |
| movie          | varchar  |
| description    | varchar  |
| rating         | float    |
+----------------+----------+
id is the primary key for this table.
Each row contains information about the id, movie name, description, and rating of a movie.
Rating is a 2 decimal places float in the range [0, 10].

Write an SQL query to find the movies with odd numbered IDs and a description that is not "boring".
Return the result table ordered by rating in descending order.

The query result format is in the following example:

Cinema table:
+----+-------------+-------------+--------+
| id | movie       | description | rating |
+----+-------------+-------------+--------+
| 1  | War         | great 3D    | 8.9    |
| 2  | Science     | boring      | 8.5    |
| 3  | Cars 2      | funny       | 7.2    |
| 4  | Ice Age     | boring      | 7.4    |
+----+-------------+-------------+--------+

Result table:
+----+-------------+-------------+--------+
| id | movie       | description | rating |
+----+-------------+-------------+--------+
| 1  | War         | great 3D    | 8.9    |
| 3  | Cars 2      | funny       | 7.2    |
+----+-------------+-------------+--------+

Explanation:
- The movies with odd numbered IDs are: War and Cars 2.
- The descriptions of these movies are not "boring".
- Their ratings are sorted in descending order.
"""

# Python Solution (Simulating SQL Query Execution)

# Since this is an SQL problem, we cannot directly execute it in Python.
# However, we can simulate the logic using Python code for demonstration purposes.

# Simulated Python solution for the problem:

def not_boring_movies(cinema):
    """
    Filters movies with odd IDs and non-boring descriptions, then sorts by rating in descending order.

    Args:
    cinema (list of dict): List of movie records, where each record is a dictionary with keys:
                           'id', 'movie', 'description', 'rating'.

    Returns:
    list of dict: Filtered and sorted list of movie records.
    """
    # Filter movies with odd IDs and non-boring descriptions
    filtered_movies = [
        movie for movie in cinema
        if movie['id'] % 2 != 0 and movie['description'] != 'boring'
    ]
    
    # Sort the filtered movies by rating in descending order
    sorted_movies = sorted(filtered_movies, key=lambda x: x['rating'], reverse=True)
    
    return sorted_movies


# Example Test Cases
if __name__ == "__main__":
    # Input Cinema Table
    cinema = [
        {"id": 1, "movie": "War", "description": "great 3D", "rating": 8.9},
        {"id": 2, "movie": "Science", "description": "boring", "rating": 8.5},
        {"id": 3, "movie": "Cars 2", "description": "funny", "rating": 7.2},
        {"id": 4, "movie": "Ice Age", "description": "boring", "rating": 7.4},
    ]

    # Expected Output
    expected_output = [
        {"id": 1, "movie": "War", "description": "great 3D", "rating": 8.9},
        {"id": 3, "movie": "Cars 2", "description": "funny", "rating": 7.2},
    ]

    # Test the function
    output = not_boring_movies(cinema)
    print("Output:", output)
    print("Expected:", expected_output)
    assert output == expected_output, "Test case failed!"

    print("All test cases passed!")


# Time and Space Complexity Analysis

"""
Time Complexity:
- Filtering the movies: O(n), where n is the number of records in the cinema table.
- Sorting the filtered movies: O(m * log(m)), where m is the number of filtered records.
Overall: O(n + m * log(m)).

Space Complexity:
- The filtered_movies list requires O(m) space, where m is the number of filtered records.
- The sorted_movies list also requires O(m) space.
Overall: O(m).

Note: In the worst case, m = n (all records are filtered), so the space complexity is O(n).
"""

# Topic: SQL Simulation / Filtering and Sorting