"""
LeetCode Problem #1967: Number of Strings That Appear as Substrings in Word

Problem Statement:
Given an array of strings `patterns` and a string `word`, return the number of strings in `patterns` that appear as substrings in `word`.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: patterns = ["a", "abc", "bc", "d"], word = "abc"
Output: 3
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".

Example 2:
Input: patterns = ["a", "b", "c"], word = "aaaaabbbbb"
Output: 2
Explanation:
- "a" appears as a substring in "aaaaabbbbb".
- "b" appears as a substring in "aaaaabbbbb".
- "c" does not appear as a substring in "aaaaabbbbb".

Example 3:
Input: patterns = ["a", "a", "a"], word = "ab"
Output: 3
Explanation:
- Each "a" in patterns appears as a substring in "ab".

Constraints:
- 1 <= patterns.length <= 100
- 1 <= patterns[i].length <= 100
- 1 <= word.length <= 100
- patterns[i] and word consist of lowercase English letters.
"""

# Clean, Correct Python Solution
def numOfStrings(patterns, word):
    """
    Counts the number of strings in patterns that appear as substrings in word.

    :param patterns: List[str] - List of patterns to check.
    :param word: str - The word in which substrings are checked.
    :return: int - Number of patterns that appear as substrings in word.
    """
    count = 0
    for pattern in patterns:
        if pattern in word:
            count += 1
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    patterns = ["a", "abc", "bc", "d"]
    word = "abc"
    print(numOfStrings(patterns, word))  # Output: 3

    # Test Case 2
    patterns = ["a", "b", "c"]
    word = "aaaaabbbbb"
    print(numOfStrings(patterns, word))  # Output: 2

    # Test Case 3
    patterns = ["a", "a", "a"]
    word = "ab"
    print(numOfStrings(patterns, word))  # Output: 3

    # Additional Test Case 4
    patterns = ["xyz", "xy", "z"]
    word = "xyzxyz"
    print(numOfStrings(patterns, word))  # Output: 3

    # Additional Test Case 5
    patterns = ["hello", "world", "leet", "code"]
    word = "leetcode"
    print(numOfStrings(patterns, word))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each pattern in the `patterns` list, we check if it exists in `word`.
- The `in` operator in Python for strings has a time complexity of O(n), where n is the length of `word`.
- If there are m patterns and the length of `word` is n, the overall time complexity is O(m * n).

Space Complexity:
- The solution uses a constant amount of extra space, as we are only using a counter variable.
- Therefore, the space complexity is O(1).
"""

# Topic: Strings