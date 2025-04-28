"""
LeetCode Problem #1303: Find the Team Size

Problem Statement:
There is a company with n employees, each with a unique ID from 0 to n - 1. The company has a hierarchical structure, and each employee has a manager. The company wants to find out the size of the team under each employee, including themselves.

You are given:
- An integer `n` representing the number of employees.
- A list `managers` where `managers[i]` is the manager of the i-th employee. If `managers[i] == -1`, then the i-th employee is the CEO and has no manager.

Your task is to return a list `team_sizes` where `team_sizes[i]` is the size of the team under the i-th employee, including themselves.

Constraints:
- 1 <= n <= 10^5
- `managers.length == n`
- -1 <= `managers[i]` < n
- `managers[i] != i` (no employee can be their own manager)
- The input is guaranteed to form a valid tree structure.

Example:
Input: n = 6, managers = [-1, 0, 0, 1, 1, 2]
Output: [6, 3, 2, 1, 1, 1]

Explanation:
- Employee 0 is the CEO and has a team of 6 (including themselves).
- Employee 1 has a team of 3 (including themselves and employees 3 and 4).
- Employee 2 has a team of 2 (including themselves and employee 5).
- Employees 3, 4, and 5 each have a team of 1 (just themselves).
"""

from collections import defaultdict

def findTeamSizes(n, managers):
    # Step 1: Build the tree structure using adjacency list
    tree = defaultdict(list)
    for employee, manager in enumerate(managers):
        if manager != -1:
            tree[manager].append(employee)
    
    # Step 2: Use DFS to calculate team sizes
    def dfs(employee):
        size = 1  # Include the current employee
        for subordinate in tree[employee]:
            size += dfs(subordinate)
        team_sizes[employee] = size
        return size

    # Step 3: Initialize the result array and start DFS from the CEO
    team_sizes = [0] * n
    for employee, manager in enumerate(managers):
        if manager == -1:  # Find the CEO
            dfs(employee)
            break

    return team_sizes

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 6
    managers1 = [-1, 0, 0, 1, 1, 2]
    print(findTeamSizes(n1, managers1))  # Output: [6, 3, 2, 1, 1, 1]

    # Test Case 2
    n2 = 1
    managers2 = [-1]
    print(findTeamSizes(n2, managers2))  # Output: [1]

    # Test Case 3
    n3 = 4
    managers3 = [-1, 0, 1, 2]
    print(findTeamSizes(n3, managers3))  # Output: [4, 3, 2, 1]

    # Test Case 4
    n4 = 5
    managers4 = [-1, 0, 0, 1, 1]
    print(findTeamSizes(n4, managers4))  # Output: [5, 3, 1, 1, 1]

"""
Time Complexity:
- Building the tree takes O(n) time since we iterate through the `managers` list once.
- The DFS traversal also takes O(n) time because we visit each employee exactly once.
- Overall time complexity: O(n).

Space Complexity:
- The adjacency list `tree` requires O(n) space to store the hierarchy.
- The recursion stack for DFS can go as deep as the height of the tree, which is O(n) in the worst case (e.g., a skewed tree).
- The `team_sizes` array requires O(n) space.
- Overall space complexity: O(n).

Topic: Tree, Depth-First Search (DFS)
"""