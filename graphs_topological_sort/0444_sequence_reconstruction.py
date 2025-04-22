"""
LeetCode Question #444: Sequence Reconstruction

Problem Statement:
Check whether the original sequence `org` can be uniquely reconstructed from the sequences in `seqs`. 
The original sequence is a permutation of integers from 1 to n (n is the length of `org`). 
Reconstruction means building a shortest common supersequence of the sequences in `seqs` (i.e., a sequence such that all sequences in `seqs` are subsequences of it). 
Determine if there is exactly one sequence that can be reconstructed from `seqs` and it is the same as `org`.

Constraints:
- 1 <= len(org) <= 10^4
- 1 <= len(seqs) <= 10^4
- 1 <= sum(len(seqs[i])) <= 10^5
- 1 <= seqs[i][j] <= n
- `org` is a permutation of the integers from 1 to n.

"""

from collections import defaultdict, deque

def sequenceReconstruction(org, seqs):
    """
    Determines if the original sequence `org` can be uniquely reconstructed from `seqs`.

    :param org: List[int] - The original sequence.
    :param seqs: List[List[int]] - List of subsequences.
    :return: bool - True if `org` can be uniquely reconstructed, False otherwise.
    """
    # Step 1: Build the graph and in-degree map
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    nodes = set()

    for seq in seqs:
        for num in seq:
            nodes.add(num)
        for i in range(len(seq) - 1):
            prev, curr = seq[i], seq[i + 1]
            if curr not in graph[prev]:
                graph[prev].append(curr)
                in_degree[curr] += 1

    # Step 2: Check if all nodes in `org` are covered
    if nodes != set(org):
        return False

    # Step 3: Topological sort using BFS
    queue = deque([node for node in org if in_degree[node] == 0])
    reconstructed = []

    while queue:
        if len(queue) > 1:
            # More than one way to reconstruct
            return False
        current = queue.popleft()
        reconstructed.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check if the reconstructed sequence matches `org`
    return reconstructed == org


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Unique reconstruction is possible
    org = [1, 2, 3]
    seqs = [[1, 2], [1, 3], [2, 3]]
    print(sequenceReconstruction(org, seqs))  # Output: True

    # Test Case 2: Unique reconstruction is not possible
    org = [1, 2, 3]
    seqs = [[1, 2], [1, 3]]
    print(sequenceReconstruction(org, seqs))  # Output: False

    # Test Case 3: `seqs` does not cover all elements in `org`
    org = [1, 2, 3]
    seqs = [[1, 2]]
    print(sequenceReconstruction(org, seqs))  # Output: False

    # Test Case 4: Empty `seqs`
    org = [1]
    seqs = []
    print(sequenceReconstruction(org, seqs))  # Output: False

    # Test Case 5: Single element sequence
    org = [1]
    seqs = [[1]]
    print(sequenceReconstruction(org, seqs))  # Output: True


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Building the graph and in-degree map: O(sum(len(seq)) for seq in seqs) = O(total number of elements in seqs).
   - Topological sort: O(V + E), where V is the number of unique nodes and E is the number of edges.
   - Overall: O(total number of elements in seqs).

2. Space Complexity:
   - Graph storage: O(V + E), where V is the number of unique nodes and E is the number of edges.
   - In-degree map: O(V).
   - Queue for BFS: O(V).
   - Overall: O(V + E).

Topic: Graphs, Topological Sort
"""