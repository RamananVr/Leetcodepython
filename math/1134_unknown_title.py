"""
LeetCode Problem #1134: Armstrong Number

Problem Statement:
-------------------
Given an integer `n`, return `true` if and only if it is an Armstrong number.

The k-digit number `n` is an Armstrong number if and only if the `k`-th power of each digit sums to `n`.

Example 1:
Input: n = 153
Output: true
Explanation: 153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.

Example 2:
Input: n = 123
Output: false
Explanation: 123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3.

Constraints:
------------
- 1 <= n <= 10^8
"""

def isArmstrong(n: int) -> bool:
    """
    Determines if a given number `n` is an Armstrong number.

    Args:
    n (int): The input number.

    Returns:
    bool: True if `n` is an Armstrong number, False otherwise.
    """
    # Convert the number to a string to extract its digits
    digits = list(map(int, str(n)))
    # Calculate the number of digits (k)
    k = len(digits)
    # Compute the sum of each digit raised to the power of k
    armstrong_sum = sum(digit ** k for digit in digits)
    # Check if the computed sum equals the original number
    return armstrong_sum == n

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Armstrong number
    n1 = 153
    print(f"Input: {n1}, Output: {isArmstrong(n1)}")  # Expected: True

    # Test Case 2: Not an Armstrong number
    n2 = 123
    print(f"Input: {n2}, Output: {isArmstrong(n2)}")  # Expected: False

    # Test Case 3: Single-digit number (all single-digit numbers are Armstrong numbers)
    n3 = 7
    print(f"Input: {n3}, Output: {isArmstrong(n3)}")  # Expected: True

    # Test Case 4: Large Armstrong number
    n4 = 9474
    print(f"Input: {n4}, Output: {isArmstrong(n4)}")  # Expected: True

    # Test Case 5: Large non-Armstrong number
    n5 = 9475
    print(f"Input: {n5}, Output: {isArmstrong(n5)}")  # Expected: False

"""
Time and Space Complexity Analysis:
-----------------------------------
Time Complexity:
- Let `k` be the number of digits in `n`.
- Converting `n` to a string takes O(k).
- Calculating the sum of each digit raised to the power of `k` involves iterating over the digits (O(k)) and performing a power operation for each digit (O(log(k)) for large numbers). 
  However, since the number of digits is small (at most 8 for n <= 10^8), this is effectively O(k).
- Overall, the time complexity is O(k).

Space Complexity:
- The space required to store the digits of `n` is O(k).
- The space used for intermediate calculations is negligible.
- Overall, the space complexity is O(k).

Topic: Math
"""