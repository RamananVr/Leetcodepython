"""
LeetCode Question #603: Consecutive Available Seats

Problem Statement:
Table: Seat
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key column for this table.
Each row of this table indicates whether the seat id is occupied by a student.

Write an SQL query to find the id of the seat which is not occupied and the id of the next seat which is also not occupied. 
Return the result table ordered by id.

The query result format is in the following example.

Example:
Input:
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | NULL    |
| 4  | NULL    |
| 5  | Emerson |
| 6  | NULL    |
+----+---------+

Output:
+----+-----+
| id | next|
+----+-----+
| 3  | 4   |
+----+-----+
| 4  | 6   |
+----+-----+

Explanation:
The seat with id 3 is not occupied and the next seat (id 4) is also not occupied.
The seat with id 4 is not occupied and the next seat (id 6) is also not occupied.
The seat with id 6 is not included because there is no next seat.
"""

# Solution:
"""
Since this is an SQL problem, the solution is written in SQL syntax.
"""

# SQL Query:
"""
SELECT 
    a.id AS id, 
    b.id AS next
FROM 
    Seat a
JOIN 
    Seat b
ON 
    a.id + 1 = b.id
WHERE 
    a.student IS NULL AND b.student IS NULL
ORDER BY 
    a.id;
"""

# Example Test Cases:
"""
Input:
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | NULL    |
| 4  | NULL    |
| 5  | Emerson |
| 6  | NULL    |
+----+---------+

Output:
+----+-----+
| id | next|
+----+-----+
| 3  | 4   |
+----+-----+
| 4  | 6   |
+----+-----+
"""

# Time and Space Complexity Analysis:
"""
Time Complexity:
The query involves a JOIN operation between two instances of the Seat table. 
If the table has N rows, the JOIN operation will take O(N) time in the worst case.

Space Complexity:
The query does not use any additional space apart from the result set, which is proportional to the number of rows satisfying the conditions. 
Thus, the space complexity is O(M), where M is the number of rows in the result set.
"""

# Topic: SQL