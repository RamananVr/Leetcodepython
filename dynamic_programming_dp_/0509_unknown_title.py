"""
LeetCode Problem #509: Fibonacci Number

Problem Statement:
The Fibonacci numbers, commonly denoted F(n), form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Constraints:
- 0 <= n <= 30
"""

# Clean, Correct Python Solution
def fib(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Smallest input
    print(fib(0))  # Expected output: 0

    # Test Case 2: Small input
    print(fib(1))  # Expected output: 1

    # Test Case 3: Small input
    print(fib(2))  # Expected output: 1

    # Test Case 4: Medium input
    print(fib(5))  # Expected output: 5

    # Test Case 5: Larger input
    print(fib(10))  # Expected output: 55

    # Test Case 6: Edge case
    print(fib(30))  # Expected output: 832040

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a loop that iterates from 2 to n (inclusive), so the time complexity is O(n).

Space Complexity:
- The solution uses only two variables (`a` and `b`) to store intermediate Fibonacci numbers, so the space complexity is O(1).

Topic: Dynamic Programming (DP)
"""