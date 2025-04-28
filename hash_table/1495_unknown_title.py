"""
LeetCode Problem #1495: Friendly Movies Streamed Last Month

Problem Statement:
You are given a list of movies streamed last month. Each movie is represented as a tuple (movie_id, user_id), 
indicating that the user with user_id streamed the movie with movie_id. A movie is considered "friendly" if it 
was streamed by at least two different users.

Write a function `friendly_movies` that takes a list of tuples `streams` and returns a list of all movie_ids 
that are "friendly". The result should be sorted in ascending order.

Constraints:
- 1 <= len(streams) <= 10^5
- 1 <= movie_id, user_id <= 10^5
- Each tuple in streams is unique.
"""

from collections import defaultdict

def friendly_movies(streams):
    """
    Finds all "friendly" movies streamed by at least two different users.

    Args:
    streams (List[Tuple[int, int]]): A list of tuples where each tuple represents (movie_id, user_id).

    Returns:
    List[int]: A sorted list of movie_ids that are "friendly".
    """
    # Dictionary to store the set of users for each movie
    movie_to_users = defaultdict(set)

    # Populate the dictionary
    for movie_id, user_id in streams:
        movie_to_users[movie_id].add(user_id)

    # Find movies streamed by at least two different users
    friendly = [movie_id for movie_id, users in movie_to_users.items() if len(users) >= 2]

    # Return the sorted list of friendly movie_ids
    return sorted(friendly)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    streams1 = [(1, 101), (1, 102), (2, 101), (3, 103), (3, 104), (3, 105)]
    print(friendly_movies(streams1))  # Output: [1, 3]

    # Test Case 2
    streams2 = [(1, 101), (2, 102), (3, 103)]
    print(friendly_movies(streams2))  # Output: []

    # Test Case 3
    streams3 = [(1, 101), (1, 102), (1, 103), (2, 101), (2, 102), (3, 103)]
    print(friendly_movies(streams3))  # Output: [1, 2]

    # Test Case 4
    streams4 = []
    print(friendly_movies(streams4))  # Output: []

    # Test Case 5
    streams5 = [(1, 101), (2, 102), (1, 102), (3, 103), (3, 103)]
    print(friendly_movies(streams5))  # Output: [1]

"""
Time Complexity Analysis:
- Let n be the number of tuples in the input list `streams`.
- Building the `movie_to_users` dictionary involves iterating through the list once, which takes O(n).
- Checking the size of the user sets and filtering the movies takes O(m), where m is the number of unique movie_ids.
- Sorting the resulting list of friendly movies takes O(f * log(f)), where f is the number of friendly movies.
- In the worst case, f = m, so the overall time complexity is O(n + m * log(m)).

Space Complexity Analysis:
- The `movie_to_users` dictionary stores up to m keys, each with a set of users. In the worst case, the space 
  complexity is O(n) if every movie has a unique user.
- The space required for the result list is O(f), where f is the number of friendly movies.
- Overall, the space complexity is O(n).

Topic: Hash Table
"""