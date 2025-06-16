"""
LeetCode Problem #2710: Remove Trailing Zeros From a String

Problem Statement:
Given a positive integer num represented as a string, return the string num with trailing zeros removed.

Constraints:
- 1 <= num.length <= 1000
- num consists of only digits.
- num doesn't have any leading zeros.
"""

def removeTrailingZeros(num):
    """
    Removes trailing zeros from a numeric string.
    
    :param num: str - String representation of a positive integer
    :return: str - String with trailing zeros removed
    """
    # Remove trailing zeros using rstrip
    return num.rstrip('0')

def removeTrailingZerosManual(num):
    """
    Manual implementation without using built-in rstrip.
    
    :param num: str - String representation of a positive integer
    :return: str - String with trailing zeros removed
    """
    # Find the last non-zero character
    end = len(num) - 1
    while end >= 0 and num[end] == '0':
        end -= 1
    
    # Return substring up to the last non-zero character
    return num[:end + 1]

def removeTrailingZerosReverse(num):
    """
    Implementation using reverse iteration.
    
    :param num: str - String representation of a positive integer
    :return: str - String with trailing zeros removed
    """
    result = []
    trailing = True
    
    # Iterate from right to left
    for i in range(len(num) - 1, -1, -1):
        if num[i] != '0' or not trailing:
            result.append(num[i])
            trailing = False
    
    # Reverse the result to get correct order
    return ''.join(reversed(result))

def removeTrailingZerosSlicing(num):
    """
    Implementation using string slicing approach.
    
    :param num: str - String representation of a positive integer
    :return: str - String with trailing zeros removed
    """
    # Find the position where trailing zeros start
    i = len(num) - 1
    while i >= 0 and num[i] == '0':
        i -= 1
    
    # Return the substring without trailing zeros
    return num[:i + 1] if i >= 0 else ""

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num = "51230100"
    print(f"Input: '{num}'")
    print(f"removeTrailingZeros: '{removeTrailingZeros(num)}'")  # Output: "512301"
    print(f"removeTrailingZerosManual: '{removeTrailingZerosManual(num)}'")  # Output: "512301"
    print(f"removeTrailingZerosReverse: '{removeTrailingZerosReverse(num)}'")  # Output: "512301"
    print(f"removeTrailingZerosSlicing: '{removeTrailingZerosSlicing(num)}'")  # Output: "512301"
    print()

    # Test Case 2
    num = "123"
    print(f"Input: '{num}'")
    print(f"removeTrailingZeros: '{removeTrailingZeros(num)}'")  # Output: "123"
    print(f"removeTrailingZerosManual: '{removeTrailingZerosManual(num)}'")  # Output: "123"
    print(f"removeTrailingZerosReverse: '{removeTrailingZerosReverse(num)}'")  # Output: "123"
    print(f"removeTrailingZerosSlicing: '{removeTrailingZerosSlicing(num)}'")  # Output: "123"
    print()

    # Test Case 3
    num = "1000"
    print(f"Input: '{num}'")
    print(f"removeTrailingZeros: '{removeTrailingZeros(num)}'")  # Output: "1"
    print(f"removeTrailingZerosManual: '{removeTrailingZerosManual(num)}'")  # Output: "1"
    print(f"removeTrailingZerosReverse: '{removeTrailingZerosReverse(num)}'")  # Output: "1"
    print(f"removeTrailingZerosSlicing: '{removeTrailingZerosSlicing(num)}'")  # Output: "1"
    print()

    # Test Case 4
    num = "10200"
    print(f"Input: '{num}'")
    print(f"removeTrailingZeros: '{removeTrailingZeros(num)}'")  # Output: "102"
    print(f"removeTrailingZerosManual: '{removeTrailingZerosManual(num)}'")  # Output: "102"
    print(f"removeTrailingZerosReverse: '{removeTrailingZerosReverse(num)}'")  # Output: "102"
    print(f"removeTrailingZerosSlicing: '{removeTrailingZerosSlicing(num)}'")  # Output: "102"
    print()

    # Test Case 5
    num = "9"
    print(f"Input: '{num}'")
    print(f"removeTrailingZeros: '{removeTrailingZeros(num)}'")  # Output: "9"
    print(f"removeTrailingZerosManual: '{removeTrailingZerosManual(num)}'")  # Output: "9"
    print(f"removeTrailingZerosReverse: '{removeTrailingZerosReverse(num)}'")  # Output: "9"
    print(f"removeTrailingZerosSlicing: '{removeTrailingZerosSlicing(num)}'")  # Output: "9"

    # Edge case: all zeros except first digit
    num = "10000"
    print(f"\nEdge case - Input: '{num}'")
    print(f"removeTrailingZeros: '{removeTrailingZeros(num)}'")  # Output: "1"

    # Validation
    assert removeTrailingZeros("51230100") == "512301"
    assert removeTrailingZerosManual("123") == "123"
    assert removeTrailingZerosReverse("1000") == "1"
    assert removeTrailingZerosSlicing("10200") == "102"
    print("All test cases passed!")

"""
Time Complexity Analysis:
Built-in rstrip:
- Time complexity: O(n) where n is the length of the string.

Manual implementations:
- Time complexity: O(n) for all manual approaches.

Space Complexity Analysis:
rstrip method:
- Space complexity: O(n) for creating the result string.

Manual methods:
- Space complexity: O(n) for the result string, O(n) additional for reverse method.

Topic: String Manipulation, String Processing
"""
