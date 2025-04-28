"""
LeetCode Problem #2427: Number of Common Factors

Problem Statement:
Given two positive integers `a` and `b`, return the number of common factors of `a` and `b`.

A common factor of two numbers is an integer that divides both numbers evenly.

Example 1:
Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.

Example 2:
Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1 and 5.

Constraints:
- 1 <= a, b <= 1000
"""

def commonFactors(a: int, b: int) -> int:
    """
    This function calculates the number of common factors of two integers a and b.
    """
    # Find the greatest common divisor (GCD) of a and b
    from math import gcd
    greatest_common_divisor = gcd(a, b)
    
    # Count the number of divisors of the GCD
    count = 0
    for i in range(1, greatest_common_divisor + 1):
        if greatest_common_divisor % i == 0:
            count += 1
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    a1, b1 = 12, 6
    print(f"Input: a = {a1}, b = {b1} -> Output: {commonFactors(a1, b1)}")  # Expected: 4

    # Test Case 2
    a2, b2 = 25, 30
    print(f"Input: a = {a2}, b = {b2} -> Output: {commonFactors(a2, b2)}")  # Expected: 2

    # Test Case 3
    a3, b3 = 100, 10
    print(f"Input: a = {a3}, b = {b3} -> Output: {commonFactors(a3, b3)}")  # Expected: 4

    # Test Case 4
    a4, b4 = 7, 13
    print(f"Input: a = {a4}, b = {b4} -> Output: {commonFactors(a4, b4)}")  # Expected: 1

    # Test Case 5
    a5, b5 = 1, 1
    print(f"Input: a = {a5}, b = {b5} -> Output: {commonFactors(a5, b5)}")  # Expected: 1

"""
Time Complexity:
- Calculating the GCD of two numbers takes O(log(min(a, b))) time.
- Iterating through all divisors of the GCD takes O(sqrt(GCD)) time.
- Therefore, the overall time complexity is O(log(min(a, b)) + sqrt(GCD)).

Space Complexity:
- The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Math
"""