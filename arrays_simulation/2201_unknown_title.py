"""
LeetCode Problem #2201: Count Artifacts That Can Be Extracted

Problem Statement:
You are given an integer n representing the size of a square grid n x n and a 0-indexed 2D integer array artifacts, 
where artifacts[i] = [r1i, c1i, r2i, c2i] denotes that the i-th artifact is located in the rectangle with its top-left 
corner (r1i, c1i) and bottom-right corner (r2i, c2i) inclusive. You are also given a 0-indexed 2D integer array dig 
where dig[i] = [ri, ci] indicates that you can excavate the cell (ri, ci).

Return the number of artifacts that can be extracted. An artifact can be extracted if and only if every cell 
within the rectangle it occupies has been excavated.

Example:
Input: n = 5, artifacts = [[0,0,0,0],[0,1,1,1],[1,0,1,0],[1,2,2,2]], dig = [[0,0],[0,1],[1,1],[2,2],[1,2],[1,0]]
Output: 2
Explanation: 
- Artifact 0 at (0,0) is fully excavated.
- Artifact 1 at (0,1) to (1,1) is not fully excavated.
- Artifact 2 at (1,0) is fully excavated.
- Artifact 3 at (1,2) to (2,2) is not fully excavated.
Thus, 2 artifacts can be extracted.

Constraints:
- 1 <= n <= 1000
- 1 <= artifacts.length, dig.length <= min(n^2, 10^5)
- artifacts[i].length == 4
- 0 <= r1i, c1i, r2i, c2i, ri, ci < n
- r1i <= r2i
- c1i <= c2i
- All the cells in artifacts are pairwise distinct.
- The cells in dig are pairwise distinct.
"""

def countArtifacts(n: int, artifacts: list[list[int]], dig: list[list[int]]) -> int:
    # Create a set of excavated cells for quick lookup
    excavated = set((r, c) for r, c in dig)
    
    # Initialize the count of extractable artifacts
    extractable_count = 0
    
    # Iterate through each artifact
    for r1, c1, r2, c2 in artifacts:
        # Check if all cells in the artifact are excavated
        can_extract = True
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if (r, c) not in excavated:
                    can_extract = False
                    break
            if not can_extract:
                break
        if can_extract:
            extractable_count += 1
    
    return extractable_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 5
    artifacts = [[0, 0, 0, 0], [0, 1, 1, 1], [1, 0, 1, 0], [1, 2, 2, 2]]
    dig = [[0, 0], [0, 1], [1, 1], [2, 2], [1, 2], [1, 0]]
    print(countArtifacts(n, artifacts, dig))  # Output: 2

    # Test Case 2
    n = 3
    artifacts = [[0, 0, 1, 1], [1, 2, 2, 2]]
    dig = [[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [2, 2]]
    print(countArtifacts(n, artifacts, dig))  # Output: 2

    # Test Case 3
    n = 4
    artifacts = [[0, 0, 0, 1], [1, 1, 2, 2], [3, 0, 3, 3]]
    dig = [[0, 0], [0, 1], [1, 1], [2, 2], [3, 0], [3, 1], [3, 2], [3, 3]]
    print(countArtifacts(n, artifacts, dig))  # Output: 3

# Time Complexity Analysis:
# Let m = len(artifacts) and k = len(dig).
# - Creating the `excavated` set takes O(k).
# - Iterating through each artifact and checking its cells takes O(m * s), where s is the average size of an artifact.
#   In the worst case, s can be O(n^2 / m), so the complexity becomes O(m * n^2 / m) = O(n^2).
# Overall time complexity: O(k + n^2).

# Space Complexity Analysis:
# - The `excavated` set takes O(k) space.
# - Other variables take O(1) space.
# Overall space complexity: O(k).

# Topic: Arrays, Simulation