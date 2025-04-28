"""
LeetCode Problem #2484: Count Palindromic Subsequences

Problem Statement:
Given a string `s`, return the number of distinct palindromic subsequences in `s`. 
You may assume that the answer fits in a 32-bit signed integer.

A subsequence of a string is obtained by deleting zero or more characters from the string 
without changing the order of the remaining characters.

A string is palindromic if it reads the same forward and backward.

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.

Your task is to count all distinct palindromic subsequences in the string `s`.
"""

def countPalindromicSubsequences(s: str) -> int:
    """
    Function to count the number of distinct palindromic subsequences in a string.
    """
    MOD = 10**9 + 7
    n = len(s)
    
    # dp[i][j] will store the number of distinct palindromic subsequences in s[i:j+1]
    dp = [[0] * n for _ in range(n)]
    
    # Base case: Single character substrings are palindromic
    for i in range(n):
        dp[i][i] = 1
    
    # Iterate over all possible substring lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                low, high = i + 1, j - 1
                
                # Find the first and last occurrence of s[i] in s[i+1:j]
                while low <= high and s[low] != s[i]:
                    low += 1
                while low <= high and s[high] != s[i]:
                    high -= 1
                
                if low > high:  # No duplicate characters in the middle
                    dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                elif low == high:  # One duplicate character in the middle
                    dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                else:  # More than one duplicate character in the middle
                    dp[i][j] = dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1]
            else:
                dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
            
            # Ensure the result is within the modulo constraint
            dp[i][j] = (dp[i][j] + MOD) % MOD
    
    return dp[0][n - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "bccb"
    print(f"Number of distinct palindromic subsequences in '{s1}': {countPalindromicSubsequences(s1)}")
    # Expected Output: 6

    # Test Case 2
    s2 = "abcd"
    print(f"Number of distinct palindromic subsequences in '{s2}': {countPalindromicSubsequences(s2)}")
    # Expected Output: 4

    # Test Case 3
    s3 = "aaa"
    print(f"Number of distinct palindromic subsequences in '{s3}': {countPalindromicSubsequences(s3)}")
    # Expected Output: 3

    # Test Case 4
    s4 = "aab"
    print(f"Number of distinct palindromic subsequences in '{s4}': {countPalindromicSubsequences(s4)}")
    # Expected Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a dynamic programming approach with a 2D table `dp` of size n x n.
- Filling each cell in the table involves constant time operations, and there are O(n^2) cells.
- Thus, the time complexity is O(n^2).

Space Complexity:
- The space complexity is dominated by the 2D DP table, which requires O(n^2) space.
- Therefore, the space complexity is O(n^2).

Topic: Dynamic Programming
"""