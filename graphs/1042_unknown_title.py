"""
LeetCode Problem #1042: Flower Planting With No Adjacent

Problem Statement:
You have N gardens, labeled from 1 to N. In each garden, you want to plant one of 4 types of flowers. 
There are paths between some gardens, and no two gardens connected by a path can have the same type of flower.

Given an integer N and an array paths where paths[i] = [x, y] describes a bidirectional path between garden x and garden y, 
return an array answer of length N where answer[i] is the type of flower planted in the (i+1)-th garden. 
The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.

Constraints:
- 1 <= N <= 10^4
- 0 <= paths.length <= 2 * 10^4
- paths[i].length == 2
- 1 <= x, y <= N
- x != y
- Every garden has at most 3 paths coming into or leaving it.

"""

from collections import defaultdict

def gardenNoAdj(N, paths):
    # Create an adjacency list for the gardens
    graph = defaultdict(list)
    for x, y in paths:
        graph[x].append(y)
        graph[y].append(x)
    
    # Result array to store the flower type for each garden
    result = [0] * N
    
    # Iterate through each garden
    for garden in range(1, N + 1):
        # Find the flower types used by the neighbors
        used_flowers = {result[neighbor - 1] for neighbor in graph[garden]}
        # Assign the first available flower type
        for flower in range(1, 5):
            if flower not in used_flowers:
                result[garden - 1] = flower
                break
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    N1 = 3
    paths1 = [[1, 2], [2, 3], [3, 1]]
    print(gardenNoAdj(N1, paths1))  # Output: [1, 2, 3] (or any valid solution)

    # Test Case 2
    N2 = 4
    paths2 = [[1, 2], [3, 4]]
    print(gardenNoAdj(N2, paths2))  # Output: [1, 2, 1, 2] (or any valid solution)

    # Test Case 3
    N3 = 5
    paths3 = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
    print(gardenNoAdj(N3, paths3))  # Output: [1, 2, 3, 4, 1] (or any valid solution)

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the adjacency list takes O(paths.length), which is O(E), where E is the number of edges.
- Assigning flower types involves iterating over all gardens (O(N)) and checking at most 3 neighbors (since each garden has at most 3 paths). 
  This results in O(N * 3) = O(N).
- Overall time complexity: O(N + E).

Space Complexity:
- The adjacency list requires O(E) space.
- The result array requires O(N) space.
- Overall space complexity: O(N + E).

Topic: Graphs
"""