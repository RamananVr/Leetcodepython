"""
LeetCode Question #378: Kth Smallest Element in a Sorted Matrix

Problem Statement:
Given an n x n matrix where each of the rows and columns is sorted in ascending order, 
return the kth smallest element in the matrix.

You must find a solution with a memory complexity better than O(n^2).

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The 8th smallest element in the matrix is 13.

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5

Constraints:
- n == matrix.length == matrix[i].length
- 1 <= n <= 300
- -10^9 <= matrix[i][j] <= 10^9
- All the rows and columns of matrix are sorted in non-decreasing order.
- 1 <= k <= n^2
"""

# Solution
import heapq

def kthSmallest(matrix, k):
    """
    Finds the kth smallest element in a sorted matrix.

    :param matrix: List[List[int]], a sorted n x n matrix
    :param k: int, the kth smallest element to find
    :return: int, the kth smallest element
    """
    n = len(matrix)
    min_heap = []
    
    # Push the first element of each row into the heap
    for i in range(n):
        heapq.heappush(min_heap, (matrix[i][0], i, 0))
    
    # Extract the smallest element k times
    for _ in range(k):
        val, row, col = heapq.heappop(min_heap)
        if col + 1 < n:
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
    
    return val

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k1 = 8
    print(kthSmallest(matrix1, k1))  # Output: 13

    # Test Case 2
    matrix2 = [[-5]]
    k2 = 1
    print(kthSmallest(matrix2, k2))  # Output: -5

    # Test Case 3
    matrix3 = [[1, 2], [1, 3]]
    k3 = 3
    print(kthSmallest(matrix3, k3))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- The heap operations (push and pop) take O(log(n)).
- We perform k heap operations, so the total time complexity is O(k * log(n)).
- In the worst case, k = n^2, so the time complexity becomes O(n^2 * log(n)).

Space Complexity:
- The heap stores at most n elements at any time, so the space complexity is O(n).

Topic: Heap (Priority Queue)
"""