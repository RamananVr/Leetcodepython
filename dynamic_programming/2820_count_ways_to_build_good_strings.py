"""
LeetCode Question #2820: Count Ways to Build Good Strings

Problem Statement:
A "good string" is a string that satisfies the following conditions:
1. It consists of only the characters '0' and '1'.
2. Its length is between `low` and `high` (inclusive).
3. The number of '0's in the string is divisible by `zero_count`.
4. The number of '1's in the string is divisible by `one_count`.

Given integers `low`, `high`, `zero_count`, and `one_count`, return the number of good strings that can be formed. Since the answer may be large, return it modulo `10^9 + 7`.

Constraints:
- 1 <= low <= high <= 10^5
- 1 <= zero_count, one_count <= high

"""

# Python Solution
def countGoodStrings(low: int, high: int, zero_count: int, one_count: int) -> int:
    MOD = 10**9 + 7

    # dp[i] represents the number of good strings of length i
    dp = [0] * (high + 1)
    dp[0] = 1  # Base case: there's one way to form an empty string

    for length in range(1, high + 1):
        if length >= zero_count:
            dp[length] += dp[length - zero_count]
        if length >= one_count:
            dp[length] += dp[length - one_count]
        dp[length] %= MOD

    # Sum up the counts for lengths between low and high
    return sum(dp[low:high + 1]) % MOD


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    low = 3
    high = 3
    zero_count = 1
    one_count = 1
    print(countGoodStrings(low, high, zero_count, one_count))  # Expected Output: 8

    # Test Case 2
    low = 2
    high = 4
    zero_count = 2
    one_count = 1
    print(countGoodStrings(low, high, zero_count, one_count))  # Expected Output: 5

    # Test Case 3
    low = 1
    high = 5
    zero_count = 2
    one_count = 3
    print(countGoodStrings(low, high, zero_count, one_count))  # Expected Output: 3


"""
Time and Space Complexity Analysis:

Time Complexity:
- The loop iterates from 1 to `high`, so the time complexity is O(high).
- Within the loop, we perform constant-time operations for each length, so the overall complexity is O(high).

Space Complexity:
- We use a list `dp` of size `high + 1`, so the space complexity is O(high).

Topic: Dynamic Programming
"""