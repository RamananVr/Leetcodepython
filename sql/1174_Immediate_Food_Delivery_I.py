"""
LeetCode Problem #1174: Immediate Food Delivery I

Problem Statement:
Table: Delivery

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
| delivery_date               | date    |
+-----------------------------+---------+
delivery_id is the primary key for this table.
This table contains information about food delivery orders.

Write an SQL query to find the percentage of orders that were delivered on the customer’s preferred delivery date.

Return the result as a float with two decimal places.

The query result format is in the following example:

Delivery table:
+-------------+-------------+------------+-----------------------------+---------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date | delivery_date |
+-------------+-------------+------------+-----------------------------+---------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  | 2019-08-02    |
| 2           | 2           | 2019-08-02 | 2019-08-02                  | 2019-08-03    |
| 3           | 3           | 2019-08-03 | 2019-08-04                  | 2019-08-04    |
| 4           | 4           | 2019-08-04 | 2019-08-04                  | 2019-08-04    |
+-------------+-------------+------------+-----------------------------+---------------+

Result table:
+----------------------+
| immediate_percentage |
+----------------------+
| 50.00                |
+----------------------+
The orders with delivery_id 1 and 4 were delivered on the customer’s preferred delivery date, so the immediate percentage is (2/4)*100 = 50.00.
"""

# Solution:
# Since this is an SQL problem, we will write the SQL query to solve it.

"""
SQL Query:
SELECT
    ROUND(SUM(CASE WHEN customer_pref_delivery_date = delivery_date THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS immediate_percentage
FROM
    Delivery;
"""

# Example Test Cases:
# The test cases are based on the example provided in the problem statement.

"""
Input:
Delivery table:
+-------------+-------------+------------+-----------------------------+---------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date | delivery_date |
+-------------+-------------+------------+-----------------------------+---------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  | 2019-08-02    |
| 2           | 2           | 2019-08-02 | 2019-08-02                  | 2019-08-03    |
| 3           | 3           | 2019-08-03 | 2019-08-04                  | 2019-08-04    |
| 4           | 4           | 2019-08-04 | 2019-08-04                  | 2019-08-04    |
+-------------+-------------+------------+-----------------------------+---------------+

Output:
+----------------------+
| immediate_percentage |
+----------------------+
| 50.00                |
+----------------------+
"""

# Time and Space Complexity Analysis:
# Time Complexity: O(N), where N is the number of rows in the Delivery table. The query scans the table once to calculate the sum and count.
# Space Complexity: O(1), as no additional space is used apart from the query's internal operations.

# Topic: SQL