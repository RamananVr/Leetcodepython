"""
LeetCode Question #2412: Minimum Money Required Before Transactions

Problem Statement:
You are given a 2D integer array `transactions` where transactions[i] = [cost_i, cashback_i].

- The `cost_i` represents the amount of money required to complete the i-th transaction.
- The `cashback_i` represents the amount of money you receive back after completing the i-th transaction.

Before performing any transaction, you need to have some initial amount of money. In other words, you need at least `cost_i` money to complete the i-th transaction.

After performing a transaction, your total money becomes:
    total_money = total_money - cost_i + cashback_i

Return the minimum amount of money you need before any transaction so that you can complete all the transactions in any order.

Constraints:
- 1 <= transactions.length <= 10^5
- 0 <= cost_i, cashback_i <= 10^9
"""

# Python Solution
def minimumMoney(transactions):
    """
    Calculate the minimum amount of money required before transactions.

    :param transactions: List[List[int]] - A list of transactions where each transaction is [cost, cashback].
    :return: int - The minimum amount of money required before any transaction.
    """
    max_loss = 0
    total_loss = 0

    for cost, cashback in transactions:
        # Calculate the loss for this transaction
        loss = max(0, cost - cashback)
        total_loss += loss
        # Track the maximum cost required for any transaction
        max_loss = max(max_loss, min(cost, cashback))

    return total_loss + max_loss


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    transactions1 = [[2, 1], [5, 0], [4, 2]]
    print(minimumMoney(transactions1))  # Expected Output: 10

    # Test Case 2
    transactions2 = [[3, 2], [4, 3], [5, 1]]
    print(minimumMoney(transactions2))  # Expected Output: 9

    # Test Case 3
    transactions3 = [[10, 5], [7, 3], [8, 6]]
    print(minimumMoney(transactions3))  # Expected Output: 18

    # Test Case 4
    transactions4 = [[1, 0], [2, 1], [3, 2]]
    print(minimumMoney(transactions4))  # Expected Output: 6

    # Test Case 5
    transactions5 = [[0, 0], [0, 0], [0, 0]]
    print(minimumMoney(transactions5))  # Expected Output: 0


"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution iterates through the `transactions` list once, performing constant-time operations for each transaction.
- Let n = len(transactions). The time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of extra space for variables like `max_loss` and `total_loss`.
- The space complexity is O(1).

Topic: Greedy
"""