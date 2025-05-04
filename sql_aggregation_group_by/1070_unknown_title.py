"""
LeetCode Problem #1070: Product Sales Analysis III

Problem Statement:
Table: Sales

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| sale_id     | int     |
| product_id  | int     |
| year        | int     |
| quantity    | int     |
| price       | int     |
+-------------+---------+
sale_id is the primary key for this table.
Each row of this table shows the ID of a sale, the ID of the product sold, the year of the sale, the quantity sold, and the price per unit.

Write an SQL query that selects the product_id, year, quantity, and price for the first year of every product_id. 
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
| 3       | 200        | 2010 | 10       | 10000 |
| 8       | 300        | 2011 | 20       | 4500  |
+---------+------------+------+----------+-------+

Output:
+------------+------+----------+-------+
| product_id | year | quantity | price |
+------------+------+----------+-------+
| 100        | 2008 | 10       | 5000  |
| 200        | 2010 | 10       | 10000 |
| 300        | 2011 | 20       | 4500  |
+------------+------+----------+-------+

Explanation:
For product_id 100, the first year is 2008.
For product_id 200, the first year is 2010.
For product_id 300, the first year is 2011.
"""

# Solution:
# Since this is an SQL problem, we will write the SQL query to solve it.

"""
SQL Query:
SELECT product_id, year, quantity, price
FROM Sales
WHERE (product_id, year) IN (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
);
"""

# Example Test Cases:
# The test cases are based on the example provided in the problem statement.

"""
Input:
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
| 3       | 200        | 2010 | 10       | 10000 |
| 8       | 300        | 2011 | 20       | 4500  |
+---------+------------+------+----------+-------+

Output:
+------------+------+----------+-------+
| product_id | year | quantity | price |
+------------+------+----------+-------+
| 100        | 2008 | 10       | 5000  |
| 200        | 2010 | 10       | 10000 |
| 300        | 2011 | 20       | 4500  |
+------------+------+----------+-------+
"""

# Time and Space Complexity Analysis:
# Time Complexity: O(N log N), where N is the number of rows in the Sales table. 
# This is because we use a GROUP BY clause to group by product_id, which typically involves sorting or hashing.
# Space Complexity: O(N), where N is the number of rows in the Sales table. 
# This is due to the space required for the intermediate results of the subquery.

# Topic: SQL, Aggregation, Group By