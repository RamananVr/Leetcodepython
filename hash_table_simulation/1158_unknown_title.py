"""
LeetCode Problem #1158: Market Analysis I

Problem Statement:
SQL problem: Write an SQL query to find the customer_number for the customer who has placed the largest number of orders. 
If there is a tie, return all customer_numbers. The result table should be sorted in ascending order by customer_number.

The Orders table is defined as follows:
+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key for this table.
This table contains information about the order ID and the customer ID of each order.

Example:
Input:
Orders table:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
+--------------+-----------------+

Output:
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+

Explanation:
The customer with customer_number 3 has two orders, which is greater than either customer 1 or 2 who each have only one order.
"""

# Note: Since this is an SQL problem, we cannot directly write a Python solution for it. 
# However, we can simulate the logic in Python for educational purposes.

# Python Simulation of the SQL Problem
from collections import Counter

def find_top_customers(orders):
    """
    Simulates the SQL query to find the customer(s) with the most orders.

    :param orders: List of tuples where each tuple represents an order (order_number, customer_number)
    :return: List of customer_numbers with the most orders, sorted in ascending order
    """
    # Count the number of orders for each customer
    customer_order_count = Counter(customer_number for _, customer_number in orders)
    
    # Find the maximum number of orders
    max_orders = max(customer_order_count.values(), default=0)
    
    # Find all customers with the maximum number of orders
    top_customers = [customer for customer, count in customer_order_count.items() if count == max_orders]
    
    # Return the result sorted in ascending order
    return sorted(top_customers)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    orders = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 3)
    ]
    print(find_top_customers(orders))  # Output: [3]

    # Test Case 2
    orders = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 3),
        (5, 2),
        (6, 2)
    ]
    print(find_top_customers(orders))  # Output: [2]

    # Test Case 3
    orders = [
        (1, 1),
        (2, 2),
        (3, 3)
    ]
    print(find_top_customers(orders))  # Output: [1, 2, 3]

    # Test Case 4
    orders = []
    print(find_top_customers(orders))  # Output: []

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting the orders for each customer takes O(n), where n is the number of orders.
- Finding the maximum number of orders takes O(k), where k is the number of unique customers.
- Sorting the top customers takes O(k log k).
Overall: O(n + k log k)

Space Complexity:
- The Counter object stores up to k unique customers, so the space complexity is O(k).
"""

# Topic: Hash Table / Simulation