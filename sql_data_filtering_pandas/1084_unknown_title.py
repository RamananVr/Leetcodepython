"""
LeetCode Problem #1084: Sales Analysis I

Problem Statement:
Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key for this table.

Table: Sales

+-------------+------+
| Column Name | Type |
+-------------+------+
| seller_id   | int  |
| product_id  | int  |
| buyer_id    | int  |
| sale_date   | date |
+-------------+------+
There is no primary key for this table. It may contain duplicate rows.

Write an SQL query that reports the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

The query result format is in the following example:

Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 1          | S8           |
| 2          | G4           |
| 3          | iPhone       |
+------------+--------------+

Sales table:
+-----------+------------+----------+------------+
| seller_id | product_id | buyer_id | sale_date  |
+-----------+------------+----------+------------+
| 1         | 1          | 1        | 2019-01-21 |
| 2         | 1          | 2        | 2019-02-17 |
| 3         | 1          | 3        | 2019-02-24 |
| 4         | 2          | 4        | 2019-03-01 |
| 5         | 3          | 5        | 2019-12-11 |
+-----------+------------+----------+------------+

Result table:
+--------------+
| product_name |
+--------------+
| S8           |
| G4           |
+--------------+
Only products 1 and 2 were sold in the first quarter of 2019 while product 3 was sold after.

"""

# Python Solution (Simulating the SQL Query with Pandas)

import pandas as pd

# Define the Product table
product_data = {
    "product_id": [1, 2, 3],
    "product_name": ["S8", "G4", "iPhone"]
}
product_df = pd.DataFrame(product_data)

# Define the Sales table
sales_data = {
    "seller_id": [1, 2, 3, 4, 5],
    "product_id": [1, 1, 1, 2, 3],
    "buyer_id": [1, 2, 3, 4, 5],
    "sale_date": ["2019-01-21", "2019-02-17", "2019-02-24", "2019-03-01", "2019-12-11"]
}
sales_df = pd.DataFrame(sales_data)

# Convert sale_date to datetime for filtering
sales_df["sale_date"] = pd.to_datetime(sales_df["sale_date"])

# Filter sales in the first quarter of 2019
first_quarter_sales = sales_df[
    (sales_df["sale_date"] >= "2019-01-01") & (sales_df["sale_date"] <= "2019-03-31")
]

# Get product IDs sold in the first quarter
first_quarter_product_ids = set(first_quarter_sales["product_id"])

# Get product IDs sold outside the first quarter
outside_quarter_sales = sales_df[
    (sales_df["sale_date"] < "2019-01-01") | (sales_df["sale_date"] > "2019-03-31")
]
outside_quarter_product_ids = set(outside_quarter_sales["product_id"])

# Find products sold only in the first quarter
exclusive_product_ids = first_quarter_product_ids - outside_quarter_product_ids

# Filter the Product table for the result
result_df = product_df[product_df["product_id"].isin(exclusive_product_ids)][["product_name"]]

# Print the result
print(result_df)

# Example Test Cases
"""
Input:
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 1          | S8           |
| 2          | G4           |
| 3          | iPhone       |
+------------+--------------+

Sales table:
+-----------+------------+----------+------------+
| seller_id | product_id | buyer_id | sale_date  |
+-----------+------------+----------+------------+
| 1         | 1          | 1        | 2019-01-21 |
| 2         | 1          | 2        | 2019-02-17 |
| 3         | 1          | 3        | 2019-02-24 |
| 4         | 2          | 4        | 2019-03-01 |
| 5         | 3          | 5        | 2019-12-11 |
+-----------+------------+----------+------------+

Output:
+--------------+
| product_name |
+--------------+
| S8           |
| G4           |
+--------------+
"""

# Time and Space Complexity Analysis
"""
Time Complexity:
- Filtering the sales table for the first quarter: O(n), where n is the number of rows in the Sales table.
- Filtering the sales table for outside the first quarter: O(n).
- Set operations to find exclusive product IDs: O(k), where k is the number of unique product IDs.
- Filtering the Product table: O(m), where m is the number of rows in the Product table.

Overall time complexity: O(n + m).

Space Complexity:
- Space used for intermediate filtered DataFrames: O(n).
- Space used for sets of product IDs: O(k).

Overall space complexity: O(n + k).

"""

# Topic: SQL, Data Filtering, Pandas