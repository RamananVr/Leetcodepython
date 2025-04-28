"""
LeetCode Problem #832: Flipping an Image

Problem Statement:
Given an n x n binary matrix `image`, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.
- For example, flipping [1,1,0] horizontally results in [0,1,1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
- For example, inverting [0,1,1] results in [1,0,0].

Example 1:
Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation:
First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]].

Example 2:
Input: image = [[1,1,0],[1,1,1],[0,1,1]]
Output: [[1,0,0],[0,0,0],[0,0,1]]
Explanation:
First reverse each row: [[0,1,1],[1,1,1],[1,1,0]].
Then, invert the image: [[1,0,0],[0,0,0],[0,0,1]].

Constraints:
- n == image.length
- n == image[i].length
- 1 <= n <= 20
- image[i][j] is either 0 or 1.
"""

# Clean and Correct Python Solution
def flipAndInvertImage(image):
    """
    Flips the image horizontally and inverts it.

    Args:
    image (List[List[int]]): A binary matrix.

    Returns:
    List[List[int]]: The resulting binary matrix after flipping and inverting.
    """
    for row in image:
        # Flip the row by reversing it and invert it by replacing 0 with 1 and 1 with 0
        for i in range((len(row) + 1) // 2):  # Iterate only halfway (inclusive of middle for odd lengths)
            # Swap and invert the elements at the two ends
            row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
    return image

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    image1 = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(flipAndInvertImage(image1))  # Expected Output: [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

    # Test Case 2
    image2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(flipAndInvertImage(image2))  # Expected Output: [[1, 0, 0], [0, 0, 0], [0, 0, 1]]

    # Test Case 3
    image3 = [[1, 0], [0, 1]]
    print(flipAndInvertImage(image3))  # Expected Output: [[1, 0], [0, 1]]

    # Test Case 4
    image4 = [[1]]
    print(flipAndInvertImage(image4))  # Expected Output: [[0]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n be the number of rows and columns in the image (n x n matrix).
- For each row, we iterate through half of its elements (O(n/2) = O(n)).
- Since there are n rows, the total time complexity is O(n * n) = O(n^2).

Space Complexity:
- The operation is performed in-place, so no additional space is used apart from a few variables.
- Space complexity is O(1).
"""

# Topic: Arrays