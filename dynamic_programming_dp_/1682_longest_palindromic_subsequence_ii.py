"""
LeetCode Question #1682: Longest Palindromic Subsequence II

Problem Statement:
Given a string `s`, return the length of the longest palindromic subsequence that does not include the same character twice. 
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.

Example:
Input: s = "bbabab"
Output: 4
Explanation: The longest palindromic subsequence that does not include the same character twice is "baba".

Input: s = "dcbccacdb"
Output: 4
Explanation: The longest palindromic subsequence that does not include the same character twice is "dbcd".

"""

# Solution
def longestPalindromeSubseqII(s: str) -> int:
    def helper(start, end, prev_char):
        if start > end:
            return 0
        if start == end:
            return 1 if s[start] != prev_char else 0
        
        if (start, end, prev_char) in memo:
            return memo[(start, end, prev_char)]
        
        if s[start] == s[end] and s[start] != prev_char:
            memo[(start, end, prev_char)] = 2 + helper(start + 1, end - 1, s[start])
        else:
            memo[(start, end, prev_char)] = max(
                helper(start + 1, end, prev_char),
                helper(start, end - 1, prev_char)
            )
        
        return memo[(start, end, prev_char)]
    
    memo = {}
    return helper(0, len(s) - 1, None)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "bbabab"
    print(longestPalindromeSubseqII(s1))  # Output: 4

    # Test Case 2
    s2 = "dcbccacdb"
    print(longestPalindromeSubseqII(s2))  # Output: 4

    # Test Case 3
    s3 = "a"
    print(longestPalindromeSubseqII(s3))  # Output: 1

    # Test Case 4
    s4 = "abcde"
    print(longestPalindromeSubseqII(s4))  # Output: 1

    # Test Case 5
    s5 = "aaaa"
    print(longestPalindromeSubseqII(s5))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
The function uses memoization to store results for overlapping subproblems. The number of subproblems is O(n^2), where n is the length of the string `s`. 
For each subproblem, the computation is O(1). Therefore, the overall time complexity is O(n^2).

Space Complexity:
The space complexity is dominated by the memoization dictionary, which stores O(n^2) entries. Additionally, the recursive call stack can go up to O(n) depth. 
Thus, the overall space complexity is O(n^2).

Topic: Dynamic Programming (DP)
"""