"""
LeetCode Question #1264: Page Recommendations

Problem Statement:
You are given a table `Likes`, containing the following columns:
- user_id: The ID of the user.
- page_id: The ID of the page.

Write an SQL query to recommend pages to users based on the pages they liked. A page is recommended to a user if:
1. The user has not liked the page yet.
2. At least one other user who liked the same page as the user also liked the recommended page.

Return the result table in any order containing the following columns:
- user_id: The ID of the user.
- page_id: The ID of the recommended page.

Example:
Input:
Likes table:
+---------+---------+
| user_id | page_id |
+---------+---------+
| 1       | 101     |
| 1       | 102     |
| 2       | 101     |
| 2       | 103     |
| 3       | 101     |
| 3       | 104     |
| 4       | 105     |
+---------+---------+

Output:
+---------+---------+
| user_id | page_id |
+---------+---------+
| 1       | 103     |
| 1       | 104     |
| 2       | 102     |
| 2       | 104     |
| 3       | 102     |
| 3       | 103     |
+---------+---------+

Explanation:
User 1 likes pages 101 and 102. User 2 also likes page 101 and likes page 103. So, page 103 is recommended to user 1.
User 3 likes pages 101 and 104. User 2 also likes page 101 and likes page 103. So, page 103 is recommended to user 3.
User 2 likes pages 101 and 103. User 1 also likes page 101 and likes page 102. So, page 102 is recommended to user 2.
User 3 likes pages 101 and 104. User 1 also likes page 101 and likes page 102. So, page 102 is recommended to user 3.
"""

# Python Solution (Simulating the SQL Query Logic in Python)

def recommend_pages(likes):
    """
    Function to recommend pages to users based on the pages they liked.

    Args:
    likes (List[Tuple[int, int]]): A list of tuples where each tuple contains user_id and page_id.

    Returns:
    List[Tuple[int, int]]: A list of tuples containing user_id and recommended page_id.
    """
    from collections import defaultdict

    # Step 1: Build a mapping of users to pages they like
    user_to_pages = defaultdict(set)
    for user_id, page_id in likes:
        user_to_pages[user_id].add(page_id)

    # Step 2: Build a mapping of pages to users who like them
    page_to_users = defaultdict(set)
    for user_id, page_id in likes:
        page_to_users[page_id].add(user_id)

    # Step 3: Generate recommendations
    recommendations = set()
    for user_id in user_to_pages:
        liked_pages = user_to_pages[user_id]
        for page_id in liked_pages:
            # Find other users who like the same page
            other_users = page_to_users[page_id] - {user_id}
            for other_user in other_users:
                # Recommend pages liked by other users but not yet liked by the current user
                for other_page in user_to_pages[other_user]:
                    if other_page not in liked_pages:
                        recommendations.add((user_id, other_page))

    # Convert the set to a sorted list for consistent output
    return sorted(recommendations)

# Example Test Cases
if __name__ == "__main__":
    likes = [
        (1, 101),
        (1, 102),
        (2, 101),
        (2, 103),
        (3, 101),
        (3, 104),
        (4, 105)
    ]

    # Expected Output:
    # [
    #     (1, 103),
    #     (1, 104),
    #     (2, 102),
    #     (2, 104),
    #     (3, 102),
    #     (3, 103)
    # ]
    print(recommend_pages(likes))

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building `user_to_pages` and `page_to_users` mappings: O(n), where n is the number of rows in the input `likes`.
- Iterating through users and their liked pages: O(n * m), where n is the number of users and m is the average number of pages liked by a user.
- Overall complexity: O(n * m).

Space Complexity:
- Space used by `user_to_pages` and `page_to_users`: O(n), where n is the number of rows in the input `likes`.
- Space used by `recommendations`: O(r), where r is the number of recommendations generated.
- Overall complexity: O(n + r).

Topic: Hash Tables
"""