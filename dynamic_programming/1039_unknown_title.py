"""
LeetCode Problem #1039: Minimum Score Triangulation of Polygon

Problem Statement:
You are given a convex polygon with `n` vertices. The vertices are labeled from `0` to `n - 1` in clockwise order, and each vertex has an associated value represented by an integer array `values` where `values[i]` is the value of the `i-th` vertex.

You must triangulate the polygon into `n - 2` triangles. For each triangle, the score is the product of the values of its vertices, and the total score of the triangulation is the sum of these scores over all `n - 2` triangles.

Return the minimum score of the triangulation of the polygon.

Constraints:
- `n == values.length`
- `3 <= n <= 50`
- `1 <= values[i] <= 100`
"""

# Solution
def minScoreTriangulation(values):
    """
    Dynamic Programming solution to find the minimum score triangulation of a convex polygon.

    :param values: List[int] - The values of the vertices of the polygon.
    :return: int - The minimum score of the triangulation.
    """
    n = len(values)
    # dp[i][j] represents the minimum score triangulation for the sub-polygon from vertex i to vertex j
    dp = [[float('inf')] * n for _ in range(n)]

    # Base case: A triangle (3 vertices) has no sub-triangulation
    for i in range(n - 2):
        dp[i][i + 2] = values[i] * values[i + 1] * values[i + 2]

    # Fill the DP table for larger sub-polygons
    for length in range(3, n + 1):  # length of the sub-polygon
        for i in range(n - length + 1):  # start vertex
            j = i + length - 1  # end vertex
            for k in range(i + 1, j):  # k is the vertex forming a triangle with i and j
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[k] * values[j])

    return dp[0][n - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    values1 = [1, 2, 3]
    print(minScoreTriangulation(values1))  # Expected Output: 6

    # Test Case 2
    values2 = [3, 7, 4, 5]
    print(minScoreTriangulation(values2))  # Expected Output: 144

    # Test Case 3
    values3 = [1, 3, 1, 4, 1, 5]
    print(minScoreTriangulation(values3))  # Expected Output: 13

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop iterates over all possible lengths of sub-polygons (from 3 to n), which is O(n).
- The second loop iterates over all possible starting vertices for a given length, which is O(n).
- The innermost loop iterates over all possible vertices k between i and j, which is O(n).
- Therefore, the total time complexity is O(n^3).

Space Complexity:
- The space complexity is dominated by the DP table, which is of size n x n. Thus, the space complexity is O(n^2).
"""

# Topic: Dynamic Programming