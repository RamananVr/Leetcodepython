"""
LeetCode Problem #1105: Filling Bookcase Shelves

Problem Statement:
You are given an array `books` where `books[i] = [thickness_i, height_i]` indicates the thickness and height of the ith book. 
You are also given an integer `shelf_width` which represents the width of each shelf.

You can place books in order on shelves, but you must follow these rules:
1. You can only place books on the same shelf if the sum of their thicknesses does not exceed `shelf_width`.
2. You can start a new shelf at any time.
3. The height of a shelf is the maximum height of the books on that shelf.

Return the minimum possible height of the bookshelf.

Constraints:
- `1 <= books.length <= 1000`
- `1 <= thickness_i, height_i <= 1000`
- `1 <= shelf_width <= 1000`
"""

# Solution
def minHeightShelves(books, shelf_width):
    """
    Dynamic Programming solution to minimize the height of the bookshelf.
    
    :param books: List[List[int]] - List of books where each book is represented as [thickness, height].
    :param shelf_width: int - Maximum width of a shelf.
    :return: int - Minimum height of the bookshelf.
    """
    n = len(books)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: no books, no height

    for i in range(1, n + 1):
        width = 0
        height = 0
        for j in range(i, 0, -1):
            width += books[j - 1][0]
            if width > shelf_width:
                break
            height = max(height, books[j - 1][1])
            dp[i] = min(dp[i], dp[j - 1] + height)

    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    books1 = [[1, 1], [2, 3], [2, 3], [1, 1]]
    shelf_width1 = 4
    print(minHeightShelves(books1, shelf_width1))  # Expected Output: 6

    # Test Case 2
    books2 = [[1, 3], [2, 4], [3, 2]]
    shelf_width2 = 6
    print(minHeightShelves(books2, shelf_width2))  # Expected Output: 4

    # Test Case 3
    books3 = [[1, 2], [2, 3], [2, 4], [1, 5]]
    shelf_width3 = 5
    print(minHeightShelves(books3, shelf_width3))  # Expected Output: 7

    # Test Case 4
    books4 = [[7, 3], [8, 7], [2, 7], [2, 5]]
    shelf_width4 = 10
    print(minHeightShelves(books4, shelf_width4))  # Expected Output: 15

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop runs for each book (O(n)).
- The inner loop iterates backward for each book, but the total number of iterations across all books is bounded by O(n).
- Therefore, the time complexity is O(n^2).

Space Complexity:
- The space complexity is O(n) due to the dp array.
"""

# Topic: Dynamic Programming