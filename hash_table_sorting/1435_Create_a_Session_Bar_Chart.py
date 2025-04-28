"""
LeetCode Problem #1435: Create a Session Bar Chart

Problem Statement:
You are given two tables: `Orders` and `Products`.

- The `Orders` table contains the following columns:
  - `order_id` (int): The ID of the order.
  - `product_id` (int): The ID of the product in the order.
  - `quantity` (int): The quantity of the product in the order.

- The `Products` table contains the following columns:
  - `product_id` (int): The ID of the product.
  - `product_name` (string): The name of the product.
  - `price` (float): The price of the product.

Write a SQL query to calculate the total revenue for each product. The revenue for a product is defined as the sum of the product of `quantity` and `price` for all orders of that product.

The query should return the following columns:
- `product_name` (string): The name of the product.
- `total_revenue` (float): The total revenue for the product.

The result should be sorted by `total_revenue` in descending order. If two products have the same revenue, sort them by `product_name` in ascending order.

Example Input:
Orders table:
+-----------+------------+----------+
| order_id  | product_id | quantity |
+-----------+------------+----------+
| 1         | 1          | 2        |
| 2         | 1          | 1        |
| 3         | 2          | 2        |
| 4         | 3          | 3        |
+-----------+------------+----------+

Products table:
+------------+--------------+-------+
| product_id | product_name | price |
+------------+--------------+-------+
| 1          | A            | 10    |
| 2          | B            | 20    |
| 3          | C            | 30    |
+------------+--------------+-------+

Example Output:
+--------------+---------------+
| product_name | total_revenue |
+--------------+---------------+
| C            | 90            |
| B            | 40            |
| A            | 30            |
+--------------+---------------+

Explanation:
- Product A: (2 * 10) + (1 * 10) = 30
- Product B: (2 * 20) = 40
- Product C: (3 * 30) = 90
"""

# Python Solution
def calculate_total_revenue(orders, products):
    """
    Calculate the total revenue for each product.

    Args:
    orders (list of dict): A list of orders, where each order is represented as a dictionary with keys:
        - 'order_id' (int): The ID of the order.
        - 'product_id' (int): The ID of the product in the order.
        - 'quantity' (int): The quantity of the product in the order.
    products (list of dict): A list of products, where each product is represented as a dictionary with keys:
        - 'product_id' (int): The ID of the product.
        - 'product_name' (str): The name of the product.
        - 'price' (float): The price of the product.

    Returns:
    list of dict: A list of dictionaries, where each dictionary contains:
        - 'product_name' (str): The name of the product.
        - 'total_revenue' (float): The total revenue for the product.
    """
    from collections import defaultdict

    # Step 1: Create a mapping of product_id to product_name and price
    product_info = {product['product_id']: (product['product_name'], product['price']) for product in products}

    # Step 2: Calculate total revenue for each product
    revenue = defaultdict(float)
    for order in orders:
        product_id = order['product_id']
        quantity = order['quantity']
        if product_id in product_info:
            product_name, price = product_info[product_id]
            revenue[product_name] += quantity * price

    # Step 3: Convert the revenue dictionary to a sorted list
    result = [{'product_name': name, 'total_revenue': total_revenue} for name, total_revenue in revenue.items()]
    result.sort(key=lambda x: (-x['total_revenue'], x['product_name']))

    return result

# Example Test Cases
if __name__ == "__main__":
    orders = [
        {"order_id": 1, "product_id": 1, "quantity": 2},
        {"order_id": 2, "product_id": 1, "quantity": 1},
        {"order_id": 3, "product_id": 2, "quantity": 2},
        {"order_id": 4, "product_id": 3, "quantity": 3},
    ]

    products = [
        {"product_id": 1, "product_name": "A", "price": 10},
        {"product_id": 2, "product_name": "B", "price": 20},
        {"product_id": 3, "product_name": "C", "price": 30},
    ]

    # Expected Output:
    # [{'product_name': 'C', 'total_revenue': 90},
    #  {'product_name': 'B', 'total_revenue': 40},
    #  {'product_name': 'A', 'total_revenue': 30}]
    print(calculate_total_revenue(orders, products))

# Time Complexity Analysis:
# - Creating the product_info dictionary: O(P), where P is the number of products.
# - Iterating through the orders to calculate revenue: O(O), where O is the number of orders.
# - Sorting the result: O(N log N), where N is the number of unique products.
# Overall Time Complexity: O(P + O + N log N)

# Space Complexity Analysis:
# - Space for the product_info dictionary: O(P).
# - Space for the revenue dictionary: O(N), where N is the number of unique products.
# Overall Space Complexity: O(P + N)

# Topic: Hash Table, Sorting