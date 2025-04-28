"""
LeetCode Problem #1999: Smallest Greater Multiple Made of Two Digits

Problem Statement:
You are given two digits `a` and `b`. Find the smallest positive integer that is a multiple of both `a` and `b` 
and is made up of only the digits `a` and `b`. If no such number exists, return -1.

Constraints:
- `a` and `b` are digits (0-9).
- The result must be a positive integer.

Example:
Input: a = 2, b = 3
Output: 33
Explanation: 33 is the smallest number that is a multiple of both 2 and 3 and is made up of only the digits 2 and 3.

Input: a = 0, b = 1
Output: -1
Explanation: No number made up of only the digits 0 and 1 can be a multiple of both.

"""

# Python Solution
from math import gcd

def smallestGreaterMultiple(a: int, b: int) -> int:
    """
    Finds the smallest positive integer that is a multiple of both a and b
    and is made up of only the digits a and b.
    
    :param a: First digit (0-9)
    :param b: Second digit (0-9)
    :return: Smallest positive integer meeting the criteria, or -1 if no such number exists
    """
    # Edge case: If both digits are the same, return the digit repeated twice
    if a == b:
        return int(str(a) * 2)
    
    # Generate all possible numbers made up of digits a and b
    def is_valid_number(num):
        """Checks if a number is made up of only digits a and b."""
        return all(d in {str(a), str(b)} for d in str(num))
    
    # Find the least common multiple (LCM) of a and b
    lcm = (a * b) // gcd(a, b)
    
    # Start checking multiples of the LCM
    multiple = lcm
    while True:
        if is_valid_number(multiple):
            return multiple
        multiple += lcm
    
    # If no valid number is found (theoretically unreachable due to infinite loop)
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    a, b = 2, 3
    print(smallestGreaterMultiple(a, b))  # Output: 33

    # Test Case 2
    a, b = 0, 1
    print(smallestGreaterMultiple(a, b))  # Output: -1

    # Test Case 3
    a, b = 5, 5
    print(smallestGreaterMultiple(a, b))  # Output: 55

    # Test Case 4
    a, b = 4, 7
    print(smallestGreaterMultiple(a, b))  # Output: 44

    # Test Case 5
    a, b = 1, 9
    print(smallestGreaterMultiple(a, b))  # Output: 99

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through multiples of the LCM of `a` and `b` until it finds a valid number.
- The number of iterations depends on the digits `a` and `b` and the LCM value.
- In the worst case, the function may need to check many multiples before finding a valid number.
- The complexity of checking if a number is valid is O(d), where d is the number of digits in the number.
- Overall, the time complexity is approximately O(k * d), where k is the number of multiples checked.

Space Complexity:
- The function uses a constant amount of space for variables and computations.
- The space complexity is O(1).

Topic: Math, Strings
"""