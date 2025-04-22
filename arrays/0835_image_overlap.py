"""
LeetCode Question #835: Image Overlap

Problem Statement:
You are given two images, img1 and img2, represented as binary matrices of size n x n. 
An image is a binary matrix with 0s and 1s as values. We translate one image (img1) 
by sliding it over the other image (img2), and the overlap is the number of positions 
where both images have a 1 in the same cell.

Return the largest possible overlap.

Example:
Input: img1 = [[1,1,0],
               [0,1,0],
               [0,1,0]],
       img2 = [[0,0,0],
               [0,1,1],
               [0,0,1]]
Output: 3

Constraints:
- n == img1.length == img1[i].length
- n == img2.length == img2[i].length
- 1 <= n <= 30
- img1[i][j] is either 0 or 1.
- img2[i][j] is either 0 or 1.
"""

# Solution
from collections import Counter

def largestOverlap(img1, img2):
    def get_ones_positions(image):
        """Helper function to get positions of 1s in the image."""
        positions = []
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == 1:
                    positions.append((i, j))
        return positions

    # Get positions of 1s in both images
    positions1 = get_ones_positions(img1)
    positions2 = get_ones_positions(img2)

    # Count translations (vector differences) between positions in img1 and img2
    translation_count = Counter()
    for p1 in positions1:
        for p2 in positions2:
            translation = (p2[0] - p1[0], p2[1] - p1[1])
            translation_count[translation] += 1

    # Return the maximum overlap found
    return max(translation_count.values(), default=0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    img1 = [[1, 1, 0],
            [0, 1, 0],
            [0, 1, 0]]
    img2 = [[0, 0, 0],
            [0, 1, 1],
            [0, 0, 1]]
    print(largestOverlap(img1, img2))  # Output: 3

    # Test Case 2
    img1 = [[1, 0],
            [0, 0]]
    img2 = [[0, 1],
            [1, 0]]
    print(largestOverlap(img1, img2))  # Output: 1

    # Test Case 3
    img1 = [[1]]
    img2 = [[1]]
    print(largestOverlap(img1, img2))  # Output: 1

    # Test Case 4
    img1 = [[0]]
    img2 = [[0]]
    print(largestOverlap(img1, img2))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Let n be the size of the image (n x n matrix).
- Extracting positions of 1s in both images takes O(n^2).
- Comparing all pairs of positions between img1 and img2 takes O(k1 * k2), 
  where k1 and k2 are the number of 1s in img1 and img2, respectively.
- In the worst case, k1 and k2 can be O(n^2), so the overall complexity is O(n^4).

Space Complexity:
- The space required to store positions of 1s is O(k1 + k2), which is O(n^2) in the worst case.
- The Counter object for translations can also take O(n^2) space in the worst case.
- Overall space complexity is O(n^2).

Topic: Arrays
"""