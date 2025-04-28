"""
LeetCode Problem #1082: Sales Analysis I

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
There is no primary key for this table. It may have duplicate rows.

Write an SQL query that reports all the products that were only sold by one distinct seller.

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
| 1         | 2          | 3        | 2019-06-02 |
| 1         | 3          | 4        | 2019-05-13 |
| 2         | 3          | 5        | 2019-03-11 |
+-----------+------------+----------+------------+

Result table:
+--------------+
| product_name |
+--------------+
| G4           |
+--------------+
Product 1 was sold by 2 different sellers (1 and 2).
Product 2 was sold by 1 seller (1).
Product 3 was sold by 2 different sellers (1 and 2).
Hence, product 2 is the only product sold by one distinct seller.
"""

# Python Solution (Simulating the SQL Query using Pandas)

import pandas as pd

def sales_analysis(product_data, sales_data):
    """
    Function to find products sold by only one distinct seller.

    Args:
    product_data (list of dict): List of dictionaries representing the Product table.
    sales_data (list of dict): List of dictionaries representing the Sales table.

    Returns:
    list: List of product names sold by only one distinct seller.
    """
    # Convert input data to DataFrames
    product_df = pd.DataFrame(product_data)
    sales_df = pd.DataFrame(sales_data)
    
    # Group by product_id and count distinct sellers
    seller_count = sales_df.groupby('product_id')['seller_id'].nunique().reset_index()
    seller_count.columns = ['product_id', 'distinct_sellers']
    
    # Filter products with only one distinct seller
    single_seller_products = seller_count[seller_count['distinct_sellers'] == 1]
    
    # Merge with product table to get product names
    result = pd.merge(single_seller_products, product_df, on='product_id', how='inner')
    
    # Return the product names as a list
    return result['product_name'].tolist()

# Example Test Cases
if __name__ == "__main__":
    # Product table data
    product_data = [
        {"product_id": 1, "product_name": "S8"},
        {"product_id": 2, "product_name": "G4"},
        {"product_id": 3, "product_name": "iPhone"}
    ]
    
    # Sales table data
    sales_data = [
        {"seller_id": 1, "product_id": 1, "buyer_id": 1, "sale_date": "2019-01-21"},
        {"seller_id": 2, "product_id": 1, "buyer_id": 2, "sale_date": "2019-02-17"},
        {"seller_id": 1, "product_id": 2, "buyer_id": 3, "sale_date": "2019-06-02"},
        {"seller_id": 1, "product_id": 3, "buyer_id": 4, "sale_date": "2019-05-13"},
        {"seller_id": 2, "product_id": 3, "buyer_id": 5, "sale_date": "2019-03-11"}
    ]
    
    # Expected Output: ['G4']
    print(sales_analysis(product_data, sales_data))

"""
Time and Space Complexity Analysis:

Time Complexity:
- Grouping by product_id and counting distinct sellers: O(n), where n is the number of rows in the Sales table.
- Merging with the Product table: O(m), where m is the number of rows in the Product table.
Overall: O(n + m)

Space Complexity:
- Space used by the DataFrames and intermediate results: O(n + m).
Overall: O(n + m)

Topic: SQL Simulation using Pandas
"""