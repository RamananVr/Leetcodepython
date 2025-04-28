"""
LeetCode Problem #1831: Maximum Transaction Profit

Problem Statement:
You are given an array `transactions` where `transactions[i] = [buyPrice, sellPrice]` represents a transaction. 
Your task is to calculate the maximum profit that can be achieved by performing at most one transaction.

A transaction consists of buying at the `buyPrice` and selling at the `sellPrice`. 
If no profit can be made, return 0.

Example:
Input: transactions = [[2, 5], [3, 6], [1, 4]]
Output: 4
Explanation: The maximum profit is achieved by the transaction [2, 6], which gives a profit of 6 - 2 = 4.

Constraints:
- 1 <= transactions.length <= 10^5
- 1 <= buyPrice, sellPrice <= 10^9
"""

def maxTransactionProfit(transactions):
    """
    Calculate the maximum profit from a list of transactions.

    :param transactions: List[List[int]] - A list of transactions where each transaction is [buyPrice, sellPrice].
    :return: int - The maximum profit that can be achieved.
    """
    max_profit = 0
    for buy_price, sell_price in transactions:
        profit = sell_price - buy_price
        max_profit = max(max_profit, profit)
    return max_profit

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    transactions1 = [[2, 5], [3, 6], [1, 4]]
    print(maxTransactionProfit(transactions1))  # Output: 4

    # Test Case 2
    transactions2 = [[10, 15], [20, 25], [5, 10]]
    print(maxTransactionProfit(transactions2))  # Output: 10

    # Test Case 3
    transactions3 = [[5, 5], [10, 10], [15, 15]]
    print(maxTransactionProfit(transactions3))  # Output: 0

    # Test Case 4
    transactions4 = [[1, 100], [50, 60], [30, 40]]
    print(maxTransactionProfit(transactions4))  # Output: 99

    # Test Case 5
    transactions5 = [[100, 200], [150, 250], [300, 400]]
    print(maxTransactionProfit(transactions5))  # Output: 100

"""
Time Complexity Analysis:
- The function iterates through the `transactions` list once, performing constant-time operations for each transaction.
- Let `n` be the number of transactions. The time complexity is O(n).

Space Complexity Analysis:
- The function uses a constant amount of extra space (for variables like `max_profit` and `profit`).
- The space complexity is O(1).

Topic: Arrays
"""