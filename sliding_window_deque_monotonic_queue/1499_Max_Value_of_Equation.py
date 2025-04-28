"""
LeetCode Problem #1499: Max Value of Equation

Problem Statement:
You are given an array `points` containing `n` points represented as [xi, yi], and an integer `k`.
The value of the equation is calculated as `(yi + yj + |xi - xj|)` where `|xi - xj|` is the absolute difference 
of xi and xj, and `i < j`.

Return the maximum value of the equation for all `1 <= i < j <= points.length` such that `|xi - xj| <= k`.

It is guaranteed that there will be at least one pair of points that satisfy the constraint `|xi - xj| <= k`.

Constraints:
- 2 <= points.length <= 10^5
- points[i].length == 2
- -10^8 <= xi, yi <= 10^8
- 0 <= k <= 2 * 10^8
- xi < xj for all 1 <= i < j <= points.length
"""

from collections import deque

def findMaxValueOfEquation(points, k):
    """
    Finds the maximum value of the equation (yi + yj + |xi - xj|) for all valid pairs of points.

    :param points: List[List[int]] - A list of points where each point is represented as [xi, yi].
    :param k: int - The maximum allowed difference between xi and xj.
    :return: int - The maximum value of the equation.
    """
    # Initialize a deque to store pairs of (yi - xi, xi)
    dq = deque()
    max_value = float('-inf')

    for x, y in points:
        # Remove points from the deque that are out of the range |xi - xj| > k
        while dq and x - dq[0][1] > k:
            dq.popleft()

        # If the deque is not empty, calculate the potential maximum value
        if dq:
            max_value = max(max_value, y + x + dq[0][0])

        # Maintain the deque in decreasing order of (yi - xi)
        while dq and dq[-1][0] <= y - x:
            dq.pop()

        # Add the current point to the deque
        dq.append((y - x, x))

    return max_value

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [[1, 3], [2, 0], [3, 10], [4, 2], [5, 8]]
    k1 = 2
    print(findMaxValueOfEquation(points1, k1))  # Expected Output: 15

    # Test Case 2
    points2 = [[1, 2], [2, 4], [3, 6]]
    k2 = 1
    print(findMaxValueOfEquation(points2, k2))  # Expected Output: 8

    # Test Case 3
    points3 = [[1, 3], [3, 5], [6, 7]]
    k3 = 3
    print(findMaxValueOfEquation(points3, k3))  # Expected Output: 12

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the `points` array once, performing O(1) operations for each point
  (deque operations like append, pop, and popleft are O(1) amortized).
- Therefore, the time complexity is O(n), where n is the number of points.

Space Complexity:
- The deque stores at most n elements in the worst case, so the space complexity is O(n).

Topic: Sliding Window, Deque, Monotonic Queue
"""