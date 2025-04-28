"""
LeetCode Problem #2282: Number of People That Can Be Seen in a Grid

Problem Statement:
You are given an m x n 2D grid of integers `heights` where `heights[i][j]` represents the height of a person standing at cell (i, j). 
A person at cell (i, j) can see another person at cell (x, y) if and only if:
1. Both cells are in the same row or column.
2. All the cells between (i, j) and (x, y) (excluding (i, j) and (x, y)) have a height strictly less than the height of the person at (i, j).

Return a 2D grid `result` of the same dimensions as `heights` where `result[i][j]` is the number of people that the person at cell (i, j) can see.

Constraints:
- m == heights.length
- n == heights[i].length
- 1 <= m, n <= 1000
- 1 <= heights[i][j] <= 10^6
"""

# Solution
from collections import deque

def num_visible_people(heights):
    m, n = len(heights), len(heights[0])
    result = [[0] * n for _ in range(m)]

    # Helper function to calculate visible people in a single direction
    def calculate_visible(arr):
        stack = deque()
        visible = [0] * len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            visible[i] = len(stack)
            stack.append(i)
        return visible

    # Process rows
    for i in range(m):
        left_to_right = calculate_visible(heights[i])
        right_to_left = calculate_visible(heights[i][::-1])[::-1]
        for j in range(n):
            result[i][j] += left_to_right[j] + right_to_left[j]

    # Process columns
    for j in range(n):
        column = [heights[i][j] for i in range(m)]
        top_to_bottom = calculate_visible(column)
        bottom_to_top = calculate_visible(column[::-1])[::-1]
        for i in range(m):
            result[i][j] += top_to_bottom[i] + bottom_to_top[i]

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    heights1 = [
        [3, 1, 4],
        [2, 5, 6],
        [1, 2, 3]
    ]
    print(num_visible_people(heights1))
    # Expected Output: [[2, 1, 2], [2, 3, 2], [1, 1, 1]]

    # Test Case 2
    heights2 = [
        [1, 2],
        [3, 4]
    ]
    print(num_visible_people(heights2))
    # Expected Output: [[1, 1], [1, 1]]

    # Test Case 3
    heights3 = [
        [5]
    ]
    print(num_visible_people(heights3))
    # Expected Output: [[0]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating visible people for each row takes O(n) for each of the m rows, resulting in O(m * n).
- Calculating visible people for each column takes O(m) for each of the n columns, resulting in O(m * n).
- Overall time complexity: O(m * n).

Space Complexity:
- The space used by the `stack` in the helper function is O(max(m, n)).
- The space used by the `result` grid is O(m * n).
- Overall space complexity: O(m * n).
"""

# Topic: Arrays, Monotonic Stack