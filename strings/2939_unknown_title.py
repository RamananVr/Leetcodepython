"""
LeetCode Problem #2939: Check if String Is a Prefix of Array

Problem Statement:
Given a string `s` and an array of strings `words`, determine if `s` is a prefix string of `words`.

A string `s` is a prefix string of `words` if `s` can be formed by concatenating the first `k` strings in `words` for some positive `k` no greater than `words.length`.

Return `true` if `s` is a prefix string of `words`, or `false` otherwise.

Constraints:
- `1 <= s.length <= 100`
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 10`
- `s` and `words[i]` consist of only lowercase English letters.
"""

def isPrefixString(s: str, words: list[str]) -> bool:
    """
    Determines if the string `s` is a prefix string of the array `words`.

    Args:
    s (str): The target string.
    words (list[str]): The array of strings.

    Returns:
    bool: True if `s` is a prefix string of `words`, False otherwise.
    """
    prefix = ""
    for word in words:
        prefix += word
        if prefix == s:
            return True
        if len(prefix) > len(s):
            return False
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: s is a prefix of words
    s1 = "iloveleetcode"
    words1 = ["i", "love", "leetcode", "apples"]
    print(isPrefixString(s1, words1))  # Expected: True

    # Test Case 2: s is not a prefix of words
    s2 = "ilove"
    words2 = ["apples", "i", "love", "leetcode"]
    print(isPrefixString(s2, words2))  # Expected: False

    # Test Case 3: s is a prefix but not the full concatenation
    s3 = "ilove"
    words3 = ["i", "love", "leetcode"]
    print(isPrefixString(s3, words3))  # Expected: True

    # Test Case 4: s is longer than the concatenation of words
    s4 = "iloveleetcodeapples"
    words4 = ["i", "love", "leetcode"]
    print(isPrefixString(s4, words4))  # Expected: False

    # Test Case 5: s is empty (invalid case per constraints, but for robustness)
    s5 = ""
    words5 = ["i", "love", "leetcode"]
    print(isPrefixString(s5, words5))  # Expected: False

# Time Complexity Analysis:
# Let `n` be the length of the string `s` and `m` be the total number of characters in `words`.
# - In the worst case, we iterate through all strings in `words` and concatenate them.
# - Concatenation of strings takes O(k) time for a string of length `k`.
# - Thus, the total time complexity is O(m), where `m` is the sum of the lengths of all strings in `words`.

# Space Complexity Analysis:
# - The space complexity is O(n), where `n` is the length of the string `s`, as we store the concatenated prefix.

# Topic: Strings