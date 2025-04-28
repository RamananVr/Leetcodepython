"""
LeetCode Question #1159: Market Analysis I

Problem Statement:
You are given a list of transactions, where each transaction is represented as a tuple (customer_id, amount, timestamp).
Your task is to analyze the transactions and return the total amount spent by each customer in ascending order of customer_id.

Write a function `market_analysis(transactions: List[Tuple[int, int, int]]) -> List[Tuple[int, int]]` that takes a list of transactions and returns a list of tuples, where each tuple contains a customer_id and the total amount spent by that customer.

Example:
Input: transactions = [(1, 100, 1), (2, 200, 2), (1, 50, 3), (3, 300, 4)]
Output: [(1, 150), (2, 200), (3, 300)]

Constraints:
- The list of transactions will have at most 10^5 elements.
- Each transaction tuple contains:
  - customer_id: an integer (1 <= customer_id <= 10^5)
  - amount: an integer (1 <= amount <= 10^5)
  - timestamp: an integer (1 <= timestamp <= 10^9)
- The customer_id values in the output must be sorted in ascending order.
"""

from typing import List, Tuple
from collections import defaultdict

def market_analysis(transactions: List[Tuple[int, int, int]]) -> List[Tuple[int, int]]:
    """
    Analyze transactions and return the total amount spent by each customer in ascending order of customer_id.

    :param transactions: List of tuples (customer_id, amount, timestamp)
    :return: List of tuples (customer_id, total_amount)
    """
    # Use a dictionary to store the total amount spent by each customer
    customer_totals = defaultdict(int)
    
    # Iterate through transactions and accumulate amounts
    for customer_id, amount, _ in transactions:
        customer_totals[customer_id] += amount
    
    # Convert the dictionary to a sorted list of tuples
    result = sorted(customer_totals.items())
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    transactions = [(1, 100, 1), (2, 200, 2), (1, 50, 3), (3, 300, 4)]
    print(market_analysis(transactions))  # Expected Output: [(1, 150), (2, 200), (3, 300)]

    # Test Case 2
    transactions = [(5, 500, 10), (3, 300, 20), (5, 200, 30), (3, 100, 40)]
    print(market_analysis(transactions))  # Expected Output: [(3, 400), (5, 700)]

    # Test Case 3
    transactions = [(1, 100, 1), (1, 200, 2), (1, 300, 3)]
    print(market_analysis(transactions))  # Expected Output: [(1, 600)]

    # Test Case 4
    transactions = []
    print(market_analysis(transactions))  # Expected Output: []

    # Test Case 5
    transactions = [(10, 1000, 100), (20, 2000, 200), (10, 500, 300)]
    print(market_analysis(transactions))  # Expected Output: [(10, 1500), (20, 2000)]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Iterating through the transactions list takes O(n), where n is the number of transactions.
- Sorting the dictionary keys takes O(k log k), where k is the number of unique customer_ids.
- Overall time complexity: O(n + k log k).

Space Complexity:
- The dictionary `customer_totals` stores up to k unique customer_ids, where k <= n.
- The result list stores k tuples.
- Overall space complexity: O(k).

Topic: Hash Table
"""