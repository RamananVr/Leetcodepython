"""
LeetCode Problem #1615: Maximal Network Rank

Problem Statement:
There is an infrastructure of n cities with some number of roads connecting these cities. Each road is a bidirectional road that connects two different cities.

You are given an integer n and an array roads where roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Return the maximal network rank of the entire infrastructure.

Constraints:
- 2 <= n <= 100
- 0 <= roads.length <= n * (n - 1) / 2
- roads[i].length == 2
- 0 <= ai, bi <= n - 1
- ai != bi
- Each pair of cities has at most one road connecting them.
"""

def maximalNetworkRank(n: int, roads: list[list[int]]) -> int:
    """
    Function to calculate the maximal network rank of the infrastructure.
    """
    # Step 1: Create adjacency list and degree count
    degree = [0] * n
    connected = set()
    
    for a, b in roads:
        degree[a] += 1
        degree[b] += 1
        connected.add((min(a, b), max(a, b)))  # Store roads in a sorted tuple for easy lookup
    
    # Step 2: Calculate maximal network rank
    max_rank = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the network rank for cities i and j
            rank = degree[i] + degree[j]
            if (i, j) in connected:
                rank -= 1  # Subtract 1 if there's a direct road between i and j
            max_rank = max(max_rank, rank)
    
    return max_rank

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 4
    roads1 = [[0, 1], [0, 3], [1, 2], [1, 3]]
    print(maximalNetworkRank(n1, roads1))  # Expected Output: 4

    # Test Case 2
    n2 = 5
    roads2 = [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]
    print(maximalNetworkRank(n2, roads2))  # Expected Output: 5

    # Test Case 3
    n3 = 8
    roads3 = [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]
    print(maximalNetworkRank(n3, roads3))  # Expected Output: 5

    # Test Case 4
    n4 = 2
    roads4 = []
    print(maximalNetworkRank(n4, roads4))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Constructing the degree array and connected set takes O(m), where m is the number of roads.
- The nested loop to calculate the maximal network rank iterates over all pairs of cities, which is O(n^2).
- Overall time complexity: O(n^2 + m).

Space Complexity:
- The degree array takes O(n) space.
- The connected set takes O(m) space.
- Overall space complexity: O(n + m).

Topic: Graphs
"""