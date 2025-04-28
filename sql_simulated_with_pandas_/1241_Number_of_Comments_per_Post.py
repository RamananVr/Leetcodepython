"""
LeetCode Problem #1241: Number of Comments per Post

Problem Statement:
Table: Comments

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| comment_id     | int     |
| user_id        | int     |
| post_id        | int     |
+----------------+---------+
(comment_id, user_id, post_id) is the primary key for this table.

Write an SQL query to find the number of comments each post has received.

The result table should contain two columns:
- post_id: the ID of the post.
- number_of_comments: the number of comments the post has received.

Return the result table ordered by post_id in ascending order.

The query result format is in the following example.

Example:
Input:
Comments table:
+------------+---------+---------+
| comment_id | user_id | post_id |
+------------+---------+---------+
| 1          | 1       | 1       |
| 2          | 2       | 1       |
| 3          | 1       | 2       |
| 4          | 2       | 2       |
| 5          | 3       | 2       |
+------------+---------+---------+

Output:
+---------+-------------------+
| post_id | number_of_comments|
+---------+-------------------+
| 1       | 2                 |
| 2       | 3                 |
+---------+-------------------+

Explanation:
Post with ID 1 has 2 comments, while post with ID 2 has 3 comments.
"""

# Python Solution (Simulating SQL Query with Pandas)
import pandas as pd

def number_of_comments_per_post(comments: pd.DataFrame) -> pd.DataFrame:
    """
    Function to calculate the number of comments per post.

    Args:
    comments (pd.DataFrame): A DataFrame containing the comments table with columns:
                             'comment_id', 'user_id', 'post_id'.

    Returns:
    pd.DataFrame: A DataFrame containing two columns:
                  'post_id' and 'number_of_comments', sorted by 'post_id' in ascending order.
    """
    # Group by 'post_id' and count the number of comments for each post
    result = comments.groupby('post_id').size().reset_index(name='number_of_comments')
    
    # Sort the result by 'post_id' in ascending order
    result = result.sort_values(by='post_id').reset_index(drop=True)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Input Data
    data = {
        "comment_id": [1, 2, 3, 4, 5],
        "user_id": [1, 2, 1, 2, 3],
        "post_id": [1, 1, 2, 2, 2]
    }
    comments = pd.DataFrame(data)

    # Expected Output:
    # +---------+-------------------+
    # | post_id | number_of_comments|
    # +---------+-------------------+
    # | 1       | 2                 |
    # | 2       | 3                 |
    # +---------+-------------------+
    print(number_of_comments_per_post(comments))

"""
Time Complexity Analysis:
- Grouping the DataFrame by 'post_id' takes O(n), where n is the number of rows in the input DataFrame.
- Counting the size of each group is also O(n).
- Sorting the result by 'post_id' takes O(k log k), where k is the number of unique post IDs.
- Overall time complexity: O(n + k log k).

Space Complexity Analysis:
- The space complexity is O(k), where k is the number of unique post IDs, as we store the grouped results.

Topic: SQL (Simulated with Pandas)
"""