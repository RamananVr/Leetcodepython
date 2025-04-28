"""
LeetCode Question #2918: Problem Statement

Given a string `s` and a dictionary of strings `wordDict`, return true if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Constraints:
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters.
- All the strings in wordDict are unique.

Example:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

# Python Solution
def wordBreak(s: str, wordDict: list[str]) -> bool:
    """
    Determines if the string `s` can be segmented into a space-separated sequence of one or more dictionary words.

    :param s: The input string.
    :param wordDict: A list of valid words.
    :return: True if `s` can be segmented, False otherwise.
    """
    word_set = set(wordDict)  # Convert wordDict to a set for O(1) lookups
    dp = [False] * (len(s) + 1)  # dp[i] indicates if s[:i] can be segmented
    dp[0] = True  # Base case: an empty string can always be segmented

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[len(s)]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    print(wordBreak(s1, wordDict1))  # Output: True

    # Test Case 2
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    print(wordBreak(s2, wordDict2))  # Output: True

    # Test Case 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    print(wordBreak(s3, wordDict3))  # Output: False

    # Test Case 4
    s4 = "pineapplepenapple"
    wordDict4 = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(wordBreak(s4, wordDict4))  # Output: True

    # Test Case 5
    s5 = "abcd"
    wordDict5 = ["a", "abc", "b", "cd"]
    print(wordBreak(s5, wordDict5))  # Output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop runs for `len(s)` iterations.
- The inner loop runs for at most `len(s)` iterations in the worst case.
- Checking if a substring is in `word_set` takes O(k) in the worst case, where k is the length of the substring.
- Overall, the time complexity is O(n^2 * k), where n is the length of `s` and k is the average length of words in `wordDict`.

Space Complexity:
- The `dp` array takes O(n) space, where n is the length of `s`.
- The `word_set` takes O(m * k) space, where m is the number of words in `wordDict` and k is the average length of the words.
- Overall, the space complexity is O(n + m * k).
"""

# Topic: Dynamic Programming (DP)