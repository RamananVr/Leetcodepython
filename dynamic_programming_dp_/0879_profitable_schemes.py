"""
LeetCode Question #879: Profitable Schemes

Problem Statement:
There is a group of `n` members, and a list of various crimes they could commit. The `i-th` crime generates a profit of `profit[i]` and requires `group[i]` members to participate in it. If a member participates in one crime, they can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least `minProfit` profit, and the total number of members participating in that subset does not exceed `n`.

Return the number of profitable schemes. Since the answer may be very large, return it modulo `10^9 + 7`.

Example 1:
Input: n = 5, minProfit = 3, group = [2, 2], profit = [2, 3]
Output: 2
Explanation: To make a profit of at least 3, there are 2 schemes:
1. Commit the 1st crime. (Profit = 2, Members = 2)
2. Commit the 2nd crime. (Profit = 3, Members = 2)

Example 2:
Input: n = 10, minProfit = 5, group = [2, 3, 5], profit = [6, 7, 8]
Output: 7
Explanation: To make a profit of at least 5, there are 7 schemes:
1. Commit the 1st crime. (Profit = 6, Members = 2)
2. Commit the 2nd crime. (Profit = 7, Members = 3)
3. Commit the 3rd crime. (Profit = 8, Members = 5)
4. Commit crimes 1 and 2. (Profit = 13, Members = 5)
5. Commit crimes 1 and 3. (Profit = 14, Members = 7)
6. Commit crimes 2 and 3. (Profit = 15, Members = 8)
7. Commit crimes 1, 2, and 3. (Profit = 21, Members = 10)

Constraints:
- 1 <= n <= 100
- 0 <= minProfit <= 100
- 1 <= group.length <= 100
- 1 <= group[i] <= 100
- 0 <= profit[i] <= 100
"""

# Clean, Correct Python Solution
def profitableSchemes(n, minProfit, group, profit):
    MOD = 10**9 + 7
    # dp[m][p] represents the number of ways to achieve at least p profit with m members
    dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: 1 way to achieve 0 profit with 0 members

    for g, p in zip(group, profit):
        # Traverse dp array in reverse to avoid overwriting
        for members in range(n, g - 1, -1):
            for curr_profit in range(minProfit, -1, -1):
                dp[members][curr_profit] += dp[members - g][max(0, curr_profit - p)]
                dp[members][curr_profit] %= MOD

    # Sum up all ways to achieve at least minProfit with any number of members
    return sum(dp[m][minProfit] for m in range(n + 1)) % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, minProfit1, group1, profit1 = 5, 3, [2, 2], [2, 3]
    print(profitableSchemes(n1, minProfit1, group1, profit1))  # Output: 2

    # Test Case 2
    n2, minProfit2, group2, profit2 = 10, 5, [2, 3, 5], [6, 7, 8]
    print(profitableSchemes(n2, minProfit2, group2, profit2))  # Output: 7

    # Test Case 3
    n3, minProfit3, group3, profit3 = 1, 1, [1, 1, 1], [1, 2, 3]
    print(profitableSchemes(n3, minProfit3, group3, profit3))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let G = len(group) (number of crimes) and N = n (number of members).
- The outer loop iterates over all crimes (O(G)).
- The inner loops iterate over members (O(N)) and profit (O(minProfit)).
- Total complexity: O(G * N * minProfit).

Space Complexity:
- The dp array has dimensions (N+1) x (minProfit+1), so the space complexity is O(N * minProfit).
"""

# Topic: Dynamic Programming (DP)