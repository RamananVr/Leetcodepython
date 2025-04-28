"""
LeetCode Problem #1397: Find All Good Strings

Problem Statement:
Given the strings s1 and s2 of size n and a string evil, return the number of good strings that satisfy the following conditions:
1. The string is greater than or equal to s1.
2. The string is less than or equal to s2.
3. The string does not contain the string evil as a substring.

Since the answer can be very large, return it modulo 10^9 + 7.

Constraints:
- 1 <= n <= 500
- s1.length == s2.length == n
- 1 <= evil.length <= 50
- s1, s2, evil consist of lowercase English letters.

"""

# Python Solution
from functools import lru_cache

def findGoodStrings(n: int, s1: str, s2: str, evil: str) -> int:
    MOD = 10**9 + 7

    # Build the KMP failure table for the "evil" string
    def build_kmp_table(pattern):
        m = len(pattern)
        kmp = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and pattern[i] != pattern[j]:
                j = kmp[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            kmp[i] = j
        return kmp

    kmp_table = build_kmp_table(evil)

    @lru_cache(None)
    def dp(index, tight1, tight2, matched):
        # Base case: if we've constructed a string of length `n`
        if index == n:
            return 1

        # Determine the range of characters to consider
        lower_bound = s1[index] if tight1 else 'a'
        upper_bound = s2[index] if tight2 else 'z'

        total = 0
        for char in range(ord(lower_bound), ord(upper_bound) + 1):
            char = chr(char)
            new_matched = matched

            # Update the KMP state
            while new_matched > 0 and char != evil[new_matched]:
                new_matched = kmp_table[new_matched - 1]
            if char == evil[new_matched]:
                new_matched += 1

            # If the "evil" string is fully matched, skip this branch
            if new_matched == len(evil):
                continue

            # Update tight constraints
            new_tight1 = tight1 and (char == lower_bound)
            new_tight2 = tight2 and (char == upper_bound)

            # Recursive call
            total += dp(index + 1, new_tight1, new_tight2, new_matched)
            total %= MOD

        return total

    return dp(0, True, True, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 2
    s1 = "aa"
    s2 = "da"
    evil = "b"
    print(findGoodStrings(n, s1, s2, evil))  # Expected Output: 51

    # Test Case 2
    n = 8
    s1 = "leetcode"
    s2 = "leetgoes"
    evil = "leet"
    print(findGoodStrings(n, s1, s2, evil))  # Expected Output: 0

    # Test Case 3
    n = 3
    s1 = "aaa"
    s2 = "abc"
    evil = "ab"
    print(findGoodStrings(n, s1, s2, evil))  # Expected Output: 597

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses dynamic programming with memoization. The number of states is O(n * len(evil) * 2 * 2), where:
  - `n` is the length of the strings.
  - `len(evil)` is the length of the "evil" string.
  - The two boolean flags (tight1 and tight2) add a factor of 2 each.
- For each state, we iterate over at most 26 characters (a-z).
- Thus, the overall time complexity is O(n * len(evil) * 2 * 2 * 26) = O(n * len(evil) * 104).

Space Complexity:
- The space complexity is dominated by the memoization table, which has O(n * len(evil) * 2 * 2) states.
- Additionally, the KMP table takes O(len(evil)) space.
- Thus, the overall space complexity is O(n * len(evil)).

Topic: Dynamic Programming (DP)
"""