"""
LeetCode Problem #72: Edit Distance

Problem Statement:
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
1. Insert a character
2. Delete a character
3. Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Example 3:
Input: word1 = "abc", word2 = "abc"
Output: 0

Constraints:
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters.
"""

def minDistance(word1: str, word2: str) -> int:
    """
    Dynamic Programming solution to calculate the minimum edit distance between two strings.
    """
    m, n = len(word1), len(word2)
    
    # Create a DP table where dp[i][j] represents the minimum edit distance
    # to convert word1[0:i] to word2[0:j].
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases: converting an empty string to another string
    for i in range(m + 1):
        dp[i][0] = i  # Deleting all characters from word1
    for j in range(n + 1):
        dp[0][j] = j  # Inserting all characters into word1
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                # Characters match, no operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Take the minimum of insert, delete, or replace
                dp[i][j] = 1 + min(dp[i - 1][j],    # Delete
                                   dp[i][j - 1],    # Insert
                                   dp[i - 1][j - 1] # Replace
                                  )
    
    return dp[m][n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "horse"
    word2 = "ros"
    print(f"Edit Distance between '{word1}' and '{word2}': {minDistance(word1, word2)}")  # Output: 3

    # Test Case 2
    word1 = "intention"
    word2 = "execution"
    print(f"Edit Distance between '{word1}' and '{word2}': {minDistance(word1, word2)}")  # Output: 5

    # Test Case 3
    word1 = "abc"
    word2 = "abc"
    print(f"Edit Distance between '{word1}' and '{word2}': {minDistance(word1, word2)}")  # Output: 0

    # Test Case 4
    word1 = ""
    word2 = "abc"
    print(f"Edit Distance between '{word1}' and '{word2}': {minDistance(word1, word2)}")  # Output: 3

    # Test Case 5
    word1 = "abc"
    word2 = ""
    print(f"Edit Distance between '{word1}' and '{word2}': {minDistance(word1, word2)}")  # Output: 3

"""
Time Complexity:
- The DP table has dimensions (m+1) x (n+1), where m = len(word1) and n = len(word2).
- Filling each cell takes O(1) time.
- Therefore, the overall time complexity is O(m * n).

Space Complexity:
- The DP table requires O(m * n) space.

Topic: Dynamic Programming (DP)
"""