"""
LeetCode Problem #712: Minimum ASCII Delete Sum for Two Strings

Problem Statement:
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of 's' (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal ("ea") and the total cost is 115 + 116 = 231.

Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "d" and "e" from "delete" to match "leet" adds 100 + 101 to the sum.
Deleting "e" from "leet" adds 101 to the sum.
At the end, both strings are equal ("leet") and the total cost is 100 + 101 + 101 = 403.

Constraints:
- 1 <= s1.length, s2.length <= 1000
- s1 and s2 consist of lowercase English letters.
"""

# Solution
def minimumDeleteSum(s1: str, s2: str) -> int:
    # Get the lengths of the strings
    m, n = len(s1), len(s2)
    
    # Create a DP table where dp[i][j] represents the minimum ASCII delete sum
    # to make s1[:i] and s2[:j] equal
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the first row and column with the ASCII sums of the prefixes
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
    
    # Fill the rest of the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                # If characters match, no deletion is needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Otherwise, delete one character from either s1 or s2
                dp[i][j] = min(
                    dp[i - 1][j] + ord(s1[i - 1]),  # Delete from s1
                    dp[i][j - 1] + ord(s2[j - 1])   # Delete from s2
                )
    
    # The result is in the bottom-right corner of the DP table
    return dp[m][n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "sea"
    s2 = "eat"
    print(f"Test Case 1: {minimumDeleteSum(s1, s2)}")  # Expected Output: 231

    # Test Case 2
    s1 = "delete"
    s2 = "leet"
    print(f"Test Case 2: {minimumDeleteSum(s1, s2)}")  # Expected Output: 403

    # Test Case 3
    s1 = "abc"
    s2 = "def"
    print(f"Test Case 3: {minimumDeleteSum(s1, s2)}")  # Expected Output: 597

    # Test Case 4
    s1 = "a"
    s2 = "a"
    print(f"Test Case 4: {minimumDeleteSum(s1, s2)}")  # Expected Output: 0

    # Test Case 5
    s1 = "abcd"
    s2 = "bc"
    print(f"Test Case 5: {minimumDeleteSum(s1, s2)}")  # Expected Output: 195

"""
Time Complexity:
- The solution uses a 2D DP table of size (m+1) x (n+1), where m and n are the lengths of s1 and s2.
- Filling the table requires O(m * n) time, as each cell is computed in constant time.
- Overall time complexity: O(m * n).

Space Complexity:
- The DP table requires O(m * n) space.
- Overall space complexity: O(m * n).

Topic: Dynamic Programming (DP)
"""