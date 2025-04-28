"""
LeetCode Problem #1641: Count Sorted Vowel Strings

Problem Statement:
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

Example 1:
Input: n = 1
Output: 5
Explanation: The strings are ["a", "e", "i", "o", "u"].

Example 2:
Input: n = 2
Output: 15
Explanation: The strings are ["aa", "ae", "ai", "ao", "au", "ee", "ei", "eo", "eu", "ii", "io", "iu", "oo", "ou", "uu"].

Example 3:
Input: n = 33
Output: 66045

Constraints:
- 1 <= n <= 50
"""

# Solution
def countVowelStrings(n: int) -> int:
    """
    Dynamic Programming solution to count the number of lexicographically sorted vowel strings of length n.
    """
    # Initialize a DP array where dp[i] represents the number of strings ending with the i-th vowel
    dp = [1] * 5  # Base case: For n = 1, there are 5 strings ["a", "e", "i", "o", "u"]

    # Iterate for lengths from 2 to n
    for _ in range(2, n + 1):
        # Update dp array for the current length
        for i in range(3, -1, -1):  # Update dp[i] based on dp[i+1]
            dp[i] += dp[i + 1]

    # The total number of strings is the sum of dp array
    return sum(dp)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 1
    print(countVowelStrings(n))  # Output: 5

    # Test Case 2
    n = 2
    print(countVowelStrings(n))  # Output: 15

    # Test Case 3
    n = 33
    print(countVowelStrings(n))  # Output: 66045

    # Additional Test Case
    n = 5
    print(countVowelStrings(n))  # Output: 126

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop runs for n iterations, and the inner loop runs for 4 iterations (constant).
- Therefore, the time complexity is O(n).

Space Complexity:
- We use a single array `dp` of size 5 to store intermediate results.
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming
"""