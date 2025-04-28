"""
LeetCode Problem #1795: Rearrange Products Table

Problem Statement:
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
product_id is the primary key for this table.
Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.

Write an SQL query to rearrange the Products table so that each row has (product_id, store, price). 
The store column will contain the name of the store, and the price column will contain the price in that store.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 1          | 100    | 200    | 300    |
| 2          | 400    | 500    | 600    |
+------------+--------+--------+--------+

Output:
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 1          | store1 | 100   |
| 1          | store2 | 200   |
| 1          | store3 | 300   |
| 2          | store1 | 400   |
| 2          | store2 | 500   |
| 2          | store3 | 600   |
+------------+--------+-------+
"""

# Solution:
# Since this is an SQL problem, the solution is written as an SQL query.

SQL_SOLUTION = """
SELECT product_id, 'store1' AS store, store1 AS price
FROM Products
UNION ALL
SELECT product_id, 'store2' AS store, store2 AS price
FROM Products
UNION ALL
SELECT product_id, 'store3' AS store, store3 AS price
FROM Products;
"""

"""
Example Test Cases:
Input:
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 1          | 100    | 200    | 300    |
| 2          | 400    | 500    | 600    |
+------------+--------+--------+--------+

Output:
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 1          | store1 | 100   |
| 1          | store2 | 200   |
| 1          | store3 | 300   |
| 2          | store1 | 400   |
| 2          | store2 | 500   |
| 2          | store3 | 600   |
+------------+--------+-------+
"""

"""
Time and Space Complexity Analysis:
- Time Complexity: O(n), where n is the number of rows in the Products table. The query processes each row three times (once for each store), but this is still linear in terms of the number of rows.
- Space Complexity: O(n), as the result table will contain three rows for each row in the original table.

Topic: SQL
"""