"""
LeetCode Problem #990: Satisfiability of Equality Equations

Problem Statement:
You are given an array of strings `equations` where each string `equations[i]` is of length 4 and takes one of two forms: 
- "a==b" means that `a` is equal to `b`.
- "a!=b" means that `a` is not equal to `b`.

Return true if it is possible to assign integers to variable names such that all the given equations are satisfied, or false otherwise.

Constraints:
1. 1 <= equations.length <= 500
2. equations[i].length == 4
3. equations[i][0] is a lowercase letter.
4. equations[i][1] is either '=' or '!' (indicating equality or inequality).
5. equations[i][2] is '=' if equations[i][1] is '='.
6. equations[i][3] is a lowercase letter.

Example:
Input: equations = ["a==b", "b!=c", "c==a"]
Output: false

Input: equations = ["c==c", "b==d", "x!=z"]
Output: true
"""

# Solution
from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # Union-Find (Disjoint Set Union) Helper Functions
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        
        # Initialize each variable to be its own parent
        for eq in equations:
            if eq[0] not in parent:
                parent[eq[0]] = eq[0]
            if eq[3] not in parent:
                parent[eq[3]] = eq[3]
        
        # Process all "==" equations to unify components
        for eq in equations:
            if eq[1:3] == "==":
                union(eq[0], eq[3])
        
        # Process all "!=" equations to check for conflicts
        for eq in equations:
            if eq[1:3] == "!=":
                if find(eq[0]) == find(eq[3]):  # Conflict detected
                    return False
        
        return True

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    equations1 = ["a==b", "b!=c", "c==a"]
    print(solution.equationsPossible(equations1))  # Output: False
    
    # Test Case 2
    equations2 = ["c==c", "b==d", "x!=z"]
    print(solution.equationsPossible(equations2))  # Output: True
    
    # Test Case 3
    equations3 = ["a==b", "b==c", "a==c"]
    print(solution.equationsPossible(equations3))  # Output: True
    
    # Test Case 4
    equations4 = ["a==b", "b!=a"]
    print(solution.equationsPossible(equations4))  # Output: False
    
    # Test Case 5
    equations5 = ["a!=a"]
    print(solution.equationsPossible(equations5))  # Output: False

"""
Time Complexity:
- The `find` operation uses path compression, which makes it nearly constant time, O(α(n)), where α is the inverse Ackermann function.
- The `union` operation is also nearly constant time.
- We process each equation once, so the overall time complexity is O(n * α(n)), where n is the number of equations.

Space Complexity:
- We use a dictionary `parent` to store the parent of each variable. In the worst case, we store all 26 lowercase letters, so the space complexity is O(1) (constant space for the alphabet).

Topic: Union-Find (Disjoint Set Union)
"""