"""
LeetCode Problem #343: Integer Break

Problem Statement:
Given an integer `n`, break it into the sum of at least two positive integers and maximize the product of those integers.
Return the maximum product you can get.

You may assume that `n` is greater than or equal to 2.

Example 1:
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

Constraints:
- 2 <= n <= 58
"""

def integerBreak(n: int) -> int:
    """
    Function to calculate the maximum product of integers that sum up to `n`.
    Uses dynamic programming to solve the problem.
    """
    # Base case: For n = 2, the only valid split is 1 + 1, and the product is 1.
    if n == 2:
        return 1
    if n == 3:
        return 2

    # dp[i] will store the maximum product for integer i
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(1, i):
            # Either split i into j and (i-j), or use the precomputed dp[i-j]
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])

    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 2
    print(f"Input: {n1}, Output: {integerBreak(n1)}")  # Expected Output: 1

    # Test Case 2
    n2 = 10
    print(f"Input: {n2}, Output: {integerBreak(n2)}")  # Expected Output: 36

    # Test Case 3
    n3 = 8
    print(f"Input: {n3}, Output: {integerBreak(n3)}")  # Expected Output: 18

    # Test Case 4
    n4 = 15
    print(f"Input: {n4}, Output: {integerBreak(n4)}")  # Expected Output: 243

    # Test Case 5
    n5 = 58
    print(f"Input: {n5}, Output: {integerBreak(n5)}")  # Expected Output: 1549681956

"""
Time Complexity:
- The outer loop runs from 2 to n, so it iterates n-1 times.
- The inner loop runs from 1 to i-1 for each i, so the total number of iterations is approximately (n^2)/2.
- Thus, the time complexity is O(n^2).

Space Complexity:
- The space complexity is O(n) due to the dp array.

Topic: Dynamic Programming (DP)
"""