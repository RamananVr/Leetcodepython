"""
LeetCode Problem #302: Smallest Rectangle Enclosing Black Pixels

Problem Statement:
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. 
The black pixels are connected, i.e., there is only one black region. Pixels are connected 
horizontally and vertically. Given the location (x, y) of one of the black pixels, return 
the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

You will be given:
- An m x n binary matrix `image`.
- An integer `x` and an integer `y` representing the coordinates of one black pixel.

Your task is to return the area of the smallest rectangle enclosing all black pixels.

Constraints:
- m == image.length
- n == image[i].length
- 1 <= m, n <= 100
- image[i][j] is either '0' or '1'.
- 1 <= x < m
- 1 <= y < n
- image[x][y] == '1'
- The black pixels are connected.

Example:
Input: image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2
Output: 6
Explanation: The smallest rectangle enclosing all black pixels is:
[[0, 2], [2, 3]], so the area is 6.
"""

from typing import List

def minArea(image: List[List[str]], x: int, y: int) -> int:
    def search_rows(image, top, bottom, left, right, opt):
        while top < bottom:
            mid = (top + bottom) // 2
            if ('1' in image[mid][left:right]) == opt:
                bottom = mid
            else:
                top = mid + 1
        return top

    def search_columns(image, top, bottom, left, right, opt):
        while left < right:
            mid = (left + right) // 2
            if any(image[i][mid] == '1' for i in range(top, bottom)) == opt:
                right = mid
            else:
                left = mid + 1
        return left

    m, n = len(image), len(image[0])
    top = search_rows(image, 0, x, 0, n, True)
    bottom = search_rows(image, x + 1, m, 0, n, False)
    left = search_columns(image, top, bottom, 0, y, True)
    right = search_columns(image, top, bottom, y + 1, n, False)

    return (bottom - top) * (right - left)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    image1 = [
        ["0", "0", "1", "0"],
        ["0", "1", "1", "0"],
        ["0", "1", "0", "0"]
    ]
    x1, y1 = 0, 2
    print(minArea(image1, x1, y1))  # Output: 6

    # Test Case 2
    image2 = [
        ["0", "0", "0", "0"],
        ["0", "1", "1", "0"],
        ["0", "1", "1", "0"],
        ["0", "0", "0", "0"]
    ]
    x2, y2 = 1, 1
    print(minArea(image2, x2, y2))  # Output: 4

    # Test Case 3
    image3 = [
        ["1"]
    ]
    x3, y3 = 0, 0
    print(minArea(image3, x3, y3))  # Output: 1

"""
Time Complexity:
- The binary search for rows and columns takes O(log(m) * n + log(n) * m), where m is the number of rows and n is the number of columns.
- In the worst case, this simplifies to O(m * log(n) + n * log(m)).

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures.

Topic: Binary Search
"""