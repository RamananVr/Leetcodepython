"""
LeetCode Question #834: Sum of Distances in Tree

Problem Statement:
You are given an integer `n`, the number of nodes in a tree, and an array `edges` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the tree.

Return an array `answer` of size `n` where `answer[i]` is the sum of the distances between the ith node and all other nodes in the tree.

Example:
Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]

Explanation:
The tree looks like this:
        0
       / \
      1   2
         /|\
        3 4 5

The sum of distances for each node is:
- Node 0: 8 (distance to nodes 1, 2, 3, 4, 5)
- Node 1: 12 (distance to nodes 0, 2, 3, 4, 5)
- Node 2: 6 (distance to nodes 0, 1, 3, 4, 5)
- Node 3: 10 (distance to nodes 0, 1, 2, 4, 5)
- Node 4: 10 (distance to nodes 0, 1, 2, 3, 5)
- Node 5: 10 (distance to nodes 0, 1, 2, 3, 4)

Constraints:
- 1 <= n <= 3 * 10^4
- edges.length == n - 1
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- The input is guaranteed to be a tree.
"""

# Python Solution
from collections import defaultdict

def sumOfDistancesInTree(n, edges):
    # Build the tree as an adjacency list
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # Initialize variables
    count = [1] * n  # Count of nodes in the subtree rooted at each node
    answer = [0] * n  # Sum of distances for each node
    
    # Post-order DFS to calculate subtree sizes and initial distances
    def postOrder(node, parent):
        for neighbor in tree[node]:
            if neighbor != parent:
                postOrder(neighbor, node)
                count[node] += count[neighbor]
                answer[node] += answer[neighbor] + count[neighbor]
    
    # Pre-order DFS to calculate final distances using parent-child relationship
    def preOrder(node, parent):
        for neighbor in tree[node]:
            if neighbor != parent:
                answer[neighbor] = answer[node] - count[neighbor] + (n - count[neighbor])
                preOrder(neighbor, node)
    
    # Start DFS from node 0 (arbitrary root)
    postOrder(0, -1)
    preOrder(0, -1)
    
    return answer

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 6
    edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    print(sumOfDistancesInTree(n, edges))  # Output: [8, 12, 6, 10, 10, 10]

    # Test Case 2
    n = 4
    edges = [[0,1],[1,2],[1,3]]
    print(sumOfDistancesInTree(n, edges))  # Output: [6, 4, 6, 6]

    # Test Case 3
    n = 1
    edges = []
    print(sumOfDistancesInTree(n, edges))  # Output: [0]

    # Test Case 4
    n = 2
    edges = [[0,1]]
    print(sumOfDistancesInTree(n, edges))  # Output: [1, 1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the adjacency list takes O(n).
- The post-order DFS traverses each edge once, taking O(n).
- The pre-order DFS also traverses each edge once, taking O(n).
- Overall time complexity: O(n).

Space Complexity:
- The adjacency list takes O(n) space.
- The count and answer arrays each take O(n) space.
- The recursion stack for DFS takes O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Tree, DFS
"""