"""
LeetCode Problem #1278: Palindrome Partitioning III

Problem Statement:
You are given a string `s` and an integer `k`. You need to divide the string into `k` non-empty substrings such that the sum of the number of characters needed to be changed in each substring to make it a palindrome is minimized.

Return the minimized sum.

Example:
Input: s = "abc", k = 2
Output: 1
Explanation: Divide the string into "ab" and "c". Change "b" to "a" in the first substring to make it a palindrome.

Constraints:
1 <= k <= len(s) <= 100
s consists of lowercase English letters.
"""

# Solution
def palindromePartition(s: str, k: int) -> int:
    # Helper function to calculate the cost of converting a substring into a palindrome
    def palindrome_cost(start: int, end: int) -> int:
        cost = 0
        while start < end:
            if s[start] != s[end]:
                cost += 1
            start += 1
            end -= 1
        return cost

    n = len(s)
    # Precompute the cost of converting every substring into a palindrome
    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            cost[i][j] = palindrome_cost(i, j)

    # DP array: dp[i][j] represents the minimum cost to divide the first i characters into j substrings
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # Base case: 0 cost to divide an empty string into 0 substrings

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for p in range(i):  # Try dividing at every possible position
                dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost[p][i - 1])

    return dp[n][k]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1, k1 = "abc", 2
    print(palindromePartition(s1, k1))  # Output: 1

    # Test Case 2
    s2, k2 = "aabbc", 3
    print(palindromePartition(s2, k2))  # Output: 0

    # Test Case 3
    s3, k3 = "leetcode", 2
    print(palindromePartition(s3, k3))  # Output: 2

    # Test Case 4
    s4, k4 = "racecar", 1
    print(palindromePartition(s4, k4))  # Output: 0

    # Test Case 5
    s5, k5 = "abcde", 5
    print(palindromePartition(s5, k5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the palindrome cost for all substrings takes O(n^2) time.
- The DP solution involves three nested loops: one for the length of the string (n), one for the number of partitions (k), and one for the possible split points (n). This results in O(n^2 * k) time complexity.
- Overall time complexity: O(n^2 + n^2 * k) = O(n^2 * k).

Space Complexity:
- The `cost` array requires O(n^2) space.
- The `dp` array requires O(n * k) space.
- Overall space complexity: O(n^2 + n * k).

Topic: Dynamic Programming (DP)
"""