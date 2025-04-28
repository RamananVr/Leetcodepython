"""
LeetCode Problem #947: Most Stones Removed with Same Row or Column

Problem Statement:
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

Constraints:
1. 1 <= stones.length <= 1000
2. 0 <= xi, yi <= 10^4
3. No two stones are at the same coordinate point.

Example:
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
- Remove stone [2,2] because it shares the same row as [2,1].
- Remove stone [2,1] because it shares the same column as [1,1].
- Remove stone [1,2] because it shares the same row as [1,0].
- Remove stone [1,0] because it shares the same column as [0,0].
- Remove stone [0,1] because it shares the same row as [0,0].
The final stone is [0,0].

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3

Input: stones = [[0,0]]
Output: 0
"""

from collections import defaultdict

def removeStones(stones):
    """
    Function to calculate the maximum number of stones that can be removed.
    Uses Union-Find (Disjoint Set Union) to group stones by connected components.
    """
    parent = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootX] = rootY

    # Initialize Union-Find for all stones
    for x, y in stones:
        # Use (x, ~y) to differentiate rows and columns in the same namespace
        if x not in parent:
            parent[x] = x
        if ~y not in parent:
            parent[~y] = ~y
        union(x, ~y)

    # Count the number of connected components
    unique_roots = len(set(find(x) for x in parent))
    return len(stones) - unique_roots


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    stones1 = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    print(removeStones(stones1))  # Output: 5

    # Test Case 2
    stones2 = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    print(removeStones(stones2))  # Output: 3

    # Test Case 3
    stones3 = [[0,0]]
    print(removeStones(stones3))  # Output: 0

    # Test Case 4
    stones4 = [[0,1],[1,0],[1,1]]
    print(removeStones(stones4))  # Output: 2

    # Test Case 5
    stones5 = [[0,0],[1,1],[2,2],[3,3]]
    print(removeStones(stones5))  # Output: 0


"""
Time and Space Complexity Analysis:

Time Complexity:
- The Union-Find operations (find and union) are nearly constant time due to path compression and union by rank.
- For n stones, we perform O(n) union operations and O(n) find operations.
- Thus, the overall time complexity is O(n * α(n)), where α(n) is the inverse Ackermann function, which grows very slowly and is nearly constant for practical inputs.

Space Complexity:
- We use a dictionary `parent` to store the parent of each node. The size of this dictionary is proportional to the number of unique rows and columns, which is O(n) in the worst case.
- Thus, the space complexity is O(n).

Topic: Union-Find (Disjoint Set Union)
"""