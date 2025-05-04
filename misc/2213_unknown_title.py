"""
LeetCode Problem #2213: Longest Substring of One Repeating Character

Problem Statement:
You are given a string `s` and a list of queries `queryCharacters` and `queryIndices` where the `i-th` query updates the character at index `queryIndices[i]` in the string `s` to `queryCharacters[i]`.

Return an array `result` where `result[i]` is the length of the longest substring of one repeating character in the string after the `i-th` query is performed.

Example:
Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1, 3, 3]
Output: [3, 3, 4]

Constraints:
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.
- `1 <= queryCharacters.length == queryIndices.length <= 10^4`
- `queryCharacters` consists of lowercase English letters.
- `0 <= queryIndices[i] < s.length`
"""

from sortedcontainers import SortedList

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        # Helper function to update the intervals
        def update_intervals(index, char):
            nonlocal max_length
            # Remove the current interval containing index
            left, right = intervals[index]
            max_length = max(max_length, 
            )
        pass

# Example Test Cases
s = Solution()
print(s.longestRepeating("babacc", "bcb", [1, 3, 3]))  # Output: [3, 3, 4]

# Time Complexity Analysis:
# Space Complexity Analysis:

# Topic: