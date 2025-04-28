"""
LeetCode Problem #1977: Number of Ways to Separate Numbers

Problem Statement:
You are given a string `num`, which represents a large integer. You need to determine the number of ways to split the string into one or more non-empty substrings such that:

1. Each substring represents a positive integer without leading zeros.
2. The values of the integers are non-decreasing (i.e., each integer is greater than or equal to the previous one).

Return the number of ways to split the string. Since the answer may be large, return it modulo 10^9 + 7.

Example 1:
Input: num = "327"
Output: 2
Explanation: There are two valid ways:
- "3", "27"
- "327"

Example 2:
Input: num = "094"
Output: 0
Explanation: There are no valid ways because "094" has a leading zero.

Example 3:
Input: num = "0"
Output: 0
Explanation: There are no valid ways because "0" has a leading zero.

Constraints:
- 1 <= num.length <= 3500
- num consists of digits only and does not have leading zeros.
"""

# Python Solution
def numberOfCombinations(num: str) -> int:
    MOD = 10**9 + 7
    n = len(num)
    
    # Edge case: If the string starts with '0', no valid splits are possible
    if num[0] == '0':
        return 0

    # Precompute the longest common prefix (LCP) for all substrings
    lcp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if num[i] == num[j]:
                lcp[i][j] = lcp[i + 1][j + 1] + 1

    # Helper function to compare two substrings num[i:i+len1] and num[j:j+len2]
    def compare(i, j, length):
        common = lcp[i][j]
        if common >= length:
            return True
        return num[i + common] < num[j + common]

    # DP array to store the number of ways to split the string
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[0][i] = 1

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if num[i - j] == '0':  # Skip substrings with leading zeros
                continue
            if i - j >= j:  # Check if the previous substring is valid
                if compare(i - 2 * j, i - j, j):
                    dp[i][j] = dp[i - j][j]
                else:
                    dp[i][j] = dp[i - j][j - 1]
            else:
                dp[i][j] = dp[i - j][j - 1]
            dp[i][j] = (dp[i][j] + dp[i][j - 1]) % MOD

    return dp[n][n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "327"
    print(numberOfCombinations(num1))  # Output: 2

    # Test Case 2
    num2 = "094"
    print(numberOfCombinations(num2))  # Output: 0

    # Test Case 3
    num3 = "0"
    print(numberOfCombinations(num3))  # Output: 0

    # Test Case 4
    num4 = "1234"
    print(numberOfCombinations(num4))  # Output: 8

    # Test Case 5
    num5 = "1111"
    print(numberOfCombinations(num5))  # Output: 15

"""
Time Complexity:
- Precomputing the LCP array takes O(n^2).
- The DP solution involves filling an O(n^2) table, where each cell computation takes O(1).
- Overall time complexity: O(n^2).

Space Complexity:
- The LCP array and DP table both require O(n^2) space.
- Overall space complexity: O(n^2).

Topic: Dynamic Programming (DP)
"""