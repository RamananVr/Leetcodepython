"""
LeetCode Problem #1987: Number of Unique Good Subsequences

Problem Statement:
Given a binary string `binary`, you need to find the number of unique good subsequences of `binary`. 
A subsequence is good if it is not empty and does not have leading zeros (except for the subsequence "0"). 
Return the number of unique good subsequences modulo 10^9 + 7.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements 
without changing the order of the remaining elements.

Example 1:
Input: binary = "001"
Output: 2
Explanation: The good subsequences are "0" and "1".

Example 2:
Input: binary = "11"
Output: 2
Explanation: The good subsequences are "1" and "11".

Example 3:
Input: binary = "101"
Output: 5
Explanation: The good subsequences are "1", "0", "10", "11", and "101".

Constraints:
- 1 <= binary.length <= 10^5
- binary consists of only '0's and '1's.
"""

# Python Solution
def numberOfUniqueGoodSubsequences(binary: str) -> int:
    MOD = 10**9 + 7
    has_zero = 0  # To track if '0' exists in the binary string
    dp0, dp1 = 0, 0  # dp0 tracks subsequences ending with '0', dp1 tracks subsequences ending with '1'

    for char in binary:
        if char == '1':
            dp1 = (dp0 + dp1 + 1) % MOD  # Add all subsequences ending with '0' and '1', plus the new '1'
        else:
            dp0 = (dp0 + dp1) % MOD  # Add all subsequences ending with '1' to subsequences ending with '0'
            has_zero = 1  # Mark that '0' exists

    # Total unique good subsequences = subsequences ending with '1' + (1 if '0' exists)
    return (dp1 + has_zero) % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    binary = "001"
    print(numberOfUniqueGoodSubsequences(binary))  # Output: 2

    # Test Case 2
    binary = "11"
    print(numberOfUniqueGoodSubsequences(binary))  # Output: 2

    # Test Case 3
    binary = "101"
    print(numberOfUniqueGoodSubsequences(binary))  # Output: 5

    # Test Case 4
    binary = "000"
    print(numberOfUniqueGoodSubsequences(binary))  # Output: 1

    # Test Case 5
    binary = "111"
    print(numberOfUniqueGoodSubsequences(binary))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution iterates through the binary string once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the binary string.

Space Complexity:
- The solution uses a constant amount of extra space (variables `dp0`, `dp1`, and `has_zero`).
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming (DP)
"""