"""
LeetCode Problem #1844: Replace All Digits with Characters

Problem Statement:
You are given a 0-indexed string `s` that has lowercase English letters in its even indices 
and digits in its odd indices.

There is a function `shift(c, x)`, where `c` is a character and `x` is a digit, that shifts 
`c` forward by `x` positions in the alphabet. For example, `shift('a', 5) = 'f'` and 
`shift('x', 0) = 'x'`.

For every odd index `i`, you want to replace the digit `s[i]` with `shift(s[i-1], int(s[i]))`.

Return `s` after replacing all digits. It is guaranteed that `shift(s[i-1], int(s[i]))` will 
never exceed 'z'.

Example 1:
Input: s = "a1c1e1"
Output: "abcdef"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a', 1) = 'b'
- s[3] -> shift('c', 1) = 'd'
- s[5] -> shift('e', 1) = 'f'

Example 2:
Input: s = "a1b2c3d4e"
Output: "abbdcfdhe"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a', 1) = 'b'
- s[3] -> shift('b', 2) = 'd'
- s[5] -> shift('c', 3) = 'f'
- s[7] -> shift('d', 4) = 'h'

Constraints:
- 1 <= s.length <= 100
- `s` consists only of lowercase English letters and digits.
- `s` has even indices as letters and odd indices as digits.
"""

# Python Solution
def replaceDigits(s: str) -> str:
    def shift(c: str, x: int) -> str:
        return chr(ord(c) + x)
    
    result = list(s)
    for i in range(1, len(s), 2):
        result[i] = shift(result[i - 1], int(result[i]))
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "a1c1e1"
    print(replaceDigits(s1))  # Output: "abcdef"

    # Test Case 2
    s2 = "a1b2c3d4e"
    print(replaceDigits(s2))  # Output: "abbdcfdhe"

    # Test Case 3
    s3 = "x5y0z9"
    print(replaceDigits(s3))  # Output: "x5y0z9"

    # Test Case 4
    s4 = "a0b0c0"
    print(replaceDigits(s4))  # Output: "aabbcc"

# Time and Space Complexity Analysis
# Time Complexity: O(n), where n is the length of the string `s`. We iterate through the string once, 
# and the `shift` function operates in O(1) time.
# Space Complexity: O(n), where n is the length of the string `s`. This is due to the creation of the 
# `result` list, which stores the modified characters.

# Topic: Strings