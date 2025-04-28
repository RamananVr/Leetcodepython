"""
LeetCode Problem #1903: Largest Odd Number in String

Problem Statement:
You are given a string `num`, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of `num`, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: num = "52"
Output: "5"
Explanation: The only odd number in the string is "5".

Example 2:
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in the string.

Example 3:
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.

Constraints:
- 1 <= num.length <= 10^5
- num only consists of digits and does not have leading zeros.
"""

# Solution
def largestOddNumber(num: str) -> str:
    """
    Finds the largest-valued odd integer (as a string) that is a non-empty substring of `num`.
    If no odd integer exists, returns an empty string.
    
    :param num: A string representing a large integer.
    :return: The largest odd integer as a string, or an empty string if no odd integer exists.
    """
    # Traverse the string from the end to find the last odd digit
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 == 1:  # Check if the digit is odd
            return num[:i + 1]  # Return the substring up to the odd digit
    return ""  # No odd digit found, return empty string


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "52"
    print(largestOddNumber(num1))  # Output: "5"

    # Test Case 2
    num2 = "4206"
    print(largestOddNumber(num2))  # Output: ""

    # Test Case 3
    num3 = "35427"
    print(largestOddNumber(num3))  # Output: "35427"

    # Test Case 4
    num4 = "1234567890"
    print(largestOddNumber(num4))  # Output: "123456789"

    # Test Case 5
    num5 = "24680"
    print(largestOddNumber(num5))  # Output: ""


# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the string `num` from the end to the beginning.
- In the worst case, it checks every character in the string once.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The function uses a constant amount of extra space (no additional data structures are used).
- Therefore, the space complexity is O(1).
"""

# Topic: Strings