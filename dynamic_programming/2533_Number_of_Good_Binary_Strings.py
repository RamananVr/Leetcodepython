"""
LeetCode Problem #2533: Number of Good Binary Strings

Problem Statement:
You are given two integers `low` and `high`, which represent a range of integers `[low, high]` (inclusive). 
You are also given two integers `zero` and `one`. A binary string is considered "good" if:
1. The string can be constructed using only the characters '0' and '1'.
2. The string has a length that lies in the range `[low, high]`.
3. The string can be constructed by concatenating exactly `zero` number of '0's and `one` number of '1's any number of times.

Return the number of "good" binary strings modulo `10^9 + 7`.

Constraints:
- 1 <= low <= high <= 10^5
- 1 <= zero, one <= high
"""

# Python Solution
def countGoodStrings(low: int, high: int, zero: int, one: int) -> int:
    MOD = 10**9 + 7

    # dp[i] will store the number of good binary strings of length i
    dp = [0] * (high + 1)
    dp[0] = 1  # Base case: There's one way to construct an empty string

    for length in range(1, high + 1):
        # Add the number of ways to form a string of length `length - zero`
        if length >= zero:
            dp[length] += dp[length - zero]
        # Add the number of ways to form a string of length `length - one`
        if length >= one:
            dp[length] += dp[length - one]
        # Take modulo to prevent overflow
        dp[length] %= MOD

    # Sum up the counts for lengths in the range [low, high]
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
- The loop runs from 1 to `high`, so the time complexity is O(high).
- Each iteration involves constant-time operations, so the overall complexity is O(high).

Space Complexity:
- The space complexity is O(high) due to the `dp` array.

Overall, the time and space complexity are both O(high).

Topic: Dynamic Programming
"""