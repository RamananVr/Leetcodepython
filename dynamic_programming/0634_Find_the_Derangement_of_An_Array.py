"""
LeetCode Problem #634: Find the Derangement of An Array

Problem Statement:
In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.

Given an integer `n`, find the number of derangements of an array `[1, 2, ..., n]`. Since the answer may be very large, return the answer modulo `10^9 + 7`.

Constraints:
- 1 <= n <= 10^6

Example:
Input: n = 3
Output: 2
Explanation: The derangements of [1, 2, 3] are [2, 3, 1] and [3, 1, 2].
"""

# Solution
def findDerangement(n: int) -> int:
    MOD = 10**9 + 7
    
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    # Use dynamic programming to calculate derangements
    dp = [0] * (n + 1)
    dp[1] = 0
    dp[2] = 1
    
    for i in range(3, n + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % MOD
    
    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    print(findDerangement(n))  # Output: 2

    # Test Case 2
    n = 4
    print(findDerangement(n))  # Output: 9

    # Test Case 3
    n = 5
    print(findDerangement(n))  # Output: 44

    # Test Case 4
    n = 1
    print(findDerangement(n))  # Output: 0

    # Test Case 5
    n = 10
    print(findDerangement(n))  # Output: 133496

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a single loop to calculate the derangements for all values up to `n`. 
- This loop runs in O(n) time, making the time complexity O(n).

Space Complexity:
- The solution uses a list `dp` of size `n + 1` to store intermediate results.
- Thus, the space complexity is O(n).

Topic: Dynamic Programming
"""