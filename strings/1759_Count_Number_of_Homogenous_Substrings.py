"""
LeetCode Problem #1759: Count Number of Homogenous Substrings

Problem Statement:
Given a string `s`, return the number of homogenous substrings of `s`. 
Since the answer may be too large, return it modulo 10^9 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a" appears 2 times.
"aa" appears 1 time.
"b" appears 2 times.
"bb" appears 1 time.
"c" appears 3 times.
"cc" appears 2 times.
"ccc" appears 1 time.
Total count = 2 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

Example 2:
Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".

Example 3:
Input: s = "zzzzz"
Output: 15

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase letters.

"""

# Python Solution
def countHomogenous(s: str) -> int:
    MOD = 10**9 + 7
    count = 0
    current_char = s[0]
    current_length = 0

    for char in s:
        if char == current_char:
            current_length += 1
        else:
            count += (current_length * (current_length + 1)) // 2
            current_char = char
            current_length = 1

    # Add the last group
    count += (current_length * (current_length + 1)) // 2

    return count % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abbcccaa"
    print(countHomogenous(s1))  # Output: 13

    # Test Case 2
    s2 = "xy"
    print(countHomogenous(s2))  # Output: 2

    # Test Case 3
    s3 = "zzzzz"
    print(countHomogenous(s3))  # Output: 15

    # Test Case 4
    s4 = "a"
    print(countHomogenous(s4))  # Output: 1

    # Test Case 5
    s5 = "abc"
    print(countHomogenous(s5))  # Output: 3

"""
Time Complexity Analysis:
- The algorithm iterates through the string `s` once, making it O(n), where `n` is the length of the string.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space, making it O(1).

Topic: Strings
"""