"""
LeetCode Question #639: Decode Ways II

Problem Statement:
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1", 'B' -> "2", ..., 'Z' -> "26".

To decode an encoded message, all the digits must be grouped in valid ways that map to letters. 
For example, "11106" can be mapped into:
- "AAJF" (1 1 10 6)
- "KJF" (11 10 6)

However, the encoded message may also contain the '*' character, which can represent any digit from '1' to '9'.

Given a string `s` containing digits and the '*' character, return the number of ways to decode it. 
Since the answer may be very large, return it modulo 10^9 + 7.

Constraints:
- 1 <= s.length <= 10^5
- `s` contains digits and the '*' character.

Example 1:
Input: s = "*"
Output: 9
Explanation: The '*' can represent any digit from '1' to '9', so there are 9 ways to decode it.

Example 2:
Input: s = "1*"
Output: 18
Explanation: The '*' can represent any digit from '1' to '9'. In this case, there are 9 choices for the '*' and 2 valid pairings: "11" and "1X" (where X is any digit from 1 to 9).

Example 3:
Input: s = "2*"
Output: 15
Explanation: The '*' can represent any digit from '1' to '9'. In this case, there are 9 choices for the '*' and 1 valid pairing: "2X" (where X is any digit from 1 to 6).

"""

# Python Solution
def numDecodings(s: str) -> int:
    MOD = 10**9 + 7
    n = len(s)
    
    # dp[i] represents the number of ways to decode the first i characters of the string
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: empty string has 1 way to decode
    
    # Initialize the first character
    if s[0] == '*':
        dp[1] = 9
    elif s[0] != '0':
        dp[1] = 1
    
    # Iterate through the string
    for i in range(2, n + 1):
        if s[i - 1] == '*':
            dp[i] += dp[i - 1] * 9  # '*' can represent digits 1-9
        elif s[i - 1] != '0':
            dp[i] += dp[i - 1]
        
        # Handle two-character combinations
        if s[i - 2] == '*':
            if s[i - 1] == '*':
                dp[i] += dp[i - 2] * 15  # "**" can represent 11-19 and 21-26
            elif '0' <= s[i - 1] <= '6':
                dp[i] += dp[i - 2] * 2  # "*X" where X is 0-6 can represent 10-16 and 20-26
            else:
                dp[i] += dp[i - 2]  # "*X" where X is 7-9 can represent 17-19
        elif s[i - 2] == '1':
            if s[i - 1] == '*':
                dp[i] += dp[i - 2] * 9  # "1*" can represent 11-19
            else:
                dp[i] += dp[i - 2]  # "1X" where X is 0-9 can represent 10-19
        elif s[i - 2] == '2':
            if s[i - 1] == '*':
                dp[i] += dp[i - 2] * 6  # "2*" can represent 21-26
            elif '0' <= s[i - 1] <= '6':
                dp[i] += dp[i - 2]  # "2X" where X is 0-6 can represent 20-26
    
        dp[i] %= MOD
    
    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "*"
    print(numDecodings(s1))  # Output: 9

    # Test Case 2
    s2 = "1*"
    print(numDecodings(s2))  # Output: 18

    # Test Case 3
    s3 = "2*"
    print(numDecodings(s3))  # Output: 15

    # Test Case 4
    s4 = "3*"
    print(numDecodings(s4))  # Output: 9

    # Test Case 5
    s5 = "**"
    print(numDecodings(s5))  # Output: 96

"""
Time Complexity:
- The solution iterates through the string once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The solution uses a dp array of size n + 1.
- Therefore, the space complexity is O(n).

Topic: Dynamic Programming (DP)
"""