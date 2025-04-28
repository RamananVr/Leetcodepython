"""
LeetCode Problem #1061: Lexicographically Smallest Equivalent String

Problem Statement:
You are given two strings of the same length `s1` and `s2` and a string `baseStr`.

We say `s1[i]` and `s2[i]` are equivalent characters. For example, if `s1 = "abc"` and `s2 = "cde"`, then we have 'a' ≡ 'c', 'b' ≡ 'd', 'c' ≡ 'e'.

Equivalent characters follow the usual rules of equivalence: 
- Reflexive: 'a' ≡ 'a'
- Symmetric: 'a' ≡ 'b' implies 'b' ≡ 'a'
- Transitive: 'a' ≡ 'b' and 'b' ≡ 'c' implies 'a' ≡ 'c'

For example, given the equivalency information from `s1 = "abc"` and `s2 = "cde"`, "acd" ≡ "cde" ≡ "bee".

You are tasked to find the lexicographically smallest equivalent string of `baseStr` by using the equivalency information from `s1` and `s2`.

Return the lexicographically smallest equivalent string that can be formed.

Constraints:
- `1 <= s1.length == s2.length <= 1000`
- `1 <= baseStr.length <= 1000`
- `s1`, `s2`, and `baseStr` consist of lowercase English letters.
"""

# Solution
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Helper function to find the root of a character
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        # Helper function to union two characters
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                # Always attach the larger root to the smaller root
                if rootX < rootY:
                    parent[rootY] = rootX
                else:
                    parent[rootX] = rootY

        # Initialize parent mapping for all lowercase English letters
        parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}

        # Process equivalency information from s1 and s2
        for c1, c2 in zip(s1, s2):
            union(c1, c2)

        # Build the result string using the smallest equivalent character
        result = ''.join(find(c) for c in baseStr)
        return result

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    print(solution.smallestEquivalentString(s1, s2, baseStr))  # Output: "makkek"

    # Test Case 2
    s1 = "hello"
    s2 = "world"
    baseStr = "hold"
    print(solution.smallestEquivalentString(s1, s2, baseStr))  # Output: "hdld"

    # Test Case 3
    s1 = "leetcode"
    s2 = "programs"
    baseStr = "sourcecode"
    print(solution.smallestEquivalentString(s1, s2, baseStr))  # Output: "aauaaaaada"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `union` and `find` operations are nearly constant time due to path compression and union by rank.
- Processing the equivalency information takes O(n), where n is the length of `s1` (or `s2`).
- Constructing the result string takes O(m), where m is the length of `baseStr`.
- Overall time complexity: O(n + m).

Space Complexity:
- The `parent` dictionary stores mappings for all 26 lowercase English letters, so it uses O(26) = O(1) space.
- Overall space complexity: O(1).

Topic: Union-Find
"""