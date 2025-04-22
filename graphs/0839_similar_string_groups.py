"""
LeetCode Question #839: Similar String Groups

Problem Statement:
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. 
Also, two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, 
but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}. 
Notice that "tars" and "arts" are in the same group even though they are not similar. 
Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

Given an array of strings `strs`, return the number of groups of similar strings.

Constraints:
- 1 <= strs.length <= 300
- 1 <= strs[i].length <= 100
- strs[i] consists of lowercase letters only.
"""

# Solution
from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(s1: str, s2: str) -> bool:
            # Check if two strings are similar
            if s1 == s2:
                return True
            diff = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff.append(i)
                    if len(diff) > 2:
                        return False
            return len(diff) == 2 and s1[diff[0]] == s2[diff[1]] and s1[diff[1]] == s2[diff[0]]

        def dfs(node: int):
            # Depth-first search to explore all connected nodes
            visited[node] = True
            for neighbor in range(len(strs)):
                if not visited[neighbor] and is_similar(strs[node], strs[neighbor]):
                    dfs(neighbor)

        n = len(strs)
        visited = [False] * n
        groups = 0

        for i in range(n):
            if not visited[i]:
                groups += 1
                dfs(i)

        return groups

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    strs1 = ["tars", "rats", "arts", "star"]
    print(solution.numSimilarGroups(strs1))  # Output: 2

    # Test Case 2
    strs2 = ["omv", "ovm"]
    print(solution.numSimilarGroups(strs2))  # Output: 1

    # Test Case 3
    strs3 = ["abc", "acb", "bac", "bca", "cab", "cba"]
    print(solution.numSimilarGroups(strs3))  # Output: 1

    # Test Case 4
    strs4 = ["abcd", "abdc", "acbd", "bacd", "badc", "bcad"]
    print(solution.numSimilarGroups(strs4))  # Output: 1

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The `is_similar` function takes O(L), where L is the length of the strings.
   - For each string, we check similarity with every other string, resulting in O(N^2 * L), where N is the number of strings.
   - The DFS traversal takes O(N^2) in the worst case, as we may visit all nodes and check all neighbors.
   - Overall time complexity: O(N^2 * L).

2. Space Complexity:
   - The `visited` array takes O(N) space.
   - The recursion stack for DFS can take up to O(N) space in the worst case.
   - Overall space complexity: O(N).

Topic: Graphs
"""