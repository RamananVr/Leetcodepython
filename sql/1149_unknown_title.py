"""
LeetCode Problem #1149: Article Views I

Problem Statement:
You are given a table called Views, containing the following columns:
- article_id (int): The ID of the article.
- author_id (int): The ID of the author who wrote the article.
- viewer_id (int): The ID of the user who viewed the article.
- view_date (date): The date when the article was viewed.

Write an SQL query to find all the authors who viewed at least one of their own articles. Return the result table sorted by id in ascending order.

The result format should be:
- id (int): The ID of the author who viewed at least one of their own articles.

Example:
Input:
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 2          | 3         | 3         | 2019-08-02 |
| 3          | 4         | 2         | 2019-08-05 |
| 4          | 4         | 4         | 2019-08-05 |
+------------+-----------+-----------+------------+

Output:
+------+
| id   |
+------+
| 3    |
| 4    |
+------+

Explanation:
- Author with ID = 3 viewed their own article with ID = 2 on 2019-08-02.
- Author with ID = 4 viewed their own article with ID = 4 on 2019-08-05.
"""

# Solution:
# Since this is an SQL problem, we will provide the SQL query as the solution.

"""
SQL Query:
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC;
"""

# Example Test Cases:
# The test cases for SQL problems are typically run in a database environment.
# Below is a representation of how the Views table would look and the expected output.

"""
Input:
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 2          | 3         | 3         | 2019-08-02 |
| 3          | 4         | 2         | 2019-08-05 |
| 4          | 4         | 4         | 2019-08-05 |
+------------+-----------+-----------+------------+

Output:
+------+
| id   |
+------+
| 3    |
| 4    |
+------+
"""

# Time and Space Complexity Analysis:
# Time Complexity: O(N), where N is the number of rows in the Views table. The query scans the table once to filter rows.
# Space Complexity: O(1), as no additional space is used apart from the result set.

# Topic: SQL