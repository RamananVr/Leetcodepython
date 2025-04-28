"""
LeetCode Problem #1062: Longest Repeating Substring

Problem Statement:
Given a string `s`, return the length of the longest repeating substring. 
If no such substring exists, return 0.

A repeating substring is defined as a substring that occurs more than once in the string.

Constraints:
- 1 <= s.length <= 2000
- s consists of lowercase English letters.

Example 1:
Input: s = "abcd"
Output: 0
Explanation: There is no repeating substring.

Example 2:
Input: s = "abbaba"
Output: 2
Explanation: The longest repeating substring is "ab" or "ba", with length 2.

Example 3:
Input: s = "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", with length 3.

Example 4:
Input: s = "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", with length 4.
"""

def longestRepeatingSubstring(s: str) -> int:
    """
    Finds the length of the longest repeating substring in the given string.

    :param s: Input string
    :return: Length of the longest repeating substring
    """
    def has_repeating_substring(length: int) -> bool:
        """
        Helper function to check if there exists a repeating substring of a given length.
        """
        seen = set()
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring in seen:
                return True
            seen.add(substring)
        return False

    # Binary search for the maximum length of the repeating substring
    left, right = 1, len(s)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if has_repeating_substring(mid):
            result = mid
            left = mid + 1  # Try for a longer substring
        else:
            right = mid - 1  # Try for a shorter substring

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abcd"
    print(longestRepeatingSubstring(s1))  # Output: 0

    # Test Case 2
    s2 = "abbaba"
    print(longestRepeatingSubstring(s2))  # Output: 2

    # Test Case 3
    s3 = "aabcaabdaab"
    print(longestRepeatingSubstring(s3))  # Output: 3

    # Test Case 4
    s4 = "aaaaa"
    print(longestRepeatingSubstring(s4))  # Output: 4

"""
Time Complexity Analysis:
- The binary search runs in O(log(n)) iterations, where n is the length of the string.
- For each iteration, the `has_repeating_substring` function is called, which takes O(n * k) time,
  where k is the length of the substring being checked (at most n).
- Therefore, the overall time complexity is O(n^2 * log(n)).

Space Complexity Analysis:
- The space complexity is O(n) due to the `seen` set used in the `has_repeating_substring` function.

Topic: Strings, Binary Search, Hashing
"""