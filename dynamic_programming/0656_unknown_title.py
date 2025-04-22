"""
LeetCode Problem #656: Coin Path

Problem Statement:
Given an array `A` of integers, you are initially positioned at the first index of the array. Each element in the array represents the cost of stepping on that index. You can jump at most `B` steps forward at a time. Your goal is to reach the last index of the array in the minimum cost. Return the path of indices (1-based) that you take to reach the last index in the minimum cost. If there are multiple paths with the same cost, return the lexicographically smallest path. If it is not possible to reach the last index, return an empty list.

Constraints:
- `1 <= len(A) <= 1000`
- `1 <= B <= 100`
- `1 <= A[i] <= 100`

Example:
Input: A = [1, 2, 4, 6, 2], B = 2
Output: [1, 3, 5]

Input: A = [1, 2, 4, 6, 2], B = 1
Output: []

"""

# Python Solution
from typing import List

def cheapestJump(A: List[int], B: int) -> List[int]:
    n = len(A)
    if n == 0 or A[-1] == -1:
        return []

    # dp[i] will store the minimum cost to reach the end from index i
    dp = [float('inf')] * n
    # path[i] will store the next index to jump to from index i
    path = [-1] * n

    dp[-1] = A[-1]  # Base case: cost to reach the end from the last index is its own cost

    # Fill dp and path arrays from right to left
    for i in range(n - 2, -1, -1):
        if A[i] == -1:  # Skip if the index is not reachable
            continue
        for j in range(i + 1, min(i + B + 1, n)):
            if dp[j] != float('inf') and dp[i] > A[i] + dp[j]:
                dp[i] = A[i] + dp[j]
                path[i] = j

    # If the first index cannot reach the end, return an empty list
    if dp[0] == float('inf'):
        return []

    # Reconstruct the path
    result = []
    current = 0
    while current != -1:
        result.append(current + 1)  # Convert to 1-based index
        current = path[current]

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    A1 = [1, 2, 4, 6, 2]
    B1 = 2
    print(cheapestJump(A1, B1))  # Output: [1, 3, 5]

    # Test Case 2
    A2 = [1, 2, 4, 6, 2]
    B2 = 1
    print(cheapestJump(A2, B2))  # Output: []

    # Test Case 3
    A3 = [1, 2, 4, -1, 2]
    B3 = 2
    print(cheapestJump(A3, B3))  # Output: [1, 3, 5]

    # Test Case 4
    A4 = [1, -1, 4, 6, 2]
    B4 = 2
    print(cheapestJump(A4, B4))  # Output: []

# Time and Space Complexity Analysis
# Time Complexity: O(n * B)
# - We iterate over each index `i` from n-2 to 0, and for each index, we check up to B indices ahead.
# - This results in a total of O(n * B) operations.

# Space Complexity: O(n)
# - We use two arrays, `dp` and `path`, each of size n. The space complexity is therefore O(n).

# Topic: Dynamic Programming