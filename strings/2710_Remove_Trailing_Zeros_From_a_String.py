"""
LeetCode Problem #2710: Remove Trailing Zeros From a String

Problem Statement:
Given a string `num` representing a number, return the same number after removing all trailing zeros.

Example 1:
Input: num = "512300"
Output: "5123"
Explanation: The trailing zeros are removed.

Example 2:
Input: num = "123"
Output: "123"
Explanation: There are no trailing zeros to remove.

Example 3:
Input: num = "1000"
Output: "1"
Explanation: The trailing zeros are removed.

Constraints:
- 1 <= num.length <= 1000
- num consists of only digits.
- num does not have leading zeros.
"""

def removeTrailingZeros(num: str) -> str:
    """
    Removes all trailing zeros from the given string representation of a number.

    :param num: A string representing a number.
    :return: A string with all trailing zeros removed.
    """
    return num.rstrip('0')

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "512300"
    print(removeTrailingZeros(num1))  # Output: "5123"

    # Test Case 2
    num2 = "123"
    print(removeTrailingZeros(num2))  # Output: "123"

    # Test Case 3
    num3 = "1000"
    print(removeTrailingZeros(num3))  # Output: "1"

    # Test Case 4
    num4 = "0"
    print(removeTrailingZeros(num4))  # Output: ""

    # Test Case 5
    num5 = "4500000"
    print(removeTrailingZeros(num5))  # Output: "45"

"""
Time Complexity Analysis:
- The `rstrip` method scans the string from the end until it encounters a character that is not '0'.
- In the worst case, it scans the entire string, so the time complexity is O(n), where n is the length of the string.

Space Complexity Analysis:
- The `rstrip` method creates a new string without the trailing zeros, so the space complexity is O(n), where n is the length of the string.

Topic: Strings
"""