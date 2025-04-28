"""
LeetCode Problem #2060: Check if an Original String Exists Given Two Encoded Strings

Problem Statement:
An original string, `original`, is encoded using a non-empty string `s1` and a non-empty string `s2` to form two encoded strings. The encoding process involves replacing some substrings of `original` with their respective lengths. For example, the string "ab" can be encoded as "2" (its length), "a1", "1b", or "ab" (no replacement).

Given two encoded strings `s1` and `s2`, return `True` if there exists an original string that could be encoded as both `s1` and `s2`. Otherwise, return `False`.

Constraints:
- `1 <= s1.length, s2.length <= 40`
- `s1` and `s2` consist of only digits and lowercase English letters.

Example:
Input: s1 = "a2", s2 = "1a1"
Output: True
Explanation: The original string "aaa" can be encoded as "a2" (replace "aa" with "2") and "1a1" (replace the first "a" with "1" and the last "a" with "1").

Input: s1 = "a", s2 = "2"
Output: False
Explanation: There is no original string that can be encoded as both "a" and "2".
"""

# Solution
def possibly_equals(s1: str, s2: str) -> bool:
    from functools import lru_cache

    @lru_cache(None)
    def dfs(i, j, diff):
        """
        i: current index in s1
        j: current index in s2
        diff: difference in length between the decoded strings so far
        """
        if i == len(s1) and j == len(s2):
            return diff == 0

        if i < len(s1) and s1[i].isdigit():
            num = 0
            for k in range(i, len(s1)):
                if s1[k].isdigit():
                    num = num * 10 + int(s1[k])
                    if dfs(k + 1, j, diff - num):
                        return True
                else:
                    break

        if j < len(s2) and s2[j].isdigit():
            num = 0
            for k in range(j, len(s2)):
                if s2[k].isdigit():
                    num = num * 10 + int(s2[k])
                    if dfs(i, k + 1, diff + num):
                        return True
                else:
                    break

        if i < len(s1) and j < len(s2) and not s1[i].isdigit() and not s2[j].isdigit():
            if s1[i] == s2[j]:
                return dfs(i + 1, j + 1, diff)

        if diff > 0 and i < len(s1) and not s1[i].isdigit():
            return dfs(i + 1, j, diff - 1)

        if diff < 0 and j < len(s2) and not s2[j].isdigit():
            return dfs(i, j + 1, diff + 1)

        return False

    return dfs(0, 0, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "a2"
    s2 = "1a1"
    print(possibly_equals(s1, s2))  # Output: True

    # Test Case 2
    s1 = "a"
    s2 = "2"
    print(possibly_equals(s1, s2))  # Output: False

    # Test Case 3
    s1 = "3x2x"
    s2 = "5x"
    print(possibly_equals(s1, s2))  # Output: True

    # Test Case 4
    s1 = "10a"
    s2 = "a10"
    print(possibly_equals(s1, s2))  # Output: True

    # Test Case 5
    s1 = "a1b2"
    s2 = "2a2"
    print(possibly_equals(s1, s2))  # Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function uses a depth-first search (DFS) approach with memoization.
- The number of states is bounded by O(len(s1) * len(s2) * max_diff), where max_diff is the maximum possible difference in lengths between the two strings.
- Since max_diff is limited by the constraints (length of s1 and s2), the time complexity is approximately O(n^3), where n is the length of the strings.

Space Complexity:
- The space complexity is determined by the recursion stack and the memoization table.
- The recursion stack depth is O(n), and the memoization table stores O(n^3) states.
- Thus, the space complexity is O(n^3).
"""

# Topic: Dynamic Programming (DP), Depth-First Search (DFS), String Manipulation