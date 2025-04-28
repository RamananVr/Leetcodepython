"""
LeetCode Question #1549: The Most Recent Orders for Each Product

Problem Statement:
Table: Orders
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| order_date    | date    |
| quantity      | int     |
+---------------+---------+
(product_id, order_date) is the primary key for this table.
This table contains information about the quantity of products ordered on specific dates.

Write an SQL query to find the most recent order (i.e., the order with the latest order_date) for each product. 
If there are multiple most recent orders for the same product, return all of them.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Orders table:
+------------+------------+----------+
| product_id | order_date | quantity |
+------------+------------+----------+
| 1          | 2020-06-01 | 10       |
| 1          | 2020-06-02 | 15       |
| 2          | 2020-06-01 | 5        |
| 2          | 2020-05-30 | 9        |
| 3          | 2020-06-01 | 20       |
| 3          | 2020-06-01 | 30       |
+------------+------------+----------+

Output:
+------------+------------+----------+
| product_id | order_date | quantity |
+------------+------------+----------+
| 1          | 2020-06-02 | 15       |
| 2          | 2020-06-01 | 5        |
| 3          | 2020-06-01 | 20       |
| 3          | 2020-06-01 | 30       |
+------------+------------+----------+

Explanation:
- The most recent order for product 1 is on 2020-06-02 with quantity 15.
- The most recent order for product 2 is on 2020-06-01 with quantity 5.
- The most recent orders for product 3 are both on 2020-06-01 with quantities 20 and 30.
"""

# Python Solution (Simulating SQL Query Using Pandas)
import pandas as pd

def most_recent_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Function to find the most recent orders for each product.
    
    Args:
    orders (pd.DataFrame): A DataFrame containing columns ['product_id', 'order_date', 'quantity'].
    
    Returns:
    pd.DataFrame: A DataFrame containing the most recent orders for each product.
    """
    # Convert order_date to datetime for proper comparison
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    
    # Find the most recent order_date for each product_id
    max_dates = orders.groupby('product_id')['order_date'].max().reset_index()
    max_dates.rename(columns={'order_date': 'max_order_date'}, inplace=True)
    
    # Merge the max_dates back with the original orders DataFrame
    result = pd.merge(orders, max_dates, left_on=['product_id', 'order_date'], 
                      right_on=['product_id', 'max_order_date'])
    
    # Drop the helper column 'max_order_date'
    result.drop(columns=['max_order_date'], inplace=True)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Input Data
    data = {
        'product_id': [1, 1, 2, 2, 3, 3],
        'order_date': ['2020-06-01', '2020-06-02', '2020-06-01', '2020-05-30', '2020-06-01', '2020-06-01'],
        'quantity': [10, 15, 5, 9, 20, 30]
    }
    orders_df = pd.DataFrame(data)
    
    # Expected Output
    """
    +------------+------------+----------+
    | product_id | order_date | quantity |
    +------------+------------+----------+
    | 1          | 2020-06-02 | 15       |
    | 2          | 2020-06-01 | 5        |
    | 3          | 2020-06-01 | 20       |
    | 3          | 2020-06-01 | 30       |
    +------------+------------+----------+
    """
    print(most_recent_orders(orders_df))

# Time and Space Complexity Analysis
"""
Time Complexity:
- Converting 'order_date' to datetime: O(n), where n is the number of rows in the DataFrame.
- Grouping by 'product_id' and finding max: O(n).
- Merging the DataFrames: O(n).
Overall: O(n).

Space Complexity:
- Storing the intermediate DataFrame for max_dates: O(k), where k is the number of unique product_ids.
- The final result DataFrame: O(n).
Overall: O(n + k).

Primary Topic: SQL Simulation / DataFrame Manipulation
"""