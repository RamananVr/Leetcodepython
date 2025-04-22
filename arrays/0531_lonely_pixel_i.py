"""
LeetCode Question #531: Lonely Pixel I

Problem Statement:
Given an `m x n` picture consisting of black ('B') and white ('W') pixels, return the number of black lonely pixels.

A black lonely pixel is a character 'B' that is located at a specific position `(r, c)` in the picture and satisfies the following conditions:
1. The entire row `r` and column `c` contain exactly one black pixel.

Example:
Input: picture = [["W", "W", "B"],
                  ["W", "B", "W"],
                  ["B", "W", "W"]]
Output: 3
Explanation: All the three 'B's are lonely pixels.

Constraints:
- `m == picture.length`
- `n == picture[i].length`
- `1 <= m, n <= 500`
- `picture[i][j]` is either 'B' or 'W'.

"""

# Solution
def findLonelyPixel(picture):
    """
    Function to find the number of black lonely pixels in the given picture.

    :param picture: List[List[str]] - 2D array of 'B' and 'W'
    :return: int - Number of lonely black pixels
    """
    m = len(picture)
    n = len(picture[0])
    
    # Count the number of 'B's in each row and column
    row_count = [0] * m
    col_count = [0] * n
    
    # First pass: Count 'B's in rows and columns
    for i in range(m):
        for j in range(n):
            if picture[i][j] == 'B':
                row_count[i] += 1
                col_count[j] += 1
    
    # Second pass: Check for lonely pixels
    lonely_pixels = 0
    for i in range(m):
        for j in range(n):
            if picture[i][j] == 'B' and row_count[i] == 1 and col_count[j] == 1:
                lonely_pixels += 1
    
    return lonely_pixels

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    picture1 = [["W", "W", "B"],
                ["W", "B", "W"],
                ["B", "W", "W"]]
    print(findLonelyPixel(picture1))  # Output: 3

    # Test Case 2
    picture2 = [["B", "W", "W"],
                ["W", "B", "W"],
                ["W", "W", "B"]]
    print(findLonelyPixel(picture2))  # Output: 3

    # Test Case 3
    picture3 = [["B", "B", "W"],
                ["W", "B", "W"],
                ["W", "W", "B"]]
    print(findLonelyPixel(picture3))  # Output: 1

    # Test Case 4
    picture4 = [["W", "W", "W"],
                ["W", "W", "W"],
                ["W", "W", "W"]]
    print(findLonelyPixel(picture4))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- First pass: O(m * n) to count the number of 'B's in rows and columns.
- Second pass: O(m * n) to check for lonely pixels.
- Total: O(m * n), where m is the number of rows and n is the number of columns.

Space Complexity:
- O(m + n) for the row_count and col_count arrays.
- Total: O(m + n).
"""

# Topic: Arrays