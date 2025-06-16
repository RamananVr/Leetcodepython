"""
2732. Find a Good Subset of the Matrix

You are given a 0-indexed m x n binary matrix grid.

Let us call a non-empty subset of rows good if for all pairs of rows in the subset, no two rows are identical.

Return any good subset of the rows of grid. If there are multiple answers, return any of them. If there are no good subsets, return an empty list.

A subset of rows of the matrix is any possible selection of 0 or more rows.

Example 1:
Input: grid = [[0,1,1,0],[0,0,0,1],[1,1,1,1]]
Output: [0,1]
Explanation: The rows at indices 0 and 1 are good.
Row 0: [0,1,1,0]
Row 1: [0,0,0,1]
The two rows are not identical.

Example 2:
Input: grid = [[0],[1],[0]]
Output: [0,1]
Explanation: The rows at indices 0 and 1 are good.
Row 0: [0]
Row 1: [1]
The two rows are not identical.

Example 3:
Input: grid = [[1],[1]]
Output: []
Explanation: There are duplicate rows, so there is no good subset.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10^4
- grid[i][j] is either 0 or 1.
"""

def good_subset_of_binary_matrix(grid: list[list[int]]) -> list[int]:
    """
    Find a good subset of rows where no two rows are identical.
    
    Args:
        grid: Binary matrix (m x n)
        
    Returns:
        list[int]: Indices of rows forming a good subset
        
    Time Complexity: O(m * n) - iterate through rows and compare
    Space Complexity: O(m * n) - storing seen rows as tuples in set
    """
    seen_rows = {}
    result = []
    
    for i, row in enumerate(grid):
        row_tuple = tuple(row)
        if row_tuple not in seen_rows:
            seen_rows[row_tuple] = i
            result.append(i)
    
    return result

def good_subset_of_binary_matrix_optimized(grid: list[list[int]]) -> list[int]:
    """
    Optimized version using bit manipulation for row comparison.
    
    Args:
        grid: Binary matrix
        
    Returns:
        list[int]: Indices of rows forming a good subset
        
    Time Complexity: O(m * n) - converting rows to integers and checking
    Space Complexity: O(m) - storing seen row bit representations
    """
    seen_rows = set()
    result = []
    
    for i, row in enumerate(grid):
        # Convert row to integer representation
        row_int = 0
        for j, bit in enumerate(row):
            if bit == 1:
                row_int |= (1 << j)
        
        if row_int not in seen_rows:
            seen_rows.add(row_int)
            result.append(i)
    
    return result

def good_subset_of_binary_matrix_greedy(grid: list[list[int]]) -> list[int]:
    """
    Greedy approach - try to find the largest good subset.
    
    Args:
        grid: Binary matrix
        
    Returns:
        list[int]: Indices of rows forming a good subset
        
    Time Complexity: O(m^2 * n) - comparing all pairs of rows
    Space Complexity: O(m) - storing result indices
    """
    m = len(grid)
    used = [False] * m
    result = []
    
    for i in range(m):
        if used[i]:
            continue
            
        # Add current row to result
        result.append(i)
        used[i] = True
        
        # Mark all identical rows as used
        for j in range(i + 1, m):
            if not used[j] and grid[i] == grid[j]:
                used[j] = True
    
    return result

def good_subset_of_binary_matrix_maximal(grid: list[list[int]]) -> list[int]:
    """
    Find maximal good subset by removing duplicates efficiently.
    
    Args:
        grid: Binary matrix
        
    Returns:
        list[int]: Indices of rows forming maximal good subset
        
    Time Complexity: O(m * n) - single pass with hash map
    Space Complexity: O(m * n) - storing row representations
    """
    row_to_indices = {}
    
    # Group identical rows
    for i, row in enumerate(grid):
        row_key = tuple(row)
        if row_key not in row_to_indices:
            row_to_indices[row_key] = []
        row_to_indices[row_key].append(i)
    
    # Take first occurrence of each unique row
    result = []
    for indices in row_to_indices.values():
        result.append(indices[0])  # Take first occurrence
    
    return sorted(result)

# Test cases
def test_good_subset_of_binary_matrix():
    test_cases = [
        # Basic test cases
        ([[0,1,1,0],[0,0,0,1],[1,1,1,1]], [0,1,2]),
        ([[0],[1],[0]], [0,1]),
        ([[1],[1]], [0]),
        
        # Edge cases
        ([[0]], [0]),                    # Single row
        ([[0,1],[0,1]], [0]),           # Two identical rows
        ([[0,1],[1,0]], [0,1]),         # Two different rows
        
        # Complex cases
        ([[1,0,1],[0,1,0],[1,0,1],[1,1,1]], [0,1,3]),  # Some duplicates
        ([[0,0],[0,1],[1,0],[1,1]], [0,1,2,3]),        # All different
        ([[1,1],[1,1],[1,1]], [0]),                     # All identical
        
        # Larger cases
        ([[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,1,0,0]], [0,1,3]),
        ([[1,0],[0,1],[1,0],[0,1],[1,1]], [0,1,4]),
    ]
    
    print("Testing good_subset_of_binary_matrix function:")
    for i, (grid, expected_pattern) in enumerate(test_cases):
        result1 = good_subset_of_binary_matrix(grid)
        result2 = good_subset_of_binary_matrix_optimized(grid)
        result3 = good_subset_of_binary_matrix_greedy(grid)
        result4 = good_subset_of_binary_matrix_maximal(grid)
        
        print(f"Test {i+1}: grid={grid}")
        print(f"  Basic: {result1}")
        print(f"  Optimized: {result2}")
        print(f"  Greedy: {result3}")
        print(f"  Maximal: {result4}")
        
        # Verify all results are valid good subsets
        def is_good_subset(grid, indices):
            if not indices:
                return True
            selected_rows = [tuple(grid[i]) for i in indices]
            return len(selected_rows) == len(set(selected_rows))
        
        assert is_good_subset(grid, result1), f"Basic result not valid for test {i+1}"
        assert is_good_subset(grid, result2), f"Optimized result not valid for test {i+1}"
        assert is_good_subset(grid, result3), f"Greedy result not valid for test {i+1}"
        assert is_good_subset(grid, result4), f"Maximal result not valid for test {i+1}"
        
        print(f"  ✓ All results are valid good subsets\n")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_good_subset_of_binary_matrix()

"""
Time Complexity Analysis:
- Basic Solution: O(m * n) - iterate through rows, tuple creation is O(n)
- Optimized Solution: O(m * n) - bit manipulation for row encoding
- Greedy Solution: O(m^2 * n) - comparing all pairs of rows
- Maximal Solution: O(m * n) - single pass with grouping

Space Complexity Analysis:
- Basic Solution: O(m * n) - storing row tuples in hash map
- Optimized Solution: O(m) - storing integer representations
- Greedy Solution: O(m) - boolean array and result
- Maximal Solution: O(m * n) - grouping identical rows

Key Insights:
1. The problem asks for any good subset, not necessarily the largest one
2. A good subset contains no duplicate rows
3. We can use hash maps or sets to efficiently detect duplicates
4. Bit manipulation can optimize space for binary matrices
5. The maximal good subset contains exactly one representative from each group of identical rows

Topics: Arrays, Hash Table, Bit Manipulation, Greedy
"""
