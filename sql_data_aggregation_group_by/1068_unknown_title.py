"""
LeetCode Problem #1068: Product Sales Analysis I

Problem Statement:
Table: Sales

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| seller_id   | int   |
| product_id  | int   |
| buyer_id    | int   |
| sale_date   | date  |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(seller_id, product_id, buyer_id, sale_date) is the primary key for this table.
This table contains information about the products sold by a seller, including the price and quantity.

Write an SQL query that reports the total sales amount for each seller. The total sales amount is calculated as 
the sum of the product of the quantity sold and the price of each sale.

The query result format is in the following example:

Sales table:
+-----------+------------+----------+------------+----------+-------+
| seller_id | product_id | buyer_id | sale_date  | quantity | price |
+-----------+------------+----------+------------+----------+-------+
| 1         | 1          | 1        | 2020-01-01 | 10       | 500   |
| 2         | 2          | 1        | 2020-02-02 | 5        | 200   |
| 1         | 3          | 2        | 2020-02-03 | 6        | 100   |
| 3         | 4          | 2        | 2020-02-04 | 2        | 300   |
+-----------+------------+----------+------------+----------+-------+

Result table:
+-----------+----------------+
| seller_id | total_amount   |
+-----------+----------------+
| 1         | 5600          |
| 2         | 1000          |
| 3         | 600           |
+-----------+----------------+
Seller 1 sold products with a total amount of (10 * 500) + (6 * 100) = 5600.
Seller 2 sold products with a total amount of (5 * 200) = 1000.
Seller 3 sold products with a total amount of (2 * 300) = 600.
"""

# Python Solution (Simulating SQL Query with Pandas)

import pandas as pd

def product_sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the total sales amount for each seller.

    Args:
    sales (pd.DataFrame): A DataFrame containing the sales data with columns:
                          ['seller_id', 'product_id', 'buyer_id', 'sale_date', 'quantity', 'price'].

    Returns:
    pd.DataFrame: A DataFrame with columns ['seller_id', 'total_amount'], where total_amount is the sum of
                  quantity * price for each seller.
    """
    # Calculate the total sales amount for each row
    sales['total_amount'] = sales['quantity'] * sales['price']
    
    # Group by seller_id and sum the total_amount
    result = sales.groupby('seller_id', as_index=False)['total_amount'].sum()
    
    # Rename the column to match the expected output
    result.rename(columns={'total_amount': 'total_amount'}, inplace=True)
    
    return result


# Example Test Cases
if __name__ == "__main__":
    # Example Sales Data
    sales_data = {
        "seller_id": [1, 2, 1, 3],
        "product_id": [1, 2, 3, 4],
        "buyer_id": [1, 1, 2, 2],
        "sale_date": ["2020-01-01", "2020-02-02", "2020-02-03", "2020-02-04"],
        "quantity": [10, 5, 6, 2],
        "price": [500, 200, 100, 300]
    }
    sales_df = pd.DataFrame(sales_data)
    
    # Expected Output:
    # +-----------+----------------+
    # | seller_id | total_amount   |
    # +-----------+----------------+
    # | 1         | 5600          |
    # | 2         | 1000          |
    # | 3         | 600           |
    # +-----------+----------------+
    
    result = product_sales_analysis(sales_df)
    print(result)


# Time and Space Complexity Analysis

# Time Complexity:
# - Calculating the 'total_amount' column is O(n), where n is the number of rows in the DataFrame.
# - Grouping by 'seller_id' and summing is O(n) in the average case.
# - Overall time complexity: O(n).

# Space Complexity:
# - The space complexity is O(n) for storing the intermediate 'total_amount' column and the grouped result.
# - Overall space complexity: O(n).

# Topic: SQL, Data Aggregation, Group By