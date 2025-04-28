"""
LeetCode Problem #1259: Handshakes That Don't Cross

Problem Statement:
You are given an even number of people `n` that stand around a circle and each person shakes hands with another person, 
so that there are `n / 2` handshakes total.

Return the number of ways these handshakes can occur such that none of the handshakes cross.

Since the answer may be very large, return the answer modulo 10^9 + 7.

Example 1:
Input: n = 2
Output: 1
Explanation: There is only one way to do a handshake without crossing: [(1, 2)].

Example 2:
Input: n = 4
Output: 2
Explanation: There are two ways to do a handshake without crossing: [(1, 2), (3, 4)] and [(1, 4), (2, 3)].

Constraints:
- 1 <= n <= 1000
- n is even.

"""

# Python Solution
def numberOfWays(n: int) -> int:
    MOD = 10**9 + 7

    # Dynamic Programming array to store the number of ways for each even number of people
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: 0 people, 1 way (no handshakes)

    # Fill the DP array
    for i in range(2, n + 1, 2):  # Only even numbers
        for j in range(0, i, 2):
            dp[i] += dp[j] * dp[i - j - 2]
            dp[i] %= MOD  # Take modulo to prevent overflow

    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 2
    print(f"Input: n = {n1}, Output: {numberOfWays(n1)}")  # Expected Output: 1

    # Test Case 2
    n2 = 4
    print(f"Input: n = {n2}, Output: {numberOfWays(n2)}")  # Expected Output: 2

    # Test Case 3
    n3 = 6
    print(f"Input: n = {n3}, Output: {numberOfWays(n3)}")  # Expected Output: 5

    # Test Case 4
    n4 = 8
    print(f"Input: n = {n4}, Output: {numberOfWays(n4)}")  # Expected Output: 14

    # Test Case 5
    n5 = 10
    print(f"Input: n = {n5}, Output: {numberOfWays(n5)}")  # Expected Output: 42

"""
Time Complexity:
- The outer loop runs for all even numbers up to `n`, which is O(n/2) = O(n).
- The inner loop runs for each even number `i`, iterating up to `i/2` times in the worst case.
- Thus, the total time complexity is O(n^2).

Space Complexity:
- The space complexity is O(n) due to the DP array.

Topic: Dynamic Programming
"""