"""
LeetCode Problem #808: Soup Servings

Problem Statement:
There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:

1. Serve 100 ml of soup A and 0 ml of soup B.
2. Serve 75 ml of soup A and 25 ml of soup B.
3. Serve 50 ml of soup A and 50 ml of soup B.
4. Serve 25 ml of soup A and 75 ml of soup B.

When we serve some soup, we give it to someone, and we no longer have it. Each turn, we choose one of the four operations uniformly at random. This continues until we cannot perform any operation.

If the remaining volume of soup is not enough to complete the operation, we serve as much as possible. For example, if we have 10 ml of soup A and 50 ml of soup B, and we choose the third operation, we will serve 10 ml of soup A and 10 ml of soup B.

We say that soup A will be empty first if soup A becomes empty while soup B is not empty. Similarly, soup B will be empty first if soup B becomes empty while soup A is not empty. If both soups become empty at the same time, we consider that both soups are empty.

Return the probability that soup A will be empty first, plus half the probability that both soups become empty at the same time. Answers within 10^-5 of the actual answer will be accepted.

Constraints:
- 0 <= n <= 10^9
- n is a multiple of 25 (i.e., n % 25 == 0).

"""

from functools import lru_cache

def soupServings(n: int) -> float:
    # If n is very large, the probability converges to 1
    if n >= 4800:
        return 1.0

    # Scale down n to make the problem manageable
    n = (n + 24) // 25  # Scale down n to units of 25

    @lru_cache(None)
    def dfs(a, b):
        # Base cases
        if a <= 0 and b <= 0:
            return 0.5  # Both soups empty at the same time
        if a <= 0:
            return 1.0  # Soup A is empty first
        if b <= 0:
            return 0.0  # Soup B is empty first

        # Recursive case: average over all four operations
        return 0.25 * (dfs(a - 4, b) + dfs(a - 3, b - 1) + dfs(a - 2, b - 2) + dfs(a - 1, b - 3))

    return dfs(n, n)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 50
    print(f"Probability for n = {n1}: {soupServings(n1):.5f}")  # Expected: 0.62500

    # Test Case 2
    n2 = 100
    print(f"Probability for n = {n2}: {soupServings(n2):.5f}")  # Expected: 0.71875

    # Test Case 3
    n3 = 4800
    print(f"Probability for n = {n3}: {soupServings(n3):.5f}")  # Expected: 1.00000

    # Test Case 4
    n4 = 0
    print(f"Probability for n = {n4}: {soupServings(n4):.5f}")  # Expected: 0.50000

"""
Time Complexity:
- For small values of n (scaled down to n/25), the time complexity is O(n^2) due to memoization and the four recursive calls.
- For large values of n (n >= 4800), the solution is O(1) since we directly return 1.0.

Space Complexity:
- The space complexity is O(n^2) due to the memoization table storing results for each pair (a, b).

Topic: Dynamic Programming (DP)
"""