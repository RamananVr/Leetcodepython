"""
LeetCode Problem #2549: Count Distinct Numbers on Board

Problem Statement:
You are given a positive integer `n`. Initially, you have a number `n` on a board. 
Every day, you replace the number `x` on the board with `x - gcd(n, x)`, where `gcd(n, x)` 
is the greatest common divisor of `n` and `x`. The process stops when you reach `x = 0`.

Return the number of distinct numbers present on the board throughout the process.

Constraints:
- 1 <= n <= 10^9
"""

# Solution
def countDistinctNumbers(n: int) -> int:
    """
    Returns the number of distinct numbers present on the board throughout the process.
    """
    # The number of distinct numbers is equal to the number of divisors of n.
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1  # i is a divisor
            if i != n // i:
                count += 1  # n // i is also a divisor
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 12
    print(countDistinctNumbers(n))  # Expected Output: 6 (Divisors: 1, 2, 3, 4, 6, 12)

    # Test Case 2
    n = 7
    print(countDistinctNumbers(n))  # Expected Output: 2 (Divisors: 1, 7)

    # Test Case 3
    n = 28
    print(countDistinctNumbers(n))  # Expected Output: 6 (Divisors: 1, 2, 4, 7, 14, 28)

    # Test Case 4
    n = 1
    print(countDistinctNumbers(n))  # Expected Output: 1 (Divisors: 1)

    # Test Case 5
    n = 100
    print(countDistinctNumbers(n))  # Expected Output: 9 (Divisors: 1, 2, 4, 5, 10, 20, 25, 50, 100)

# Time and Space Complexity Analysis
"""
Time Complexity:
- The loop runs up to sqrt(n), and for each divisor found, we perform constant-time operations.
- Therefore, the time complexity is O(sqrt(n)).

Space Complexity:
- We use only a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Math (Number Theory)