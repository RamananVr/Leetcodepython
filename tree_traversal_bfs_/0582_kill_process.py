"""
LeetCode Question #582: Kill Process

Problem Statement:
You have n processes forming a rooted tree structure. You are given two integer arrays pid and ppid, 
where pid[i] is the ID of the i-th process and ppid[i] is the ID of the parent process of the i-th process. 
Each process has only one parent process but may have one or more children processes. 
The root process has ppid[i] = 0.

You are also given an integer kill representing the ID of a process you want to kill. 
When a process is killed, all of its children processes will also be killed.

Return a list of the IDs of all processes that will be killed in any order.

Example 1:
Input: pid = [1, 3, 10, 5], ppid = [3, 0, 5, 3], kill = 5
Output: [5, 10]
Explanation: The processes with IDs 5 and 10 are killed.

Constraints:
- n == pid.length == ppid.length
- 1 <= n <= 10^5
- 1 <= pid[i] <= 10^5
- 0 <= ppid[i] <= 10^5
- Only one process has ppid[i] = 0.
- kill is guaranteed to be in pid.
"""

# Python Solution
from collections import defaultdict, deque

def killProcess(pid, ppid, kill):
    # Build a tree structure using adjacency list
    tree = defaultdict(list)
    for child, parent in zip(pid, ppid):
        tree[parent].append(child)
    
    # Perform BFS to find all processes to kill
    result = []
    queue = deque([kill])
    while queue:
        current = queue.popleft()
        result.append(current)
        queue.extend(tree[current])  # Add all children of the current process to the queue
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    pid = [1, 3, 10, 5]
    ppid = [3, 0, 5, 3]
    kill = 5
    print(killProcess(pid, ppid, kill))  # Output: [5, 10]

    # Test Case 2
    pid = [1, 2, 3, 4, 5]
    ppid = [0, 1, 1, 2, 2]
    kill = 1
    print(killProcess(pid, ppid, kill))  # Output: [1, 2, 3, 4, 5]

    # Test Case 3
    pid = [1, 2, 3]
    ppid = [0, 1, 1]
    kill = 2
    print(killProcess(pid, ppid, kill))  # Output: [2]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Building the tree takes O(n), where n is the length of the pid array.
- BFS traversal of the tree takes O(n) in the worst case, as we visit each node once.
- Overall time complexity: O(n).

Space Complexity:
- The adjacency list (tree) takes O(n) space.
- The queue used for BFS takes O(n) space in the worst case.
- The result list takes O(n) space in the worst case.
- Overall space complexity: O(n).
"""

# Topic: Tree Traversal (BFS)