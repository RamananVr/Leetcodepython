"""
LeetCode Problem #709: To Lower Case

Problem Statement:
Given a string `s`, return the string after replacing every uppercase letter with the same lowercase letter.

Example 1:
Input: s = "Hello"
Output: "hello"

Example 2:
Input: s = "here"
Output: "here"

Example 3:
Input: s = "LOVELY"
Output: "lovely"

Constraints:
- 1 <= s.length <= 100
- s consists of printable ASCII characters.
"""

# Solution
def toLowerCase(s: str) -> str:
    """
    Converts all uppercase letters in the input string to lowercase.

    :param s: Input string
    :return: String with all uppercase letters converted to lowercase
    """
    return s.lower()

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "Hello"
    print(toLowerCase(s1))  # Expected Output: "hello"

    # Test Case 2
    s2 = "here"
    print(toLowerCase(s2))  # Expected Output: "here"

    # Test Case 3
    s3 = "LOVELY"
    print(toLowerCase(s3))  # Expected Output: "lovely"

    # Test Case 4
    s4 = "Python3.9"
    print(toLowerCase(s4))  # Expected Output: "python3.9"

    # Test Case 5
    s5 = "123ABCdef"
    print(toLowerCase(s5))  # Expected Output: "123abcdef"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `lower()` method in Python iterates through the string once, converting each character to lowercase if needed.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The `lower()` method creates a new string with the converted characters, which requires O(n) space.
- Hence, the space complexity is O(n).

Topic: String Manipulation
"""