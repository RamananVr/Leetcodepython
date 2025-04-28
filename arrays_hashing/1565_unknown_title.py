"""
LeetCode Problem #1565: Unique Orders in a Restaurant

Problem Statement:
A restaurant receives a list of orders. Each order is represented as a list of items. 
The goal is to determine the number of unique orders in the restaurant. Two orders are 
considered unique if their items differ in any way (order of items does not matter).

Write a function `countUniqueOrders(orders: List[List[str]]) -> int` that takes a list of 
orders and returns the number of unique orders.

Constraints:
- 1 <= len(orders) <= 10^4
- 1 <= len(order[i]) <= 10
- 1 <= len(order[i][j]) <= 20
- All items in an order are unique.
- Items are strings consisting of lowercase English letters.

Example:
Input: orders = [["burger", "fries"], ["fries", "burger"], ["soda"], ["burger", "soda"]]
Output: 3
Explanation: There are 3 unique orders: ["burger", "fries"], ["soda"], and ["burger", "soda"].
"""

from typing import List

def countUniqueOrders(orders: List[List[str]]) -> int:
    """
    Function to count the number of unique orders in a restaurant.
    """
    # Use a set to store unique orders
    unique_orders = set()
    
    for order in orders:
        # Sort the items in the order to ensure uniqueness regardless of order
        sorted_order = tuple(sorted(order))
        unique_orders.add(sorted_order)
    
    # The size of the set represents the number of unique orders
    return len(unique_orders)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    orders1 = [["burger", "fries"], ["fries", "burger"], ["soda"], ["burger", "soda"]]
    print(countUniqueOrders(orders1))  # Output: 3

    # Test Case 2
    orders2 = [["pizza"], ["burger", "fries"], ["fries", "burger"], ["pizza"]]
    print(countUniqueOrders(orders2))  # Output: 2

    # Test Case 3
    orders3 = [["pasta", "salad"], ["salad", "pasta"], ["pasta"], ["salad"]]
    print(countUniqueOrders(orders3))  # Output: 3

    # Test Case 4
    orders4 = [["a", "b", "c"], ["c", "b", "a"], ["a", "c", "b"], ["b", "a", "c"]]
    print(countUniqueOrders(orders4))  # Output: 1

    # Test Case 5
    orders5 = [["apple"], ["banana"], ["apple", "banana"], ["banana", "apple"]]
    print(countUniqueOrders(orders5))  # Output: 3

"""
Time Complexity Analysis:
- Sorting each order takes O(k log k), where k is the average length of an order.
- Iterating through all orders takes O(n), where n is the number of orders.
- Adding a sorted tuple to the set takes O(1) on average.
- Overall time complexity: O(n * k log k), where n is the number of orders and k is the average length of an order.

Space Complexity Analysis:
- The set `unique_orders` stores up to n unique orders, each of size k.
- Space complexity: O(n * k), where n is the number of orders and k is the average length of an order.

Topic: Arrays, Hashing
"""