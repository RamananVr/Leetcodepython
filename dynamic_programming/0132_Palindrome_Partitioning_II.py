"""
LeetCode Problem #132: Palindrome Partitioning II

Problem Statement:
Given a string `s`, partition `s` such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of `s`.

Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa", "b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0
Explanation: The string is already a palindrome, so no cuts are needed.

Example 3:
Input: s = "ab"
Output: 1
Explanation: The palindrome partitioning ["a", "b"] could be produced using 1 cut.

Constraints:
- 1 <= s.length <= 2000
- s consists of lowercase English letters only.
"""

def minCut(s: str) -> int:
    """
    Function to compute the minimum cuts needed for a palindrome partitioning of the string `s`.
    """
    n = len(s)
    # Step 1: Precompute palindrome substrings using dynamic programming
    is_palindrome = [[False] * n for _ in range(n)]
    for i in range(n):
        is_palindrome[i][i] = True  # Single character is always a palindrome
    for length in range(2, n + 1):  # Check substrings of length 2 to n
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    is_palindrome[i][j] = True
                else:
                    is_palindrome[i][j] = is_palindrome[i + 1][j - 1]

    # Step 2: Use dynamic programming to find the minimum cuts
    dp = [float('inf')] * n
    for i in range(n):
        if is_palindrome[0][i]:  # If the substring s[0:i+1] is a palindrome, no cuts are needed
            dp[i] = 0
        else:
            for j in range(i):
                if is_palindrome[j + 1][i]:  # If s[j+1:i+1] is a palindrome
                    dp[i] = min(dp[i], dp[j] + 1)

    return dp[-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aab"
    print(f"Minimum cuts for '{s1}': {minCut(s1)}")  # Expected Output: 1

    # Test Case 2
    s2 = "a"
    print(f"Minimum cuts for '{s2}': {minCut(s2)}")  # Expected Output: 0

    # Test Case 3
    s3 = "ab"
    print(f"Minimum cuts for '{s3}': {minCut(s3)}")  # Expected Output: 1

    # Test Case 4
    s4 = "racecar"
    print(f"Minimum cuts for '{s4}': {minCut(s4)}")  # Expected Output: 0

    # Test Case 5
    s5 = "civicracecar"
    print(f"Minimum cuts for '{s5}': {minCut(s5)}")  # Expected Output: 0

"""
Time Complexity:
- Precomputing the `is_palindrome` table takes O(n^2) time, where `n` is the length of the string.
- Filling the `dp` array also takes O(n^2) time, as for each index `i`, we may iterate over all previous indices `j`.
- Overall time complexity: O(n^2).

Space Complexity:
- The `is_palindrome` table takes O(n^2) space.
- The `dp` array takes O(n) space.
- Overall space complexity: O(n^2).

Topic: Dynamic Programming
"""