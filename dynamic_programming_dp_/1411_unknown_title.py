"""
LeetCode Problem #1411: Number of Ways to Paint N × 3 Grid

Problem Statement:
You have a grid of size n × 3 and you want to paint it such that:
1. Each cell is painted with one of the three colors: red, yellow, or green.
2. No two adjacent cells have the same color.

Return the number of ways to paint the grid modulo 10^9 + 7.

Constraints:
- 1 <= n <= 5000

Example:
Input: n = 1
Output: 12
Explanation: There are 12 ways to paint a 1 × 3 grid.

Input: n = 2
Output: 54
Explanation: There are 54 ways to paint a 2 × 3 grid.

Input: n = 3
Output: 246
Explanation: There are 246 ways to paint a 3 × 3 grid.
"""

# Solution
def numOfWays(n: int) -> int:
    MOD = 10**9 + 7
    
    # Two types of patterns:
    # 1. "abc" pattern: All three cells in a row have different colors.
    # 2. "aba" pattern: The first and third cells in a row have the same color, and the middle cell is different.
    
    # Initialize counts for the first row
    abc_count = 6  # "abc" pattern
    aba_count = 6  # "aba" pattern
    
    for _ in range(1, n):
        # Transition rules:
        # - "abc" can transition to both "abc" and "aba".
        # - "aba" can transition to both "abc" and "aba".
        new_abc_count = (3 * abc_count + 2 * aba_count) % MOD
        new_aba_count = (2 * abc_count + 2 * aba_count) % MOD
        
        # Update counts
        abc_count, aba_count = new_abc_count, new_aba_count
    
    # Total ways to paint the grid
    return (abc_count + aba_count) % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 1
    print(numOfWays(n))  # Output: 12

    # Test Case 2
    n = 2
    print(numOfWays(n))  # Output: 54

    # Test Case 3
    n = 3
    print(numOfWays(n))  # Output: 246

    # Test Case 4
    n = 4
    print(numOfWays(n))  # Output: 1122

    # Test Case 5
    n = 5000
    print(numOfWays(n))  # Output: Large number modulo 10^9 + 7

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves a single loop that iterates `n - 1` times.
- Each iteration performs constant-time calculations.
- Therefore, the time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of space to store the counts (`abc_count` and `aba_count`).
- No additional data structures are used.
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming (DP)
"""