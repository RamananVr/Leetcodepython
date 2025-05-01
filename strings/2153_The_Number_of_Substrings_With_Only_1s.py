"""
LeetCode Problem #2153: "The Number of Substrings With Only 1s"

Problem Statement:
Given a binary string `s`, return the number of substrings with all characters equal to '1'. 
Since the answer may be too large, return it modulo 10^9 + 7.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "0110111"
Output: 9
Explanation: There are 9 substrings with only 1s: "1", "1", "1", "11", "11", "111", "1", "1".

Example 2:
Input: s = "101"
Output: 2
Explanation: Substrings with only 1s are "1", "1".

Example 3:
Input: s = "111111"
Output: 21
Explanation: All substrings of "111111" are valid.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either '0' or '1'.
"""

# Python Solution
def numSub(s: str) -> int:
    MOD = 10**9 + 7
    count = 0
    result = 0

    for char in s:
        if char == '1':
            count += 1
            result += count
        else:
            count = 0

    return result % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "0110111"
    print(numSub(s1))  # Output: 9

    # Test Case 2
    s2 = "101"
    print(numSub(s2))  # Output: 2

    # Test Case 3
    s3 = "111111"
    print(numSub(s3))  # Output: 21

    # Test Case 4
    s4 = "0"
    print(numSub(s4))  # Output: 0

    # Test Case 5
    s5 = "1"
    print(numSub(s5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the string `s` once, performing O(1) operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The solution uses a constant amount of extra space (variables `count`, `result`, and `MOD`).
- Therefore, the space complexity is O(1).
"""

# Topic: Strings