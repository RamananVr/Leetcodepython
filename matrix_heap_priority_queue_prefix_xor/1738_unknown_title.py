"""
LeetCode Problem #1738: Find Kth Largest XOR Coordinate Value

Problem Statement:
You are given a 2D matrix `matrix` of size `m x n`, consisting of non-negative integers. You are also given an integer `k`.

The value of the coordinate `(a, b)` of the matrix is defined as:
    - The XOR of all matrix[i][j] where `0 <= i <= a` and `0 <= j <= b` (inclusive).

Find the k-th largest value (1-indexed) of all the coordinates' values.

Constraints:
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 1000`
- `0 <= matrix[i][j] <= 10^6`
- `1 <= k <= m * n`
"""

from heapq import heappush, heappop

def kthLargestValue(matrix, k):
    """
    Finds the k-th largest XOR coordinate value in the given matrix.

    :param matrix: List[List[int]] - 2D matrix of non-negative integers
    :param k: int - The rank of the largest XOR value to find
    :return: int - The k-th largest XOR coordinate value
    """
    m, n = len(matrix), len(matrix[0])
    xor_matrix = [[0] * n for _ in range(m)]
    min_heap = []

    for i in range(m):
        for j in range(n):
            # Compute the XOR value for the current cell
            xor_matrix[i][j] = matrix[i][j]
            if i > 0:
                xor_matrix[i][j] ^= xor_matrix[i - 1][j]
            if j > 0:
                xor_matrix[i][j] ^= xor_matrix[i][j - 1]
            if i > 0 and j > 0:
                xor_matrix[i][j] ^= xor_matrix[i - 1][j - 1]

            # Use a min-heap to keep track of the k largest values
            heappush(min_heap, xor_matrix[i][j])
            if len(min_heap) > k:
                heappop(min_heap)

    # The root of the min-heap is the k-th largest value
    return min_heap[0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [[5, 2], [1, 6]]
    k1 = 1
    print(kthLargestValue(matrix1, k1))  # Output: 7

    # Test Case 2
    matrix2 = [[5, 2], [1, 6]]
    k2 = 2
    print(kthLargestValue(matrix2, k2))  # Output: 5

    # Test Case 3
    matrix3 = [[5, 2], [1, 6]]
    k3 = 3
    print(kthLargestValue(matrix3, k3))  # Output: 4

    # Test Case 4
    matrix4 = [[5, 2], [1, 6]]
    k4 = 4
    print(kthLargestValue(matrix4, k4))  # Output: 0

"""
Time Complexity Analysis:
- Computing the XOR values for the entire matrix takes O(m * n) time, where m is the number of rows and n is the number of columns.
- Maintaining the min-heap of size k takes O(log k) time for each of the m * n elements, resulting in a total of O(m * n * log k).
- Overall time complexity: O(m * n * log k).

Space Complexity Analysis:
- The XOR matrix requires O(m * n) space.
- The min-heap requires O(k) space.
- Overall space complexity: O(m * n + k).

Topic: Matrix, Heap (Priority Queue), Prefix XOR
"""