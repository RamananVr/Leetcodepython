"""
LeetCode Problem #363: Max Sum of Rectangle No Larger Than K

Problem Statement:
Given an m x n matrix `matrix` and an integer `k`, return the max sum of a rectangle in the matrix such that its sum is no larger than `k`.

It is guaranteed that there will be a rectangle with a sum no larger than `k`.

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -100 <= matrix[i][j] <= 100
- -10^5 <= k <= 10^5
"""

from sortedcontainers import SortedList

def maxSumSubmatrix(matrix, k):
    """
    Finds the maximum sum of a rectangle in the matrix such that the sum is no larger than k.

    :param matrix: List[List[int]] - 2D matrix of integers
    :param k: int - the maximum allowed sum
    :return: int - the maximum sum of a rectangle no larger than k
    """
    def maxSumSubarray(nums, k):
        """
        Helper function to find the maximum sum of a subarray no larger than k.
        Uses a sorted list to maintain prefix sums and find the closest sum <= k.
        """
        prefix_sums = SortedList([0])
        current_sum = 0
        max_sum = float('-inf')
        
        for num in nums:
            current_sum += num
            # Find the smallest prefix sum such that current_sum - prefix_sum <= k
            target = current_sum - k
            idx = prefix_sums.bisect_left(target)
            if idx < len(prefix_sums):
                max_sum = max(max_sum, current_sum - prefix_sums[idx])
            prefix_sums.add(current_sum)
        
        return max_sum

    rows, cols = len(matrix), len(matrix[0])
    max_sum = float('-inf')

    # Iterate over all pairs of rows
    for top in range(rows):
        # Initialize a 1D array to store the sum of elements between two rows
        col_sums = [0] * cols
        for bottom in range(top, rows):
            # Update the column sums for the current row range
            for col in range(cols):
                col_sums[col] += matrix[bottom][col]
            # Find the maximum subarray sum no larger than k for the current column sums
            max_sum = max(max_sum, maxSumSubarray(col_sums, k))
    
    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [[1, 0, 1], [0, -2, 3]]
    k1 = 2
    print(maxSumSubmatrix(matrix1, k1))  # Output: 2

    # Test Case 2
    matrix2 = [[2, 2, -1]]
    k2 = 3
    print(maxSumSubmatrix(matrix2, k2))  # Output: 3

    # Test Case 3
    matrix3 = [[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]]
    k3 = 8
    print(maxSumSubmatrix(matrix3, k3))  # Output: 8

"""
Time Complexity:
- Let m = number of rows, n = number of columns.
- The outer loop iterates over all pairs of rows, which is O(m^2).
- For each pair of rows, we calculate the column sums (O(n)) and find the maximum subarray sum no larger than k using a sorted list (O(n log n)).
- Overall time complexity: O(m^2 * n log n).

Space Complexity:
- The space complexity is dominated by the sorted list used in the helper function, which can store up to n elements.
- Space complexity: O(n).

Topic: Dynamic Programming (DP), Prefix Sum, Sorted Containers
"""