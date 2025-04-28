"""
LeetCode Question #1073: Adding Two Negabinary Numbers

Problem Statement:
Given two numbers arr1 and arr2 in base -2, return the result of adding the two numbers in the same base (-2).
The numbers are given as arrays of digits, where each digit is either 0 or 1. The input arrays are given in reverse order, 
meaning the least significant digit comes first, and the most significant digit is at the end of the array.

You may assume the input arrays are non-empty.

Example 1:
Input: arr1 = [1,1,1,1,0], arr2 = [1,0,1]
Output: [1,0,0,0,0]

Example 2:
Input: arr1 = [0], arr2 = [0]
Output: [0]

Example 3:
Input: arr1 = [0], arr2 = [1]
Output: [1]

Constraints:
- 1 <= arr1.length, arr2.length <= 1000
- arr1[i] and arr2[i] are 0 or 1
- arr1 and arr2 are given in reverse order
"""

def addNegabinary(arr1, arr2):
    """
    Adds two numbers represented in base -2 and returns the result in base -2.
    """
    i, j = len(arr1) - 1, len(arr2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry != 0:
        digit1 = arr1[i] if i >= 0 else 0
        digit2 = arr2[j] if j >= 0 else 0

        # Sum of current digits and carry
        total = digit1 + digit2 + carry

        # Append the current digit in base -2
        result.append(total % 2)

        # Update carry for base -2
        carry = -(total // 2)

        # Move to the next digits
        i -= 1
        j -= 1

    # Remove leading zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    # Reverse the result to match the required format
    return result[::-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 1, 1, 1, 0]
    arr2 = [1, 0, 1]
    print(addNegabinary(arr1, arr2))  # Output: [1, 0, 0, 0, 0]

    # Test Case 2
    arr1 = [0]
    arr2 = [0]
    print(addNegabinary(arr1, arr2))  # Output: [0]

    # Test Case 3
    arr1 = [0]
    arr2 = [1]
    print(addNegabinary(arr1, arr2))  # Output: [1]

    # Additional Test Case
    arr1 = [1, 0, 0, 1]
    arr2 = [1, 1, 0]
    print(addNegabinary(arr1, arr2))  # Output: [1, 1, 1, 1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the digits of both input arrays, which have lengths `len(arr1)` and `len(arr2)`.
- The loop runs for max(len(arr1), len(arr2)) iterations, so the time complexity is O(max(len(arr1), len(arr2))).

Space Complexity:
- The result array stores the digits of the sum in base -2. In the worst case, the size of the result array is proportional to max(len(arr1), len(arr2)).
- Therefore, the space complexity is O(max(len(arr1), len(arr2))).

Topic: Arrays
"""