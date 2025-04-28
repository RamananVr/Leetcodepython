"""
LeetCode Problem #521: Longest Uncommon Subsequence I

Problem Statement:
Given two strings `a` and `b`, return the length of the longest uncommon subsequence between them. 
If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence between two strings is a string that is a subsequence of one but not the other.

A subsequence of a string `s` is a string that can be obtained after deleting any number of characters 
(possibly zero) from `s`.

Example:
- "abc" is a subsequence of "aebdc" because you can delete the characters 'e' and 'd'.
- "axc" is not a subsequence of "aebdc".

Constraints:
1. 1 <= a.length, b.length <= 100
2. a and b consist of lower-case English letters.
"""

# Python Solution
def findLUSlength(a: str, b: str) -> int:
    """
    Returns the length of the longest uncommon subsequence between two strings a and b.
    """
    # If the strings are equal, there is no uncommon subsequence
    if a == b:
        return -1
    # Otherwise, the longer string itself is the longest uncommon subsequence
    return max(len(a), len(b))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Strings are different
    a = "abc"
    b = "def"
    print(findLUSlength(a, b))  # Expected Output: 3

    # Test Case 2: Strings are the same
    a = "aaa"
    b = "aaa"
    print(findLUSlength(a, b))  # Expected Output: -1

    # Test Case 3: Strings of different lengths
    a = "abcd"
    b = "abc"
    print(findLUSlength(a, b))  # Expected Output: 4

    # Test Case 4: One string is empty
    a = "abc"
    b = ""
    print(findLUSlength(a, b))  # Expected Output: 3

    # Test Case 5: Both strings are single characters and different
    a = "a"
    b = "b"
    print(findLUSlength(a, b))  # Expected Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution involves a single comparison of the two strings and a length calculation.
- Comparing two strings takes O(min(len(a), len(b))) time, and calculating the length of a string is O(1).
- Therefore, the overall time complexity is O(min(len(a), len(b))).

Space Complexity:
- The solution uses a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Strings