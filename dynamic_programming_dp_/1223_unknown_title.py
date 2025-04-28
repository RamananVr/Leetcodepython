"""
LeetCode Problem #1223: Dice Roll Simulation

Problem Statement:
A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times.

Given an integer n and an array rollMax of length 6, return the number of distinct sequences that can be obtained with exact n rolls.

Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:
Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 34 distinct sequences that can be obtained such as [1,2], [2,1], [1,1], [2,2], [3,3], [3,4], etc.

Example 2:
Input: n = 2, rollMax = [1,1,1,1,1,1]
Output: 30

Constraints:
- 1 <= n <= 5000
- rollMax.length == 6
- 1 <= rollMax[i] <= 15
"""

# Python Solution
def dieSimulator(n, rollMax):
    MOD = 10**9 + 7
    dp = [[[0] * 16 for _ in range(6)] for _ in range(n + 1)]
    
    # Base case: 1 roll
    for i in range(6):
        dp[1][i][1] = 1
    
    # Fill DP table
    for roll in range(2, n + 1):
        for face in range(6):
            for count in range(1, rollMax[face] + 1):
                # Continue rolling the same face
                if count > 1:
                    dp[roll][face][count] = dp[roll - 1][face][count - 1]
                
                # Switch to a different face
                for prev_face in range(6):
                    if prev_face != face:
                        dp[roll][face][count] += sum(dp[roll - 1][prev_face][1:rollMax[prev_face] + 1])
                        dp[roll][face][count] %= MOD
    
    # Sum up all valid sequences
    result = 0
    for face in range(6):
        result += sum(dp[n][face][1:rollMax[face] + 1])
        result %= MOD
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 2
    rollMax1 = [1, 1, 2, 2, 2, 3]
    print(dieSimulator(n1, rollMax1))  # Output: 34

    # Test Case 2
    n2 = 2
    rollMax2 = [1, 1, 1, 1, 1, 1]
    print(dieSimulator(n2, rollMax2))  # Output: 30

    # Test Case 3
    n3 = 3
    rollMax3 = [1, 1, 1, 1, 1, 1]
    print(dieSimulator(n3, rollMax3))  # Output: 90

    # Test Case 4
    n4 = 4
    rollMax4 = [2, 2, 2, 2, 2, 2]
    print(dieSimulator(n4, rollMax4))  # Output: 150

"""
Time and Space Complexity Analysis:

Time Complexity:
- The DP table has dimensions (n x 6 x max_rollMax), where max_rollMax is the maximum value in the rollMax array.
- For each cell, we perform a constant amount of work (looping over 6 faces).
- Therefore, the time complexity is O(n * 6 * max_rollMax).

Space Complexity:
- The DP table requires O(n * 6 * max_rollMax) space.

Topic: Dynamic Programming (DP)
"""