"""
LeetCode Problem #2127: Maximum Employees to Be Invited to a Meeting

Problem Statement:
A company has n employees numbered from 0 to n - 1. Each employee has a favorite person and is invited to a meeting. 
The favorite person of an employee is not necessarily different from the employee. The favorite person is given in 
a 0-indexed integer array `favorite` where `favorite[i]` denotes the favorite person of the i-th employee.

A meeting can be held if and only if the following conditions are satisfied:
1. Every employee attending the meeting loves at least one other employee in the meeting.
2. The meeting should have the maximum number of attendees.

Return the maximum number of employees that can be invited to the meeting.

Constraints:
- 2 <= n <= 10^5
- favorite.length == n
- 0 <= favorite[i] < n
- favorite[i] != i
"""

from collections import defaultdict, deque

def maximumInvitations(favorite):
    def find_cycle_length(node):
        """Find the length of the cycle starting from the given node."""
        visited[node] = True
        stack.append(node)
        next_node = favorite[node]
        if visited[next_node]:
            if next_node in stack:
                return len(stack) - stack.index(next_node)
            return 0
        return find_cycle_length(next_node)

    def find_longest_chain(node):
        """Find the longest chain ending at the given node."""
        if longest_chain[node] != -1:
            return longest_chain[node]
        next_node = reverse_graph[node]
        if not next_node:
            longest_chain[node] = 1
        else:
            longest_chain[node] = 1 + find_longest_chain(next_node[0])
        return longest_chain[node]

    n = len(favorite)
    visited = [False] * n
    stack = []
    reverse_graph = defaultdict(list)
    longest_chain = [-1] * n

    # Build reverse graph
    for i in range(n):
        reverse_graph[favorite[i]].append(i)

    # Find all cycles and their lengths
    max_cycle_length = 0
    for i in range(n):
        if not visited[i]:
            stack = []
            max_cycle_length = max(max_cycle_length, find_cycle_length(i))

    # Find the longest chain for each node
    for i in range(n):
        if longest_chain[i] == -1:
            find_longest_chain(i)

    # Handle the special case of 2-cycles
    two_cycle_sum = 0
    for i in range(n):
        if favorite[favorite[i]] == i and i < favorite[i]:
            two_cycle_sum += longest_chain[i] + longest_chain[favorite[i]]

    return max(max_cycle_length, two_cycle_sum)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    favorite = [2, 2, 1, 2]
    print(maximumInvitations(favorite))  # Output: 3

    # Test Case 2
    favorite = [1, 2, 0]
    print(maximumInvitations(favorite))  # Output: 3

    # Test Case 3
    favorite = [3, 0, 1, 4, 1]
    print(maximumInvitations(favorite))  # Output: 4

"""
Time Complexity:
- Building the reverse graph takes O(n).
- Finding cycles takes O(n) since each node is visited once.
- Calculating the longest chain for each node also takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- The reverse graph uses O(n) space.
- The visited array and longest_chain array use O(n) space each.
- The stack used during DFS traversal also uses O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Graphs, DFS, Cycles
"""