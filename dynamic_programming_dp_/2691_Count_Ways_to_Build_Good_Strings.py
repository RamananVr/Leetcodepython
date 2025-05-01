"""
LeetCode Problem #2691: "Count Ways to Build Good Strings"

Problem Statement:
Given two integers `low` and `high`, and two integers `zero` and `one`, you are tasked to count the number of different strings of length between `low` and `high` (inclusive) that can be formed using only the characters '0' and '1'. The strings must satisfy the following conditions:
1. The number of '0's in the string must be a multiple of `zero`.
2. The number of '1's in the string must be a multiple of `one`.

Return the total number of such strings modulo `10^9 + 7`.

Constraints:
- 1 <= low <= high <= 10^5
- 1 <= zero, one <= high
"""

# Python Solution
def countGoodStrings(low: int, high: int, zero: int, one: int) -> int:
    MOD = 10**9 + 7

    # dp[i] will store the number of good strings of length i
    dp = [0] * (high + 1)
    dp[0] = 1  # Base case: There's one way to form an empty string

    for length in range(1, high + 1):
        if length >= zero:
            dp[length] += dp[length - zero]
        if length >= one:
            dp[length] += dp[length - one]
        dp[length] %= MOD

    # Sum up the counts for lengths between low and high
    return sum(dp[low:high + 1]) % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    low = 3
    high = 3
    zero = 1
    one = 1
    print(countGoodStrings(low, high, zero, one))  # Expected Output: 8

    # Test Case 2
    low = 2
    high = 3
    zero = 1
    one = 2
    print(countGoodStrings(low, high, zero, one))  # Expected Output: 5

    # Test Case 3
    low = 1
    high = 5
    zero = 2
    one = 3
    print(countGoodStrings(low, high, zero, one))  # Expected Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- The loop runs from 1 to high, so the time complexity is O(high).
- Each iteration involves constant-time operations, so the overall complexity is O(high).

Space Complexity:
- The space complexity is O(high) due to the dp array.

Overall:
Time Complexity: O(high)
Space Complexity: O(high)
"""

# Topic: Dynamic Programming (DP)