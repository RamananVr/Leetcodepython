"""
LeetCode Problem #2307: Check for Contradictions in Equations

Problem Statement:
You are given a list of equations, where each equation is represented as a tuple (a, b, eq). 
- `a` and `b` are strings representing variables.
- `eq` is a string that can either be "==" (indicating equality) or "!=" (indicating inequality).

Your task is to determine if there are any contradictions in the equations. A contradiction occurs if:
1. Two variables are declared equal ("==") and later declared unequal ("!=").
2. Equality relationships form a cycle that conflicts with inequality relationships.

Return `True` if there are contradictions in the equations, otherwise return `False`.

Constraints:
- The number of equations is at most 1000.
- Each variable name is a string of length at most 10.
- Variables are case-sensitive.

Example:
Input: equations = [("a", "b", "=="), ("b", "c", "=="), ("a", "c", "!=")]
Output: True
Explanation: "a == b" and "b == c" imply "a == c", which contradicts "a != c".

Input: equations = [("a", "b", "=="), ("b", "c", "!=")]
Output: False
Explanation: There is no contradiction.

"""

# Python Solution
from collections import defaultdict

class Solution:
    def equationsPossible(self, equations):
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        # Step 1: Initialize parent dictionary for union-find
        parent = {}

        # Step 2: Process equality equations ("==")
        for a, b, eq in equations:
            if a not in parent:
                parent[a] = a
            if b not in parent:
                parent[b] = b
            if eq == "==":
                union(a, b)

        # Step 3: Process inequality equations ("!=")
        for a, b, eq in equations:
            if eq == "!=":
                if a == b:  # Same variable cannot be unequal to itself
                    return True
                if a in parent and b in parent and find(a) == find(b):
                    return True

        return False


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Contradiction exists
    equations1 = [("a", "b", "=="), ("b", "c", "=="), ("a", "c", "!=")]
    print(solution.equationsPossible(equations1))  # Output: True

    # Test Case 2: No contradiction
    equations2 = [("a", "b", "=="), ("b", "c", "!=")]
    print(solution.equationsPossible(equations2))  # Output: False

    # Test Case 3: Same variable declared unequal to itself
    equations3 = [("a", "a", "!=")]
    print(solution.equationsPossible(equations3))  # Output: True

    # Test Case 4: Multiple variables with no contradiction
    equations4 = [("x", "y", "=="), ("y", "z", "=="), ("a", "b", "!=")]
    print(solution.equationsPossible(equations4))  # Output: False

    # Test Case 5: Contradiction due to transitive equality
    equations5 = [("a", "b", "=="), ("b", "c", "=="), ("c", "d", "=="), ("a", "d", "!=")]
    print(solution.equationsPossible(equations5))  # Output: True


# Time and Space Complexity Analysis
"""
Time Complexity:
- Union-Find operations (find and union) are nearly constant time due to path compression and union by rank.
- Processing all equations takes O(n), where n is the number of equations.
- Overall time complexity: O(n).

Space Complexity:
- The parent dictionary stores at most 2n entries (for all variables in the equations).
- Space complexity: O(n).

"""

# Topic: Union-Find (Disjoint Set)