"""
LeetCode Problem #1811: Find All Valid Pickup and Delivery Options

Problem Statement:
Given n orders, each order consists of a pickup and a delivery service. 
We need to find all the valid pickup and delivery sequences such that delivery(i) is always after pickup(i). 
Since the answer may be too large, return it modulo 10^9 + 7.

A valid sequence should satisfy the following conditions:
1. For every pickup(i), there is a corresponding delivery(i) that occurs after it.
2. No delivery(i) can occur before its corresponding pickup(i).

You are given an integer n, the number of orders. Return the number of valid sequences modulo 10^9 + 7.

Constraints:
- 1 <= n <= 500
"""

# Python Solution
def countOrders(n: int) -> int:
    MOD = 10**9 + 7
    result = 1
    for i in range(1, n + 1):
        result = result * i * (2 * i - 1) % MOD
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 1
    print(f"Number of valid sequences for n={n1}: {countOrders(n1)}")  # Expected: 1

    # Test Case 2
    n2 = 2
    print(f"Number of valid sequences for n={n2}: {countOrders(n2)}")  # Expected: 6

    # Test Case 3
    n3 = 3
    print(f"Number of valid sequences for n={n3}: {countOrders(n3)}")  # Expected: 90

    # Test Case 4
    n4 = 4
    print(f"Number of valid sequences for n={n4}: {countOrders(n4)}")  # Expected: 2520

# Time and Space Complexity Analysis
"""
Time Complexity:
The solution iterates through numbers from 1 to n, performing constant-time operations for each iteration.
Thus, the time complexity is O(n).

Space Complexity:
The solution uses a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Dynamic Programming, Combinatorics