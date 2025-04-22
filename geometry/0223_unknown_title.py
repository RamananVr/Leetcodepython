"""
LeetCode Problem #223: Rectangle Area

Problem Statement:
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
The first rectangle is defined by its bottom-left corner (A, B) and top-right corner (C, D).
The second rectangle is defined by its bottom-left corner (E, F) and top-right corner (G, H).

Note:
- Rectangles can overlap.
- If the two rectangles overlap, subtract the overlapping area from the total area.

Constraints:
- -10^4 <= A, B, C, D, E, F, G, H <= 10^4
- The input rectangles are guaranteed to be well-formed, meaning that A < C and B < D, and E < G and F < H.

Example:
Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Explanation: The total area covered by the two rectangles is 45.
"""

# Python Solution
def computeArea(A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
    # Calculate the area of the first rectangle
    area1 = (C - A) * (D - B)
    
    # Calculate the area of the second rectangle
    area2 = (G - E) * (H - F)
    
    # Calculate the overlapping area
    overlap_width = max(0, min(C, G) - max(A, E))
    overlap_height = max(0, min(D, H) - max(B, F))
    overlap_area = overlap_width * overlap_height
    
    # Total area is the sum of both areas minus the overlapping area
    total_area = area1 + area2 - overlap_area
    
    return total_area

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    A, B, C, D, E, F, G, H = -3, 0, 3, 4, 0, -1, 9, 2
    print(computeArea(A, B, C, D, E, F, G, H))  # Output: 45

    # Test Case 2
    A, B, C, D, E, F, G, H = 0, 0, 2, 2, 1, 1, 3, 3
    print(computeArea(A, B, C, D, E, F, G, H))  # Output: 7

    # Test Case 3
    A, B, C, D, E, F, G, H = -2, -2, 2, 2, -2, -2, 2, 2
    print(computeArea(A, B, C, D, E, F, G, H))  # Output: 16

    # Test Case 4
    A, B, C, D, E, F, G, H = -2, -2, 2, 2, 3, 3, 4, 4
    print(computeArea(A, B, C, D, E, F, G, H))  # Output: 16

# Time and Space Complexity Analysis
# Time Complexity:
# - Calculating the area of each rectangle is O(1).
# - Calculating the overlap dimensions and area is O(1).
# - Overall, the time complexity is O(1).

# Space Complexity:
# - The solution uses a constant amount of space for variables.
# - Overall, the space complexity is O(1).

# Topic: Geometry