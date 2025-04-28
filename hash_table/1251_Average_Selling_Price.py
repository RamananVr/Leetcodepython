"""
LeetCode Problem #1251: Average Selling Price

Problem Statement:
Given two tables, `Products` and `Sales`, write an SQL query to find the average selling price of each product. 
The `Products` table contains the product ID and name, while the `Sales` table contains the product ID, quantity sold, and price per unit.

The result should include the product name and the average selling price, rounded to two decimal places. 
If a product has no sales, its average selling price should be shown as 0.00.

Tables:
1. Products:
   +-------------+---------+
   | product_id  | name    |
   +-------------+---------+
   | 1           | TV      |
   | 2           | Radio   |
   | 3           | Phone   |
   +-------------+---------+

2. Sales:
   +-------------+----------+-------+
   | product_id  | quantity | price |
   +-------------+----------+-------+
   | 1           | 10       | 100   |
   | 2           | 5        | 200   |
   | 1           | 5        | 150   |
   +-------------+----------+-------+

Expected Output:
   +---------+-------------------+
   | name    | average_price     |
   +---------+-------------------+
   | TV      | 125.00            |
   | Radio   | 200.00            |
   | Phone   | 0.00              |
   +---------+-------------------+

Constraints:
- The `Products` table contains unique product IDs.
- The `Sales` table may contain multiple entries for the same product ID.
- The average selling price is calculated as the total revenue (quantity * price) divided by the total quantity sold for each product.

Note: This is an SQL problem, but for the purpose of this task, we will simulate the solution in Python.
"""

# Python Solution
from collections import defaultdict

def average_selling_price(products, sales):
    """
    Calculate the average selling price for each product.

    :param products: List of tuples representing the Products table [(product_id, name), ...]
    :param sales: List of tuples representing the Sales table [(product_id, quantity, price), ...]
    :return: List of tuples [(name, average_price), ...]
    """
    # Create a dictionary to store total revenue and total quantity for each product
    revenue_and_quantity = defaultdict(lambda: [0, 0])  # {product_id: [total_revenue, total_quantity]}

    # Process the sales data
    for product_id, quantity, price in sales:
        revenue_and_quantity[product_id][0] += quantity * price  # Add to total revenue
        revenue_and_quantity[product_id][1] += quantity         # Add to total quantity

    # Prepare the result
    result = []
    for product_id, name in products:
        total_revenue, total_quantity = revenue_and_quantity[product_id]
        average_price = total_revenue / total_quantity if total_quantity > 0 else 0.0
        result.append((name, round(average_price, 2)))

    return result

# Example Test Cases
if __name__ == "__main__":
    # Input data
    products = [
        (1, "TV"),
        (2, "Radio"),
        (3, "Phone")
    ]
    sales = [
        (1, 10, 100),
        (2, 5, 200),
        (1, 5, 150)
    ]

    # Expected Output: [("TV", 125.00), ("Radio", 200.00), ("Phone", 0.00)]
    print(average_selling_price(products, sales))

"""
Time Complexity:
- Let `n` be the number of products and `m` be the number of sales.
- Processing the sales data takes O(m) time.
- Preparing the result takes O(n) time.
- Overall time complexity: O(n + m).

Space Complexity:
- The `revenue_and_quantity` dictionary stores data for each product, which takes O(n) space.
- The result list takes O(n) space.
- Overall space complexity: O(n).

Topic: Hash Table
"""