"""
LeetCode Problem #1444: Number of Ways of Cutting a Pizza

Problem Statement:
You are given a rectangular pizza represented as a rows x cols matrix containing the following characters:
- 'A' (an apple)
- '.' (empty cell)

You have to cut the pizza into k pieces using k-1 cuts. For each cut, you choose the direction: vertical or horizontal. 
After a cut, each piece must contain at least one apple. If a cut cannot be made, it is invalid. 

Return the number of ways of cutting the pizza such that each piece contains at least one apple. 
Since the answer can be large, return it modulo 10^9 + 7.

Constraints:
- 1 <= rows, cols <= 50
- 1 <= k <= 10
- pizza[i][j] is either 'A' or '.'

Example:
Input: pizza = ["A..","AAA","..."], k = 3
Output: 3
Explanation: The pizza can be cut as follows:
1. Horizontal cut between row 1 and row 2, then vertical cut between column 1 and column 2.
2. Horizontal cut between row 1 and row 2, then vertical cut between column 2 and column 3.
3. Vertical cut between column 1 and column 2, then horizontal cut between row 1 and row 2.
"""

# Solution
from functools import lru_cache

def ways(pizza, k):
    MOD = 10**9 + 7
    rows, cols = len(pizza), len(pizza[0])
    
    # Precompute the prefix sum of apples in the pizza
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows - 1, -1, -1):
        for c in range(cols - 1, -1, -1):
            prefix[r][c] = (1 if pizza[r][c] == 'A' else 0) + prefix[r + 1][c] + prefix[r][c + 1] - prefix[r + 1][c + 1]
    
    # Helper function to check if a sub-pizza has at least one apple
    def has_apple(r1, c1, r2, c2):
        return prefix[r1][c1] - prefix[r2][c1] - prefix[r1][c2] + prefix[r2][c2] > 0
    
    # Memoized recursive function
    @lru_cache(None)
    def dp(r, c, cuts):
        if cuts == 0:  # Base case: no more cuts to make
            return 1 if has_apple(r, c, rows, cols) else 0
        
        ways = 0
        # Horizontal cuts
        for nr in range(r + 1, rows):
            if has_apple(r, c, nr, cols):
                ways = (ways + dp(nr, c, cuts - 1)) % MOD
        # Vertical cuts
        for nc in range(c + 1, cols):
            if has_apple(r, c, rows, nc):
                ways = (ways + dp(r, nc, cuts - 1)) % MOD
        
        return ways
    
    return dp(0, 0, k - 1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    pizza1 = ["A..", "AAA", "..."]
    k1 = 3
    print(ways(pizza1, k1))  # Output: 3

    # Test Case 2
    pizza2 = ["A..", "AA.", "..."]
    k2 = 3
    print(ways(pizza2, k2))  # Output: 1

    # Test Case 3
    pizza3 = ["A.A", "AAA", "A.A"]
    k3 = 4
    print(ways(pizza3, k3))  # Output: 10

"""
Time and Space Complexity Analysis:

Time Complexity:
- Precomputing the prefix sum takes O(rows * cols).
- The recursive function dp(r, c, cuts) explores all possible cuts. In the worst case, there are O(rows * cols * k) states, 
  and for each state, we iterate over rows and columns to make cuts, leading to O(rows + cols) work per state.
- Overall, the time complexity is O(rows * cols * k * (rows + cols)).

Space Complexity:
- The prefix sum array takes O(rows * cols) space.
- The memoization cache stores O(rows * cols * k) states.
- Overall, the space complexity is O(rows * cols * k).

Topic: Dynamic Programming
"""