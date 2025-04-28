"""
LeetCode Problem #1163: Last Substring in Lexicographical Order

Problem Statement:
Given a string `s`, return the last substring of `s` in lexicographical order.

Example:
Input: "abab"
Output: "bab"

Explanation:
The substrings of "abab" are: "abab", "bab", "ab", "b", "a".
Among them, "bab" is the largest in lexicographical order.

Constraints:
- 1 <= s.length <= 4 * 10^5
- s contains only lowercase English letters.
"""

def lastSubstring(s: str) -> str:
    """
    Returns the last substring of `s` in lexicographical order.

    Args:
    s (str): The input string.

    Returns:
    str: The last lexicographical substring.
    """
    n = len(s)
    i, j, k = 0, 1, 0  # i is the current candidate, j is the next candidate, k is the offset

    while j + k < n:
        if s[i + k] == s[j + k]:
            k += 1
        elif s[i + k] < s[j + k]:
            i = max(i + k + 1, j)  # Move i to the next candidate
            j = i + 1
            k = 0
        else:
            j = j + k + 1  # Move j to the next candidate
            k = 0

    return s[i]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abab"
    print(lastSubstring(s1))  # Expected Output: "bab"

    # Test Case 2
    s2 = "leetcode"
    print(lastSubstring(s2))  # Expected Output: "tcode"

    # Test Case 3
    s3 = "zzzzzz"
    print(lastSubstring(s3))  # Expected Output: "zzzzzz"

    # Test Case 4
    s4 = "abcabc"
    print(lastSubstring(s4))  # Expected Output: "cabc"

    # Test Case 5
    s5 = "a"
    print(lastSubstring(s5))  # Expected Output: "a"

"""
Time Complexity Analysis:
- The algorithm uses a two-pointer approach to compare substrings.
- In the worst case, each character in the string is compared at most twice.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space.
- Therefore, the space complexity is O(1).

Topic: Strings
"""