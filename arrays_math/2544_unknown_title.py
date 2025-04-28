"""
LeetCode Problem #2544: Alternating Digit Sum

Problem Statement:
You are given a positive integer `n`. Each digit of `n` has a sign according to its position:
- The most significant digit is assigned a positive sign.
- Each other digit has an opposite sign to its adjacent digits.

Return the sum of all digits with their corresponding signs.

Example 1:
Input: n = 521
Output: 4
Explanation: (+5) + (-2) + (+1) = 4.

Example 2:
Input: n = 111
Output: 1
Explanation: (+1) + (-1) + (+1) = 1.

Example 3:
Input: n = 886996
Output: 0
Explanation: (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.

Constraints:
- 1 <= n <= 10^9
"""

def alternateDigitSum(n: int) -> int:
    """
    Calculate the alternating digit sum of a given positive integer n.

    :param n: A positive integer
    :return: The alternating digit sum
    """
    # Convert the number to a string to process each digit
    digits = list(map(int, str(n)))
    # Initialize the result
    result = 0
    # Iterate through the digits with their indices
    for i, digit in enumerate(digits):
        # Add or subtract the digit based on its position
        if i % 2 == 0:  # Even index (0-based) -> positive sign
            result += digit
        else:           # Odd index -> negative sign
            result -= digit
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 521
    print(f"Input: {n1}, Output: {alternateDigitSum(n1)}")  # Expected Output: 4

    # Test Case 2
    n2 = 111
    print(f"Input: {n2}, Output: {alternateDigitSum(n2)}")  # Expected Output: 1

    # Test Case 3
    n3 = 886996
    print(f"Input: {n3}, Output: {alternateDigitSum(n3)}")  # Expected Output: 0

    # Test Case 4
    n4 = 1
    print(f"Input: {n4}, Output: {alternateDigitSum(n4)}")  # Expected Output: 1

    # Test Case 5
    n5 = 123456789
    print(f"Input: {n5}, Output: {alternateDigitSum(n5)}")  # Expected Output: 5

"""
Time Complexity Analysis:
- Converting the integer `n` to a string takes O(d), where `d` is the number of digits in `n`.
- Iterating through the digits and performing addition/subtraction also takes O(d).
- Therefore, the overall time complexity is O(d), where `d` is the number of digits in `n`.

Space Complexity Analysis:
- The space required to store the digits as a list is O(d), where `d` is the number of digits in `n`.
- Thus, the space complexity is O(d).

Topic: Arrays, Math
"""