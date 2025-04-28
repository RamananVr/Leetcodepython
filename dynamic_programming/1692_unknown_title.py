"""
LeetCode Problem #1692: Count Ways to Distribute Candies

Problem Statement:
Alice has `n` candies, and she wants to distribute them among `k` children. Each child must receive at least one candy. 
Alice wants to know the number of ways to distribute the candies such that every child gets at least one candy.

Return the number of ways to distribute the candies modulo 10^9 + 7.

Constraints:
- 1 <= n <= 1000
- 1 <= k <= 1000

Note:
If there are fewer candies than children (`n < k`), the answer is 0 because it's impossible to distribute candies such that every child gets at least one candy.

"""

# Solution
def countWaysToDistributeCandies(n: int, k: int) -> int:
    MOD = 10**9 + 7

    # If there are fewer candies than children, return 0
    if n < k:
        return 0

    # Initialize a DP table
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: 0 candies and 0 children

    # Fill the DP table
    for candies in range(1, n + 1):
        for children in range(1, k + 1):
            # Case 1: Give at least one candy to a new child
            dp[candies][children] = dp[candies - 1][children - 1]

            # Case 2: Add the candy to an existing child
            dp[candies][children] += dp[candies - 1][children] * children

            # Take modulo to prevent overflow
            dp[candies][children] %= MOD

    return dp[n][k]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic case
    n1, k1 = 7, 3
    print(countWaysToDistributeCandies(n1, k1))  # Expected output: 15

    # Test Case 2: Edge case where n < k
    n2, k2 = 3, 5
    print(countWaysToDistributeCandies(n2, k2))  # Expected output: 0

    # Test Case 3: Large input
    n3, k3 = 1000, 1000
    print(countWaysToDistributeCandies(n3, k3))  # Expected output: (large number modulo 10^9 + 7)

    # Test Case 4: Edge case where n == k
    n4, k4 = 5, 5
    print(countWaysToDistributeCandies(n4, k4))  # Expected output: 1

    # Test Case 5: Edge case where k == 1
    n5, k5 = 10, 1
    print(countWaysToDistributeCandies(n5, k5))  # Expected output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a dynamic programming approach with a table of size (n+1) x (k+1).
- Filling the table requires O(n * k) operations.
- Therefore, the time complexity is O(n * k).

Space Complexity:
- The DP table requires O(n * k) space.
- Therefore, the space complexity is O(n * k).

Topic: Dynamic Programming
"""