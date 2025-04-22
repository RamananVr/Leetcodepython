"""
LeetCode Problem #661: Image Smoother

Problem Statement:
An image is represented by a 2D integer matrix `img` where `img[i][j]` represents the pixel value of the image.

You need to smooth the image with the following rules:
1. For a pixel located at `img[i][j]`, consider all its 8 neighbors and itself. If a neighbor is out of bounds, it is not considered.
2. The value of `img[i][j]` should be the floor of the average of the pixel values in the 3x3 grid centered around `img[i][j]`.

Return the resulting "smoothed" image as a 2D integer matrix.

Constraints:
- `m == img.length`
- `n == img[i].length`
- `1 <= m, n <= 200`
- `0 <= img[i][j] <= 255`
"""

def imageSmoother(img):
    """
    Smooths the given image by calculating the average of each pixel and its neighbors.

    :param img: List[List[int]] - 2D matrix representing the image
    :return: List[List[int]] - Smoothed 2D matrix
    """
    # Dimensions of the image
    m, n = len(img), len(img[0])
    
    # Resultant smoothed image
    result = [[0] * n for _ in range(m)]
    
    # Directions for 8 neighbors and the cell itself
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for i in range(m):
        for j in range(n):
            total, count = 0, 0
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n:  # Check bounds
                    total += img[ni][nj]
                    count += 1
            result[i][j] = total // count  # Floor division for average
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    img1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    print("Test Case 1 Output:", imageSmoother(img1))
    # Expected Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Test Case 2
    img2 = [
        [100, 200, 100],
        [200, 50, 200],
        [100, 200, 100]
    ]
    print("Test Case 2 Output:", imageSmoother(img2))
    # Expected Output: [[137, 141, 137], [141, 138, 141], [137, 141, 137]]

    # Test Case 3
    img3 = [
        [7, 4],
        [0, 10]
    ]
    print("Test Case 3 Output:", imageSmoother(img3))
    # Expected Output: [[5, 5], [5, 5]]

"""
Time Complexity Analysis:
- Let `m` be the number of rows and `n` be the number of columns in the image.
- For each pixel in the image (O(m * n)), we iterate over at most 9 neighbors (constant time).
- Therefore, the time complexity is O(m * n).

Space Complexity Analysis:
- The space complexity is O(m * n) for the result matrix.
- No additional space is used apart from the result matrix and a few variables, so the space complexity is O(m * n).

Topic: Arrays, Matrix
"""