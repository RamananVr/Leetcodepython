"""
LeetCode Problem #1869: Longer Contiguous Segments of Ones than Zeros

Problem Statement:
Given a binary string `s`, return `true` if the longest contiguous segment of 1s is strictly greater than the longest contiguous segment of 0s in the string, and `false` otherwise.

A contiguous segment is a substring consisting of consecutive characters of the same value.

Example 1:
Input: s = "1101"
Output: true
Explanation: The longest contiguous segment of 1s is "11" with length 2. The longest contiguous segment of 0s is "0" with length 1. Since 2 > 1, return true.

Example 2:
Input: s = "111000"
Output: false
Explanation: The longest contiguous segment of 1s is "111" with length 3. The longest contiguous segment of 0s is "000" with length 3. Since 3 is not greater than 3, return false.

Example 3:
Input: s = "110100010"
Output: false
Explanation: The longest contiguous segment of 1s is "11" with length 2. The longest contiguous segment of 0s is "000" with length 3. Since 2 is not greater than 3, return false.

Constraints:
- 1 <= s.length <= 100
- s[i] is either '0' or '1'.
"""

# Solution
def checkZeroOnes(s: str) -> bool:
    max_ones = max_zeros = 0
    current_ones = current_zeros = 0

    for char in s:
        if char == '1':
            current_ones += 1
            current_zeros = 0
        else:
            current_zeros += 1
            current_ones = 0

        max_ones = max(max_ones, current_ones)
        max_zeros = max(max_zeros, current_zeros)

    return max_ones > max_zeros

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "1101"
    print(checkZeroOnes(s1))  # Output: True

    # Test Case 2
    s2 = "111000"
    print(checkZeroOnes(s2))  # Output: False

    # Test Case 3
    s3 = "110100010"
    print(checkZeroOnes(s3))  # Output: False

    # Additional Test Case 4
    s4 = "1"
    print(checkZeroOnes(s4))  # Output: True

    # Additional Test Case 5
    s5 = "0"
    print(checkZeroOnes(s5))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the string `s` once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where `n` is the length of the string.

Space Complexity:
- The function uses a constant amount of extra space to store variables (`max_ones`, `max_zeros`, `current_ones`, `current_zeros`).
- Therefore, the space complexity is O(1).

Topic: Strings
"""