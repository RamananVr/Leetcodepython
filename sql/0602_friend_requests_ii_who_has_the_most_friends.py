"""
LeetCode Question #602: Friend Requests II: Who Has the Most Friends

Problem Statement:
Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key for this table.
name is the name of the person.

Table: FriendRequest
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| sender_id   | int     |
| send_to_id  | int     |
+-------------+---------+
There is no primary key for this table. It may contain duplicates.
Each row in this table indicates that the person with id sender_id sent a friend request to the person with id send_to_id.

Write an SQL query to find the people who have the most friends and the number of their friends.

A friend request sent from sender_id to send_to_id is considered accepted if sender_id in (SELECT id FROM Person) and send_to_id in (SELECT id FROM Person).

Return the result table in any order. The result format is in the following example.

Example:
Input:
Person table:
+----+-------+
| id | name  |
+----+-------+
| 1  | A     |
| 2  | B     |
| 3  | C     |
| 4  | D     |
+----+-------+

FriendRequest table:
+-----------+-----------+
| sender_id | send_to_id|
+-----------+-----------+
| 1         | 2         |
| 1         | 3         |
| 1         | 4         |
| 2         | 4         |
| 3         | 4         |
| 4         | 1         |
+-----------+-----------+

Output:
+----+-----+
| id | num |
+----+-----+
| 4  | 3   |
+----+-----+

Explanation:
The person with id=4 has three friends (id=1, id=2, id=3).
"""

# Python Solution
# Note: Since this is an SQL problem, the solution is provided as an SQL query.

SQL_QUERY = """
SELECT
    p.id,
    COUNT(DISTINCT fr.sender_id) AS num
FROM
    Person p
LEFT JOIN
    FriendRequest fr
ON
    p.id = fr.send_to_id
WHERE
    fr.sender_id IN (SELECT id FROM Person)
GROUP BY
    p.id
ORDER BY
    num DESC
LIMIT 1;
"""

# Example Test Cases
# These test cases are provided for clarity on how the SQL query works.

"""
Input:
Person table:
+----+-------+
| id | name  |
+----+-------+
| 1  | A     |
| 2  | B     |
| 3  | C     |
| 4  | D     |
+----+-------+

FriendRequest table:
+-----------+-----------+
| sender_id | send_to_id|
+-----------+-----------+
| 1         | 2         |
| 1         | 3         |
| 1         | 4         |
| 2         | 4         |
| 3         | 4         |
| 4         | 1         |
+-----------+-----------+

Output:
+----+-----+
| id | num |
+----+-----+
| 4  | 3   |
+----+-----+
"""

# Time and Space Complexity Analysis
"""
Time Complexity:
- The query involves a JOIN operation between the `Person` and `FriendRequest` tables, which is O(N * M) where N is the number of rows in `Person` and M is the number of rows in `FriendRequest`.
- The COUNT operation and GROUP BY are O(M) for the `FriendRequest` table.
- The subquery to check if `sender_id` exists in `Person` is O(N).
- Overall complexity: O(N * M).

Space Complexity:
- The space complexity is O(N + M) due to the storage of intermediate results during the JOIN and GROUP BY operations.

Primary Topic: SQL
"""