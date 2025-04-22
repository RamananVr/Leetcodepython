"""
LeetCode Problem #465: Optimal Account Balancing

Problem Statement:
A group of friends went on a vacation and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later, Bill paid for Charlie's coffee for $20. We can model each transaction as a tuple (x, y, z) which means that person x gave person y an amount of money z.

Given a list of transactions, return the minimum number of transactions required to settle the debt.

Note:
1. A transaction is defined as a tuple (x, y, z) where x, y are people and z is the amount of money.
2. You may assume that the input is valid and all amounts are positive.
3. You cannot split a single transaction. Each transaction must be used in its entirety.

Example:
Input:
transactions = [[0,1,10], [2,0,5]]

Output:
1

Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Thus, person #1 owes person #0 $10 - $5 = $5.
Person #2 owes person #0 $5.
Therefore, the minimum number of transactions required to settle the debt is 1.
"""

from typing import List

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        from collections import defaultdict

        # Step 1: Calculate net balance for each person
        balance = defaultdict(int)
        for giver, receiver, amount in transactions:
            balance[giver] -= amount
            balance[receiver] += amount

        # Step 2: Filter out people with zero balance
        debts = [amount for amount in balance.values() if amount != 0]

        # Helper function to recursively settle debts
        def dfs(index: int) -> int:
            # Skip settled debts
            while index < len(debts) and debts[index] == 0:
                index += 1
            # If all debts are settled
            if index == len(debts):
                return 0

            min_transactions = float('inf')
            for i in range(index + 1, len(debts)):
                # Only try to settle debts with opposite signs
                if debts[index] * debts[i] < 0:
                    # Settle debts[index] with debts[i]
                    debts[i] += debts[index]
                    min_transactions = min(min_transactions, 1 + dfs(index + 1))
                    # Backtrack
                    debts[i] -= debts[index]

            return min_transactions

        return dfs(0)

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    transactions1 = [[0, 1, 10], [2, 0, 5]]
    print("Test Case 1 Output:", solution.minTransfers(transactions1))  # Expected Output: 1

    # Test Case 2
    transactions2 = [[0, 1, 10], [1, 2, 5], [2, 0, 5]]
    print("Test Case 2 Output:", solution.minTransfers(transactions2))  # Expected Output: 1

    # Test Case 3
    transactions3 = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 0, 10]]
    print("Test Case 3 Output:", solution.minTransfers(transactions3))  # Expected Output: 3

"""
Time Complexity Analysis:
- Calculating the net balance for each person takes O(T), where T is the number of transactions.
- The DFS function explores all possible ways to settle debts. In the worst case, there are 2^(N-1) subsets of debts to consider, where N is the number of people with non-zero balances. Thus, the time complexity is O(2^N).
- Overall time complexity: O(T + 2^N).

Space Complexity Analysis:
- The space complexity is O(N) for storing the debts array and the recursion stack.
- Overall space complexity: O(N).

Topic: Dynamic Programming (DP), Backtracking
"""