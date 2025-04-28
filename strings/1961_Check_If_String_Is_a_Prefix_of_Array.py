"""
LeetCode Problem #1961: Check If String Is a Prefix of Array

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
    concatenated = ""
    for word in words:
        concatenated += word
        if concatenated == s:
            return True
        if len(concatenated) > len(s):
            return False
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "iloveleetcode"
    words1 = ["i", "love", "leetcode", "apples"]
    print(isPrefixString(s1, words1))  # Output: True

    # Test Case 2
    s2 = "iloveleetcode"
    words2 = ["apples", "i", "love", "leetcode"]
    print(isPrefixString(s2, words2))  # Output: False

    # Test Case 3
    s3 = "hello"
    words3 = ["he", "llo", "world"]
    print(isPrefixString(s3, words3))  # Output: True

    # Test Case 4
    s4 = "prefix"
    words4 = ["pre", "fix", "suffix"]
    print(isPrefixString(s4, words4))  # Output: True

    # Test Case 5
    s5 = "prefixsuffix"
    words5 = ["pre", "fix", "suffix"]
    print(isPrefixString(s5, words5))  # Output: True

    # Test Case 6
    s6 = "prefixsuffixextra"
    words6 = ["pre", "fix", "suffix"]
    print(isPrefixString(s6, words6))  # Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `words` array and concatenates strings until the concatenated string matches `s` or exceeds its length.
- In the worst case, we iterate through all `words` and concatenate all strings, which takes O(n * m), where `n` is the number of words and `m` is the average length of each word.

Space Complexity:
- The space complexity is O(m * n) due to the `concatenated` string, which grows as we concatenate strings from `words`.

Overall:
- Time Complexity: O(n * m)
- Space Complexity: O(n * m)
"""

# Topic: Strings