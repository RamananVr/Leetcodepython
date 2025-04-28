"""
LeetCode Problem #2738: Sum of Matrix After Queries

Problem Statement:
You are given an integer `n` and a 2D integer array `queries` where `queries[i] = [type, index, val]`.

- `type` can be either 0 or 1:
  - If `type == 0`, set all elements in the `index`-th row of an `n x n` matrix to `val`.
  - If `type == 1`, set all elements in the `index`-th column of an `n x n` matrix to `val`.

Initially, all elements of the matrix are 0. Return the sum of the elements in the matrix after processing all the queries.

Constraints:
- 1 <= n <= 10^4
- 1 <= queries.length <= 10^5
- 0 <= index < n
- 0 <= val <= 10^6
"""

def matrixSumQueries(n: int, queries: list[list[int]]) -> int:
    """
    Calculate the sum of the matrix after applying the queries.

    Args:
    n (int): The size of the matrix (n x n).
    queries (list[list[int]]): The list of queries to apply.

    Returns:
    int: The sum of the matrix after applying all queries.
    """
    # Track rows and columns that have been updated
    updated_rows = set()
    updated_cols = set()
    
    # Resultant sum
    total_sum = 0
    
    # Process queries in reverse order
    for query in reversed(queries):
        q_type, index, val = query
        
        if q_type == 0:  # Row update
            if index not in updated_rows:
                total_sum += val * (n - len(updated_cols))
                updated_rows.add(index)
        elif q_type == 1:  # Column update
            if index not in updated_cols:
                total_sum += val * (n - len(updated_rows))
                updated_cols.add(index)
    
    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 3
    queries1 = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 0, 4]]
    print(matrixSumQueries(n1, queries1))  # Expected Output: 23

    # Test Case 2
    n2 = 2
    queries2 = [[0, 0, 5], [1, 1, 10], [0, 1, 3]]
    print(matrixSumQueries(n2, queries2))  # Expected Output: 31

    # Test Case 3
    n3 = 4
    queries3 = [[0, 0, 7], [1, 2, 6], [0, 3, 5], [1, 1, 4]]
    print(matrixSumQueries(n3, queries3))  # Expected Output: 66

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each query is processed once in reverse order, so the time complexity is O(queries.length).
- Checking if a row or column is in the updated set is O(1) on average.
- Overall time complexity: O(queries.length).

Space Complexity:
- We use two sets to track updated rows and columns, which can each grow up to size n.
- Space complexity: O(n).

Topic: Arrays, Simulation, HashSet
"""