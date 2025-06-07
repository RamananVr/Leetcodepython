"""
LeetCode Problem #2646: Minimize the Total Price of the Trips

Problem Statement:
There exists an undirected and unrooted tree with n nodes indexed from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Each node has an associated price. You are given an integer array price where price[i] is the price of the ith node.

The price of a path is the sum of the prices of all nodes lying on the path.

Additionally, you are given a 2D integer array trips where trips[i] = [starti, endi] indicates that you start the ith trip from node starti and travel to node endi by any path.

Before performing any trip, you can choose some nodes and reduce their prices by half. However, you can only reduce the price of each node at most once.

Return the minimum total price to perform all the given trips after the optimal price reduction.

Example 1:
Input: n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,2],[2,3]]
Output: 23
Explanation: 
The diagram above denotes the original tree where the red nodes are the starting and ending nodes.
- For trip [0,2], we choose path [0,1,2]. The trip costs 2 + 2 + 10 = 14.
- For trip [2,3], we choose path [2,1,3]. The trip costs 10 + 2 + 6 = 18.
Total cost before reduction: 14 + 18 = 32.
We can reduce the price of nodes 1 and 10 by half. The new prices become [2,1,5,6].
- For trip [0,2], the cost becomes 2 + 1 + 5 = 8.
- For trip [2,3], the cost becomes 5 + 1 + 6 = 12.
Total cost after reduction: 8 + 12 = 20.

Example 2:
Input: n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]
Output: 1
Explanation: There is only one node in the path, which is node 0, so we reduce its price to 1.

Constraints:
- 1 <= n <= 50
- edges.length == n - 1
- 0 <= ai, bi <= n - 1
- edges represents a valid tree
- price.length == n
- price[i] is an even integer.
- 1 <= price[i] <= 1000
- 1 <= trips.length <= 100
- 0 <= starti, endi <= n - 1
"""

from collections import defaultdict, deque
from typing import List

def minimumTotalPrice(n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
    """
    Approach:
    1. Build adjacency list from edges
    2. For each trip, find the path using BFS/DFS
    3. Count frequency of each node usage across all trips
    4. Use tree DP to determine optimal nodes to reduce (similar to House Robber on Tree)
    """
    # Build adjacency list
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # Function to find path between two nodes in tree
    def find_path(start: int, end: int) -> List[int]:
        if start == end:
            return [start]
        
        parent = [-1] * n
        visited = [False] * n
        queue = deque([start])
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            if node == end:
                break
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        # Reconstruct path
        path = []
        current = end
        while current != -1:
            path.append(current)
            current = parent[current]
        
        return path[::-1]
    
    # Count frequency of each node usage
    count = [0] * n
    for start, end in trips:
        path = find_path(start, end)
        for node in path:
            count[node] += 1
    
    # Tree DP to find optimal nodes to reduce
    # For each node: dp[node][0] = min cost without reducing node
    #                dp[node][1] = min cost with reducing node
    def dfs(node: int, parent: int) -> tuple:
        # Cost without reducing current node
        cost_no_reduce = price[node] * count[node]
        # Cost with reducing current node
        cost_reduce = (price[node] // 2) * count[node]
        
        for neighbor in graph[node]:
            if neighbor != parent:
                child_no_reduce, child_reduce = dfs(neighbor, node)
                # If we don't reduce current node, we can choose optimal for child
                cost_no_reduce += min(child_no_reduce, child_reduce)
                # If we reduce current node, we cannot reduce adjacent child
                cost_reduce += child_no_reduce
        
        return cost_no_reduce, cost_reduce
    
    # Start DFS from node 0 (any node works since it's a tree)
    no_reduce, reduce = dfs(0, -1)
    return min(no_reduce, reduce)

def minimumTotalPriceAlternative(n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
    """
    Alternative approach using DFS for path finding
    """
    # Build adjacency list
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # DFS to find path between two nodes
    def find_path_dfs(start: int, end: int, visited: set, path: List[int]) -> bool:
        if start == end:
            path.append(start)
            return True
        
        visited.add(start)
        path.append(start)
        
        for neighbor in graph[start]:
            if neighbor not in visited:
                if find_path_dfs(neighbor, end, visited, path):
                    return True
        
        path.pop()
        return False
    
    # Count node frequencies
    count = [0] * n
    for start, end in trips:
        path = []
        visited = set()
        find_path_dfs(start, end, visited, path)
        for node in path:
            count[node] += 1
    
    # Tree DP
    def dfs(node: int, parent: int) -> tuple:
        cost_no_reduce = price[node] * count[node]
        cost_reduce = (price[node] // 2) * count[node]
        
        for neighbor in graph[node]:
            if neighbor != parent:
                child_no_reduce, child_reduce = dfs(neighbor, node)
                cost_no_reduce += min(child_no_reduce, child_reduce)
                cost_reduce += child_no_reduce
        
        return cost_no_reduce, cost_reduce
    
    no_reduce, reduce = dfs(0, -1)
    return min(no_reduce, reduce)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 4
    edges1 = [[0,1],[1,2],[1,3]]
    price1 = [2,2,10,6]
    trips1 = [[0,2],[2,3]]
    print(f"Test Case 1: {minimumTotalPrice(n1, edges1, price1, trips1)}")  # Expected: 23
    
    # Test Case 2
    n2 = 2
    edges2 = [[0,1]]
    price2 = [2,2]
    trips2 = [[0,0]]
    print(f"Test Case 2: {minimumTotalPrice(n2, edges2, price2, trips2)}")  # Expected: 1
    
    # Test Case 3: Single node tree
    n3 = 1
    edges3 = []
    price3 = [4]
    trips3 = [[0,0]]
    print(f"Test Case 3: {minimumTotalPrice(n3, edges3, price3, trips3)}")  # Expected: 2
    
    # Test Case 4: Linear tree
    n4 = 3
    edges4 = [[0,1],[1,2]]
    price4 = [4,6,8]
    trips4 = [[0,2]]
    print(f"Test Case 4: {minimumTotalPrice(n4, edges4, price4, trips4)}")  # Expected: 11 (reduce nodes 0,2)

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph: O(n)
- Finding paths for all trips: O(trips * n) in worst case
- Tree DP: O(n)
- Overall: O(trips * n + n) = O(trips * n)

Space Complexity:
- Graph adjacency list: O(n)
- Path finding: O(n) for recursion stack
- Count array: O(n)
- Overall: O(n)

Topic: Tree, Dynamic Programming, Graph
"""
