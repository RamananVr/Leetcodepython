"""
LeetCode Problem #547: Number of Provinces

Problem Statement:
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, 
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly 
connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:
- 1 <= n <= 200
- isConnected[i][j] is 1 or 0.
- isConnected[i][i] == 1
- isConnected[i][j] == isConnected[j][i]
"""

# Solution
def findCircleNum(isConnected):
    def dfs(node):
        for neighbor in range(len(isConnected)):
            if isConnected[node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    n = len(isConnected)
    visited = set()
    provinces = 0

    for i in range(n):
        if i not in visited:
            provinces += 1
            visited.add(i)
            dfs(i)

    return provinces

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    isConnected1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(findCircleNum(isConnected1))  # Output: 2

    # Test Case 2
    isConnected2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(findCircleNum(isConnected2))  # Output: 3

    # Test Case 3
    isConnected3 = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
    print(findCircleNum(isConnected3))  # Output: 2

    # Test Case 4
    isConnected4 = [[1]]
    print(findCircleNum(isConnected4))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm uses Depth First Search (DFS) to traverse the graph.
- In the worst case, we visit each node and its neighbors once, resulting in O(n^2) time complexity, 
  where n is the number of cities (nodes in the graph).

Space Complexity:
- The space complexity is O(n) due to the `visited` set and the recursive call stack in DFS.

Overall:
Time Complexity: O(n^2)
Space Complexity: O(n)
"""

# Topic: Graphs