"""
LeetCode Problem #1758: Minimum Changes To Make Alternating Binary String

Problem Statement:
You are given a binary string `s` consisting only of the characters '0' and '1'. 
You can change any character in the string to the other character ('0' to '1' or '1' to '0').

Return the minimum number of changes needed to make `s` an alternating binary string.

An alternating binary string is a string where no two adjacent characters are equal. 
For example, "010" and "101" are alternating binary strings, while "0100" and "1011" are not.

Example 1:
Input: s = "0100"
Output: 1
Explanation: We can change the last character to '1' to make the string "0101".

Example 2:
Input: s = "10"
Output: 0
Explanation: The string is already alternating.

Example 3:
Input: s = "1111"
Output: 2
Explanation: We can change the first two characters to make the string "1010" or "0101".

Constraints:
- 1 <= s.length <= 10^4
- s[i] is either '0' or '1'.
"""

# Python Solution
def minOperations(s: str) -> int:
    """
    Calculate the minimum number of changes needed to make the binary string alternating.
    
    :param s: A binary string consisting of '0' and '1'.
    :return: Minimum number of changes required.
    """
    n = len(s)
    # Pattern 1: Alternating starting with '0' -> "010101..."
    changes_pattern1 = 0
    # Pattern 2: Alternating starting with '1' -> "101010..."
    changes_pattern2 = 0
    
    for i in range(n):
        expected_char_pattern1 = '0' if i % 2 == 0 else '1'
        expected_char_pattern2 = '1' if i % 2 == 0 else '0'
        
        if s[i] != expected_char_pattern1:
            changes_pattern1 += 1
        if s[i] != expected_char_pattern2:
            changes_pattern2 += 1
    
    # Return the minimum changes required for either pattern
    return min(changes_pattern1, changes_pattern2)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "0100"
    print(minOperations(s1))  # Output: 1

    # Test Case 2
    s2 = "10"
    print(minOperations(s2))  # Output: 0

    # Test Case 3
    s3 = "1111"
    print(minOperations(s3))  # Output: 2

    # Test Case 4
    s4 = "0000"
    print(minOperations(s4))  # Output: 2

    # Test Case 5
    s5 = "101010"
    print(minOperations(s5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the string `s` once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The function uses a constant amount of extra space (two integer variables for counting changes).
- Therefore, the space complexity is O(1).

Topic: Strings
"""