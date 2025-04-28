"""
LeetCode Problem #625: Minimum Factorization

Problem Statement:
Given a positive integer `a`, find the smallest positive integer `b` whose multiplication of each digit equals `a`.
If there is no answer or the answer is not fit in a 32-bit signed integer, return 0.

Example 1:
Input: a = 48
Output: 68
Explanation: 6 * 8 = 48

Example 2:
Input: a = 15
Output: 35
Explanation: 3 * 5 = 15

Constraints:
- 1 <= a <= 2^31 - 1
"""

def smallestFactorization(a: int) -> int:
    """
    Finds the smallest positive integer b such that the product of its digits equals a.
    Returns 0 if no such b exists or if b exceeds the 32-bit signed integer limit.
    """
    if a < 10:
        return a  # Single-digit numbers are their own smallest factorization
    
    result = []
    for factor in range(9, 1, -1):  # Start from the largest single-digit factor
        while a % factor == 0:
            result.append(factor)
            a //= factor
    
    if a > 1:  # If a cannot be fully factorized into single-digit numbers
        return 0
    
    # Combine the digits in ascending order to form the smallest number
    result.sort()
    b = int("".join(map(str, result)))
    
    # Check if b fits in a 32-bit signed integer
    return b if b <= 2**31 - 1 else 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    a = 48
    print(smallestFactorization(a))  # Output: 68

    # Test Case 2
    a = 15
    print(smallestFactorization(a))  # Output: 35

    # Test Case 3
    a = 1
    print(smallestFactorization(a))  # Output: 1

    # Test Case 4
    a = 180
    print(smallestFactorization(a))  # Output: 259

    # Test Case 5
    a = 1000000000
    print(smallestFactorization(a))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The loop iterates over factors from 9 to 2, and for each factor, it divides `a` repeatedly until `a` is no longer divisible by the factor.
- In the worst case, the number of divisions is proportional to the number of digits in `a` (log10(a)).
- Therefore, the time complexity is O(log(a)).

Space Complexity:
- The space complexity is O(log(a)) due to the `result` list, which stores the factors of `a`.
- The size of the list is proportional to the number of digits in the factorized representation of `a`.

Topic: Math
"""