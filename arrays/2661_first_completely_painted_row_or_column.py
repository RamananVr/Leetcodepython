"""
LeetCode Question #2661: First Completely Painted Row or Column

Problem Statement:
You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, n * m].

Go through arr from the beginning and paint the cell in mat which has the integer from arr. Return the index of the first element in arr which paints either a complete row or a complete column in mat.

Examples:
Example 1:
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column are complete after arr[2] is painted.

Example 2:
Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
Output: 3
Explanation: The second column is complete after arr[3] is painted.

Constraints:
- m == mat.length
- n == mat[i].length
- arr.length == m * n
- 1 <= m, n <= 10^5
- 1 <= arr[i], mat[i][j] <= m * n
- All the integers of arr are unique.
- All the integers of mat are unique.
"""

from typing import List

def firstCompleteIndex(arr: List[int], mat: List[List[int]]) -> int:
    """
    Find the first index where a complete row or column is painted.
    
    Strategy:
    1. Create a mapping from value to position in matrix
    2. Keep track of how many cells are painted in each row/column
    3. Return when any row or column is completely painted
    """
    m, n = len(mat), len(mat[0])
    
    # Create mapping from value to (row, col) position
    value_to_pos = {}
    for i in range(m):
        for j in range(n):
            value_to_pos[mat[i][j]] = (i, j)
    
    # Track painted cells in each row and column
    row_count = [0] * m
    col_count = [0] * n
    
    # Process elements in arr
    for idx, value in enumerate(arr):
        row, col = value_to_pos[value]
        
        # Update counts
        row_count[row] += 1
        col_count[col] += 1
        
        # Check if row or column is complete
        if row_count[row] == n or col_count[col] == m:
            return idx
    
    return -1  # Should never reach here given constraints

def firstCompleteIndexOptimized(arr: List[int], mat: List[List[int]]) -> int:
    """
    Optimized version with slightly better organization.
    """
    m, n = len(mat), len(mat[0])
    
    # Build position mapping
    pos_map = {}
    for r in range(m):
        for c in range(n):
            pos_map[mat[r][c]] = (r, c)
    
    # Initialize counters
    row_painted = [0] * m
    col_painted = [0] * n
    
    # Paint cells and check completion
    for i, num in enumerate(arr):
        r, c = pos_map[num]
        row_painted[r] += 1
        col_painted[c] += 1
        
        # Check if any row or column is complete
        if row_painted[r] == n or col_painted[c] == m:
            return i
    
    return -1

def firstCompleteIndexSet(arr: List[int], mat: List[List[int]]) -> int:
    """
    Alternative approach using sets to track painted cells.
    """
    m, n = len(mat), len(mat[0])
    
    # Create mapping and initialize painted sets
    value_to_pos = {}
    painted_in_row = [set() for _ in range(m)]
    painted_in_col = [set() for _ in range(n)]
    
    for i in range(m):
        for j in range(n):
            value_to_pos[mat[i][j]] = (i, j)
    
    # Process painting
    for idx, value in enumerate(arr):
        row, col = value_to_pos[value]
        
        painted_in_row[row].add(col)
        painted_in_col[col].add(row)
        
        # Check completion
        if len(painted_in_row[row]) == n or len(painted_in_col[col]) == m:
            return idx
    
    return -1

def firstCompleteIndexVerbose(arr: List[int], mat: List[List[int]]) -> int:
    """
    Verbose version for debugging and understanding.
    """
    m, n = len(mat), len(mat[0])
    print(f"Matrix dimensions: {m}x{n}")
    
    # Create position mapping
    pos_map = {}
    for i in range(m):
        for j in range(n):
            pos_map[mat[i][j]] = (i, j)
    
    print(f"Position mapping: {pos_map}")
    
    # Initialize tracking
    row_count = [0] * m
    col_count = [0] * n
    
    # Process each element
    for idx, num in enumerate(arr):
        row, col = pos_map[num]
        row_count[row] += 1
        col_count[col] += 1
        
        print(f"Step {idx}: Paint {num} at ({row},{col})")
        print(f"  Row counts: {row_count}")
        print(f"  Col counts: {col_count}")
        
        # Check completion
        if row_count[row] == n:
            print(f"  Row {row} completed!")
            return idx
        if col_count[col] == m:
            print(f"  Column {col} completed!")
            return idx
    
    return -1

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([1, 3, 4, 2], [[1, 4], [2, 3]], 2),
        ([2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]], 3),
        ([1, 4, 2, 3], [[1, 2], [3, 4]], 1),
        ([1], [[1]], 0),
        ([1, 2, 3, 4, 5, 6], [[1, 2, 3], [4, 5, 6]], 2)
    ]
    
    print("Testing main approach:")
    for arr, mat, expected in test_cases:
        result = firstCompleteIndex(arr, mat)
        print(f"firstCompleteIndex({arr}, {mat}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting optimized approach:")
    for arr, mat, expected in test_cases:
        result = firstCompleteIndexOptimized(arr, mat)
        print(f"firstCompleteIndexOptimized({arr}, {mat}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting set approach:")
    for arr, mat, expected in test_cases:
        result = firstCompleteIndexSet(arr, mat)
        print(f"firstCompleteIndexSet({arr}, {mat}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    # Detailed trace for first example
    print("\nDetailed trace for first example:")
    firstCompleteIndexVerbose([1, 3, 4, 2], [[1, 4], [2, 3]])

"""
Time and Space Complexity Analysis:

All Approaches:
Time Complexity: O(m * n + len(arr)) = O(m * n) since len(arr) = m * n
- O(m * n) to build position mapping
- O(m * n) to process array elements
Space Complexity: O(m * n + m + n) = O(m * n) 
- O(m * n) for position mapping
- O(m + n) for row/column counters

Main Approach:
- Uses simple arrays to count painted cells
- Most memory efficient

Set Approach:
- Uses sets to track painted positions
- Slightly more memory overhead but same complexity

Key Insights:
1. Need to map each value to its matrix position
2. Track progress for each row and column separately
3. First completion (row or column) determines the answer
4. Since arr contains all matrix values exactly once, completion is guaranteed

Optimization Notes:
- Position mapping is essential for O(1) lookups
- Counter arrays are more efficient than sets for this problem
- Early termination when first complete row/column is found

Topic: Arrays, Matrix, Hash Map, Simulation, Counting
"""
