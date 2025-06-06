"""
LeetCode Problem #2643: Row With Maximum Ones

Problem Statement:
Given a m x n binary matrix mat, find the 0-indexed row that contains the maximum count of ones, and the number of ones in that row.

In case there are multiple rows that have the maximum count of ones, the row with the smallest index should be returned.

Return an array containing the index of the row, and the number of ones in that row.

Constraints:
- m == mat.length
- n == mat[i].length  
- 1 <= m, n <= 100
- mat[i][j] is either 0 or 1

Examples:
Input: mat = [[0,1],[1,0]]
Output: [0,1]
Explanation: Both rows have the same number of 1's. But the first row is smaller, so we return [0,1].

Input: mat = [[0,0,0],[0,1,1]]
Output: [1,2]
Explanation: The row indexed 1 has the maximum count of ones (2).

Input: mat = [[0,0],[1,1],[0,0]]
Output: [1,2]
Explanation: The row indexed 1 has the maximum count of ones (2).
"""

def rowAndMaximumOnes(mat: list[list[int]]) -> list[int]:
    """
    Find the row with maximum number of ones.
    
    :param mat: Binary matrix
    :return: [row_index, max_ones_count]
    """
    max_ones = 0
    max_row_index = 0
    
    for i in range(len(mat)):
        # Count the number of ones in the current row
        ones_count = sum(mat[i])
        
        # Update if we found a row with more ones
        if ones_count > max_ones:
            max_ones = ones_count
            max_row_index = i
    
    return [max_row_index, max_ones]

def build_tree_from_list(values):
    """Helper function to build a tree from a list (for testing purposes)"""
    if not values or values[0] is None:
        return None
    # This is a placeholder for tree building if needed
    return values

def tree_to_list(root):
    """Helper function to convert tree to list (for testing purposes)"""
    if not root:
        return []
    # This is a placeholder for tree conversion if needed
    return root

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Multiple rows with same count, return smallest index
    print("Test Case 1:")
    mat1 = [[0, 1], [1, 0]]
    result1 = rowAndMaximumOnes(mat1)
    print(f"Input: {mat1}")
    print(f"Output: {result1}")  # Expected Output: [0, 1]
    
    # Test Case 2: Clear maximum in row 1
    print("\nTest Case 2:")
    mat2 = [[0, 0, 0], [0, 1, 1]]
    result2 = rowAndMaximumOnes(mat2)
    print(f"Input: {mat2}")
    print(f"Output: {result2}")  # Expected Output: [1, 2]
    
    # Test Case 3: Maximum in the middle row
    print("\nTest Case 3:")
    mat3 = [[0, 0], [1, 1], [0, 0]]
    result3 = rowAndMaximumOnes(mat3)
    print(f"Input: {mat3}")
    print(f"Output: {result3}")  # Expected Output: [1, 2]
    
    # Test Case 4: All zeros
    print("\nTest Case 4:")
    mat4 = [[0, 0], [0, 0], [0, 0]]
    result4 = rowAndMaximumOnes(mat4)
    print(f"Input: {mat4}")
    print(f"Output: {result4}")  # Expected Output: [0, 0]
    
    # Test Case 5: All ones in first row
    print("\nTest Case 5:")
    mat5 = [[1, 1, 1], [0, 1, 0], [1, 0, 1]]
    result5 = rowAndMaximumOnes(mat5)
    print(f"Input: {mat5}")
    print(f"Output: {result5}")  # Expected Output: [0, 3]
    
    # Test Case 6: Single row, single column
    print("\nTest Case 6:")
    mat6 = [[1]]
    result6 = rowAndMaximumOnes(mat6)
    print(f"Input: {mat6}")
    print(f"Output: {result6}")  # Expected Output: [0, 1]
    
    # Test Case 7: Large matrix with maximum at the end
    print("\nTest Case 7:")
    mat7 = [[0, 1, 0], [1, 0, 1], [0, 0, 0], [1, 1, 1]]
    result7 = rowAndMaximumOnes(mat7)
    print(f"Input: {mat7}")
    print(f"Output: {result7}")  # Expected Output: [3, 3]
    
    # Test Case 8: Multiple rows with same maximum count
    print("\nTest Case 8:")
    mat8 = [[1, 1, 0], [0, 1, 1], [1, 0, 1]]
    result8 = rowAndMaximumOnes(mat8)
    print(f"Input: {mat8}")
    print(f"Output: {result8}")  # Expected Output: [0, 2] (first row with count 2)

"""
Time and Space Complexity Analysis:

Time Complexity:
- We iterate through each row of the matrix once: O(m)
- For each row, we count the ones by summing the row: O(n)
- Overall time complexity: O(m * n), where m is the number of rows and n is the number of columns

Space Complexity:
- We only use a constant amount of extra space for variables (max_ones, max_row_index, ones_count)
- Overall space complexity: O(1)

Algorithm Explanation:
1. Initialize variables to track the maximum count of ones and the corresponding row index
2. Iterate through each row of the matrix
3. For each row, count the number of ones using sum()
4. If the current count is greater than the maximum seen so far, update both the maximum count and row index
5. Return the row index and maximum count as a list

The key insight is that we only need to update when we find a STRICTLY greater count of ones, 
which automatically handles the case where multiple rows have the same count (we keep the first one).

Topic: Arrays, Matrix
"""
