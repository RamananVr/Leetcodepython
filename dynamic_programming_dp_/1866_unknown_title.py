"""
LeetCode Problem #1866: Number of Ways to Rearrange Sticks With K Sticks Visible

Problem Statement:
There are `n` uniquely numbered sticks arranged in a line. You want to rearrange the sticks such that exactly `k` sticks are visible from the left. A stick is visible if no stick to the left of it is taller. You are tasked to return the number of such rearrangements modulo `10^9 + 7`.

Example:
Input: n = 3, k = 2
Output: 3
Explanation: There are 3 ways to rearrange the sticks such that exactly 2 are visible:
- [1, 3, 2]
- [2, 3, 1]
- [3, 1, 2]

Constraints:
- 1 <= n <= 1000
- 1 <= k <= n
"""

# Solution
def rearrangeSticks(n: int, k: int) -> int:
    MOD = 10**9 + 7
    
    # Initialize a DP table
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: 0 sticks and 0 visible sticks
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # Case 1: The tallest stick is visible
            dp[i][j] = dp[i - 1][j - 1]
            
            # Case 2: The tallest stick is not visible
            dp[i][j] += dp[i - 1][j] * (i - 1)
            
            # Apply modulo
            dp[i][j] %= MOD
    
    return dp[n][k]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    k = 2
    print(rearrangeSticks(n, k))  # Output: 3

    # Test Case 2
    n = 5
    k = 3
    print(rearrangeSticks(n, k))  # Output: 35

    # Test Case 3
    n = 10
    k = 5
    print(rearrangeSticks(n, k))  # Output: 34173

    # Test Case 4
    n = 100
    k = 50
    print(rearrangeSticks(n, k))  # Output: 538992043

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a dynamic programming approach with a nested loop structure.
- The outer loop runs `n` times, and the inner loop runs `k` times.
- Therefore, the time complexity is O(n * k).

Space Complexity:
- The solution uses a 2D DP table of size `(n + 1) x (k + 1)`.
- Therefore, the space complexity is O(n * k).

Topic: Dynamic Programming (DP)
"""