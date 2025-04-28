"""
LeetCode Problem #2988: Check if a String is a Prefix of Array

Problem Statement:
You are given a string `s` and an array of strings `words`. Determine if `s` is a prefix string of `words`.

A string `s` is a prefix string of `words` if `s` can be formed by concatenating the first `k` strings in `words` for some positive `k` no larger than `words.length`.

Return `true` if `s` is a prefix string of `words`, or `false` otherwise.

Constraints:
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `1 <= s.length <= 100`
- `words[i]` and `s` consist of only lowercase English letters.
"""

def isPrefixString(s: str, words: list[str]) -> bool:
    """
    Determines if the string `s` is a prefix string of the array `words`.

    Args:
    s (str): The target string to check.
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

    # Test Case 5: s is empty (edge case)
    s5 = ""
    words5 = ["i", "love", "leetcode"]
    print(isPrefixString(s5, words5))  # Expected: False

    # Test Case 6: Single word matches s
    s6 = "hello"
    words6 = ["hello"]
    print(isPrefixString(s6, words6))  # Expected: True

# Time Complexity Analysis:
# Let `n` be the length of `s` and `m` be the total number of characters in `words`.
# - In the worst case, we iterate through all the strings in `words` and concatenate them.
# - Each concatenation operation takes O(k), where `k` is the length of the current word.
# - Thus, the total time complexity is O(m), where `m` is the sum of the lengths of all strings in `words`.

# Space Complexity Analysis:
# - The space complexity is O(n), where `n` is the length of `s`, as we store the `prefix` string during the computation.

# Topic: Strings