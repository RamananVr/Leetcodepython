"""
LeetCode Problem #1216: Valid Palindrome III

Problem Statement:
Given a string s and an integer k, return true if s is a k-palindrome.
A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.

Example 1:
Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters to make "acdeca" a palindrome.

Example 2:
Input: s = "abbababa", k = 1
Output: true

Constraints:
- 1 <= s.length <= 1000
- s consists of only lowercase English letters.
- 0 <= k <= s.length
"""

# Solution
def isValidPalindrome(s: str, k: int) -> bool:
    def longest_palindromic_subsequence_length(s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Fill the DP table
        for length in range(2, n + 1):  # Substring lengths from 2 to n
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][n - 1]
    
    # Calculate the length of the longest palindromic subsequence
    lps_length = longest_palindromic_subsequence_length(s)
    
    # Check if the number of characters to remove is within the allowed limit
    return len(s) - lps_length <= k

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abcdeca"
    k1 = 2
    print(isValidPalindrome(s1, k1))  # Output: True

    # Test Case 2
    s2 = "abbababa"
    k2 = 1
    print(isValidPalindrome(s2, k2))  # Output: True

    # Test Case 3
    s3 = "abcd"
    k3 = 1
    print(isValidPalindrome(s3, k3))  # Output: False

    # Test Case 4
    s4 = "a"
    k4 = 0
    print(isValidPalindrome(s4, k4))  # Output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function `longest_palindromic_subsequence_length` uses a dynamic programming approach.
- The DP table has dimensions n x n, where n is the length of the string s.
- Filling the table involves iterating over all substrings of s, which takes O(n^2) time.
- Therefore, the overall time complexity is O(n^2).

Space Complexity:
- The DP table requires O(n^2) space to store intermediate results.
- Thus, the space complexity is O(n^2).

Topic: Dynamic Programming
"""