"""
LeetCode Problem #1837: Sum of Digits in Base K

Problem Statement:
Given an integer `n` (in decimal) and an integer `k`, return the sum of the digits of `n` after converting `n` from decimal to base `k`.

Example 1:
Input: n = 34, k = 6
Output: 9
Explanation: 34 (decimal) in base 6 is "54". 5 + 4 = 9.

Example 2:
Input: n = 10, k = 10
Output: 1
Explanation: 10 (decimal) in base 10 is "10". 1 + 0 = 1.

Constraints:
- 1 <= n <= 100
- 2 <= k <= 10
"""

def sumBase(n: int, k: int) -> int:
    """
    Convert the number `n` from decimal to base `k` and return the sum of its digits.
    """
    # Convert n to base k
    base_k_digits = []
    while n > 0:
        base_k_digits.append(n % k)
        n //= k
    
    # Sum the digits in base k
    return sum(base_k_digits)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, k1 = 34, 6
    print(f"Input: n = {n1}, k = {k1} -> Output: {sumBase(n1, k1)}")  # Expected: 9

    # Test Case 2
    n2, k2 = 10, 10
    print(f"Input: n = {n2}, k = {k2} -> Output: {sumBase(n2, k2)}")  # Expected: 1

    # Test Case 3
    n3, k3 = 7, 2
    print(f"Input: n = {n3}, k = {k3} -> Output: {sumBase(n3, k3)}")  # Expected: 3

    # Test Case 4
    n4, k4 = 100, 10
    print(f"Input: n = {n4}, k = {k4} -> Output: {sumBase(n4, k4)}")  # Expected: 1

    # Test Case 5
    n5, k5 = 42, 5
    print(f"Input: n = {n5}, k = {k5} -> Output: {sumBase(n5, k5)}")  # Expected: 8

"""
Time Complexity:
- The time complexity is O(log_k(n)), where `log_k(n)` is the number of digits in the base `k` representation of `n`.
  This is because we repeatedly divide `n` by `k` until `n` becomes 0.

Space Complexity:
- The space complexity is O(log_k(n)) as well, due to the storage of the digits in the `base_k_digits` list.

Topic: Math, Number Conversion
"""