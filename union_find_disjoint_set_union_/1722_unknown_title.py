"""
LeetCode Problem #1722: Minimize Hamming Distance After Swap Operations

Problem Statement:
You are given two integer arrays, `source` and `target`, both of length `n`. You are also given an array `allowedSwaps` where each `allowedSwaps[i] = [ai, bi]` indicates that you are allowed to swap the elements at index `ai` and index `bi` (0-indexed) of the array `source`. Note that you can swap elements at a specific pair of indices multiple times and in any order.

The Hamming distance of two arrays of the same length is the number of positions where the elements are different. Formally, the Hamming distance is the number of indices `i` where `source[i] != target[i]` (0-indexed).

Return the minimum Hamming distance of `source` and `target` after performing any number of swaps on `source` using the `allowedSwaps`.

Constraints:
1. `n == source.length == target.length`
2. `1 <= n <= 10^5`
3. `1 <= source[i], target[i] <= 10^5`
4. `0 <= allowedSwaps.length <= 10^5`
5. `0 <= ai, bi < n`
6. `ai != bi`

"""

from collections import defaultdict
from collections import Counter

def minimumHammingDistance(source, target, allowedSwaps):
    """
    Function to calculate the minimum Hamming distance between source and target arrays
    after performing allowed swaps.

    :param source: List[int] - The source array
    :param target: List[int] - The target array
    :param allowedSwaps: List[List[int]] - List of allowed index swaps
    :return: int - The minimum Hamming distance
    """
    # Helper function to find the root of a node in the Union-Find structure
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    # Helper function to union two nodes in the Union-Find structure
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootX] = rootY

    n = len(source)
    parent = list(range(n))  # Union-Find parent array

    # Build connected components using Union-Find
    for a, b in allowedSwaps:
        union(a, b)

    # Group indices by their connected component
    groups = defaultdict(list)
    for i in range(n):
        root = find(i)
        groups[root].append(i)

    # Calculate the minimum Hamming distance
    min_hamming_distance = 0
    for indices in groups.values():
        # Count the frequency of elements in the source and target arrays for this group
        source_count = Counter(source[i] for i in indices)
        target_count = Counter(target[i] for i in indices)

        # Calculate the number of matches within this group
        matches = sum((source_count & target_count).values())  # Intersection of counters
        min_hamming_distance += len(indices) - matches

    return min_hamming_distance


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    source = [1, 2, 3, 4]
    target = [2, 1, 4, 5]
    allowedSwaps = [[0, 1], [2, 3]]
    print(minimumHammingDistance(source, target, allowedSwaps))  # Output: 1

    # Test Case 2
    source = [1, 2, 3, 4]
    target = [1, 2, 3, 4]
    allowedSwaps = []
    print(minimumHammingDistance(source, target, allowedSwaps))  # Output: 0

    # Test Case 3
    source = [5, 1, 2, 4, 3]
    target = [1, 5, 4, 2, 3]
    allowedSwaps = [[0, 4], [4, 2], [1, 3], [1, 4]]
    print(minimumHammingDistance(source, target, allowedSwaps))  # Output: 0


"""
Time Complexity:
- Union-Find operations (find and union) are nearly O(1) due to path compression and union by rank.
- Building the connected components takes O(n + m), where n is the length of the arrays and m is the length of allowedSwaps.
- Counting elements in each group and calculating the Hamming distance takes O(n).
- Overall time complexity: O(n + m).

Space Complexity:
- The Union-Find parent array takes O(n) space.
- The groups dictionary and Counter objects take O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Union-Find (Disjoint Set Union)
"""