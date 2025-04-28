"""
LeetCode Problem #1820: Maximum Number of Accepted Invitations

Problem Statement:
There are m boys and n girls in a class. You are given an m x n binary matrix grid, 
where grid[i][j] = 1 indicates that boy i can invite girl j to the dance, and grid[i][j] = 0 indicates he cannot.

Return the maximum number of invitations the boys can send out such that no two boys invite the same girl 
and no two girls accept invitations from the same boy.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- grid[i][j] is either 0 or 1.

"""

# Solution
def maximumInvitations(grid):
    def dfs(boy, visited):
        for girl in range(n):
            if grid[boy][girl] == 1 and not visited[girl]:
                visited[girl] = True
                if match[girl] == -1 or dfs(match[girl], visited):
                    match[girl] = boy
                    return True
        return False

    m, n = len(grid), len(grid[0])
    match = [-1] * n  # match[girl] stores the boy matched to the girl, or -1 if no match
    result = 0

    for boy in range(m):
        visited = [False] * n
        if dfs(boy, visited):
            result += 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1]
    ]
    print(maximumInvitations(grid1))  # Output: 3

    # Test Case 2
    grid2 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    print(maximumInvitations(grid2))  # Output: 3

    # Test Case 3
    grid3 = [
        [1, 0],
        [0, 1]
    ]
    print(maximumInvitations(grid3))  # Output: 2

    # Test Case 4
    grid4 = [
        [1, 1],
        [1, 1]
    ]
    print(maximumInvitations(grid4))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses a depth-first search (DFS) for each boy. In the worst case, each DFS traverses all girls.
- For m boys and n girls, the complexity is O(m * n), where m is the number of boys and n is the number of girls.

Space Complexity:
- The space complexity is O(n) for the visited array used in each DFS call.
- Additionally, the match array takes O(n) space.
- Total space complexity: O(n).

Topic: Graphs (Maximum Bipartite Matching)
"""