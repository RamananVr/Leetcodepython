"""
LeetCode Question #608: Tree Node

Problem Statement:
Table: Tree
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| p_id        | int  |
+-------------+------+
id is the primary key column for this table.
Each row of this table contains information about the id of a node and the id of its parent node in a tree.
The given structure always forms a valid tree.

Write an SQL query to report the type of each node in the tree.
The three types of nodes are:
- "Root": if the node is the root node (i.e., p_id is NULL).
- "Leaf": if the node is a leaf node (i.e., the node does not have any child nodes).
- "Inner": If the node is neither a root node nor a leaf node.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | NULL |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+

Output:
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
| 2  | Inner |
| 3  | Leaf  |
| 4  | Leaf  |
| 5  | Leaf  |
+----+-------+
"""

# Solution:
# Since this is an SQL problem, we will write the SQL query to solve it.

"""
SQL Query:
SELECT 
    t1.id,
    CASE 
        WHEN t1.p_id IS NULL THEN 'Root'
        WHEN t1.id NOT IN (SELECT DISTINCT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM Tree t1;
"""

# Example Test Cases:
# The test cases are based on the example provided in the problem statement.

"""
Input:
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | NULL |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+

Output:
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
| 2  | Inner |
| 3  | Leaf  |
| 4  | Leaf  |
| 5  | Leaf  |
+----+-------+
"""

# Time and Space Complexity Analysis:
# Time Complexity:
# - The query involves scanning the Tree table multiple times:
#   - Once for the main SELECT statement.
#   - Once for the subquery to find all parent IDs.
# - If there are N rows in the Tree table, the time complexity is O(N^2) in the worst case due to the subquery.

# Space Complexity:
# - The query does not use any additional space apart from the result set.
# - Space complexity is O(N), where N is the number of rows in the Tree table.

# Topic: SQL