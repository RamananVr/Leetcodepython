"""
LeetCode Problem #1690: Stone Game VII

Problem Statement:
Alice and Bob take turns playing a game, with Alice starting first. There are n stones arranged in a row. 
Each stone has a positive integer value. In each turn, the player can remove the leftmost stone or the 
rightmost stone from the row and receive points equal to the sum of the remaining stones' values in the row. 
The game ends when there are no stones left to remove.

The score difference between Alice and Bob is Alice's score minus Bob's score. Alice and Bob play optimally. 
Return the maximum score difference Alice can achieve if she goes first.

Constraints:
- 2 <= stones.length <= 1000
- 1 <= stones[i] <= 1000
"""

# Solution
def stoneGameVII(stones):
    """
    :type stones: List[int]
    :rtype: int
    """
    n = len(stones)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + stones[i]
    
    # dp[i][j] represents the maximum score difference Alice can achieve for stones[i:j+1]
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n + 1):  # Length of the subarray
        for i in range(n - length + 1):
            j = i + length - 1
            # If Alice removes the leftmost stone, Bob's turn starts with stones[i+1:j+1]
            score_remove_left = prefix_sum[j + 1] - prefix_sum[i + 1]
            # If Alice removes the rightmost stone, Bob's turn starts with stones[i:j]
            score_remove_right = prefix_sum[j] - prefix_sum[i]
            dp[i][j] = max(score_remove_left - dp[i + 1][j], score_remove_right - dp[i][j - 1])
    
    return dp[0][n - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    stones1 = [5, 3, 1, 4, 2]
    print(stoneGameVII(stones1))  # Expected Output: 6

    # Test Case 2
    stones2 = [7, 90, 5, 1, 100, 10, 10, 2]
    print(stoneGameVII(stones2))  # Expected Output: 122

    # Test Case 3
    stones3 = [1, 2]
    print(stoneGameVII(stones3))  # Expected Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a dynamic programming approach with a nested loop structure.
- The outer loop iterates over the possible lengths of subarrays (from 2 to n), and the inner loop iterates over the starting index of the subarray.
- The total number of iterations is proportional to n^2, where n is the length of the stones array.
- Calculating the prefix sum takes O(n) time.
- Overall time complexity: O(n^2).

Space Complexity:
- The `dp` table requires O(n^2) space to store the maximum score difference for all subarrays.
- The `prefix_sum` array requires O(n) space.
- Overall space complexity: O(n^2).

Topic: Dynamic Programming
"""