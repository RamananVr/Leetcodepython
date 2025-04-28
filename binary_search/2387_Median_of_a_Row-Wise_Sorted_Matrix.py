"""
LeetCode Problem #2387: Median of a Row-Wise Sorted Matrix

Problem Statement:
You are given an `m x n` matrix `grid` where each row is sorted in non-decreasing order. 
Find the median of the matrix. The median is the middle value in the sorted order of all 
the elements in the matrix. If the number of elements is even, the median is the smaller 
of the two middle values.

You must solve the problem in less than O(m * n) time complexity.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 500
- 1 <= grid[i][j] <= 10^6
- grid[i] is sorted in non-decreasing order.
"""

from typing import List

def findMedian(grid: List[List[int]]) -> int:
    """
    Finds the median of a row-wise sorted matrix.
    
    Args:
    grid (List[List[int]]): A 2D list where each row is sorted in non-decreasing order.
    
    Returns:
    int: The median of the matrix.
    """
    def countLessEqual(row, target):
        """Helper function to count elements <= target in a sorted row."""
        left, right = 0, len(row)
        while left < right:
            mid = (left + right) // 2
            if row[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    m, n = len(grid), len(grid[0])
    low, high = 1, 10**6  # Given constraints for grid[i][j]
    median_pos = (m * n + 1) // 2  # Position of the median in the sorted order

    while low < high:
        mid = (low + high) // 2
        count = sum(countLessEqual(row, mid) for row in grid)
        if count < median_pos:
            low = mid + 1
        else:
            high = mid

    return low

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]
    ]
    print(findMedian(grid1))  # Output: 5

    # Test Case 2
    grid2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(findMedian(grid2))  # Output: 5

    # Test Case 3
    grid3 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    print(findMedian(grid3))  # Output: 1

    # Test Case 4
    grid4 = [
        [1, 3, 8],
        [2, 4, 6],
        [5, 7, 9]
    ]
    print(findMedian(grid4))  # Output: 5

"""
Time Complexity Analysis:
- Let m = number of rows, n = number of columns.
- The binary search runs in O(log(max_val - min_val)), where max_val = 10^6 and min_val = 1.
- For each binary search step, we count elements <= mid in all rows, which takes O(m * log(n)) 
  (binary search on each row).
- Overall time complexity: O(m * log(n) * log(max_val)).
- Since max_val is a constant (10^6), this simplifies to O(m * log(n)).

Space Complexity Analysis:
- The algorithm uses O(1) additional space, as we only use a few variables for binary search.

Topic: Binary Search
"""