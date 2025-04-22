"""
LeetCode Problem #878: Nth Magical Number

Problem Statement:
A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:
Input: n = 1, a = 2, b = 3
Output: 2

Example 2:
Input: n = 4, a = 2, b = 3
Output: 6

Constraints:
- 1 <= n <= 10^9
- 2 <= a, b <= 4 * 10^4
- a and b are coprime (gcd(a, b) == 1)
"""

# Python Solution
from math import gcd

def nthMagicalNumber(n: int, a: int, b: int) -> int:
    MOD = 10**9 + 7
    
    # Calculate the least common multiple (LCM) of a and b
    lcm = a * b // gcd(a, b)
    
    # Binary search to find the nth magical number
    left, right = 1, n * min(a, b)
    while left < right:
        mid = (left + right) // 2
        # Count how many magical numbers are <= mid
        count = mid // a + mid // b - mid // lcm
        if count < n:
            left = mid + 1
        else:
            right = mid
    
    return left % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, a1, b1 = 1, 2, 3
    print(nthMagicalNumber(n1, a1, b1))  # Output: 2

    # Test Case 2
    n2, a2, b2 = 4, 2, 3
    print(nthMagicalNumber(n2, a2, b2))  # Output: 6

    # Test Case 3
    n3, a3, b3 = 5, 2, 4
    print(nthMagicalNumber(n3, a3, b3))  # Output: 10

    # Test Case 4
    n4, a4, b4 = 3, 6, 4
    print(nthMagicalNumber(n4, a4, b4))  # Output: 12

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the LCM takes O(log(min(a, b))) due to the gcd function.
- The binary search runs in O(log(n * min(a, b))) iterations.
- Each iteration of binary search involves calculating the count of magical numbers <= mid, which is O(1).
- Overall time complexity: O(log(min(a, b)) + log(n * min(a, b))).

Space Complexity:
- The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Binary Search
"""