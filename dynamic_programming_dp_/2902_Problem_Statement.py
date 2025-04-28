"""
LeetCode Problem #2902: Problem Statement

(Note: As of my knowledge cutoff in October 2023, LeetCode does not have a problem #2902. 
For the purpose of this task, I will create a hypothetical problem statement.)

Problem Statement:
Given a string `s` and a dictionary of words `wordDict`, determine if `s` can be segmented into 
a space-separated sequence of one or more dictionary words.

You may assume that the dictionary does not contain duplicate words.

Example:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: True
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: True
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: False

Constraints:
1. 1 <= len(s) <= 300
2. 1 <= len(wordDict) <= 1000
3. 1 <= len(wordDict[i]) <= 20
4. s and wordDict[i] consist of only lowercase English letters.
"""

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
    print(wordBreak(s1, wordDict1))  # Expected Output: True

    # Test Case 2
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    print(wordBreak(s2, wordDict2))  # Expected Output: True

    # Test Case 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    print(wordBreak(s3, wordDict3))  # Expected Output: False

    # Test Case 4
    s4 = "pineapplepenapple"
    wordDict4 = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(wordBreak(s4, wordDict4))  # Expected Output: True

    # Test Case 5
    s5 = "abcd"
    wordDict5 = ["a", "abc", "b", "cd"]
    print(wordBreak(s5, wordDict5))  # Expected Output: True


"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop runs for `len(s)` iterations.
- The inner loop runs for at most `len(s)` iterations in the worst case.
- Checking if a substring is in `word_set` takes O(k), where k is the length of the substring.
  However, since the total number of characters checked across all iterations is bounded by `len(s)`,
  the overall complexity of substring checks is O(len(s)).
- Therefore, the total time complexity is O(len(s)^2).

Space Complexity:
- The `dp` array takes O(len(s)) space.
- The `word_set` takes O(len(wordDict) * average length of words) space.
- Overall space complexity is O(len(s) + len(wordDict)).

Topic: Dynamic Programming (DP)
"""