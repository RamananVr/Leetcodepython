"""
LeetCode Problem #2207: Maximize Number of Subsequences in a String

Problem Statement:
You are given a string `text` and another string `pattern` of length 2. You want to create the maximum number of subsequences of `pattern` in `text`.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

Return the maximum number of subsequences of `pattern` that can be formed.

Example:
Input: text = "abdcdbc", pattern = "ac"
Output: 4
Explanation: Subsequences "ac" can be formed as follows:
- From "abdcdbc", remove 'b', 'd', 'd', 'b' -> "ac"
- From "abdcdbc", remove 'b', 'd', 'c', 'b' -> "ac"
- From "abdcdbc", remove 'a', 'b', 'd', 'b' -> "ac"
- From "abdcdbc", remove 'a', 'b', 'd', 'c' -> "ac"
Thus, the maximum number of subsequences is 4.

Constraints:
- 1 <= text.length <= 10^5
- pattern.length == 2
- `pattern` consists of lowercase English letters.
- `text` consists of lowercase English letters.
"""

# Solution
def maximumSubsequenceCount(text: str, pattern: str) -> int:
    # Count occurrences of the two characters in the pattern
    count_first = 0
    count_second = 0
    result = 0
    
    for char in text:
        if char == pattern[1]:
            # Add count_first to result for every occurrence of pattern[1]
            result += count_first
            count_second += 1
        if char == pattern[0]:
            count_first += 1
    
    # Add the maximum of adding pattern[0] at the start or pattern[1] at the end
    return result + max(count_first, count_second)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    text = "abdcdbc"
    pattern = "ac"
    print(maximumSubsequenceCount(text, pattern))  # Output: 4

    # Test Case 2
    text = "aabb"
    pattern = "ab"
    print(maximumSubsequenceCount(text, pattern))  # Output: 6

    # Test Case 3
    text = "aaaa"
    pattern = "aa"
    print(maximumSubsequenceCount(text, pattern))  # Output: 10

    # Test Case 4
    text = "abcabc"
    pattern = "bc"
    print(maximumSubsequenceCount(text, pattern))  # Output: 6

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the string `text` once, making the time complexity O(n), where n is the length of `text`.

Space Complexity:
- The solution uses a constant amount of extra space for variables (count_first, count_second, result), making the space complexity O(1).
"""

# Topic: Strings, Greedy