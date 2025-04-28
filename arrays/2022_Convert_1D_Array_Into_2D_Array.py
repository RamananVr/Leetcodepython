"""
LeetCode Problem #2022: Convert 1D Array Into 2D Array

Problem Statement:
You are given a 1D integer array `original` and two integers, `m` and `n`, representing the number of rows and the number of columns of a 2D array, respectively.

The task is to reshape the 1D array `original` into a 2D array with `m` rows and `n` columns. If it is not possible to reshape the array, return an empty 2D array.

Example 1:
Input: original = [1, 2, 3, 4], m = 2, n = 2
Output: [[1, 2], [3, 4]]
Explanation: The array is split into 2 rows and 2 columns.

Example 2:
Input: original = [1, 2, 3], m = 1, n = 3
Output: [[1, 2, 3]]
Explanation: The array is split into 1 row and 3 columns.

Example 3:
Input: original = [1, 2], m = 1, n = 1
Output: []
Explanation: It is impossible to reshape the array into a 1x1 2D array because it requires 1 element, but there are 2 elements in the original array.

Constraints:
- `1 <= original.length <= 5 * 10^4`
- `1 <= original[i] <= 10^5`
- `1 <= m, n <= 4 * 10^4`
"""

def construct2DArray(original, m, n):
    """
    Reshapes a 1D array into a 2D array with m rows and n columns.
    If the reshape is not possible, returns an empty 2D array.

    :param original: List[int] - The 1D array to reshape
    :param m: int - Number of rows in the 2D array
    :param n: int - Number of columns in the 2D array
    :return: List[List[int]] - The reshaped 2D array or an empty array if not possible
    """
    if len(original) != m * n:
        return []
    
    result = []
    for i in range(m):
        result.append(original[i * n:(i + 1) * n])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    original = [1, 2, 3, 4]
    m, n = 2, 2
    print(construct2DArray(original, m, n))  # Output: [[1, 2], [3, 4]]

    # Test Case 2
    original = [1, 2, 3]
    m, n = 1, 3
    print(construct2DArray(original, m, n))  # Output: [[1, 2, 3]]

    # Test Case 3
    original = [1, 2]
    m, n = 1, 1
    print(construct2DArray(original, m, n))  # Output: []

    # Test Case 4
    original = [1, 2, 3, 4, 5, 6]
    m, n = 3, 2
    print(construct2DArray(original, m, n))  # Output: [[1, 2], [3, 4], [5, 6]]

    # Test Case 5
    original = [1, 2, 3, 4, 5, 6]
    m, n = 2, 3
    print(construct2DArray(original, m, n))  # Output: [[1, 2, 3], [4, 5, 6]]

# Time Complexity Analysis:
# The function iterates through the `original` array once to construct the 2D array.
# Therefore, the time complexity is O(m * n), where m * n is the size of the 2D array.

# Space Complexity Analysis:
# The function creates a new 2D array to store the reshaped result.
# Therefore, the space complexity is O(m * n), where m * n is the size of the 2D array.

# Topic: Arrays