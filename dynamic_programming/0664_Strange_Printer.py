"""
LeetCode Problem #664: Strange Printer

Problem Statement:
There is a strange printer with the following two special properties:
1. The printer can only print a sequence of the same character each time.
2. At each turn, the printer can print new characters starting and ending at any place and will overwrite the existing characters.

Given a string `s`, your task is to calculate the minimum number of turns the printer needs to print it.

Constraints:
- 1 <= s.length <= 100
- s consists of lowercase English letters.
"""

def strangePrinter(s: str) -> int:
    """
    Dynamic Programming solution to calculate the minimum number of turns
    the printer needs to print the string `s`.
    """
    n = len(s)
    if n == 0:
        return 0

    # dp[i][j] represents the minimum number of turns needed to print s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: single character substrings
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table for substrings of increasing lengths
    for length in range(2, n + 1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = dp[i][j - 1] + 1  # Initialize with the worst case
            for k in range(i, j):
                if s[k] == s[j]:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j - 1])

    return dp[0][n - 1]


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aaabbb"
    print(f"Minimum turns to print '{s1}': {strangePrinter(s1)}")  # Expected: 2

    # Test Case 2
    s2 = "aba"
    print(f"Minimum turns to print '{s2}': {strangePrinter(s2)}")  # Expected: 2

    # Test Case 3
    s3 = "abcba"
    print(f"Minimum turns to print '{s3}': {strangePrinter(s3)}")  # Expected: 3

    # Test Case 4
    s4 = "a"
    print(f"Minimum turns to print '{s4}': {strangePrinter(s4)}")  # Expected: 1

    # Test Case 5
    s5 = "aa"
    print(f"Minimum turns to print '{s5}': {strangePrinter(s5)}")  # Expected: 1


"""
Time Complexity Analysis:
- The solution uses a dynamic programming approach with a 2D DP table.
- The outer loop iterates over substring lengths (from 2 to n), and the inner loops iterate over all possible substrings of that length.
- For each substring, we may perform an additional loop to check for matching characters.
- This results in a time complexity of O(n^3), where n is the length of the string.

Space Complexity Analysis:
- The solution uses a 2D DP table of size n x n to store results for all substrings.
- Thus, the space complexity is O(n^2).

Topic: Dynamic Programming
"""