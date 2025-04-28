"""
LeetCode Problem #1239: Maximum Length of a Concatenated String with Unique Characters

Problem Statement:
You are given an array of strings `arr`. A string `s` is formed by concatenating a subsequence of `arr` and 
checking if the resulting string contains only unique characters.

Return the maximum possible length of `s`.

Example:
Input: arr = ["un", "iq", "ue"]
Output: 4
Explanation: All possible concatenations are:
- "" (empty string) -> length = 0
- "un" -> length = 2
- "iq" -> length = 2
- "ue" -> length = 2
- "uniq" -> length = 4 (valid, all unique characters)
- "ique" -> length = 4 (valid, all unique characters)
- "unique" -> invalid (repeated characters)
The maximum length is 4.

Constraints:
- 1 <= arr.length <= 16
- 1 <= arr[i].length <= 26
- arr[i] contains only lowercase English letters.
"""

# Python Solution
from typing import List

def maxLength(arr: List[str]) -> int:
    def is_unique(s: str) -> bool:
        """Check if a string has all unique characters."""
        return len(s) == len(set(s))
    
    def backtrack(index: int, current: str) -> int:
        """Backtracking function to explore all subsequences."""
        if not is_unique(current):
            return 0
        
        max_len = len(current)
        for i in range(index, len(arr)):
            max_len = max(max_len, backtrack(i + 1, current + arr[i]))
        return max_len
    
    return backtrack(0, "")

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = ["un", "iq", "ue"]
    print(maxLength(arr1))  # Output: 4

    # Test Case 2
    arr2 = ["cha", "r", "act", "ers"]
    print(maxLength(arr2))  # Output: 6

    # Test Case 3
    arr3 = ["abcdefghijklmnopqrstuvwxyz"]
    print(maxLength(arr3))  # Output: 26

    # Test Case 4
    arr4 = ["aa", "bb"]
    print(maxLength(arr4))  # Output: 0

    # Test Case 5
    arr5 = ["a", "b", "c", "d", "e"]
    print(maxLength(arr5))  # Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The backtracking function explores all possible subsequences of the input array `arr`.
- Since there are 2^n possible subsequences for an array of length `n`, the time complexity is O(2^n).
- For each subsequence, we check if the concatenated string has unique characters, which takes O(k), 
  where `k` is the length of the concatenated string. In the worst case, `k` can be up to 26 (the maximum 
  length of a string in `arr`).
- Overall time complexity: O(2^n * k), where `n` is the length of `arr` and `k` is the maximum length of a string.

Space Complexity:
- The space complexity is determined by the recursion stack depth, which is O(n) in the worst case.
- Additionally, the `current` string used in the backtracking function can grow up to O(k) in size.
- Overall space complexity: O(n + k).

Topic: Backtracking
"""