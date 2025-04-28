"""
LeetCode Problem #415: Add Strings

Problem Statement:
Given two non-negative integers, num1 and num2 represented as strings, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as Python's `int`) and without directly converting the inputs to integers.

Constraints:
- 1 <= num1.length, num2.length <= 10^4
- num1 and num2 consist of only digits.
- num1 and num2 don't have any leading zeros except for the number 0 itself.
"""

def addStrings(num1: str, num2: str) -> str:
    """
    Adds two non-negative integers represented as strings and returns the result as a string.
    """
    i, j = len(num1) - 1, len(num2) - 1  # Pointers for num1 and num2
    carry = 0  # Initialize carry
    result = []  # List to store the result digits

    # Process both strings from the end to the beginning
    while i >= 0 or j >= 0 or carry:
        digit1 = int(num1[i]) if i >= 0 else 0  # Get digit from num1 or 0 if out of bounds
        digit2 = int(num2[j]) if j >= 0 else 0  # Get digit from num2 or 0 if out of bounds

        # Calculate the sum of the digits and the carry
        total = digit1 + digit2 + carry
        carry = total // 10  # Update carry
        result.append(str(total % 10))  # Append the last digit of the sum to the result

        # Move to the next digits
        i -= 1
        j -= 1

    # The result is built in reverse order, so reverse it before returning
    return ''.join(result[::-1])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "11"
    num2 = "123"
    print(addStrings(num1, num2))  # Output: "134"

    # Test Case 2
    num1 = "456"
    num2 = "77"
    print(addStrings(num1, num2))  # Output: "533"

    # Test Case 3
    num1 = "0"
    num2 = "0"
    print(addStrings(num1, num2))  # Output: "0"

    # Test Case 4
    num1 = "999"
    num2 = "1"
    print(addStrings(num1, num2))  # Output: "1000"

    # Test Case 5
    num1 = "1"
    num2 = "9999"
    print(addStrings(num1, num2))  # Output: "10000"

"""
Time Complexity Analysis:
- Let n = max(len(num1), len(num2)).
- The algorithm processes each digit of the two strings once, so the time complexity is O(n).

Space Complexity Analysis:
- The result list stores at most n + 1 digits (including a possible carry), so the space complexity is O(n).

Topic: Strings
"""