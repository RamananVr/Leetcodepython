"""
LeetCode Problem #2066: Account Balancing

Problem Statement:
You are given a list of transactions where transactions[i] = [from_i, to_i, amount_i] indicates that the person with ID from_i gave amount_i dollars to the person with ID to_i. Each person has a unique ID between 0 and n - 1, where n is the number of people.

Return the minimum number of transactions required to settle the debt.

Constraints:
1. 1 <= transactions.length <= 8
2. transactions[i].length == 3
3. 0 <= from_i, to_i < n
4. from_i != to_i
5. 1 <= amount_i <= 100

Example:
Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
Explanation:
Person #0 gave $10 to person #1.
Person #2 gave $5 to person #0.
Two transactions are needed. One way to settle the debt is:
- Person #1 pays $5 to person #0.
- Person #1 pays $5 to person #2.

Topic: Backtracking
"""

from typing import List

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        from collections import defaultdict

        # Step 1: Calculate net balance for each person
        balance = defaultdict(int)
        for frm, to, amount in transactions:
            balance[frm] -= amount
            balance[to] += amount

        # Step 2: Filter out people with zero balance
        debts = [amount for amount in balance.values() if amount != 0]

        # Helper function for backtracking
        def dfs(index):
            # Skip settled debts
            while index < len(debts) and debts[index] == 0:
                index += 1
            # If all debts are settled
            if index == len(debts):
                return 0

            min_transactions = float('inf')
            for i in range(index + 1, len(debts)):
                # If debts[index] and debts[i] can cancel each other
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
    print("Test Case 1 Output:", solution.minTransfers(transactions1))  # Expected Output: 2

    # Test Case 2
    transactions2 = [[0, 1, 10], [1, 2, 5], [2, 0, 5]]
    print("Test Case 2 Output:", solution.minTransfers(transactions2))  # Expected Output: 1

    # Test Case 3
    transactions3 = [[0, 1, 5], [1, 2, 5], [2, 0, 5]]
    print("Test Case 3 Output:", solution.minTransfers(transactions3))  # Expected Output: 2

    # Test Case 4
    transactions4 = [[0, 1, 5], [1, 2, 10], [2, 0, 5]]
    print("Test Case 4 Output:", solution.minTransfers(transactions4))  # Expected Output: 2


"""
Time Complexity:
- Let n be the number of people with non-zero balances (len(debts)).
- The backtracking algorithm explores all possible ways to settle debts, which is O(n!).
- However, due to pruning (skipping settled debts and avoiding redundant calculations), the actual runtime is much faster in practice.

Space Complexity:
- O(n) for the debts array and recursion stack.

Topic: Backtracking
"""