"""
LeetCode Problem #434: Number of Segments in a String

Problem Statement:
You are given a string `s`, return the number of segments in the string. 

A segment is defined to be a contiguous sequence of non-space characters.

Example 1:
Input: s = "Hello, my name is John"
Output: 5

Example 2:
Input: s = "Hello"
Output: 1

Example 3:
Input: s = "love live! mu'sic forever"
Output: 4

Example 4:
Input: s = ""
Output: 0

Constraints:
- 0 <= s.length <= 300
- s consists of lowercase and uppercase English letters, digits, or special characters.
- The only space character in `s` is ' '.
"""

# Solution
def countSegments(s: str) -> int:
    """
    This function counts the number of segments in a given string `s`.
    A segment is defined as a contiguous sequence of non-space characters.
    
    :param s: Input string
    :return: Number of segments in the string
    """
    # Split the string by spaces and filter out empty strings
    return len(s.split())

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "Hello, my name is John"
    print(countSegments(s1))  # Output: 5

    # Test Case 2
    s2 = "Hello"
    print(countSegments(s2))  # Output: 1

    # Test Case 3
    s3 = "love live! mu'sic forever"
    print(countSegments(s3))  # Output: 4

    # Test Case 4
    s4 = ""
    print(countSegments(s4))  # Output: 0

    # Test Case 5
    s5 = "    "
    print(countSegments(s5))  # Output: 0

    # Test Case 6
    s6 = "   Hello   world   "
    print(countSegments(s6))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting the string `s` by spaces takes O(n), where `n` is the length of the string.
- Filtering out empty strings and counting the segments is O(k), where `k` is the number of segments.
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(k), where `k` is the number of segments created by splitting the string.
- In the worst case, if the string has no spaces, the space complexity is O(n).
"""

# Topic: Strings