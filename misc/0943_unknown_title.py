"""
LeetCode Problem #943: Find the Shortest Superstring

Problem Statement:
Given an array of strings `words`, find the shortest string that contains each string in `words` as a substring. 
If there are multiple valid strings of the shortest length, return any of them.

You may assume that no string in `words` is a substring of another string in `words`.

Constraints:
- 1 <= words.length <= 12
- 1 <= words[i].length <= 20
- words[i] consists of lowercase English letters.

Example:
Input: words = ["alex", "loves", "leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of the strings in words are considered, and the one that results in the shortest superstring is chosen.

"""

from itertools import permutations

def shortestSuperstring(words):
    """
    Finds the shortest superstring that contains all strings in the input list as substrings.

    :param words: List[str] - List of input strings
    :return: str - Shortest superstring
    """
    def overlap(a, b):
        """
        Calculates the maximum overlap between two strings a and b.
        """
        max_overlap = 0
        for i in range(1, len(a) + 1):
            if b.startswith(a[-i:]):
                max_overlap = i
        return max_overlap

    def merge(a, b):
        """
        Merges two strings a and b based on their overlap.
        """
        overlap_len = overlap(a, b)
        return a + b[overlap_len:]

    n = len(words)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dp[i][j] = overlap(words[i], words[j])

    # Use dynamic programming to find the shortest superstring
    from functools import lru_cache

    @lru_cache(None)
    def dfs(mask, last):
        if mask == (1 << n) - 1:
            return "", 0
        ans = float("inf")
        for nxt in range(n):
            if not (mask & (1 << nxt)):
                nxt_str, nxt_cost = dfs(mask | (1 << nxt), nxt)
                nxt_cost += dp[last][nxt]
                if nxt_cost < ans:
                    ans = nxt_cost
                    ans_str = nxt_str

    return ans