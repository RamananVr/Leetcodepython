"""
LeetCode Problem #467: Unique Substrings in Wraparound String

Problem Statement:
We define the string `s` to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", 
so `s` will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...".

Given a string `p`, return the number of unique non-empty substrings of `p` that are present in `s`.

Constraints:
- 1 <= p.length <= 10^5
- `p` consists of lowercase English letters.

Example:
Input: p = "zab"
Output: 6
Explanation: The substrings are "z", "a", "b", "za", "ab", "zab". 
              "zab" is a substring of the infinite wraparound string.

"""

# Solution
def findSubstringInWraproundString(p: str) -> int:
    # Dictionary to store the maximum length of substrings ending with each character
    dp = {}
    max_len = 0  # Tracks the length of the current valid substring

    for i in range(len(p)):
        # Check if the current character is consecutive to the previous one
        if i > 0 and (ord(p[i]) - ord(p[i - 1]) == 1 or (p[i - 1] == 'z' and p[i] == 'a')):
            max_len += 1
        else:
            max_len = 1

        # Update the maximum length of substrings ending with p[i]
        dp[p[i]] = max(dp.get(p[i], 0), max_len)

    # The result is the sum of all maximum lengths for each character
    return sum(dp.values())

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    p1 = "zab"
    print(findSubstringInWraproundString(p1))  # Output: 6

    # Test Case 2
    p2 = "cac"
    print(findSubstringInWraproundString(p2))  # Output: 2

    # Test Case 3
    p3 = "a"
    print(findSubstringInWraproundString(p3))  # Output: 1

    # Test Case 4
    p4 = "zabcdefghijklmnopqrstuvwxyz"
    print(findSubstringInWraproundString(p4))  # Output: 26

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string `p` once, performing constant-time operations for each character.
- Thus, the time complexity is O(n), where n is the length of the string `p`.

Space Complexity:
- The space complexity is O(1) for the `dp` dictionary, as it stores at most 26 entries (one for each letter of the alphabet).
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming (DP)
"""