"""
LeetCode Problem #2097: Valid Arrangement of Pairs

Problem Statement:
You are given a 2D integer array pairs where pairs[i] = [start_i, end_i]. An arrangement of pairs is valid if for every 
i = 1, 2, ..., pairs.length - 1, the end of pairs[i-1] is equal to the start of pairs[i].

Return any valid arrangement of pairs.

Note:
- The input pairs are guaranteed to have at least one valid arrangement.
- You may return the pairs in any order as long as the arrangement is valid.

Constraints:
- 1 <= pairs.length <= 10^5
- pairs[i].length == 2
- 0 <= start_i, end_i <= 10^5
"""

from collections import defaultdict, deque

def validArrangement(pairs):
    """
    Function to find a valid arrangement of pairs.
    """
    # Step 1: Build the graph and calculate in-degrees and out-degrees
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    for start, end in pairs:
        graph[start].append(end)
        out_degree[start] += 1
        in_degree[end] += 1

    # Step 2: Find the starting node for Eulerian path
    start_node = pairs[0][0]  # Default start node
    for node in graph:
        if out_degree[node] - in_degree[node] == 1:
            start_node = node
            break

    # Step 3: Perform Hierholzer's algorithm to find the Eulerian path
    stack = [start_node]
    result = deque()

    while stack:
        while graph[stack[-1]]:
            next_node = graph[stack[-1]].pop()
            stack.append(next_node)
        result.appendleft(stack.pop())

    # Step 4: Convert the Eulerian path into the required pair arrangement
    arrangement = []
    result = list(result)
    for i in range(len(result) - 1):
        arrangement.append([result[i], result[i + 1]])

    return arrangement

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    pairs = [[5, 1], [4, 5], [11, 9], [9, 4]]
    print(validArrangement(pairs))
    # Output: [[11, 9], [9, 4], [4, 5], [5, 1]] (or any valid arrangement)

    # Test Case 2
    pairs = [[1, 3], [3, 2], [2, 1]]
    print(validArrangement(pairs))
    # Output: [[1, 3], [3, 2], [2, 1]] (or any valid arrangement)

    # Test Case 3
    pairs = [[1, 2], [2, 3], [3, 4]]
    print(validArrangement(pairs))
    # Output: [[1, 2], [2, 3], [3, 4]] (or any valid arrangement)

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(n), where n is the number of pairs.
- Finding the Eulerian path using Hierholzer's algorithm takes O(n) since we traverse each edge exactly once.
- Constructing the arrangement from the Eulerian path also takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- The graph is stored as an adjacency list, which takes O(n) space.
- The in-degree and out-degree dictionaries also take O(n) space.
- The stack and result deque take O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Graphs
"""