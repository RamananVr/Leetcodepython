"""
LeetCode Problem #1203: Sort Items by Groups Respecting Dependencies

Problem Statement:
There are `n` items each belonging to zero or one of `m` groups where `group[i]` is the group to which the `i-th` item belongs, and it's -1 if the `i-th` item belongs to no group. The items and the groups are zero-indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:
1. The items that belong to the same group are next to each other in the sorted list.
2. There are some dependencies between these items given as a list `beforeItems` where `beforeItems[i]` is a list containing all the items that should come before the `i-th` item in the sorted order (to the left of `i`).

Return any solution if there is more than one solution, and return an empty list if there is no solution.

Constraints:
- `1 <= n <= 3 * 10^4`
- `0 <= m <= n`
- `group.length == beforeItems.length == n`
- `-1 <= group[i] < m`
- `0 <= beforeItems[i].length <= n - 1`
- `0 <= beforeItems[i][j] < n`
- `i != beforeItems[i][j]`
- `beforeItems[i]` does not contain duplicates.
"""

from collections import defaultdict, deque
from typing import List

def sortItems(n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
    # Step 1: Assign unique group IDs to items with no group (-1)
    for i in range(n):
        if group[i] == -1:
            group[i] = m
            m += 1

    # Step 2: Build adjacency lists and in-degree counts for items and groups
    item_graph = defaultdict(list)
    item_indegree = [0] * n
    group_graph = defaultdict(list)
    group_indegree = [0] * m

    for i in range(n):
        for before in beforeItems[i]:
            # Add edge between items
            item_graph[before].append(i)
            item_indegree[i] += 1
            # Add edge between groups if they are different
            if group[before] != group[i]:
                group_graph[group[before]].append(group[i])
                group_indegree[group[i]] += 1

    # Step 3: Topological sort for items
    def topological_sort(graph, indegree, nodes):
        queue = deque([node for node in nodes if indegree[node] == 0])
        sorted_order = []
        while queue:
            node = queue.popleft()
            sorted_order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return sorted_order if len(sorted_order) == len(nodes) else []

    # Topological sort for items
    items_sorted = topological_sort(item_graph, item_indegree, range(n))
    if not items_sorted:
        return []

    # Topological sort for groups
    groups_sorted = topological_sort(group_graph, group_indegree, range(m))
    if not groups_sorted:
        return []

    # Step 4: Group items by their group ID
    group_to_items = defaultdict(list)
    for item in items_sorted:
        group_to_items[group[item]].append(item)

    # Step 5: Combine items in group order
    result = []
    for group_id in groups_sorted:
        result.extend(group_to_items[group_id])

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, m1 = 8, 2
    group1 = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems1 = [[], [6], [5], [6], [3, 6], [], [], []]
    print(sortItems(n1, m1, group1, beforeItems1))  # Expected: [6, 3, 4, 1, 5, 2, 0, 7]

    # Test Case 2
    n2, m2 = 8, 2
    group2 = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems2 = [[], [6], [5], [6], [3], [], [4], []]
    print(sortItems(n2, m2, group2, beforeItems2))  # Expected: []

    # Test Case 3
    n3, m3 = 5, 5
    group3 = [2, 0, -1, 3, 0]
    beforeItems3 = [[], [0], [1], [2], [3]]
    print(sortItems(n3, m3, group3, beforeItems3))  # Expected: [0, 1, 2, 3, 4]

"""
Time Complexity:
- Building the graphs: O(V + E), where V is the number of items (n) and E is the total number of dependencies in beforeItems.
- Topological sorting: O(V + E) for both item and group graphs.
- Combining results: O(n).
Overall: O(V + E) = O(n + total_dependencies).

Space Complexity:
- Graph storage: O(V + E) = O(n + total_dependencies).
- Indegree arrays: O(V) = O(n).
- Result storage: O(n).
Overall: O(n + total_dependencies).

Topic: Graph, Topological Sort
"""