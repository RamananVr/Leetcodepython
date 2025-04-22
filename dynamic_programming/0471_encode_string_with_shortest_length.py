"""
LeetCode Question #471: Encode String with Shortest Length

Problem Statement:
Given a string s, encode the string such that its encoded length is the shortest. 
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.

Note:
- k must be greater than or equal to 1.
- If an encoding process does not make the string shorter, then do not encode it.
- If there are multiple solutions, return any of them.

Example 1:
Input: s = "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.

Example 2:
Input: s = "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa".

Example 3:
Input: s = "aabcaabcd"
Output: "2[aabc]d"
Explanation: "2[aabc]d" is shorter than "aabcaabcd".

Example 4:
Input: s = "abbbabbbcabbbabbbc"
Output: "2[abbbabbbc]"
Explanation: "2[abbbabbbc]" is shorter than "abbbabbbcabbbabbbc".

Constraints:
- 1 <= s.length <= 150
- s consists of only lowercase English letters.
"""

# Solution
def encode(s: str) -> str:
    n = len(s)
    dp = [[""] * n for _ in range(n)]

    for l in range(1, n + 1):  # Length of substring
        for i in range(n - l + 1):  # Start index
            j = i + l - 1  # End index
            substr = s[i:j + 1]
            dp[i][j] = substr  # Initialize with the original substring

            # Check if we can split into two parts and combine their encodings
            for k in range(i, j):
                if len(dp[i][k] + dp[k + 1][j]) < len(dp[i][j]):
                    dp[i][j] = dp[i][k] + dp[k + 1][j]

            # Check if we can encode the substring
            for k in range(1, len(substr)):
                repeat_str = substr[:k]
                if len(substr) % k == 0 and substr == repeat_str * (len(substr) // k):
                    encoded = f"{len(substr) // k}[{dp[i][i + k - 1]}]"
                    if len(encoded) < len(dp[i][j]):
                        dp[i][j] = encoded

    return dp[0][n - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aaa"
    print(encode(s1))  # Output: "aaa"

    # Test Case 2
    s2 = "aaaaa"
    print(encode(s2))  # Output: "5[a]"

    # Test Case 3
    s3 = "aabcaabcd"
    print(encode(s3))  # Output: "2[aabc]d"

    # Test Case 4
    s4 = "abbbabbbcabbbabbbc"
    print(encode(s4))  # Output: "2[abbbabbbc]"

# Time and Space Complexity Analysis
"""
Time Complexity:
The solution uses dynamic programming to compute the shortest encoding for all substrings of the input string.
- The outer loop iterates over all possible substring lengths (1 to n), which is O(n).
- The inner loop iterates over all possible starting indices for substrings of a given length, which is O(n).
- For each substring, we check all possible splits and encodings, which is O(n) in the worst case.
Thus, the overall time complexity is O(n^3).

Space Complexity:
The solution uses a 2D DP table of size n x n to store the shortest encoding for each substring.
Thus, the space complexity is O(n^2).
"""

# Topic: Dynamic Programming