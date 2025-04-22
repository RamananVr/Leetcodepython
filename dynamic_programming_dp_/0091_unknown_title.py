"""
LeetCode Problem #91: Decode Ways

Problem Statement:
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1", 'B' -> "2", ..., 'Z' -> "26".

To decode an encoded message, all the digits must be grouped in such a way that they can be mapped to letters using the above mapping. Note that the mapping is case-sensitive, and "01" is not a valid mapping since "0" cannot be mapped to any letter.

Given a string `s` containing only digits, return the total number of ways to decode it.

The test cases are guaranteed to contain only valid numbers and the input string `s` will not be empty.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" can be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" can be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "0"
Output: 0
Explanation: There is no valid mapping for "0".

Example 4:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because "0" cannot be used as a standalone digit.

Constraints:
- 1 <= s.length <= 100
- s contains only digits and may contain leading zeros.
"""

# Clean and Correct Python Solution
def numDecodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: empty string has one way to decode
    dp[1] = 1  # Base case: single character (if not '0') has one way to decode

    for i in range(2, n + 1):
        # Check if the single digit is valid
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]

        # Check if the two-digit number is valid
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "12"
    print(numDecodings(s1))  # Output: 2

    # Test Case 2
    s2 = "226"
    print(numDecodings(s2))  # Output: 3

    # Test Case 3
    s3 = "0"
    print(numDecodings(s3))  # Output: 0

    # Test Case 4
    s4 = "06"
    print(numDecodings(s4))  # Output: 0

    # Test Case 5
    s5 = "11106"
    print(numDecodings(s5))  # Output: 2

    # Test Case 6
    s6 = "10"
    print(numDecodings(s6))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the string once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string `s`.

Space Complexity:
- The solution uses a DP array of size n+1 to store intermediate results.
- Therefore, the space complexity is O(n).
"""

# Topic: Dynamic Programming (DP)