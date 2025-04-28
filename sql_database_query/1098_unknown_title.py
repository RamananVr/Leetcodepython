"""
LeetCode Problem #1098: Unpopular Books

Problem Statement:
You are given a table `Books` with the following columns:
- `book_id` (int): The ID of the book.
- `author_id` (int): The ID of the author of the book.
- `sold` (int): The number of copies sold for the book.

Write an SQL query to find the `author_id` of all authors who have sold fewer than 500 copies for every book they have written.

Return the result table in any order.

Example:
Books table:
+---------+-----------+------+
| book_id | author_id | sold |
+---------+-----------+------+
| 1       | 1         | 600  |
| 2       | 1         | 500  |
| 3       | 2         | 200  |
| 4       | 2         | 300  |
| 5       | 3         | 1000 |
+---------+-----------+------+

Result table:
+-----------+
| author_id |
+-----------+
| 2         |
+-----------+

Explanation:
- Author 1 has sold 600 copies for book 1 and 500 copies for book 2. Since not all books have sold fewer than 500 copies, author 1 is not included.
- Author 2 has sold 200 copies for book 3 and 300 copies for book 4. Since all books have sold fewer than 500 copies, author 2 is included.
- Author 3 has sold 1000 copies for book 5. Since not all books have sold fewer than 500 copies, author 3 is not included.
"""

# Solution:
# Since this is an SQL problem, the solution is provided as an SQL query.

"""
SQL Query:
SELECT DISTINCT author_id
FROM Books
WHERE author_id NOT IN (
    SELECT author_id
    FROM Books
    WHERE sold >= 500
);
"""

# Example Test Cases:
"""
Input:
Books table:
+---------+-----------+------+
| book_id | author_id | sold |
+---------+-----------+------+
| 1       | 1         | 600  |
| 2       | 1         | 500  |
| 3       | 2         | 200  |
| 4       | 2         | 300  |
| 5       | 3         | 1000 |
+---------+-----------+------+

Output:
+-----------+
| author_id |
+-----------+
| 2         |
+-----------+
"""

# Time and Space Complexity Analysis:
"""
Time Complexity:
- The query involves scanning the `Books` table twice: once for the main query and once for the subquery.
- Let `n` be the number of rows in the `Books` table. The time complexity is O(n).

Space Complexity:
- The space complexity is O(n) due to the storage required for the intermediate results of the subquery.

Overall, the query is efficient for typical database sizes.

"""

# Topic: SQL, Database Query