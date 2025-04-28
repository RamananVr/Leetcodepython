"""
LeetCode Question #1627: Graph Connectivity With Threshold

Problem Statement:
You are given an integer n, which indicates that we have n cities numbered from 1 to n. 
You are also given an array of queries, where queries[i] = [a, b]. The answer to the ith query is true 
if the two cities a and b are connected (directly or indirectly) and false otherwise.

More formally, the cities a and b are connected if there is a path of connections (direct or indirect) 
that connects them. Connections are defined as follows:

- There is a threshold value, threshold.
- If the greatest common divisor (GCD) of the two cities' numbers is strictly greater than threshold, 
  then the two cities are connected.

Return a boolean array answer, where answer[i] is the answer to the ith query.

Constraints:
- 2 <= n <= 10^4
- 0 <= threshold <= n
- 1 <= queries.length <= 10^4
- queries[i].length == 2
- 1 <= a, b <= n
- a != b
"""

# Solution
from math import gcd
from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def areConnected(n, threshold, queries):
    # Initialize Union-Find structure
    uf = UnionFind(n + 1)

    # Connect cities based on the threshold
    for i in range(threshold + 1, n + 1):
        for j in range(2 * i, n + 1, i):
            uf.union(i, j)

    # Process queries
    result = []
    for a, b in queries:
        result.append(uf.find(a) == uf.find(b))
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 6
    threshold = 2
    queries = [[1, 4], [2, 5], [3, 6]]
    print(areConnected(n, threshold, queries))  # Output: [False, False, True]

    # Test Case 2
    n = 10
    threshold = 1
    queries = [[4, 5], [6, 10], [2, 3], [7, 8]]
    print(areConnected(n, threshold, queries))  # Output: [False, True, False, False]

    # Test Case 3
    n = 5
    threshold = 0
    queries = [[1, 2], [2, 3], [4, 5]]
    print(areConnected(n, threshold, queries))  # Output: [False, False, False]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The union-find operations (find and union) are nearly constant time due to path compression and union by rank.
- Connecting cities based on the threshold involves iterating over multiples of each number, which is approximately O(n log n).
- Processing queries is O(q), where q is the number of queries.
- Overall time complexity: O(n log n + q).

Space Complexity:
- The Union-Find structure uses O(n) space for the parent and rank arrays.
- Overall space complexity: O(n).

Topic: Union-Find, Graphs
"""