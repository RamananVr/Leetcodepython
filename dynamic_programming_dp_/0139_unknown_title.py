"""
LeetCode Problem #139: Word Break

Problem Statement:
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note:
- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

Constraints:
- 1 <= s.length <= 10^4
- 1 <= wordDict.length <= 10^3
- 1 <= wordDict[i].length <= 10^4
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings in `wordDict` are unique.
"""

def wordBreak(s: str, wordDict: list[str]) -> bool:
    """
    Determines if the string `s` can be segmented into a space-separated sequence of one or more dictionary words.

    Args:
    s (str): The input string.
    wordDict (list[str]): The list of valid dictionary words.

    Returns:
    bool: True if `s` can be segmented, False otherwise.
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
    wordDict4 = ["apple", "pen", "pine", "pineapple"]
    print(wordBreak(s4, wordDict4))  # Output: True

    # Test Case 5
    s5 = "abcd"
    wordDict5 = ["a", "abc", "b", "cd"]
    print(wordBreak(s5, wordDict5))  # Output: True


"""
Time Complexity:
- Let `n` be the length of the string `s` and `m` be the maximum length of a word in `wordDict`.
- The outer loop runs `n` times (for each character in `s`).
- The inner loop runs up to `n` times in the worst case.
- Checking if `s[j:i]` is in `word_set` takes O(m) in the worst case (length of the substring).
- Overall time complexity: O(n^2 * m).

Space Complexity:
- The `dp` array takes O(n) space.
- The `word_set` takes O(k) space, where `k` is the total length of all words in `wordDict`.
- Overall space complexity: O(n + k).

Topic: Dynamic Programming (DP)
"""