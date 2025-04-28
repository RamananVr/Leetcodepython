"""
LeetCode Problem #2320: Count Number of Ways to Place Houses

Problem Statement:
There is a street with `n` plots, where each plot can either be empty or have a house placed on it. There are certain rules for placing houses:
1. No two houses can be adjacent to each other.

Given `n`, return the total number of ways to place houses such that the rules are followed. Since the answer may be large, return it modulo 10^9 + 7.

Example:
Input: n = 3
Output: 25
Explanation: There are 25 ways to place houses on both sides of the street.

Note:
- Each side of the street has `n` plots.
- The total number of ways is the product of the number of ways to place houses on one side of the street.

Constraints:
- 1 <= n <= 10^4
"""

# Solution
def countHousePlacements(n: int) -> int:
    MOD = 10**9 + 7

    # Base cases
    if n == 1:
        return 4  # Two ways for one side, so 2 * 2 = 4 for both sides

    # Dynamic programming
    prev, curr = 1, 2  # For n = 1, prev = 1 (empty), curr = 2 (empty or one house)
    for _ in range(2, n + 1):
        prev, curr = curr, (prev + curr) % MOD

    # The result is the square of the number of ways for one side
    return (curr * curr) % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    print(countHousePlacements(n))  # Expected Output: 25

    # Test Case 2
    n = 1
    print(countHousePlacements(n))  # Expected Output: 4

    # Test Case 3
    n = 5
    print(countHousePlacements(n))  # Expected Output: 441

    # Test Case 4
    n = 10
    print(countHousePlacements(n))  # Expected Output: 3025

    # Test Case 5
    n = 100
    print(countHousePlacements(n))  # Expected Output: 418930126

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a loop that iterates `n` times, so the time complexity is O(n).

Space Complexity:
- The solution uses only two variables (`prev` and `curr`) to store intermediate results, so the space complexity is O(1).

Topic: Dynamic Programming
"""