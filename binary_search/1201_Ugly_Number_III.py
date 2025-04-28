"""
LeetCode Problem #1201: Ugly Number III

Problem Statement:
An integer is called an "ugly number" if it is divisible by any of a, b, or c. Given four integers n, a, b, and c, 
return the nth ugly number.

An ugly number is a positive integer that is divisible by at least one of a, b, or c.

Constraints:
- 1 <= n <= 10^9
- 2 <= a, b, c <= 10^5
- 1 <= a * b * c <= 10^18
- It is guaranteed that the result will be in the range of a 32-bit signed integer (1 to 2^31 - 1).

Example:
Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The first three ugly numbers are 2, 3, and 4.

Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The first four ugly numbers are 2, 3, 4, and 6.

Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The first five ugly numbers are 2, 4, 6, 8, and 10.

Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
Output: 1999999984
"""

# Python Solution
from math import gcd

def nthUglyNumber(n: int, a: int, b: int, c: int) -> int:
    def lcm(x, y):
        """Helper function to calculate Least Common Multiple (LCM)"""
        return x * y // gcd(x, y)
    
    def count_ugly_numbers(x):
        """Helper function to count how many ugly numbers <= x"""
        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(ab, c)
        return (x // a) + (x // b) + (x // c) - (x // ab) - (x // ac) - (x // bc) + (x // abc)
    
    # Binary search to find the nth ugly number
    left, right = 1, 2 * 10**9
    while left < right:
        mid = (left + right) // 2
        if count_ugly_numbers(mid) < n:
            left = mid + 1
        else:
            right = mid
    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n, a, b, c = 3, 2, 3, 5
    print(nthUglyNumber(n, a, b, c))  # Output: 4

    # Test Case 2
    n, a, b, c = 4, 2, 3, 4
    print(nthUglyNumber(n, a, b, c))  # Output: 6

    # Test Case 3
    n, a, b, c = 5, 2, 11, 13
    print(nthUglyNumber(n, a, b, c))  # Output: 10

    # Test Case 4
    n, a, b, c = 1000000000, 2, 217983653, 336916467
    print(nthUglyNumber(n, a, b, c))  # Output: 1999999984

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search runs in O(log(max_value)), where max_value is 2 * 10^9.
- The count_ugly_numbers function involves calculating LCMs and performing arithmetic operations, which are O(1).
- Overall, the time complexity is O(log(max_value)) = O(log(2 * 10^9)) ≈ O(31).

Space Complexity:
- The space complexity is O(1) since we are only using a few variables and no additional data structures.

Topic: Binary Search
"""