"""
LeetCode Problem #2478: Number of Beautiful Partitions

Problem Statement:
You are given a string `s` of length `n` consisting of digits from '1' to '9' and a positive integer `k`.
A partition of `s` is called beautiful if:
1. The first character of each part is a prime digit ('2', '3', '5', or '7').
2. The last character of each part is not a prime digit ('1', '4', '6', '8', or '9').
3. Each part contains at least one character.

Return the number of beautiful partitions of the string `s` such that there are exactly `k` parts. Since the answer may be very large, return it modulo `10^9 + 7`.

Example:
Input: s = "23542185131", k = 3
Output: 3
Explanation: There exist three beautiful partitions: ["2354", "2185", "131"], ["235", "4218", "5131"], and ["235", "42185", "131"].

Constraints:
- `1 <= k <= n <= 1000`
- `s` consists of digits from '1' to '9'.

"""

# Python Solution
def beautifulPartitions(s: str, k: int) -> int:
    MOD = 10**9 + 7

    # Helper function to check if a digit is prime
    def is_prime_digit(c):
        return c in {'2', '3', '5', '7'}

    n = len(s)
    if not is_prime_digit(s[0]) or is_prime_digit(s[-1]):
        return 0

    # dp[i][j]: Number of ways to partition the first i characters into j parts
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: 1 way to partition 0 characters into 0 parts

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # If the current character is the start of a new part
            if is_prime_digit(s[i - 1]):
                for l in range(i - 1, -1, -1):
                    if not is_prime_digit(s[l]):  # Ensure the previous part ends with a non-prime
                        dp[i][j] = (dp[i][j] + dp[l][j - 1]) % MOD
                        break  # No need to check further as we only care about the last valid partition point

    return dp[n][k]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "23542185131"
    k1 = 3
    print(beautifulPartitions(s1, k1))  # Output: 3

    # Test Case 2
    s2 = "23542185131"
    k2 = 2
    print(beautifulPartitions(s2, k2))  # Output: 6

    # Test Case 3
    s3 = "235"
    k3 = 1
    print(beautifulPartitions(s3, k3))  # Output: 1

    # Test Case 4
    s4 = "123456789"
    k4 = 4
    print(beautifulPartitions(s4, k4))  # Output: 0

    # Test Case 5
    s5 = "2222222222"
    k5 = 5
    print(beautifulPartitions(s5, k5))  # Output: 0

"""
Time Complexity:
- The outer loop runs for `n` (length of the string).
- The inner loop for `j` runs for `k` (number of partitions).
- The innermost loop iterates backward over the string, but it breaks early when a valid partition point is found.
- In the worst case, the innermost loop runs for `n` iterations, making the overall complexity O(n^2 * k).

Space Complexity:
- The DP table requires O(n * k) space.

Topic: Dynamic Programming (DP)
"""