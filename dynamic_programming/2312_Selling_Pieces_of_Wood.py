"""
LeetCode Problem #2312: Selling Pieces of Wood

Problem Statement:
You are given two integers `m` and `n` which represent the dimensions of a rectangular piece of wood. 
You are also given a 2D array `prices` where `prices[i] = [hi, wi, pricei]` indicates you can sell a 
piece of wood of size `hi x wi` for `pricei` dollars. You can cut the wood into any number of rectangular 
pieces by performing horizontal or vertical cuts any number of times.

Return the maximum money you can earn after cutting the wood optimally.

Note:
- You can sell multiple pieces of the same size, and you can sell pieces even if they are not in the `prices` list.
- You must use the entire piece of wood.

Constraints:
- 1 <= m, n <= 200
- 1 <= prices.length <= 200
- 1 <= hi <= m
- 1 <= wi <= n
- 1 <= pricei <= 10^6
"""

# Solution
def sellingWood(m: int, n: int, prices: list[list[int]]) -> int:
    # Create a price lookup table for quick access
    price_map = {}
    for h, w, price in prices:
        price_map[(h, w)] = price

    # Initialize a DP table where dp[i][j] represents the maximum profit for a piece of size i x j
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Check if the current piece can be sold directly
            if (i, j) in price_map:
                dp[i][j] = price_map[(i, j)]

            # Try all possible horizontal cuts
            for cut in range(1, i):
                dp[i][j] = max(dp[i][j], dp[cut][j] + dp[i - cut][j])

            # Try all possible vertical cuts
            for cut in range(1, j):
                dp[i][j] = max(dp[i][j], dp[i][cut] + dp[i][j - cut])

    return dp[m][n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    m1, n1 = 3, 5
    prices1 = [[1, 2, 3], [2, 1, 2], [2, 2, 7], [3, 5, 10]]
    print(sellingWood(m1, n1, prices1))  # Expected Output: 10

    # Test Case 2
    m2, n2 = 4, 6
    prices2 = [[1, 1, 1], [2, 2, 5], [3, 3, 8], [4, 6, 20]]
    print(sellingWood(m2, n2, prices2))  # Expected Output: 20

    # Test Case 3
    m3, n3 = 2, 2
    prices3 = [[1, 1, 2], [2, 2, 5]]
    print(sellingWood(m3, n3, prices3))  # Expected Output: 5

# Time and Space Complexity Analysis
"""
Time Complexity:
- The DP table has dimensions m x n, so we iterate over all cells (O(m * n)).
- For each cell, we try all possible horizontal cuts (O(m)) and vertical cuts (O(n)).
- Thus, the overall time complexity is O(m * n * (m + n)).

Space Complexity:
- The DP table requires O(m * n) space.
- The price_map dictionary requires O(p) space, where p is the number of entries in the prices list.
- Overall space complexity is O(m * n + p).
"""

# Topic: Dynamic Programming