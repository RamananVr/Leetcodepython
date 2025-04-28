"""
LeetCode Problem #1763: Longest Nice Substring

Problem Statement:
A string `s` is called nice if, for every letter of the alphabet that `s` contains, it appears both in uppercase and lowercase. 
For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, 
but 'B' does not.

Given a string `s`, return the longest substring of `s` that is nice. If there are multiple, return the substring of the 
earliest occurrence. If there are none, return an empty string.

Example 1:
Input: s = "YazaAay"
Output: "aAa"

Example 2:
Input: s = "Bb"
Output: "Bb"

Example 3:
Input: s = "c"
Output: ""

Constraints:
- 1 <= s.length <= 100
- `s` consists of uppercase and lowercase English letters.
"""

def longestNiceSubstring(s: str) -> str:
    """
    Finds the longest nice substring of the given string `s`.
    
    :param s: Input string
    :return: Longest nice substring or an empty string if none exists
    """
    if len(s) < 2:
        return ""
    
    # Check if the string is nice
    char_set = set(s)
    for char in s:
        if char.swapcase() not in char_set:
            # Split the string at the first invalid character
            left = longestNiceSubstring(s[:s.index(char)])
            right = longestNiceSubstring(s[s.index(char) + 1:])
            # Return the longer of the two substrings
            return left if len(left) >= len(right) else right
    
    # If the string is nice, return it
    return s

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "YazaAay"
    print(longestNiceSubstring(s1))  # Output: "aAa"

    # Test Case 2
    s2 = "Bb"
    print(longestNiceSubstring(s2))  # Output: "Bb"

    # Test Case 3
    s3 = "c"
    print(longestNiceSubstring(s3))  # Output: ""

    # Test Case 4
    s4 = "dDzeE"
    print(longestNiceSubstring(s4))  # Output: "dD"

    # Test Case 5
    s5 = "aAaBbCc"
    print(longestNiceSubstring(s5))  # Output: "aAaBbCc"

"""
Time Complexity Analysis:
- Let `n` be the length of the string `s`.
- In the worst case, the function splits the string at every character, leading to a recurrence relation similar to T(n) = 2T(n/2) + O(n).
- This results in a time complexity of O(n^2) in the worst case.

Space Complexity Analysis:
- The space complexity is O(n) due to the recursive call stack.

Topic: Strings, Recursion
"""