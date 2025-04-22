"""
LeetCode Problem #96: Unique Binary Search Trees

Problem Statement:
Given an integer `n`, return the number of structurally unique BSTs (binary search trees) which have exactly `n` nodes of unique values from 1 to `n`.

Constraints:
- 1 <= n <= 19

Example:
Input: n = 3
Output: 5
Explanation:
There are a total of 5 unique BSTs:
   1         1          2         3        3
    \         \       / \       /        /
     3         2     1   3     2        1
    /           \                \        \
   2             3                1        2
"""

# Solution
def numTrees(n: int) -> int:
    """
    Calculate the number of unique binary search trees (BSTs) that can be formed with `n` nodes.
    Uses dynamic programming to compute the Catalan number for `n`.
    """
    # DP array to store the number of unique BSTs for each count of nodes
    dp = [0] * (n + 1)
    
    # Base cases
    dp[0] = 1  # Empty tree
    dp[1] = 1  # Single node tree
    
    # Fill the DP array for all values from 2 to n
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]
    
    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    print(f"Input: n = {n}")
    print(f"Output: {numTrees(n)}")  # Expected Output: 5

    # Test Case 2
    n = 1
    print(f"Input: n = {n}")
    print(f"Output: {numTrees(n)}")  # Expected Output: 1

    # Test Case 3
    n = 4
    print(f"Input: n = {n}")
    print(f"Output: {numTrees(n)}")  # Expected Output: 14

    # Test Case 4
    n = 5
    print(f"Input: n = {n}")
    print(f"Output: {numTrees(n)}")  # Expected Output: 42

# Time and Space Complexity Analysis
"""
Time Complexity:
The solution uses nested loops to compute the number of unique BSTs for each `i` from 2 to `n`. 
For each `i`, the inner loop iterates `i` times. Thus, the total number of iterations is:
1 + 2 + 3 + ... + n = O(n^2).
Therefore, the time complexity is O(n^2).

Space Complexity:
The solution uses a DP array of size `n + 1` to store intermediate results. 
Thus, the space complexity is O(n).
"""

# Topic: Dynamic Programming