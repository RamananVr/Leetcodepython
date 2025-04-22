"""
LeetCode Problem #533: Lonely Pixel II

Problem Statement:
Given an `m x n` picture consisting of black ('B') and white ('W') pixels, return the number of black lonely pixels.

A black lonely pixel is a character 'B' that located at a specific position (r, c) where:
1. Row r and column c both contain exactly N black pixels.
2. For all rows that have a black pixel at column c, they should be exactly the same as row r.

Example 1:
Input: picture = [["W", "B", "W", "B", "B"],
                  ["W", "B", "W", "B", "B"],
                  ["W", "B", "W", "B", "B"]], N = 3
Output: 6
Explanation: All the black pixels at column 1 and 3 are black lonely pixels.

Example 2:
Input: picture = [["W", "B", "W"],
                  ["W", "B", "W"],
                  ["W", "B", "W"]], N = 1
Output: 0
Explanation: No black lonely pixel found.

Constraints:
- The picture is a 2D array of size `m x n` where `m, n <= 200`.
- The picture consists of characters 'B' and 'W' only.
- `N` is an integer in the range `[1, min(m, n)]`.
"""

def findBlackPixel(picture, N):
    """
    Function to find the number of black lonely pixels in the given picture.

    :param picture: List[List[str]] - 2D array of 'B' and 'W' characters
    :param N: int - The required number of black pixels in a row/column
    :return: int - The count of black lonely pixels
    """
    from collections import Counter

    # Count the rows
    row_count = Counter(map(tuple, picture))
    col_count = [0] * len(picture[0])

    # Count black pixels in each column
    for row in picture:
        for col in range(len(row)):
            if row[col] == 'B':
                col_count[col] += 1

    lonely_pixel_count = 0

    # Check for lonely pixels
    for row in picture:
        if row_count[tuple(row)] == N and row.count('B') == N:
            for col in range(len(row)):
                if row[col] == 'B' and col_count[col] == N:
                    lonely_pixel_count += 1

    return lonely_pixel_count


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    picture1 = [
        ["W", "B", "W", "B", "B"],
        ["W", "B", "W", "B", "B"],
        ["W", "B", "W", "B", "B"]
    ]
    N1 = 3
    print(findBlackPixel(picture1, N1))  # Output: 6

    # Test Case 2
    picture2 = [
        ["W", "B", "W"],
        ["W", "B", "W"],
        ["W", "B", "W"]
    ]
    N2 = 1
    print(findBlackPixel(picture2, N2))  # Output: 0

    # Test Case 3
    picture3 = [
        ["B", "W", "B"],
        ["B", "W", "B"],
        ["B", "W", "B"]
    ]
    N3 = 3
    print(findBlackPixel(picture3, N3))  # Output: 3

    # Test Case 4
    picture4 = [
        ["B", "B", "B"],
        ["B", "B", "B"],
        ["B", "B", "B"]
    ]
    N4 = 3
    print(findBlackPixel(picture4, N4))  # Output: 9


"""
Time Complexity Analysis:
- Let m = number of rows, n = number of columns.
- Counting rows and columns takes O(m * n).
- Checking for lonely pixels involves iterating through the rows and columns, which is O(m * n).
- Overall time complexity: O(m * n).

Space Complexity Analysis:
- The space used for row_count is O(m) (number of unique rows).
- The space used for col_count is O(n).
- Overall space complexity: O(m + n).

Topic: Arrays, Hash Table
"""