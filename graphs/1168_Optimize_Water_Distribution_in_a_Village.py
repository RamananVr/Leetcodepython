"""
LeetCode Problem #1168: Optimize Water Distribution in a Village

Problem Statement:
There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

- For each house i, we can either build a well inside it with a cost `wells[i]`.
- Alternatively, we can connect it to another house with a pipe. The cost of connecting house i and house j is `pipes[k] = [house1, house2, cost]`.

Return the minimum total cost to supply water to all houses.

Constraints:
- 1 <= n <= 10000
- wells.length == n
- 1 <= wells[i] <= 10^5
- 1 <= pipes.length <= 10000
- pipes[k].length == 3
- 1 <= house1, house2 <= n
- 1 <= cost <= 10^5

The input consists of:
- wells: A list of integers where wells[i] is the cost of building a well in house i.
- pipes: A list of lists where pipes[k] = [house1, house2, cost] represents the cost of connecting house1 and house2.

The goal is to minimize the total cost to supply water to all houses.
"""

from heapq import heappop, heappush

def minCostToSupplyWater(n, wells, pipes):
    """
    Function to calculate the minimum cost to supply water to all houses.

    :param n: Number of houses
    :param wells: List of costs to build wells in each house
    :param pipes: List of pipes with costs to connect houses
    :return: Minimum total cost to supply water
    """
    # Create a graph representation
    graph = {i: [] for i in range(1, n + 1)}
    
    # Add virtual node 0 to represent wells
    for i in range(n):
        graph[0].append((wells[i], i + 1))
    
    # Add pipes to the graph
    for house1, house2, cost in pipes:
        graph[house1].append((cost, house2))
        graph[house2].append((cost, house1))
    
    # Prim's algorithm to find Minimum Spanning Tree (MST)
    visited = set()
    min_heap = [(0, 0)]  # (cost, house), start with virtual node 0
    total_cost = 0
    
    while len(visited) < n + 1:
        cost, house = heappop(min_heap)
        if house in visited:
            continue
        visited.add(house)
        total_cost += cost
        
        for next_cost, next_house in graph[house]:
            if next_house not in visited:
                heappush(min_heap, (next_cost, next_house))
    
    return total_cost

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    wells = [1, 2, 2]
    pipes = [[1, 2, 1], [2, 3, 1]]
    print(minCostToSupplyWater(n, wells, pipes))  # Output: 3

    # Test Case 2
    n = 4
    wells = [1, 2, 2, 3]
    pipes = [[1, 2, 1], [2, 3, 2], [3, 4, 1], [1, 4, 3]]
    print(minCostToSupplyWater(n, wells, pipes))  # Output: 6

    # Test Case 3
    n = 2
    wells = [5, 5]
    pipes = [[1, 2, 1]]
    print(minCostToSupplyWater(n, wells, pipes))  # Output: 6

"""
Time and Space Complexity Analysis:

Time Complexity:
- Constructing the graph takes O(n + m), where n is the number of houses and m is the number of pipes.
- Prim's algorithm runs in O((n + m) * log(n + m)) due to the use of a priority queue.

Overall time complexity: O((n + m) * log(n + m))

Space Complexity:
- The graph representation takes O(n + m) space.
- The priority queue can hold up to O(n + m) elements.

Overall space complexity: O(n + m)

Topic: Graphs
"""