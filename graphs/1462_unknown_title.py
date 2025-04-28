"""
LeetCode Problem #1462: Course Schedule IV

Problem Statement:
There are a total of `n` courses labeled from `0` to `n-1`. You are given an array `prerequisites` where 
`prerequisites[i] = [ai, bi]` indicates that you must take course `bi` before course `ai`.

You are also given an array `queries` where `queries[j] = [uj, vj]`. For the `j-th` query, you should answer 
whether course `uj` is a prerequisite of course `vj` or not.

Return a boolean array `result`, where `result[j]` is the answer to the `j-th` query.

Constraints:
- `2 <= n <= 100`
- `0 <= prerequisites.length <= (n * (n - 1) / 2)`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- The prerequisites graph has no cycles.
- `1 <= queries.length <= 10^4`
- `queries[j].length == 2`
- `0 <= uj, vj < n`
- `uj != vj`

Follow-up: Could you optimize your solution to handle up to `10^4` queries?

"""

from typing import List

def checkIfPrerequisite(n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    """
    Solution using Floyd-Warshall algorithm to determine if a course is a prerequisite of another.
    """
    # Initialize a 2D matrix to track prerequisites
    is_prerequisite = [[False] * n for _ in range(n)]
    
    # Mark direct prerequisites
    for a, b in prerequisites:
        is_prerequisite[a][b] = True
    
    # Floyd-Warshall algorithm to compute transitive closure
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if is_prerequisite[i][k] and is_prerequisite[k][j]:
                    is_prerequisite[i][j] = True
    
    # Answer the queries
    result = []
    for u, v in queries:
        result.append(is_prerequisite[u][v])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 2
    prerequisites = [[0, 1]]
    queries = [[0, 1], [1, 0]]
    print(checkIfPrerequisite(n, prerequisites, queries))  # Output: [True, False]

    # Test Case 2
    n = 4
    prerequisites = [[0, 1], [1, 2], [2, 3]]
    queries = [[0, 3], [3, 0], [1, 3], [3, 1]]
    print(checkIfPrerequisite(n, prerequisites, queries))  # Output: [True, False, True, False]

    # Test Case 3
    n = 3
    prerequisites = []
    queries = [[0, 1], [1, 2], [2, 0]]
    print(checkIfPrerequisite(n, prerequisites, queries))  # Output: [False, False, False]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Constructing the `is_prerequisite` matrix takes O(n^2).
- The Floyd-Warshall algorithm runs in O(n^3) since it involves three nested loops over `n`.
- Answering the queries takes O(q), where `q` is the number of queries.
- Overall time complexity: O(n^3 + q).

Space Complexity:
- The `is_prerequisite` matrix requires O(n^2) space.
- Overall space complexity: O(n^2).

Topic: Graphs
"""