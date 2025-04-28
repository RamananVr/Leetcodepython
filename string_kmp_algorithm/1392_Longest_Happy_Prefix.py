"""
LeetCode Problem #1392: Longest Happy Prefix

Problem Statement:
A "happy prefix" is a non-empty prefix which is also a suffix (excluding the entire string itself). 
Given a string `s`, return the longest happy prefix of `s`. If no such prefix exists, return an empty string.

Example 1:
Input: s = "level"
Output: "l"
Explanation: The longest happy prefix is "l", as it is both a prefix and a suffix.

Example 2:
Input: s = "ababab"
Output: "abab"
Explanation: The longest happy prefix is "abab", as it is both a prefix and a suffix.

Example 3:
Input: s = "leetcodeleet"
Output: "leet"
Explanation: The longest happy prefix is "leet", as it is both a prefix and a suffix.

Example 4:
Input: s = "a"
Output: ""
Explanation: There is no happy prefix for a single character string.

Constraints:
- `1 <= s.length <= 10^5`
- `s` contains only lowercase English letters.
"""

# Solution
def longestPrefix(s: str) -> str:
    """
    Finds the longest happy prefix of the given string `s`.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The longest happy prefix, or an empty string if no such prefix exists.
    """
    n = len(s)
    lps = [0] * n  # Longest Prefix Suffix array
    j = 0  # Length of the previous longest prefix suffix

    # Build the LPS array using the KMP algorithm
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = lps[j - 1]
        if s[i] == s[j]:
            j += 1
        lps[i] = j

    # The value of lps[-1] gives the length of the longest happy prefix
    return s[:lps[-1]]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "level"
    print(longestPrefix(s1))  # Output: "l"

    # Test Case 2
    s2 = "ababab"
    print(longestPrefix(s2))  # Output: "abab"

    # Test Case 3
    s3 = "leetcodeleet"
    print(longestPrefix(s3))  # Output: "leet"

    # Test Case 4
    s4 = "a"
    print(longestPrefix(s4))  # Output: ""

    # Test Case 5
    s5 = "aaaaa"
    print(longestPrefix(s5))  # Output: "aaaa"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses the KMP algorithm to compute the LPS array, which takes O(n) time, where `n` is the length of the string `s`.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The solution uses an auxiliary array `lps` of size `n` to store the longest prefix suffix values.
- Therefore, the space complexity is O(n).

Topic: String, KMP Algorithm
"""