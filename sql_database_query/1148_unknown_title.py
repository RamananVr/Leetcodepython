"""
LeetCode Problem #1148: Article Views I

Problem Statement:
Table: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
+---------------+---------+
There is no primary key for this table. It may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author).

Write an SQL query to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

The query result format is in the following example.

Example:
Input:
Views table:
+------------+-----------+-----------+
| article_id | author_id | viewer_id |
+------------+-----------+-----------+
| 1          | 3         | 5         |
| 2          | 3         | 3         |
| 3          | 4         | 4         |
| 4          | 4         | 5         |
+------------+-----------+-----------+

Output:
+-----------+
| author_id |
+-----------+
| 3         |
| 4         |
+-----------+
"""

# Python Solution
# Since this is an SQL problem, we will write the SQL query as the solution.

"""
SQL Solution:
SELECT DISTINCT author_id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id;
"""

# Example Test Cases
"""
Input:
Views table:
+------------+-----------+-----------+
| article_id | author_id | viewer_id |
+------------+-----------+-----------+
| 1          | 3         | 5         |
| 2          | 3         | 3         |
| 3          | 4         | 4         |
| 4          | 4         | 5         |
+------------+-----------+-----------+

Output:
+-----------+
| author_id |
+-----------+
| 3         |
| 4         |
+-----------+
"""

# Time and Space Complexity Analysis
"""
Time Complexity:
The query scans the Views table and filters rows where `author_id = viewer_id`. 
Assuming there are N rows in the table, the time complexity is O(N).

Space Complexity:
The space complexity is O(1) since the query does not use any additional data structures.
"""

# Topic: SQL, Database Query