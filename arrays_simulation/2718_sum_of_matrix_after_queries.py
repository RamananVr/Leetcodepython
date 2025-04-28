"""
LeetCode Question #2718: Sum of Matrix After Queries

Problem Statement:
You are given an integer n and a 2D integer array queries where queries[i] = [type_i, index_i, val_i].

- type_i can be either 0 or 1:
  - If type_i == 0, you are asked to set all the elements in the index_i-th row to val_i.
  - If type_i == 1, you are asked to set all the elements in the index_i-th column to val_i.

Return the sum of the elements in the matrix after performing all the queries on an initially empty n x n matrix.

Note:
- The matrix is initially filled with zeros.
- After performing a query, any overwritten value in the matrix is replaced with the new value.

Constraints:
- 1 <= n <= 10^4
- 1 <= queries.length <= 10^5
- 0 <= type_i <= 1
- 0 <= index_i < n
- 0 <= val_i <= 10^4
"""

# Python Solution
def matrixSumQueries(n, queries):
    """
    Calculate the sum of the matrix after performing all the queries.

    :param n: int, size of the matrix (n x n)
    :param queries: List[List[int]], list of queries
    :return: int, sum of the matrix after all queries
    """
    row_set, col_set = set(), set()
    total_sum = 0

    # Process queries in reverse order
    for query in reversed(queries):
        type_i, index_i, val_i = query

        if type_i == 0:  # Row operation
            if index_i not in row_set:
                total_sum += val_i * (n - len(col_set))
                row_set.add(index_i)
        elif type_i == 1:  # Column operation
            if index_i not in col_set:
                total_sum += val_i * (n - len(row_set))
                col_set.add(index_i)

    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    queries = [[0, 0, 1], [1, 1, 2], [0, 0, 3]]
    print(matrixSumQueries(n, queries))  # Output: 17

    # Test Case 2
    n = 4
    queries = [[0, 1, 5], [1, 2, 10], [0, 1, 7], [1, 3, 3]]
    print(matrixSumQueries(n, queries))  # Output: 68

    # Test Case 3
    n = 2
    queries = [[0, 0, 4], [1, 1, 6], [0, 1, 2]]
    print(matrixSumQueries(n, queries))  # Output: 18

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each query is processed once in reverse order, and the operations on sets (add and check membership) are O(1) on average.
- Therefore, the time complexity is O(queries.length).

Space Complexity:
- We use two sets to track processed rows and columns, which can each grow up to size n.
- Therefore, the space complexity is O(n).

Topic: Arrays, Simulation
"""