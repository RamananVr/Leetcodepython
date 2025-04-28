"""
LeetCode Problem #2218: Maximum Value of K Coins From Piles

Problem Statement:
You have n piles of coins. Each pile has a positive integer number of coins in it. In each step, you can pick any number of coins from any one pile until you have picked exactly k coins.

Given a list `piles`, where `piles[i]` is a list of integers denoting the coins in the ith pile, and an integer `k`, return the maximum value of coins you can collect.

Example:
Input: piles = [[1,100,3],[7,8,9]], k = 2
Output: 101
Explanation:
- Take 1 coin from the first pile, and 1 coin from the second pile.

Constraints:
- `n == piles.length`
- `1 <= n <= 1000`
- `1 <= piles[i].length <= 2000`
- `1 <= piles[i][j] <= 10^5`
- `1 <= k <= sum(piles[i].length for i in range(n))`
"""

# Solution
from functools import lru_cache

def maxValueOfCoins(piles, k):
    """
    Function to calculate the maximum value of k coins from piles.

    :param piles: List[List[int]] - List of piles where each pile is a list of integers representing coin values.
    :param k: int - Number of coins to pick.
    :return: int - Maximum value of coins that can be collected.
    """
    # Precompute prefix sums for each pile
    prefix_sums = []
    for pile in piles:
        prefix = [0]
        for coin in pile:
            prefix.append(prefix[-1] + coin)
        prefix_sums.append(prefix)

    @lru_cache(None)
    def dp(i, remaining_k):
        # Base case: No piles left or no coins to pick
        if i == len(piles) or remaining_k == 0:
            return 0

        # Option 1: Skip the current pile
        max_value = dp(i + 1, remaining_k)

        # Option 2: Take coins from the current pile
        for coins_taken in range(1, min(len(prefix_sums[i]), remaining_k + 1)):
            max_value = max(max_value, prefix_sums[i][coins_taken] + dp(i + 1, remaining_k - coins_taken))

        return max_value

    return dp(0, k)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    piles = [[1, 100, 3], [7, 8, 9]]
    k = 2
    print(maxValueOfCoins(piles, k))  # Output: 101

    # Test Case 2
    piles = [[100], [200], [300]]
    k = 2
    print(maxValueOfCoins(piles, k))  # Output: 500

    # Test Case 3
    piles = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 4
    print(maxValueOfCoins(piles, k))  # Output: 26

    # Test Case 4
    piles = [[1], [2], [3], [4], [5]]
    k = 3
    print(maxValueOfCoins(piles, k))  # Output: 12

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n be the number of piles and m be the average number of coins per pile.
- Precomputing prefix sums takes O(n * m).
- The DP function has n states and k subproblems, and for each subproblem, we iterate over up to m coins.
- Thus, the overall time complexity is O(n * k * m).

Space Complexity:
- The space complexity is O(n * k) for the memoization table and O(n * m) for the prefix sums.
- Total space complexity is O(n * k + n * m).
"""

# Topic: Dynamic Programming