"""
LeetCode Problem #504: Base 7

Problem Statement:
Given an integer num, return a string representing its base 7 representation.

Example 1:
Input: num = 100
Output: "202"

Example 2:
Input: num = -7
Output: "-10"

Constraints:
- -10^7 <= num <= 10^7
"""

def convertToBase7(num: int) -> str:
    """
    Converts an integer to its base 7 representation as a string.

    Args:
    num (int): The integer to convert.

    Returns:
    str: The base 7 representation of the integer.
    """
    if num == 0:
        return "0"
    
    is_negative = num < 0
    num = abs(num)
    base7 = []
    
    while num > 0:
        base7.append(str(num % 7))
        num //= 7
    
    if is_negative:
        base7.append('-')
    
    return ''.join(reversed(base7))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num = 100
    print(convertToBase7(num))  # Output: "202"

    # Test Case 2
    num = -7
    print(convertToBase7(num))  # Output: "-10"

    # Test Case 3
    num = 0
    print(convertToBase7(num))  # Output: "0"

    # Test Case 4
    num = 49
    print(convertToBase7(num))  # Output: "100"

    # Test Case 5
    num = -343
    print(convertToBase7(num))  # Output: "-1000"

"""
Time and Space Complexity Analysis:

Time Complexity:
The time complexity of the solution is O(log7(num)), where num is the absolute value of the input number.
This is because we repeatedly divide the number by 7 until it becomes 0, and the number of divisions is proportional to the logarithm of the number in base 7.

Space Complexity:
The space complexity is O(log7(num)) as well, because we store the digits of the base 7 representation in a list before reversing and joining them into a string.

Topic: Math
"""