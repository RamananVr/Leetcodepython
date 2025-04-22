"""
LeetCode Problem #474: Ones and Zeroes

You are given an array of binary strings `strs` and two integers `m` and `n`.

Return the size of the largest subset of `strs` such that there are at most `m` 0's and `n` 1's in the subset.

A set `x` is a subset of a set `y` if all elements of `x` are also elements of `y`.

Constraints:
- 1 <= strs.length <= 600
- 1 <= strs[i].length <= 100
- strs[i] consists only of '0' and '1'.
- 1 <= m, n <= 100
"""

# Solution
from typing import List

def findMaxForm(strs: List[str], m: int, n: int) -> int:
    # Initialize a 2D DP array where dp[i][j] represents the maximum subset size
    # that can be formed with at most i 0's and j 1's.
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Iterate through each string in strs
    for s in strs:
        # Count the number of 0's and 1's in the current string
        zeros = s.count('0')
        ones = s.count('1')
        
        # Update the DP table in reverse to avoid overwriting results
        for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
    
    # The answer is the maximum subset size that can be formed with at most m 0's and n 1's
    return dp[m][n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    print(findMaxForm(strs, m, n))  # Expected Output: 4

    # Test Case 2
    strs = ["10", "0", "1"]
    m = 1
    n = 1
    print(findMaxForm(strs, m, n))  # Expected Output: 2

    # Test Case 3
    strs = ["10", "0001", "111001", "1", "0"]
    m = 3
    n = 4
    print(findMaxForm(strs, m, n))  # Expected Output: 3

"""
Time Complexity Analysis:
- Let k be the length of the input list `strs` and l be the average length of strings in `strs`.
- Counting zeros and ones in a string takes O(l) time.
- The DP table has dimensions (m+1) x (n+1), and for each string, we update the table in O(m * n) time.
- Overall time complexity: O(k * l + k * m * n).

Space Complexity Analysis:
- The DP table requires O(m * n) space.
- Overall space complexity: O(m * n).

Topic: Dynamic Programming (DP)
"""