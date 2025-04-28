"""
LeetCode Problem #1843: Suspicious Bank Accounts

Problem Statement:
You are given a list of bank accounts represented as a 2D integer array `accounts` where `accounts[i]` is a list of integers representing the transactions of the i-th account. A transaction is considered suspicious if it is negative (indicating a withdrawal). An account is considered suspicious if it has at least one suspicious transaction.

Return the indices of all suspicious accounts in ascending order.

Example:
Input: accounts = [[1, 2, 3], [-1, 2, 3], [4, -5, 6], [7, 8, 9]]
Output: [1, 2]
Explanation:
- Account 0 has no suspicious transactions.
- Account 1 has a suspicious transaction (-1).
- Account 2 has a suspicious transaction (-5).
- Account 3 has no suspicious transactions.
Thus, the indices of suspicious accounts are [1, 2].

Constraints:
- 1 <= accounts.length <= 1000
- 1 <= accounts[i].length <= 1000
- -10^6 <= accounts[i][j] <= 10^6
"""

def find_suspicious_accounts(accounts):
    """
    Finds the indices of all suspicious accounts.

    Args:
    accounts (List[List[int]]): A 2D list where each sublist represents transactions of an account.

    Returns:
    List[int]: A list of indices of suspicious accounts in ascending order.
    """
    suspicious_indices = []
    for i, account in enumerate(accounts):
        if any(transaction < 0 for transaction in account):
            suspicious_indices.append(i)
    return suspicious_indices

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    accounts = [[1, 2, 3], [-1, 2, 3], [4, -5, 6], [7, 8, 9]]
    print(find_suspicious_accounts(accounts))  # Output: [1, 2]

    # Test Case 2
    accounts = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    print(find_suspicious_accounts(accounts))  # Output: []

    # Test Case 3
    accounts = [[-10, 20, 30], [40, -50, 60], [-70, 80, -90]]
    print(find_suspicious_accounts(accounts))  # Output: [0, 1, 2]

    # Test Case 4
    accounts = [[1], [-1], [0], [-1000000]]
    print(find_suspicious_accounts(accounts))  # Output: [1, 3]

    # Test Case 5
    accounts = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [-1, -2, -3, -4, -5]]
    print(find_suspicious_accounts(accounts))  # Output: [2]

"""
Time Complexity Analysis:
- Let `n` be the number of accounts and `m` be the average number of transactions per account.
- The outer loop iterates over `n` accounts.
- The inner loop (via `any`) iterates over `m` transactions for each account.
- Thus, the time complexity is O(n * m).

Space Complexity Analysis:
- The space complexity is O(1) for the algorithm itself, as we only use a list to store the indices of suspicious accounts.
- The output list of indices has a space complexity of O(k), where `k` is the number of suspicious accounts.

Topic: Arrays
"""