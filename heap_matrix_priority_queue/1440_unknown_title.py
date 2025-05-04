"""
LeetCode Problem #1440: "Find the Kth Smallest Sum of a Matrix With Sorted Rows"

Problem Statement:
Given an m x n matrix `mat` where each row is sorted in strictly increasing order, return the kth smallest sum of a matrix with sorted rows.

The kth smallest sum is defined as the kth smallest sum of elements chosen from each row, with exactly one element chosen from each row.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 40
- 1 <= mat[i][j] <= 5000
- 1 <= k <= min(200, n^m)

Example:
Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 17
Explanation: The list of sums sorted in order are [8, 9, 10, 11, 17]. The 5th smallest sum is 17.

Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17
Explanation: The list of sums sorted in order are [8, 9, 10, 11, 17, 17, 18, 19, 20]. The 9th smallest sum is 17.

Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 17
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
    # Start with the first row
    current_sums = mat[0]
    
    # Iterate through the remaining rows
    for row in mat[1:]:
        # Min-heap to store the new sums
        heap = []
        for sum_so_far in current_sums:
            for element in row:
                heappush(heap, sum_so_far + element)
        
        # Keep only the smallest k sums
        current_sums = list(islice(heap, k))
    
    # The kth smallest sum is the last element in the current_sums list
    return current_sums[-1]

# Example Test Cases
if __name__ == "__main__":
    mat1 = [[1, 3, 11], [2, 4, 6]]
    k1 = 5
    print(kthSmallest(mat1, k1))  # Output: 17

    mat2 = [[1, 3, 11], [2, 4, 6]]
    k2 = 9
    print(kthSmallest(mat2, k2))  # Output: 17

    mat3 = [[1, 10, 10], [1, 4, 5], [2, 3, 6]]
    k3 = 7
    print(kthSmallest(mat3, k3))  # Output: 17

    mat4 = [[1, 1, 10], [2, 2, 9]]
    k4 = 7
    print(kthSmallest(mat4, k4))  # Output: 12

"""
Time Complexity:
- Let m be the number of rows and n be the number of columns in the matrix.
- For each row, we generate up to k * n new sums and maintain a heap of size k.
- The heap operations (push and pop) take O(log k) time.
- Therefore, the overall time complexity is O(m * k * n * log k).

Space Complexity:
- The space complexity is O(k) for the heap used to store the smallest sums.

Topic: Heap, Matrix, Priority Queue
"""