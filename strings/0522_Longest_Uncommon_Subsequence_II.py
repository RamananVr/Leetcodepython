"""
LeetCode Problem #522: Longest Uncommon Subsequence II

Problem Statement:
Given an array of strings `strs`, return the length of the longest uncommon subsequence among them. 
If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence is a subsequence that is not a subsequence of any other string in the array.

A subsequence of a string `s` is a string that can be obtained after deleting any number of characters 
(possibly zero) from `s`.

Example:
Input: strs = ["aba", "cdc", "eae"]
Output: 3

Constraints:
- 1 <= strs.length <= 50
- 1 <= strs[i].length <= 10
- strs[i] consists of lowercase English letters.
"""

# Solution
from typing import List

def findLUSlength(strs: List[str]) -> int:
    def is_subsequence(s1: str, s2: str) -> bool:
        """Check if s1 is a subsequence of s2."""
        it = iter(s2)
        return all(char in it for char in s1)

    # Sort strings by length in descending order
    strs.sort(key=len, reverse=True)
    
    for i, s1 in enumerate(strs):
        # Check if s1 is not a subsequence of any other string
        if all(not is_subsequence(s1, strs[j]) for j in range(len(strs)) if i != j):
            return len(s1)
    
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    strs1 = ["aba", "cdc", "eae"]
    print(findLUSlength(strs1))  # Output: 3

    # Test Case 2
    strs2 = ["aaa", "aaa", "aa"]
    print(findLUSlength(strs2))  # Output: -1

    # Test Case 3
    strs3 = ["aabbcc", "aabbcc", "cb"]
    print(findLUSlength(strs3))  # Output: 2

    # Test Case 4
    strs4 = ["abcd", "abc", "def"]
    print(findLUSlength(strs4))  # Output: 4

    # Test Case 5
    strs5 = ["a", "b", "c"]
    print(findLUSlength(strs5))  # Output: 1

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Sorting the strings by length: O(n * log(n)), where n is the number of strings.
   - For each string, we check if it is a subsequence of other strings:
     - Checking subsequence takes O(m), where m is the length of the longer string.
     - In the worst case, we compare each string with all other strings, leading to O(n^2 * m).
   - Overall time complexity: O(n^2 * m), where n is the number of strings and m is the average length of the strings.

2. Space Complexity:
   - The space used by the sorting operation is O(n).
   - The subsequence check uses an iterator, which is O(1) space.
   - Overall space complexity: O(n).

Topic: Strings
"""