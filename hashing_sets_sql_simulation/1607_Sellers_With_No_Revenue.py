"""
LeetCode Problem #1607: Sellers With No Revenue

Problem Statement:
You are given two tables, `Products` and `Orders`.

Table: Products
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| seller_id   | int     |
+-------------+---------+
product_id is the primary key for this table.
Each row in this table contains the ID of a product and the ID of the seller who sells this product.

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| product_id  | int  |
+-------------+------+
order_id is the primary key for this table.
product_id is a foreign key to the Products table.
Each row in this table contains the ID of an order and the ID of the product ordered.

Write an SQL query to report the IDs of all sellers who did not make any revenue. In other words, report the seller_id of the sellers who have no orders for their products.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Products table:
+------------+-----------+
| product_id | seller_id |
+------------+-----------+
| 1          | 1         |
| 2          | 2         |
| 3          | 3         |
| 4          | 4         |
+------------+-----------+

Orders table:
+------------+------------+
| order_id   | product_id |
+------------+------------+
| 1          | 1          |
| 2          | 2          |
+------------+------------+

Output:
+-----------+
| seller_id |
+-----------+
| 3         |
| 4         |
+-----------+
"""

# Python Solution
def sellers_with_no_revenue(products, orders):
    """
    Function to find seller IDs with no revenue.

    Args:
    products: List of tuples representing the Products table. Each tuple contains (product_id, seller_id).
    orders: List of tuples representing the Orders table. Each tuple contains (order_id, product_id).

    Returns:
    List of seller IDs with no revenue.
    """
    # Create a set of product IDs that have orders
    ordered_product_ids = {order[1] for order in orders}

    # Find seller IDs whose products are not in the ordered_product_ids set
    seller_ids_with_no_revenue = {product[1] for product in products if product[0] not in ordered_product_ids}

    # Return the result as a sorted list (optional for consistent output)
    return sorted(seller_ids_with_no_revenue)

# Example Test Cases
if __name__ == "__main__":
    # Input tables
    products = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
    ]
    orders = [
        (1, 1),
        (2, 2)
    ]

    # Expected Output: [3, 4]
    print(sellers_with_no_revenue(products, orders))

    # Additional Test Case
    products = [
        (1, 1),
        (2, 2),
        (3, 3)
    ]
    orders = [
        (1, 1)
    ]

    # Expected Output: [2, 3]
    print(sellers_with_no_revenue(products, orders))

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the set of ordered product IDs: O(m), where m is the number of orders.
- Iterating through the products table to find sellers with no revenue: O(n), where n is the number of products.
- Overall time complexity: O(n + m).

Space Complexity:
- Space used for the set of ordered product IDs: O(m).
- Space used for the set of seller IDs with no revenue: O(n).
- Overall space complexity: O(n + m).
"""

# Topic: Hashing, Sets, SQL Simulation