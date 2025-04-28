"""
LeetCode Problem #1045: Customers Who Bought All Products

Problem Statement:
Table: Customer

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
(customer_id, product_key) is the primary key for this table.
This table contains data about the products each customer bought.

Write an SQL query to report the customer ids from the Customer table that bought all the products.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 1           | 6           |
| 1           | 7           |
| 2           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 3           | 7           |
+-------------+-------------+

Output:
+-------------+
| customer_id |
+-------------+
| 1           |
| 3           |
+-------------+

Explanation:
The customers who bought all the products (5, 6, and 7) are customers with IDs 1 and 3.
"""

# Python Solution:
# Since this is an SQL problem, we will provide the SQL query as the solution.

"""
SQL Query Solution:

SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(DISTINCT product_key) FROM Customer);
"""

# Example Test Cases:
# The test cases for this problem would be run in an SQL environment, not in Python.
# However, we can describe the test cases here:

"""
Test Case 1:
Input:
Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 1           | 6           |
| 1           | 7           |
| 2           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 3           | 7           |
+-------------+-------------+

Output:
+-------------+
| customer_id |
+-------------+
| 1           |
| 3           |
+-------------+

Test Case 2:
Input:
Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 2           | 1           |
| 2           | 2           |
| 2           | 3           |
| 3           | 1           |
| 3           | 2           |
| 3           | 3           |
+-------------+-------------+

Output:
+-------------+
| customer_id |
+-------------+
| 3           |
+-------------+

Test Case 3:
Input:
Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 2           | 1           |
| 2           | 2           |
+-------------+-------------+

Output:
+-------------+
| customer_id |
+-------------+
| 1           |
| 2           |
+-------------+
"""

# Time and Space Complexity Analysis:
"""
Time Complexity:
- Let N be the number of rows in the Customer table.
- The subquery SELECT COUNT(DISTINCT product_key) FROM Customer runs in O(N) time.
- The main query groups the data by customer_id and counts distinct product_key values, which also takes O(N) time.
- Overall, the time complexity is O(N).

Space Complexity:
- The space complexity is O(U + P), where U is the number of unique customer_ids and P is the number of unique product_keys.
- This is because we need to store the grouped data and distinct counts in memory.
"""

# Topic: SQL, Aggregation, Group By