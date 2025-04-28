"""
LeetCode Problem #397: Integer Replacement

Problem Statement:
Given a positive integer `n`, you can perform any of the following operations:
1. If `n` is even, replace `n` with `n / 2`.
2. If `n` is odd, you can replace `n` with either `n + 1` or `n - 1`.

Return the minimum number of operations needed for `n` to become 1.

Constraints:
- 1 <= n <= 2^31 - 1
"""

def integerReplacement(n: int) -> int:
    """
    This function calculates the minimum number of operations required to reduce
    the given integer `n` to 1 using the specified rules.
    """
    # Use a dictionary to memoize results for previously computed values
    memo = {}

    def helper(x):
        # Base case: if x is 1, no operations are needed
        if x == 1:
            return 0
        # Check if the result is already memoized
        if x in memo:
            return memo[x]
        # If x is even, divide by 2
        if x % 2 == 0:
            memo[x] = 1 + helper(x // 2)
        else:
            # If x is odd, try both x + 1 and x - 1, and take the minimum
            memo[x] = 1 + min(helper(x + 1), helper(x - 1))
        return memo[x]

    return helper(n)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 8
    print(f"Minimum operations to reduce {n1} to 1: {integerReplacement(n1)}")  # Expected: 3

    # Test Case 2
    n2 = 7
    print(f"Minimum operations to reduce {n2} to 1: {integerReplacement(n2)}")  # Expected: 4

    # Test Case 3
    n3 = 4
    print(f"Minimum operations to reduce {n3} to 1: {integerReplacement(n3)}")  # Expected: 2

    # Test Case 4
    n4 = 15
    print(f"Minimum operations to reduce {n4} to 1: {integerReplacement(n4)}")  # Expected: 5

    # Test Case 5
    n5 = 1
    print(f"Minimum operations to reduce {n5} to 1: {integerReplacement(n5)}")  # Expected: 0

"""
Time Complexity:
- The time complexity is O(log(n)) because the number of recursive calls is proportional to the number of bits in `n`.
- Each recursive call either halves `n` (for even numbers) or increments/decrements it (for odd numbers), reducing the problem size significantly.

Space Complexity:
- The space complexity is O(log(n)) due to the recursion stack and memoization dictionary, which stores results for up to log(n) unique values.

Topic: Dynamic Programming (DP), Recursion
"""