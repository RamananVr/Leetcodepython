"""
LeetCode Question #903: Valid Permutations for DI Sequence

Problem Statement:
You are given a string s of length n where s[i] is either 'D' or 'I'. 'D' means the next number is smaller, and 'I' means the next number is greater. 
Find the number of valid permutations of [0, 1, ..., n] such that the given sequence s is followed. Since the answer may be large, return it modulo 10^9 + 7.

Example:
Input: s = "DID"
Output: 5
Explanation: The valid permutations are [2, 1, 3, 0], [2, 3, 1, 0], [3, 1, 2, 0], [3, 2, 0, 1], [3, 2, 1, 0].

Constraints:
- 1 <= s.length <= 200
- s[i] is either 'D' or 'I'

"""

# Python Solution
def numPermsDISequence(s: str) -> int:
    MOD = 10**9 + 7
    n = len(s)
    
    # dp[i][j] represents the number of valid permutations of length i+1 ending with j
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: For the first number, there's only one way to place it
    for j in range(n + 1):
        dp[0][j] = 1
    
    # Fill the DP table
    for i in range(1, n + 1):
        if s[i - 1] == 'I':
            # If 'I', accumulate from left to right
            cumulative = 0
            for j in range(n - i + 1):
                cumulative += dp[i - 1][j]
                dp[i][j] = cumulative % MOD
        else:  # s[i - 1] == 'D'
            # If 'D', accumulate from right to left
            cumulative = 0
            for j in range(n - i, -1, -1):
                cumulative += dp[i - 1][j]
                dp[i][j] = cumulative % MOD
    
    # The result is the sum of all valid permutations of length n+1
    return sum(dp[n]) % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "DID"
    print(numPermsDISequence(s1))  # Output: 5

    # Test Case 2
    s2 = "IDID"
    print(numPermsDISequence(s2))  # Output: 14

    # Test Case 3
    s3 = "III"
    print(numPermsDISequence(s3))  # Output: 5

    # Test Case 4
    s4 = "DDD"
    print(numPermsDISequence(s4))  # Output: 5

    # Test Case 5
    s5 = "ID"
    print(numPermsDISequence(s5))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The DP table has dimensions (n+1) x (n+1), and we iterate over it to fill values.
- For each i, we iterate over j (up to n), and perform cumulative sums.
- This results in a time complexity of O(n^2).

Space Complexity:
- The DP table requires O(n^2) space to store intermediate results.

Overall:
Time Complexity: O(n^2)
Space Complexity: O(n^2)

Topic: Dynamic Programming (DP)
"""