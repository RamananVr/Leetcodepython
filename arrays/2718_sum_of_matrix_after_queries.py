"""
LeetCode Question #2718: Sum of Matrix After Queries

Problem Statement:
You are given an integer `n` and a 0-indexed 2D array `queries` where `queries[i] = [type_i, index_i, val_i]`.

Initially, there is a 0-indexed `n x n` matrix filled with `0`s. For each query, you must apply one of the following changes:
- if `type_i == 0`, set the values in the row `index_i` to `val_i`, overriding any previous values.
- if `type_i == 1`, set the values in the column `index_i` to `val_i`, overriding any previous values.

Return the sum of integers in the matrix after all queries are applied.

Constraints:
- `1 <= n <= 10^4`
- `1 <= queries.length <= 5 * 10^4`
- `queries[i].length == 3`
- `0 <= type_i <= 1`
- `0 <= index_i < n`
- `0 <= val_i <= 10^5`

Example:
Input: n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
Output: 23
Explanation: The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 23.

Input: n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
Output: 17
Explanation: The sum of the matrix after all queries are applied is 17.
"""

def matrixSumQueries(n, queries):
    """
    Calculate the sum of matrix after applying all queries.
    
    Args:
        n: Integer representing the size of the n x n matrix
        queries: List of queries where each query is [type, index, val]
    
    Returns:
        Integer representing the sum of all elements in the matrix
    """
    # Process queries in reverse order to handle overwrites efficiently
    row_set = set()
    col_set = set()
    total_sum = 0
    
    # Process queries in reverse to handle overwrites
    for i in range(len(queries) - 1, -1, -1):
        query_type, index, val = queries[i]
        
        if query_type == 0:  # Row operation
            if index not in row_set:
                row_set.add(index)
                # Add value for columns not yet processed
                total_sum += val * (n - len(col_set))
        else:  # Column operation
            if index not in col_set:
                col_set.add(index)
                # Add value for rows not yet processed
                total_sum += val * (n - len(row_set))
    
    return total_sum

def matrixSumQueries_simulation(n, queries):
    """
    Brute force approach using matrix simulation.
    
    Args:
        n: Integer representing the size of the n x n matrix
        queries: List of queries where each query is [type, index, val]
    
    Returns:
        Integer representing the sum of all elements in the matrix
    """
    matrix = [[0] * n for _ in range(n)]
    
    for query_type, index, val in queries:
        if query_type == 0:  # Row operation
            for j in range(n):
                matrix[index][j] = val
        else:  # Column operation
            for i in range(n):
                matrix[i][index] = val
    
    return sum(sum(row) for row in matrix)

def matrixSumQueries_optimized(n, queries):
    """
    Optimized approach using last update tracking.
    
    Args:
        n: Integer representing the size of the n x n matrix
        queries: List of queries where each query is [type, index, val]
    
    Returns:
        Integer representing the sum of all elements in the matrix
    """
    # Track the last update for each row and column
    row_vals = [0] * n
    col_vals = [0] * n
    row_time = [-1] * n
    col_time = [-1] * n
    
    for time, (query_type, index, val) in enumerate(queries):
        if query_type == 0:  # Row operation
            row_vals[index] = val
            row_time[index] = time
        else:  # Column operation
            col_vals[index] = val
            col_time[index] = time
    
    total_sum = 0
    for i in range(n):
        for j in range(n):
            # Use the value from the most recent operation
            if row_time[i] > col_time[j]:
                total_sum += row_vals[i]
            else:
                total_sum += col_vals[j]
    
    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
    result = matrixSumQueries(n, queries)
    print(f"Test 1 - Expected: 23, Got: {result}")
    assert result == 23
    
    # Test Case 2
    n = 3
    queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
    result = matrixSumQueries(n, queries)
    print(f"Test 2 - Expected: 17, Got: {result}")
    assert result == 17
    
    # Test Case 3 - Single query
    n = 2
    queries = [[0,0,5]]
    result = matrixSumQueries(n, queries)
    print(f"Test 3 - Expected: 10, Got: {result}")
    assert result == 10
    
    # Test Case 4 - Column only queries
    n = 2
    queries = [[1,0,3],[1,1,4]]
    result = matrixSumQueries(n, queries)
    print(f"Test 4 - Expected: 14, Got: {result}")
    assert result == 14
    
    # Test Case 5 - Large matrix
    n = 4
    queries = [[0,0,1],[1,1,2],[0,2,3],[1,3,4]]
    result = matrixSumQueries(n, queries)
    print(f"Test 5 - Expected: 26, Got: {result}")
    assert result == 26
    
    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

Optimal Solution (Reverse Processing):
1. Time Complexity: O(q) where q is the number of queries
   - We process each query once in reverse order
   - Each query operation is O(1)

2. Space Complexity: O(n) for storing row and column sets

Simulation Solution:
1. Time Complexity: O(n^2 + q*n) 
   - O(q*n) for processing queries (each row/column operation takes O(n))
   - O(n^2) for summing the final matrix

2. Space Complexity: O(n^2) for storing the matrix

Optimized Solution:
1. Time Complexity: O(q + n^2)
   - O(q) for processing queries
   - O(n^2) for calculating final sum

2. Space Complexity: O(n) for storing last update information

Topic: Arrays, Matrix Operations, Greedy
"""
