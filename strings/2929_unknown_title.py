"""
LeetCode Problem #2929: Check if a String is a Prefix of Array

Problem Statement:
Given a string `s` and an array of strings `words`, determine whether `s` is a prefix string of `words`.

A string `s` is a prefix string of `words` if `s` can be formed by concatenating the first `k` strings in `words` for some positive `k` no larger than `words.length`.

Return `true` if `s` is a prefix string of `words`, or `false` otherwise.

Example 1:
Input: s = "iloveleetcode", words = ["i", "love", "leetcode", "apples"]
Output: true
Explanation: s can be formed by concatenating "i", "love", and "leetcode".

Example 2:
Input: s = "iloveleetcode", words = ["apples", "i", "love", "leetcode"]
Output: false
Explanation: s cannot be formed by concatenating the first k strings in words.

Constraints:
- 1 <= s.length <= 100
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- `s` and `words[i]` consist of only lowercase English letters.
"""

# Python Solution
def isPrefixString(s: str, words: list[str]) -> bool:
    """
    Determines whether the string `s` is a prefix string of the array `words`.

    :param s: The target string.
    :param words: The array of strings.
    :return: True if `s` is a prefix string of `words`, False otherwise.
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
    # Test Case 1
    s1 = "iloveleetcode"
    words1 = ["i", "love", "leetcode", "apples"]
    print(isPrefixString(s1, words1))  # Expected Output: True

    # Test Case 2
    s2 = "iloveleetcode"
    words2 = ["apples", "i", "love", "leetcode"]
    print(isPrefixString(s2, words2))  # Expected Output: False

    # Test Case 3
    s3 = "hello"
    words3 = ["he", "llo", "world"]
    print(isPrefixString(s3, words3))  # Expected Output: True

    # Test Case 4
    s4 = "prefix"
    words4 = ["pre", "fix", "suffix"]
    print(isPrefixString(s4, words4))  # Expected Output: True

    # Test Case 5
    s5 = "prefixsuffix"
    words5 = ["pre", "fix"]
    print(isPrefixString(s5, words5))  # Expected Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `words` array, concatenating strings until the prefix matches `s` or exceeds its length.
- Let `n` be the length of `s` and `m` be the total number of characters in `words`.
- In the worst case, we concatenate all strings in `words`, which takes O(m) time.
- Therefore, the time complexity is O(m).

Space Complexity:
- The function uses a single string `prefix` to store the concatenated result.
- The space used by `prefix` is proportional to the length of `s` in the worst case.
- Therefore, the space complexity is O(n), where `n` is the length of `s`.
"""

# Topic: Strings