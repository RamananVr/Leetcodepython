"""
LeetCode Problem #2355: Maximum Number of Books You Can Take

Problem Statement:
You are given an array `books` where `books[i]` represents the number of books on the i-th shelf. You want to take books from the shelves such that:
1. You can only take books from consecutive shelves.
2. If you take books from the i-th shelf, you cannot take more than `books[i]` books.
3. If you take books from the i-th shelf, you cannot take more than `books[i-1] - 1` books from the (i+1)-th shelf, and so on.

Return the maximum number of books you can take.

Constraints:
- `1 <= books.length <= 10^5`
- `1 <= books[i] <= 10^9`
"""

# Solution
def maximumBooks(books):
    n = len(books)
    dp = [0] * n  # dp[i] represents the maximum number of books we can take ending at shelf i
    stack = []  # Monotonic stack to keep track of valid shelves

    for i in range(n):
        # Calculate the maximum number of books we can take from shelf i
        max_books = books[i]
        if stack:
            prev = stack[-1]
            max_books = min(max_books, books[prev] - (i - prev))
        
        # Update dp[i]
        dp[i] = max_books + (dp[stack[-1]] if stack else 0)
        
        # Maintain the monotonic stack
        while stack and books[stack[-1]] >= books[i]:
            stack.pop()
        stack.append(i)

    return max(dp)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    books1 = [4, 2, 3, 1]
    print(maximumBooks(books1))  # Expected Output: 7

    # Test Case 2
    books2 = [5, 5, 5, 5]
    print(maximumBooks(books2))  # Expected Output: 15

    # Test Case 3
    books3 = [1, 2, 3, 4, 5]
    print(maximumBooks(books3))  # Expected Output: 15

    # Test Case 4
    books4 = [10, 1, 1, 1, 1]
    print(maximumBooks(books4))  # Expected Output: 10

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the `books` array once, and each element is pushed and popped from the stack at most once.
- Therefore, the time complexity is O(n), where n is the length of the `books` array.

Space Complexity:
- The space complexity is O(n) due to the `dp` array and the monotonic stack.

Topic: Dynamic Programming, Monotonic Stack
"""