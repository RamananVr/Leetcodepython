"""
LeetCode Problem #1164: Product Price at a Given Date

Problem Statement:
Table: Products
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| product_id       | int     |
| new_price        | int     |
| change_date      | date    |
+------------------+---------+
(product_id, change_date) is the primary key for this table.
Each row of this table indicates that the price of some product was changed to a new price at change_date.

Write an SQL query to find the price of each product for each day between the minimum and maximum change_date in the database. 
Assume that the price of all products is the same as the latest price before the date. If there is no price change before a date, 
the price is considered to be 0.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Products table:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2020-02-17  |
| 1          | 30        | 2020-02-18  |
| 2          | 10        | 2020-02-18  |
| 2          | 25        | 2020-02-19  |
+------------+-----------+-------------+

Output:
+------------+------------+------------+
| product_id | sell_date  | price      |
+------------+------------+------------+
| 1          | 2020-02-17 | 20         |
| 1          | 2020-02-18 | 30         |
| 1          | 2020-02-19 | 30         |
| 2          | 2020-02-17 | 0          |
| 2          | 2020-02-18 | 10         |
| 2          | 2020-02-19 | 25         |
+------------+------------+------------+
"""

# Python Solution:
# Since this is an SQL problem, we will simulate the solution using Python for demonstration purposes.

from datetime import datetime, timedelta
from collections import defaultdict

def product_price_at_given_date(products):
    """
    Simulates the SQL query to find the price of each product for each day between the minimum and maximum change_date.
    
    :param products: List of tuples representing the Products table. Each tuple is (product_id, new_price, change_date).
    :return: List of tuples representing the result table. Each tuple is (product_id, sell_date, price).
    """
    # Parse the input and sort by product_id and change_date
    products.sort(key=lambda x: (x[0], x[2]))
    
    # Find the minimum and maximum dates
    min_date = min(products, key=lambda x: x[2])[2]
    max_date = max(products, key=lambda x: x[2])[2]
    
    # Generate all dates between min_date and max_date
    all_dates = [min_date + timedelta(days=i) for i in range((max_date - min_date).days + 1)]
    
    # Dictionary to store the price history for each product
    price_history = defaultdict(list)
    
    for product_id, new_price, change_date in products:
        price_history[product_id].append((change_date, new_price))
    
    # Result list
    result = []
    
    # Iterate over each product and calculate the price for each date
    for product_id in price_history:
        price_changes = price_history[product_id]
        current_price = 0
        change_index = 0
        
        for date in all_dates:
            # Update the price if there is a change on this date
            while change_index < len(price_changes) and price_changes[change_index][0] <= date:
                current_price = price_changes[change_index][1]
                change_index += 1
            
            # Append the result for this product and date
            result.append((product_id, date, current_price))
    
    # Handle products with no price changes
    all_product_ids = set(product_id for product_id, _, _ in products)
    for product_id in all_product_ids:
        if product_id not in price_history:
            for date in all_dates:
                result.append((product_id, date, 0))
    
    # Sort the result by product_id and sell_date
    result.sort(key=lambda x: (x[0], x[1]))
    
    return result

# Example Test Cases
if __name__ == "__main__":
    products = [
        (1, 20, datetime(2020, 2, 17)),
        (1, 30, datetime(2020, 2, 18)),
        (2, 10, datetime(2020, 2, 18)),
        (2, 25, datetime(2020, 2, 19))
    ]
    
    result = product_price_at_given_date(products)
    for row in result:
        print(row)

"""
Expected Output:
(1, datetime(2020, 2, 17), 20)
(1, datetime(2020, 2, 18), 30)
(1, datetime(2020, 2, 19), 30)
(2, datetime(2020, 2, 17), 0)
(2, datetime(2020, 2, 18), 10)
(2, datetime(2020, 2, 19), 25)
"""

# Time Complexity Analysis:
# Sorting the products list: O(n log n), where n is the number of rows in the products table.
# Generating all dates between min_date and max_date: O(d), where d is the number of days in the range.
# Iterating over products and dates: O(p * d), where p is the number of unique products.
# Overall: O(n log n + p * d)

# Space Complexity Analysis:
# Storing price history: O(p * c), where c is the average number of price changes per product.
# Storing the result: O(p * d).
# Overall: O(p * (c + d))

# Topic: Simulation, Date Manipulation