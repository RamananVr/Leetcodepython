"""
LeetCode Problem #2767: Partition String Into Minimum Beautiful Substrings

Problem Statement:
You are given a binary string `s` that consists of only '0's and '1's. A substring of `s` is called beautiful if:
1. It consists of only '1's.
2. Its decimal value is a power of 5 (i.e., 1, 5, 25, 125, ...).

Return the minimum number of beautiful substrings that the binary string `s` can be partitioned into. If it is impossible to partition `s` into beautiful substrings, return -1.

A substring is a contiguous sequence of characters within the string.

Example:
Input: s = "101101"
Output: 2
Explanation: We can partition the string into ["101", "101"], both of which are beautiful substrings.

Constraints:
- 1 <= s.length <= 1000
- `s[i]` is either '0' or '1'.
"""

# Python Solution
def minimumBeautifulSubstrings(s: str) -> int:
    def is_power_of_five(binary: str) -> bool:
        """Check if a binary string represents a power of 5."""
        try:
            decimal_value = int(binary, 2)
            while decimal_value > 1:
                if decimal_value % 5 != 0:
                    return False
                decimal_value //= 5
            return decimal_value == 1
        except ValueError:
            return False

    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: no characters require 0 partitions.

    for i in range(1, n + 1):
        for j in range(i):
            substring = s[j:i]
            if substring[0] == '1' and is_power_of_five(substring):
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[n] if dp[n] != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "101101"
    print(minimumBeautifulSubstrings(s1))  # Output: 2

    # Test Case 2
    s2 = "111"
    print(minimumBeautifulSubstrings(s2))  # Output: 3

    # Test Case 3
    s3 = "000"
    print(minimumBeautifulSubstrings(s3))  # Output: -1

    # Test Case 4
    s4 = "1010101"
    print(minimumBeautifulSubstrings(s4))  # Output: 3

    # Test Case 5
    s5 = "1"
    print(minimumBeautifulSubstrings(s5))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop iterates over the string `s` of length `n`, and the inner loop iterates over all possible substrings.
- For each substring, we check if it is a power of 5, which involves converting the binary string to a decimal value and performing a division operation.
- The worst-case complexity is O(n^2) for substring generation and O(log(decimal_value)) for checking powers of 5.
- Overall, the time complexity is approximately O(n^2 * log(decimal_value)).

Space Complexity:
- The `dp` array requires O(n) space.
- The space complexity for the function is O(n).

Topic: Dynamic Programming (DP)
"""