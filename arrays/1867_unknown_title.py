"""
LeetCode Problem #1867: Orders With Maximum Quantity

Problem Statement:
You are given a table `Orders` with the following columns:
- `order_id` (int): The unique ID of the order.
- `product_id` (int): The ID of the product in the order.
- `quantity` (int): The quantity of the product in the order.

Write an SQL query to find the `order_id` of the orders that have the maximum quantity. If there are multiple orders with the same maximum quantity, return all of them.

Return the result table in any order.

Example:
Input:
Orders table:
+----------+------------+----------+
| order_id | product_id | quantity |
+----------+------------+----------+
|    1     |     101    |    10    |
|    2     |     102    |    15    |
|    3     |     103    |    15    |
|    4     |     104    |    8     |
+----------+------------+----------+

Output:
+----------+
| order_id |
+----------+
|    2     |
|    3     |
+----------+

Explanation:
The maximum quantity is 15, and orders 2 and 3 have this quantity.
"""

# Python Solution
def orders_with_max_quantity(orders):
    """
    Function to find the order IDs with the maximum quantity.

    Args:
    orders (List[Dict]): A list of dictionaries representing the Orders table.
                         Each dictionary contains 'order_id', 'product_id', and 'quantity'.

    Returns:
    List[int]: A list of order IDs with the maximum quantity.
    """
    # Step 1: Find the maximum quantity
    max_quantity = max(order['quantity'] for order in orders)

    # Step 2: Filter orders with the maximum quantity
    result = [order['order_id'] for order in orders if order['quantity'] == max_quantity]

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    orders = [
        {"order_id": 1, "product_id": 101, "quantity": 10},
        {"order_id": 2, "product_id": 102, "quantity": 15},
        {"order_id": 3, "product_id": 103, "quantity": 15},
        {"order_id": 4, "product_id": 104, "quantity": 8},
    ]
    print(orders_with_max_quantity(orders))  # Output: [2, 3]

    # Test Case 2
    orders = [
        {"order_id": 1, "product_id": 101, "quantity": 5},
        {"order_id": 2, "product_id": 102, "quantity": 5},
        {"order_id": 3, "product_id": 103, "quantity": 5},
    ]
    print(orders_with_max_quantity(orders))  # Output: [1, 2, 3]

    # Test Case 3
    orders = [
        {"order_id": 1, "product_id": 101, "quantity": 20},
        {"order_id": 2, "product_id": 102, "quantity": 10},
        {"order_id": 3, "product_id": 103, "quantity": 15},
    ]
    print(orders_with_max_quantity(orders))  # Output: [1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Finding the maximum quantity: O(n), where n is the number of orders.
- Filtering orders with the maximum quantity: O(n).
- Overall: O(n).

Space Complexity:
- The space used for the result list is proportional to the number of orders with the maximum quantity: O(k), where k is the number of such orders.
- Overall: O(k).
"""

# Topic: Arrays