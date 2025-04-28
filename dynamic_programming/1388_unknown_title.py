"""
LeetCode Problem #1388: Pizza With 3n Slices

Problem Statement:
There is a pizza with 3n slices of varying sizes, represented by an array `slices` of integers. 
You and your friends will take slices of pizza as follows:

- You will pick any slice of pizza.
- Your friend will pick the next slice in the clockwise direction, and then the next slice after that.
- You will pick another slice, and so on.

If there are multiple slices available, you can only pick slices that are not adjacent to each other. 
Your goal is to maximize the total sum of the slices you pick.

Given an integer array `slices` of size `3n`, return the maximum possible sum of slices you can pick.

Constraints:
- 1 <= slices.length <= 500
- slices.length % 3 == 0
- 1 <= slices[i] <= 1000
"""

# Solution
from typing import List

def maxSizeSlices(slices: List[int]) -> int:
    def max_sum(slices: List[int], n: int) -> int:
        # Dynamic programming to solve the problem
        dp = [[0] * (n + 1) for _ in range(len(slices) + 1)]
        for i in range(1, len(slices) + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 1][j], (dp[i - 2][j - 1] if i > 1 else 0) + slices[i - 1])
        return dp[len(slices)][n]

    n = len(slices) // 3
    # Case 1: Exclude the first slice
    case1 = max_sum(slices[1:], n)
    # Case 2: Exclude the last slice
    case2 = max_sum(slices[:-1], n)
    # Return the maximum of the two cases
    return max(case1, case2)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    slices = [1, 2, 3, 4, 5, 6]
    print(maxSizeSlices(slices))  # Expected Output: 10

    # Test Case 2
    slices = [8, 9, 8, 6, 1, 1]
    print(maxSizeSlices(slices))  # Expected Output: 16

    # Test Case 3
    slices = [4, 1, 2, 5, 8, 3, 1, 9, 7]
    print(maxSizeSlices(slices))  # Expected Output: 21

    # Test Case 4
    slices = [3, 1, 2]
    print(maxSizeSlices(slices))  # Expected Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- The `max_sum` function uses a dynamic programming approach with a 2D table of size O(len(slices) * n).
- Since we call `max_sum` twice (once for each case), the overall time complexity is O(len(slices) * n).
- Given that len(slices) = 3n, the time complexity simplifies to O(n^2).

Space Complexity:
- The space complexity is dominated by the 2D DP table, which is O(len(slices) * n).
- This simplifies to O(n^2) since len(slices) = 3n.
"""

# Topic: Dynamic Programming