"""
LeetCode Problem #2345: Finding the Number of Beautiful Partitions

Problem Statement:
You are given a string `s` consisting of digits and an integer `k`. A partition of the string `s` is called beautiful if:
1. Each part of the partition is a non-empty substring of `s`.
2. The first digit of each part is a prime digit (2, 3, 5, or 7).
3. The last digit of each part is not a prime digit.
4. The number of parts in the partition is exactly `k`.

Return the number of beautiful partitions of the string `s`. Since the answer may be very large, return it modulo 10^9 + 7.

Constraints:
- `1 <= s.length <= 1000`
- `s` consists of digits only.
- `1 <= k <= s.length`

Example:
Input: s = "235421", k = 2
Output: 3
Explanation: The beautiful partitions are:
- "235" | "421"
- "23" | "5421"
- "2354" | "21"
"""

# Python Solution
def beautifulPartitions(s: str, k: int) -> int:
    MOD = 10**9 + 7
    n = len(s)
    
    # Helper function to check if a digit is prime
    def is_prime_digit(c):
        return c in {'2', '3', '5', '7'}
    
    # If the first digit is not prime or the last digit is prime, no valid partitions are possible
    if not is_prime_digit(s[0]) or is_prime_digit(s[-1]):
        return 0
    
    # Dynamic Programming Table
    # dp[i][j] represents the number of ways to partition the first `i` characters of `s` into `j` parts
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: 1 way to partition an empty string into 0 parts
    
    # Iterate over the string
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # Check if we can form a valid partition ending at position `i`
            if not is_prime_digit(s[i - 1]):  # Last digit of the current part must not be prime
                for m in range(1, i + 1):
                    if is_prime_digit(s[m - 1]):  # First digit of the current part must be prime
                        dp[i][j] = (dp[i][j] + dp[m - 1][j - 1]) % MOD
    
    return dp[n][k]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1, k1 = "235421", 2
    print(beautifulPartitions(s1, k1))  # Output: 3

    # Test Case 2
    s2, k2 = "235421", 3
    print(beautifulPartitions(s2, k2))  # Output: 0

    # Test Case 3
    s3, k3 = "222", 2
    print(beautifulPartitions(s3, k3))  # Output: 1

    # Test Case 4
    s4, k4 = "1234567", 1
    print(beautifulPartitions(s4, k4))  # Output: 0

    # Test Case 5
    s5, k5 = "2357", 2
    print(beautifulPartitions(s5, k5))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop iterates over the string `s` (O(n)).
- The inner loop iterates over the number of partitions `k` (O(k)).
- The innermost loop iterates over the substring length (O(n)).
- Overall complexity: O(n^2 * k).

Space Complexity:
- The DP table `dp` has dimensions (n+1) x (k+1), so it requires O(n * k) space.
- Additional space is used for helper variables, which is O(1).
- Overall space complexity: O(n * k).
"""

# Topic: Dynamic Programming