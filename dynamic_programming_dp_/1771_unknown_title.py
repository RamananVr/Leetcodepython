"""
LeetCode Problem #1771: Maximize Palindrome Length From Subsequences

Problem Statement:
You are given two strings, `word1` and `word2`. You want to construct a string by concatenating `word1` and `word2`, 
then find the longest palindrome that can be formed as a subsequence of the resulting string.

Return the length of the longest palindrome that can be formed.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted 
without changing the relative order of the remaining characters.

Example:
Input: word1 = "cacb", word2 = "cbba"
Output: 5
Explanation: The longest palindrome subsequence is "bacab".

Constraints:
- 1 <= word1.length, word2.length <= 100
- word1 and word2 consist of lowercase English letters.
"""

# Solution
def longestPalindrome(word1: str, word2: str) -> int:
    # Combine the two words into one string
    combined = word1 + word2
    n = len(combined)
    
    # Initialize a DP table
    dp = [[0] * n for _ in range(n)]
    
    # Base case: single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Fill the DP table for substrings of length 2 and more
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if combined[i] == combined[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    # Find the longest palindrome that uses at least one character from both word1 and word2
    max_length = 0
    for i in range(len(word1)):
        for j in range(len(word1), n):
            if combined[i] == combined[j]:
                max_length = max(max_length, dp[i][j])
    
    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "cacb"
    word2 = "cbba"
    print(longestPalindrome(word1, word2))  # Output: 5

    # Test Case 2
    word1 = "ab"
    word2 = "ab"
    print(longestPalindrome(word1, word2))  # Output: 3

    # Test Case 3
    word1 = "a"
    word2 = "b"
    print(longestPalindrome(word1, word2))  # Output: 0

    # Test Case 4
    word1 = "abc"
    word2 = "def"
    print(longestPalindrome(word1, word2))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The DP table has dimensions n x n, where n is the length of the combined string (word1 + word2).
- Filling the DP table requires O(n^2) operations, as we iterate over all substrings of the combined string.
- The final loop to find the longest palindrome that uses characters from both word1 and word2 takes O(len(word1) * len(word2)).
- Overall time complexity: O(n^2), where n = len(word1) + len(word2).

Space Complexity:
- The DP table requires O(n^2) space.
- Overall space complexity: O(n^2), where n = len(word1) + len(word2).

Topic: Dynamic Programming (DP)
"""