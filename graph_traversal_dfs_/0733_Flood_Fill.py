"""
LeetCode Problem #733: Flood Fill

Problem Statement:
An image is represented by a 2D array of integers, where each integer represents the pixel value of the image. 
You are given a starting pixel (sr, sc) and a new color. Write a function to perform a "flood fill" on the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel 
of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same 
color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the new color.

Return the modified image after performing the flood fill.

Constraints:
- The number of rows in the image is in the range [1, 50].
- The number of columns in the image is in the range [1, 50].
- The pixel value of the image is in the range [0, 65535].
- The starting pixel (sr, sc) is within the bounds of the image.
- The new color is an integer in the range [0, 65535].

Example:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image (with position (1, 1)), all pixels connected by a path of the same color as 
the starting pixel are colored with the new color.

"""

# Solution
def floodFill(image, sr, sc, newColor):
    """
    Perform a flood fill on the given image starting from pixel (sr, sc).

    :param image: List[List[int]] - 2D array representing the image
    :param sr: int - starting row index
    :param sc: int - starting column index
    :param newColor: int - new color to apply
    :return: List[List[int]] - modified image after flood fill
    """
    rows, cols = len(image), len(image[0])
    originalColor = image[sr][sc]
    
    # If the original color is the same as the new color, no need to proceed
    if originalColor == newColor:
        return image
    
    def dfs(r, c):
        # Base case: check if the current pixel is out of bounds or not the original color
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != originalColor:
            return
        
        # Change the color of the current pixel
        image[r][c] = newColor
        
        # Recursively call dfs for the 4 neighboring pixels
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left
    
    # Start the flood fill from the given starting pixel
    dfs(sr, sc)
    return image

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    image1 = [[1,1,1],[1,1,0],[1,0,1]]
    sr1, sc1, newColor1 = 1, 1, 2
    print(floodFill(image1, sr1, sc1, newColor1))  # Expected: [[2,2,2],[2,2,0],[2,0,1]]

    # Test Case 2
    image2 = [[0,0,0],[0,0,0]]
    sr2, sc2, newColor2 = 0, 0, 2
    print(floodFill(image2, sr2, sc2, newColor2))  # Expected: [[2,2,2],[2,2,2]]

    # Test Case 3
    image3 = [[1,1,1],[1,1,1],[1,1,1]]
    sr3, sc3, newColor3 = 2, 2, 1
    print(floodFill(image3, sr3, sc3, newColor3))  # Expected: [[1,1,1],[1,1,1],[1,1,1]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each pixel is visited at most once during the DFS traversal.
- Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns in the image.

Space Complexity:
- The space complexity is determined by the recursion stack used in DFS.
- In the worst case, the recursion stack can go as deep as the number of pixels in the image, i.e., O(m * n).
- Thus, the space complexity is O(m * n).

"""

# Topic: Graph Traversal (DFS)