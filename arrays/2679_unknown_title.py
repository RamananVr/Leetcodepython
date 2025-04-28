"""
LeetCode Problem #2679: Sum in a Matrix

Problem Statement:
You are given a 0-indexed 2D integer array `nums`. Initially, your score is `0`. 
Perform the following operations until `nums` becomes empty:

1. Pick the row with the maximum value in its last column. If there are multiple rows with the same value, pick any of them.
2. Add the maximum value in that row to your score.
3. Remove the picked row from `nums`.

Return the score after performing the above operations.

Constraints:
- `1 <= nums.length <= 100`
- `1 <= nums[i].length <= 100`
- `1 <= nums[i][j] <= 10^3`
"""

# Python Solution
from typing import List

def matrixSum(nums: List[List[int]]) -> int:
    # Sort each row in descending order
    for row in nums:
        row.sort(reverse=True)
    
    score = 0
    while nums:
        # Find the maximum value in the last column of all rows
        max_value = max(row[-1] for row in nums)
        score += max_value
        
        # Remove the row containing the maximum value
        for i in range(len(nums)):
            if nums[i][-1] == max_value:
                nums.pop(i)
                break
    
    return score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrixSum(nums1))  # Expected Output: 18

    # Test Case 2
    nums2 = [[10, 20, 30], [5, 15, 25], [1, 2, 3]]
    print(matrixSum(nums2))  # Expected Output: 75

    # Test Case 3
    nums3 = [[1]]
    print(matrixSum(nums3))  # Expected Output: 1

    # Test Case 4
    nums4 = [[1, 2], [3, 4], [5, 6]]
    print(matrixSum(nums4))  # Expected Output: 12

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting each row takes O(m * n * log(n)), where `m` is the number of rows and `n` is the number of columns.
- Finding the maximum value in the last column takes O(m) per iteration, and there are `m` iterations.
- Overall time complexity: O(m * n * log(n)).

Space Complexity:
- The space complexity is O(1) since we are modifying the input array in place and using a constant amount of extra space.
"""

# Topic: Arrays