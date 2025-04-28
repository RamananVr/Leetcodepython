"""
LeetCode Problem #1198: Find Smallest Common Element in All Rows

Problem Statement:
Given an m x n matrix `mat` where every row is sorted in strictly increasing order, return the smallest common element in all rows.

If there is no common element, return -1.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 500
- 1 <= mat[i][j] <= 10^4
- mat[i] is sorted in strictly increasing order.

Example 1:
Input: mat = [[1,2,3,4,5],
              [2,4,5,8,10],
              [3,5,7,9,11],
              [1,3,5,7,9]]
Output: 5

Example 2:
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: -1
"""

# Solution
def smallestCommonElement(mat):
    """
    Finds the smallest common element in all rows of the matrix.

    :param mat: List[List[int]] - A 2D list where each row is sorted in strictly increasing order.
    :return: int - The smallest common element, or -1 if no common element exists.
    """
    from collections import Counter

    # Count the occurrences of each element across all rows
    count = Counter()
    rows = len(mat)

    for row in mat:
        for num in row:
            count[num] += 1

    # Find the smallest element that appears in all rows
    for num in sorted(count.keys()):
        if count[num] == rows:
            return num

    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[1, 2, 3, 4, 5],
            [2, 4, 5, 8, 10],
            [3, 5, 7, 9, 11],
            [1, 3, 5, 7, 9]]
    print(smallestCommonElement(mat1))  # Output: 5

    # Test Case 2
    mat2 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    print(smallestCommonElement(mat2))  # Output: -1

    # Test Case 3
    mat3 = [[1, 2, 3, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6]]
    print(smallestCommonElement(mat3))  # Output: 3

    # Test Case 4
    mat4 = [[1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]]
    print(smallestCommonElement(mat4))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting elements: O(m * n), where m is the number of rows and n is the number of columns.
- Sorting the keys of the counter: O(k * log(k)), where k is the number of unique elements in the matrix.
  In the worst case, k = m * n, but typically k is much smaller than m * n.
- Overall: O(m * n + k * log(k)).

Space Complexity:
- The Counter stores up to m * n unique elements in the worst case, so the space complexity is O(k), where k is the number of unique elements.
"""

# Topic: Arrays