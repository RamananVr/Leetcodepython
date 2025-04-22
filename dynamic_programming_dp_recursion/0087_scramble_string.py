"""
LeetCode Question #87: Scramble String

Problem Statement:
Given two strings `s1` and `s2` of the same length, determine if `s2` is a scrambled string of `s1`.

A scrambled string of a string `s1` is a string that is obtained by recursively dividing the string into two non-empty substrings and swapping them. Specifically, a scrambled string can be formed by:
1. Splitting the string into two non-empty substrings at some index.
2. Recursively applying the same process to the substrings.
3. Swapping the two substrings.

You are required to return `True` if `s2` is a scrambled string of `s1`, otherwise return `False`.

Constraints:
- `s1.length == s2.length`
- `1 <= s1.length <= 30`
- `s1` and `s2` consist of lowercase English letters.

"""

# Solution
def isScramble(s1: str, s2: str) -> bool:
    # Base case: if the strings are equal, they are scrambled versions of each other
    if s1 == s2:
        return True
    
    # If the sorted characters of s1 and s2 don't match, they can't be scrambled versions
    if sorted(s1) != sorted(s2):
        return False
    
    n = len(s1)
    # Try splitting the strings at every possible index
    for i in range(1, n):
        # Case 1: No swap
        if isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:]):
            return True
        # Case 2: Swap
        if isScramble(s1[:i], s2[-i:]) and isScramble(s1[i:], s2[:-i]):
            return True
    
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Scrambled string with swaps
    s1 = "great"
    s2 = "rgeat"
    print(isScramble(s1, s2))  # Expected output: True

    # Test Case 2: Scrambled string with multiple swaps
    s1 = "abcde"
    s2 = "caebd"
    print(isScramble(s1, s2))  # Expected output: False

    # Test Case 3: Identical strings
    s1 = "a"
    s2 = "a"
    print(isScramble(s1, s2))  # Expected output: True

    # Test Case 4: Scrambled string with recursive swaps
    s1 = "abc"
    s2 = "bca"
    print(isScramble(s1, s2))  # Expected output: True

    # Test Case 5: Strings with different characters
    s1 = "abc"
    s2 = "def"
    print(isScramble(s1, s2))  # Expected output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
The function uses recursion to check all possible splits of the strings. For each split, it recursively checks two pairs of substrings. 
The number of splits is proportional to the length of the string, and the recursion depth is also proportional to the length of the string.
Thus, the time complexity is approximately O(n^4), where n is the length of the string.

Space Complexity:
The space complexity is determined by the recursion stack. In the worst case, the recursion depth is proportional to the length of the string.
Thus, the space complexity is O(n), where n is the length of the string.

Topic: Dynamic Programming (DP), Recursion
"""