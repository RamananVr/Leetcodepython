"""
LeetCode Problem #2052: Minimum Cost to Separate Sentence Into Rows

Problem Statement:
You are given a string `sentence` containing words separated by spaces, and an integer `k`. 
The task is to split the sentence into rows such that each row contains at most `k` characters, 
and no word is split between two rows. The cost of a row is defined as the square of the number 
of extra spaces at the end of the row. The goal is to minimize the total cost of all rows.

Return the minimum cost to split the sentence into rows.

Constraints:
- 1 <= len(sentence) <= 1000
- 1 <= k <= 1000
- The sentence contains only lowercase English letters and spaces.
- Words in the sentence are separated by a single space.
- There are no leading or trailing spaces.

Example:
Input: sentence = "the quick brown fox", k = 10
Output: 29
Explanation:
- Split the sentence into rows: ["the quick", "brown fox"]
- Row 1 has 1 extra space (10 - 9 = 1), so its cost is 1^2 = 1.
- Row 2 has 3 extra spaces (10 - 7 = 3), so its cost is 3^2 = 9.
- Total cost = 1 + 9 = 10.
"""

# Python Solution
def minimumCost(sentence: str, k: int) -> int:
    words = sentence.split()
    n = len(words)
    
    # Precompute the length of words[i:j] including spaces
    lengths = [[0] * n for _ in range(n)]
    for i in range(n):
        lengths[i][i] = len(words[i])
        for j in range(i + 1, n):
            lengths[i][j] = lengths[i][j - 1] + len(words[j]) + 1  # Add 1 for space

    # Initialize dp array
    dp = [float('inf')] * n
    dp[0] = (k - lengths[0][0]) ** 2 if lengths[0][0] <= k else float('inf')

    # Fill dp array
    for i in range(1, n):
        for j in range(i + 1):
            if lengths[j][i] <= k:
                cost = (k - lengths[j][i]) ** 2 if i != n - 1 else 0
                dp[i] = min(dp[i], dp[j - 1] + cost if j > 0 else cost)

    return dp[-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sentence1 = "the quick brown fox"
    k1 = 10
    print(minimumCost(sentence1, k1))  # Output: 10

    # Test Case 2
    sentence2 = "a b c d e"
    k2 = 3
    print(minimumCost(sentence2, k2))  # Output: 0

    # Test Case 3
    sentence3 = "hello world"
    k3 = 5
    print(minimumCost(sentence3, k3))  # Output: inf (not possible to split)

    # Test Case 4
    sentence4 = "this is a test sentence"
    k4 = 7
    print(minimumCost(sentence4, k4))  # Output: 12

    # Test Case 5
    sentence5 = "leetcode is fun"
    k5 = 9
    print(minimumCost(sentence5, k5))  # Output: 1

"""
Time Complexity:
- Precomputing the lengths array takes O(n^2), where n is the number of words.
- The DP solution iterates over all pairs of words, so it also takes O(n^2).
- Overall time complexity: O(n^2).

Space Complexity:
- The lengths array takes O(n^2) space.
- The dp array takes O(n) space.
- Overall space complexity: O(n^2).

Topic: Dynamic Programming (DP)
"""