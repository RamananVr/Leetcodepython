"""
LeetCode Question #586: Customer Placing the Largest Number of Orders

Problem Statement:
Table: Orders

+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_id        | int      |
| customer_id     | int      |
+-----------------+----------+
order_id is the primary key for this table.
This table contains information about the ID of a customer and the ID of the order.

Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.
The test cases are generated so that exactly one customer will have placed more orders than any other customer.

The query result format is in the following example:

Orders table:
+------------+-------------+
| order_id   | customer_id |
+------------+-------------+
| 1          | 1           |
| 2          | 2           |
| 3          | 3           |
| 4          | 3           |
| 5          | 3           |
+------------+-------------+

Result table:
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+
The customer with ID 3 has placed three orders, which is more than any other customer.
"""

# Python Solution:
# Since this is an SQL problem, we will simulate the solution using Python for demonstration purposes.

from collections import Counter

def customer_with_largest_orders(orders):
    """
    Function to find the customer who placed the largest number of orders.

    :param orders: List of tuples where each tuple represents (order_id, customer_id)
    :return: The customer_id of the customer with the largest number of orders
    """
    # Count the number of orders for each customer
    customer_order_count = Counter(customer_id for _, customer_id in orders)
    
    # Find the customer with the maximum number of orders
    max_customer = max(customer_order_count, key=customer_order_count.get)
    
    return max_customer

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    orders = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 3),
        (5, 3)
    ]
    print(customer_with_largest_orders(orders))  # Output: 3

    # Test Case 2
    orders = [
        (1, 10),
        (2, 20),
        (3, 20),
        (4, 30),
        (5, 30),
        (6, 30)
    ]
    print(customer_with_largest_orders(orders))  # Output: 30

    # Test Case 3
    orders = [
        (1, 5),
        (2, 5),
        (3, 5),
        (4, 6),
        (5, 6)
    ]
    print(customer_with_largest_orders(orders))  # Output: 5

# Time and Space Complexity Analysis:
# Time Complexity:
# - Counting the orders for each customer takes O(n), where n is the number of orders.
# - Finding the maximum customer takes O(k), where k is the number of unique customers.
# - Overall time complexity: O(n).

# Space Complexity:
# - The Counter object stores the count of orders for each unique customer, which takes O(k) space.
# - Overall space complexity: O(k), where k is the number of unique customers.

# Topic: Hash Table / SQL Simulation