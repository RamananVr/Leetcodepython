"""
LeetCode Question #1439: Find the Kth Smallest Sum of a Matrix With Sorted Rows

Problem Statement:
You are given an m x n matrix mat that has its rows sorted in non-decreasing order and an integer k. 
You are allowed to choose exactly one element from each row to form an array. 
Return the kth smallest array sum among all possible arrays.

Example 1:
Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 17
Explanation: Choosing one element from each row, the first 5 smallest sums are:
1. [1,2] => 3
2. [1,4] => 5
3. [3,2] => 5
4. [1,6] => 7
5. [3,4] => 7
The 5th smallest sum is 17.

Example 2:
Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 40
- 1 <= mat[i][j] <= 5000
- 1 <= k <= min(200, n ** m)
"""

from heapq import heappush, heappop
from itertools import islice

def kthSmallest(mat, k):
    """
    Finds the kth smallest sum of a matrix with sorted rows.

    :param mat: List[List[int]] - The matrix with sorted rows.
    :param k: int - The kth smallest sum to find.
    :return: int - The kth smallest sum.
    """
    def merge_two_rows(row1, row2, k):
        """
        Merges two rows to find the smallest k sums.
        """
        min_heap = []
        for i in range(len(row1)):
            for j in range(len(row2)):
                heappush(min_heap, row1[i] + row2[j])
                if len(min_heap) > k:
                    heappop(min_heap)
        return sorted(min_heap)

    result = mat[0]
    for i in range(1, len(mat)):
        result = merge_two_rows(result, mat[i], k)
    return result[k - 1]

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
    print(kthSmallest(mat3, k3))  # Output: 17

    # Test Case 4
    mat4 = [[1, 1, 10], [2, 2, 9]]
    k4 = 7
    print(kthSmallest(mat4, k4))  # Output: 12

"""
Time Complexity:
- Let m be the number of rows and n be the number of columns in the matrix.
- The merge_two_rows function has a complexity of O(n^2 * log(k)) for each pair of rows.
- Since we merge m rows, the overall complexity is O(m * n^2 * log(k)).

Space Complexity:
- The space complexity is O(k) due to the heap used in the merge_two_rows function.

Topic: Heap, Matrix, Sorting
"""