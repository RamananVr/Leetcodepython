"""
LeetCode Problem #459: Repeated Substring Pattern

Problem Statement:
Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10,000.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times.

Constraints:
- 1 <= s.length <= 10^4
- s consists of lowercase English letters.
"""

def repeatedSubstringPattern(s: str) -> bool:
    """
    Determines if the string can be constructed by repeating a substring.

    Args:
    s (str): The input string.

    Returns:
    bool: True if the string can be constructed by repeating a substring, False otherwise.
    """
    n = len(s)
    for i in range(1, n // 2 + 1):  # Only consider substrings up to half the length of s
        if n % i == 0:  # The substring length must divide the total length
            substring = s[:i]
            if substring * (n // i) == s:  # Check if repeating the substring forms the original string
                return True
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abab"
    print(repeatedSubstringPattern(s1))  # Output: True

    # Test Case 2
    s2 = "aba"
    print(repeatedSubstringPattern(s2))  # Output: False

    # Test Case 3
    s3 = "abcabcabcabc"
    print(repeatedSubstringPattern(s3))  # Output: True

    # Test Case 4
    s4 = "a"
    print(repeatedSubstringPattern(s4))  # Output: False

    # Test Case 5
    s5 = "aaaa"
    print(repeatedSubstringPattern(s5))  # Output: True

"""
Time Complexity:
- The outer loop runs up to n // 2 iterations, where n is the length of the string.
- For each iteration, checking if the substring repeats takes O(n) time.
- In the worst case, the total time complexity is O(n^2).

Space Complexity:
- The space complexity is O(1) as we are not using any additional data structures that scale with the input size.

Topic: String
"""