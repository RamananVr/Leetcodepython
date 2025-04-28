"""
LeetCode Problem #1384: Find the Kth Smallest Sum of a Matrix With Sorted Rows

Problem Statement:
You are given an m x n matrix `mat` that is sorted in non-decreasing order both row-wise and column-wise. 
You are also given an integer `k`. You need to return the kth smallest sum of a matrix with sorted rows.

In other words, you need to find the kth smallest sum of selecting one element from each row of the matrix.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 40
- 1 <= mat[i][j] <= 5000
- 1 <= k <= min(200, n ** m)

Example:
Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 17
Explanation: The list of sums are [8, 9, 10, 11, 11, 12, 13, 14, 17, 17, 18, 19, 20, ...]. The 5th smallest is 17.

Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17

Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
"""

from heapq import heappush, heappop
from itertools import islice

def kthSmallest(mat, k):
    """
    Finds the kth smallest sum of a matrix with sorted rows.

    :param mat: List[List[int]] - The input matrix with sorted rows.
    :param k: int - The kth smallest sum to find.
    :return: int - The kth smallest sum.
    """
    def merge_two_lists(list1, list2, k):
        """Helper function to merge two sorted lists and keep only the smallest k sums."""
        min_heap = []
        for x in list1:
            for y in list2:
                heappush(min_heap, x + y)
                if len(min_heap) > k:
                    heappop(min_heap)
        return list(min_heap)

    # Start with the first row
    current_sums = mat[0]

    # Iteratively merge each row into the current sums
    for i in range(1, len(mat)):
        current_sums = merge_two_lists(current_sums, mat[i], k)

    # Return the kth smallest sum
    return sorted(current_sums)[k - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[1, 3, 11], [2, 4, 6]]
    k1 = 5
    print(kthSmallest(mat1, k1))  # Output: 17

    # Test Case 2
    mat2 = [[1, 3, 11], [2, 4, 6]]
    k2 = 9
    print(kthSmallest(mat2, k2))  # Output: 17

    # Test Case 3
    mat3 = [[1, 10, 10], [1, 4, 5], [2, 3, 6]]
    k3 = 7
    print(kthSmallest(mat3, k3))  # Output: 9

    # Test Case 4
    mat4 = [[1, 1, 10], [2, 2, 9]]
    k4 = 7
    print(kthSmallest(mat4, k4))  # Output: 12

"""
Time Complexity:
- Let m = number of rows, n = number of columns, and k = given input.
- The merge_two_lists function has a complexity of O(k * n * log(k)) because we iterate over two lists of size k and n, and maintain a heap of size k.
- Since we merge m rows, the overall complexity is O(m * k * n * log(k)).

Space Complexity:
- The space complexity is O(k) due to the heap used in the merge_two_lists function.

Topic: Heap, Matrix, Priority Queue
"""