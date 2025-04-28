"""
LeetCode Problem #1416: Restore The Array

Problem Statement:
A program was supposed to print an array of integers. The program forgot to print whitespaces, and the array is given as a string `s` and an integer `k`. There can be multiple ways to restore the array.

Given the string `s` and the integer `k`, return the number of possible arrays that can be printed as `s` using the following conditions:
1. The integers in the array must be between 1 and `k` (inclusive).
2. The integers in the array should not contain leading zeros.
3. The array elements are concatenated without any delimiters to form the string `s`.

Since the answer may be large, return it modulo `10^9 + 7`.

Constraints:
- `1 <= s.length <= 10^5`
- `s` consists of only digits and does not contain leading zeros.
- `1 <= k <= 10^9`
"""

# Python Solution
def numOfArrays(s: str, k: int) -> int:
    MOD = 10**9 + 7
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: There's one way to restore an empty string.

    for i in range(1, n + 1):
        for j in range(1, min(i, len(str(k))) + 1):  # Limit the length of the substring to the length of k.
            if s[i - j] == '0':  # Skip substrings with leading zeros.
                continue
            num = int(s[i - j:i])  # Extract the substring as an integer.
            if num > k:  # If the number exceeds k, stop further processing.
                break
            dp[i] = (dp[i] + dp[i - j]) % MOD  # Add the number of ways to restore the previous substring.

    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "1000"
    k1 = 10000
    print(numOfArrays(s1, k1))  # Expected Output: 1

    # Test Case 2
    s2 = "1000"
    k2 = 10
    print(numOfArrays(s2, k2))  # Expected Output: 0

    # Test Case 3
    s3 = "1317"
    k3 = 2000
    print(numOfArrays(s3, k3))  # Expected Output: 8

    # Test Case 4
    s4 = "2020"
    k4 = 30
    print(numOfArrays(s4, k4))  # Expected Output: 1

    # Test Case 5
    s5 = "1234567890"
    k5 = 90
    print(numOfArrays(s5, k5))  # Expected Output: 34

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop runs `n` times, where `n` is the length of the string `s`.
- The inner loop runs up to `min(len(str(k)), i)` times for each iteration of the outer loop.
- In the worst case, the inner loop runs up to `log10(k)` times for each character in `s`.
- Therefore, the time complexity is O(n * log10(k)).

Space Complexity:
- The space complexity is O(n) due to the `dp` array of size `n + 1`.

Topic: Dynamic Programming (DP)
"""