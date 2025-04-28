"""
LeetCode Problem #1069: Product Sales Analysis II

Problem Statement:
Table: Sales

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key for this table.
product_id is a foreign key to Product table.

Table: Product

+----------------+-------+
| Column Name    | Type  |
+----------------+-------+
| product_id     | int   |
| product_name   | varchar |
+----------------+-------+
product_id is the primary key for this table.

Write an SQL query that reports the product_name, year, and price for each sale_id in the Sales table.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+

Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
+------------+--------------+

Output:
+--------------+------+-------+
| product_name | year | price |
+--------------+------+-------+
| Nokia        | 2008 | 5000 |
| Nokia        | 2009 | 5000 |
| Apple        | 2011 | 9000 |
+--------------+------+-------+
"""

# Solution:
# Since this is an SQL problem, the solution is written in SQL syntax.

SQL_SOLUTION = """
SELECT 
    p.product_name,
    s.year,
    s.price
FROM 
    Sales s
JOIN 
    Product p
ON 
    s.product_id = p.product_id;
"""

# Example Test Cases:
# The test cases are based on the example provided in the problem statement.

# Input:
# Sales table:
# +---------+------------+------+----------+-------+
# | sale_id | product_id | year | quantity | price |
# +---------+------------+------+----------+-------+
# | 1       | 100        | 2008 | 10       | 5000  |
# | 2       | 100        | 2009 | 12       | 5000  |
# | 7       | 200        | 2011 | 15       | 9000  |
# +---------+------------+------+----------+-------+

# Product table:
# +------------+--------------+
# | product_id | product_name |
# +------------+--------------+
# | 100        | Nokia        |
# | 200        | Apple        |
# +------------+--------------+

# Output:
# +--------------+------+-------+
# | product_name | year | price |
# +--------------+------+-------+
# | Nokia        | 2008 | 5000 |
# | Nokia        | 2009 | 5000 |
# | Apple        | 2011 | 9000 |
# +--------------+------+-------+

# Time and Space Complexity Analysis:
# Time Complexity:
# - The query involves a JOIN operation between the Sales and Product tables.
# - Assuming Sales has `m` rows and Product has `n` rows, the JOIN operation has a time complexity of O(m * n) in the worst case.
# - However, with proper indexing on `product_id`, the JOIN operation can be optimized to O(m + n).

# Space Complexity:
# - The space complexity is O(m + n) for storing the intermediate results of the JOIN operation.

# Topic: SQL, Database Queries