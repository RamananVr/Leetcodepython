"""
LeetCode Problem #851: Loud and Rich

Problem Statement:
There is a group of n people labeled from 0 to n - 1 where each person has a different amount of money and a different level of quietness.

You are given an array `richer` where `richer[i] = [a, b]` indicates that person `a` has more money than person `b` and an integer array `quiet` where `quiet[i]` is the quietness of the i-th person. All the given data in richer are logically correct (i.e., the data will not lead to a cycle).

Return an integer array `answer` where `answer[x] = y` means that person `y` is the least quiet person (that is, the person `y` with the smallest value of `quiet[y]`) among all people who definitely have equal to or more money than the person `x` (including person `x`).

Example 1:
Input: richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]], quiet = [3, 2, 5, 4, 6, 1, 7, 0]
Output: [5, 5, 2, 5, 4, 5, 6, 7]
Explanation: 
answer[0] = 5.
Person 5 has more money than 3, which has more money than 1, which has more money than 0.
The only person who is quieter (with a lower quiet[x]) is person 5.
answer[7] = 7.
Among all people that have equal to or more money than person 7, the person who is the quietest (with quiet[7] = 0) is person 7 itself.

Example 2:
Input: richer = [], quiet = [0]
Output: [0]

Constraints:
- n == quiet.length
- 1 <= n <= 500
- 0 <= quiet[i] < n
- All the values of quiet are unique.
- 0 <= richer.length <= n * (n - 1) / 2
- 0 <= a, b < n
- a != b
- All the pairs (a, b) in richer are unique.
- The observations in richer are all logically consistent.
"""

from collections import defaultdict, deque

def loudAndRich(richer, quiet):
    n = len(quiet)
    graph = defaultdict(list)
    
    # Build the graph
    for a, b in richer:
        graph[b].append(a)
    
    # Result array
    answer = [-1] * n
    
    def dfs(node):
        # If already computed, return the result
        if answer[node] != -1:
            return answer[node]
        
        # Start with the current node
        answer[node] = node
        for neighbor in graph[node]:
            candidate = dfs(neighbor)
            if quiet[candidate] < quiet[answer[node]]:
                answer[node] = candidate
        
        return answer[node]
    
    # Compute the answer for each person
    for i in range(n):
        dfs(i)
    
    return answer

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
    quiet = [3, 2, 5, 4, 6, 1, 7, 0]
    print(loudAndRich(richer, quiet))  # Output: [5, 5, 2, 5, 4, 5, 6, 7]

    # Test Case 2
    richer = []
    quiet = [0]
    print(loudAndRich(richer, quiet))  # Output: [0]

    # Test Case 3
    richer = [[0, 1], [1, 2]]
    quiet = [1, 0, 2]
    print(loudAndRich(richer, quiet))  # Output: [0, 0, 0]

"""
Time Complexity:
- Building the graph takes O(E), where E is the number of edges in the `richer` list.
- The DFS traversal takes O(V + E), where V is the number of nodes (people) and E is the number of edges.
- Since we perform DFS for each node, the total complexity is O(V * (V + E)).
- In the worst case, E can be O(V^2), so the overall complexity is O(V^3).

Space Complexity:
- The graph representation takes O(E) space.
- The recursion stack in the worst case can go up to O(V).
- The `answer` array takes O(V) space.
- Overall space complexity is O(V + E).

Topic: Graph, Depth-First Search (DFS)
"""