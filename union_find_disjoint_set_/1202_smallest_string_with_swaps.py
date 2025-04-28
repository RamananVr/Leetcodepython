"""
LeetCode Question #1202: Smallest String With Swaps

Problem Statement:
You are given a string `s`, and an array of pairs of indices in the string `pairs` where `pairs[i] = [a, b]` indicates 
that you can swap the characters at index `a` and index `b`.

You can swap characters any number of times.

Return the lexicographically smallest string that `s` can be after using the swaps.

Example 1:
Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "bacd"
Explanation: 
- Swap s[0] and s[3], s = "bcad"
- Swap s[1] and s[2], s = "bacd"
- Swap s[0] and s[2], s = "bacd"

Example 2:
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explanation: 
- Swap s[0] and s[3], s = "bcad"
- Swap s[1] and s[2], s = "bacd"

Example 3:
Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explanation: 
- Swap s[0] and s[1], s = "bca"
- Swap s[1] and s[2], s = "abc"

Constraints:
- 1 <= s.length <= 10^5
- 0 <= pairs.length <= 10^5
- 0 <= pairs[i][0], pairs[i][1] < s.length
- s only contains lowercase English letters.
"""

# Python Solution
from collections import defaultdict

def smallestStringWithSwaps(s, pairs):
    # Helper function for Union-Find
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX  # Union

    # Step 1: Initialize Union-Find structure
    n = len(s)
    parent = list(range(n))

    # Step 2: Apply union operation for each pair
    for a, b in pairs:
        union(a, b)

    # Step 3: Group indices by their connected components
    groups = defaultdict(list)
    for i in range(n):
        root = find(i)
        groups[root].append(i)

    # Step 4: Sort characters within each group and reconstruct the string
    result = list(s)
    for indices in groups.values():
        # Extract characters, sort them, and place them back in sorted order
        sorted_chars = sorted(result[i] for i in indices)
        for i, char in zip(sorted(indices), sorted_chars):
            result[i] = char

    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "dcab"
    pairs1 = [[0, 3], [1, 2], [0, 2]]
    print(smallestStringWithSwaps(s1, pairs1))  # Output: "bacd"

    # Test Case 2
    s2 = "dcab"
    pairs2 = [[0, 3], [1, 2]]
    print(smallestStringWithSwaps(s2, pairs2))  # Output: "bacd"

    # Test Case 3
    s3 = "cba"
    pairs3 = [[0, 1], [1, 2]]
    print(smallestStringWithSwaps(s3, pairs3))  # Output: "abc"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Union-Find operations (find and union) are nearly constant time due to path compression and union by rank.
- For `pairs`, we perform union operations O(pairs.length).
- Grouping indices takes O(s.length).
- Sorting characters within each group takes O(s.length * log(s.length)) in the worst case.

Overall time complexity: O(s.length * log(s.length) + pairs.length).

Space Complexity:
- The Union-Find structure uses O(s.length) space for the parent array.
- The groups dictionary uses O(s.length) space in the worst case.

Overall space complexity: O(s.length).
"""

# Topic: Union-Find (Disjoint Set)