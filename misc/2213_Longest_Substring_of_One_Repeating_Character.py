"""
LeetCode Problem #2213: Longest Substring of One Repeating Character

Problem Statement:
You are given a string `s` and a list of queries `queryCharacters` and `queryIndices`, both of length `n`. 
You want to perform `n` queries on the string `s`.

For the ith query, you replace the character at index `queryIndices[i]` with `queryCharacters[i]`.

Return an array `result` of length `n` where `result[i]` is the length of the longest substring of one repeating character 
in the string `s` after the ith query is performed.

Example:
Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1, 3, 3]
Output: [3, 3, 4]

Explanation:
- After applying the 1st query, the string becomes "bbbacc". The longest substring is "bbb" with length 3.
- After applying the 2nd query, the string becomes "bbbccc". The longest substring is "bbb" or "ccc" with length 3.
- After applying the 3rd query, the string becomes "bbbbcc". The longest substring is "bbbb" with length 4.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- n == queryCharacters.length == queryIndices.length
- 1 <= n <= 10^4
- queryCharacters consists of lowercase English letters.
- 0 <= queryIndices[i] < s.length
"""

# Solution
from sortedcontainers import SortedList

def longestRepeating(s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
    # Helper function to update the intervals
    def update_intervals(index, char):
        nonlocal max_length
        # Remove the current interval containing index
        left, right = intervals[index]
        max_length = max_length - (right - left + 1)
        del intervals[index]
        
        # Split into new intervals
        if left < index:
            intervals[left] = index - 1
            max_length = max(max_length, index - left)
        if index < right:
            intervals[index + 1] = right
            max_length = max(max_length, right - index)
        
        # Merge with left and right intervals if possible
        if index > left and s[index - 1] == char:
            left = index - 1