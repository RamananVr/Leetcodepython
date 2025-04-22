"""
LeetCode Question #67: Add Binary

Problem Statement:
Given two binary strings `a` and `b`, return their sum as a binary string.

The input strings are guaranteed to be non-empty and contain only the characters '0' and '1'.
The resulting binary string should not contain leading zeros unless the result is "0".

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
- Each string consists only of '0' or '1' characters.
- 1 <= a.length, b.length <= 10^4
- The input strings are guaranteed to be non-empty.
"""

# Solution
def addBinary(a: str, b: str) -> str:
    """
    Adds two binary strings and returns their sum as a binary string.

    :param a: Binary string
    :param b: Binary string
    :return: Sum of the binary strings as a binary string
    """
    # Initialize pointers for both strings and a carry variable
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []

    # Traverse both strings from right to left
    while i >= 0 or j >= 0 or carry:
        # Get the current digit from each string (or 0 if out of bounds)
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        # Calculate the sum of the digits and the carry
        total = digit_a + digit_b + carry
        carry = total // 2  # Update carry (1 if total >= 2, else 0)
        result.append(str(total % 2))  # Append the current binary digit to the result

        # Move to the next digits
        i -= 1
        j -= 1

    # Reverse the result list to get the correct binary string
    return ''.join(result[::-1])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    a = "11"
    b = "1"
    print(addBinary(a, b))  # Output: "100"

    # Test Case 2
    a = "1010"
    b = "1011"
    print(addBinary(a, b))  # Output: "10101"

    # Test Case 3
    a = "0"
    b = "0"
    print(addBinary(a, b))  # Output: "0"

    # Test Case 4
    a = "1111"
    b = "1111"
    print(addBinary(a, b))  # Output: "11110"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the length of the longer string (max(len(a), len(b))).
- Therefore, the time complexity is O(max(len(a), len(b))).

Space Complexity:
- The space complexity is O(max(len(a), len(b))) due to the result list storing the binary digits.
- Additional space is used for the carry variable and temporary variables, but these are constant (O(1)).
"""

# Topic: Strings