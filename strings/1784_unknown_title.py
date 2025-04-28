"""
LeetCode Problem #1784: Check if Binary String Has at Most One Segment of Ones

Problem Statement:
Given a binary string s, return true if the binary string has at most one segment of ones. Otherwise, return false.

A segment of ones is a contiguous substring consisting of only the character '1'.

Example 1:
Input: s = "1001"
Output: false
Explanation: The binary string has two segments of ones: "1" and "1".

Example 2:
Input: s = "110"
Output: true
Explanation: The binary string has one segment of ones: "11".

Constraints:
- 1 <= s.length <= 100
- s[i] is either '0' or '1'.
"""

def checkOnesSegment(s: str) -> bool:
    """
    Function to check if the binary string has at most one segment of ones.

    Args:
    s (str): Binary string consisting of '0' and '1'.

    Returns:
    bool: True if the binary string has at most one segment of ones, False otherwise.
    """
    # A binary string has at most one segment of ones if "01" does not appear in the string.
    return "01" not in s


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "1001"
    print(checkOnesSegment(s1))  # Output: False

    # Test Case 2
    s2 = "110"
    print(checkOnesSegment(s2))  # Output: True

    # Test Case 3
    s3 = "1"
    print(checkOnesSegment(s3))  # Output: True

    # Test Case 4
    s4 = "0"
    print(checkOnesSegment(s4))  # Output: True

    # Test Case 5
    s5 = "111111"
    print(checkOnesSegment(s5))  # Output: True

    # Test Case 6
    s6 = "101010"
    print(checkOnesSegment(s6))  # Output: False


"""
Time and Space Complexity Analysis:

Time Complexity:
- The function checks for the presence of the substring "01" in the binary string `s`.
- This operation takes O(n) time, where n is the length of the string `s`.

Space Complexity:
- The function uses O(1) additional space since no extra data structures are used.

Overall:
Time Complexity: O(n)
Space Complexity: O(1)

Topic: Strings
"""