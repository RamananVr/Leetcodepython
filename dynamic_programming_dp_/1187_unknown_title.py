"""
LeetCode Problem #1187: Make Array Strictly Increasing

Problem Statement:
Given two integer arrays `arr1` and `arr2`, return the minimum number of operations (possibly zero) required to make `arr1` strictly increasing. In one operation, you can choose any element from `arr2` and replace any element of `arr1` with it.

Note:
- The chosen elements from `arr2` can be reused any number of times.
- `arr2` may contain duplicates, but you can reorder it as you wish.

If it is impossible to make `arr1` strictly increasing, return -1.

Constraints:
- 1 <= arr1.length, arr2.length <= 2000
- 0 <= arr1[i], arr2[i] <= 10^9
"""

# Solution
from bisect import bisect_right
from functools import lru_cache

def makeArrayIncreasing(arr1, arr2):
    """
    Function to determine the minimum number of operations required to make arr1 strictly increasing.
    :param arr1: List[int] - The first array.
    :param arr2: List[int] - The second array.
    :return: int - Minimum number of operations or -1 if impossible.
    """
    arr2 = sorted(set(arr2))  # Remove duplicates and sort arr2

    @lru_cache(None)
    def dfs(index, prev):
        # Base case: If we've processed all elements in arr1
        if index == len(arr1):
            return 0

        # Initialize the minimum operations to infinity
        min_operations = float('inf')

        # Option 1: Keep the current element in arr1 if it's strictly greater than `prev`
        if arr1[index] > prev:
            min_operations = min(min_operations, dfs(index + 1, arr1[index]))

        # Option 2: Replace the current element in arr1 with an element from arr2
        # Find the smallest element in arr2 that is strictly greater than `prev`
        replace_index = bisect_right(arr2, prev)
        if replace_index < len(arr2):
            min_operations = min(min_operations, 1 + dfs(index + 1, arr2[replace_index]))

        return min_operations

    # Start the DFS from the first index with a previous value of -inf
    result = dfs(0, float('-inf'))

    # If the result is infinity, it means it's impossible to make arr1 strictly increasing
    return result if result != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 5, 3, 6, 7]
    arr2 = [1, 3, 2, 4]
    print(makeArrayIncreasing(arr1, arr2))  # Expected Output: 1

    # Test Case 2
    arr1 = [1, 5, 3, 6, 7]
    arr2 = [4, 3, 1]
    print(makeArrayIncreasing(arr1, arr2))  # Expected Output: 2

    # Test Case 3
    arr1 = [1, 5, 3, 6, 7]
    arr2 = [1, 6, 3, 3]
    print(makeArrayIncreasing(arr1, arr2))  # Expected Output: -1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting `arr2` takes O(n2 log n2), where n2 is the length of arr2.
- The DFS function is called for each index in arr1 and each possible `prev` value.
- Since `arr2` is sorted and deduplicated, the number of possible `prev` values is at most n2.
- Thus, the total complexity is O(n1 * n2), where n1 is the length of arr1.

Space Complexity:
- The space complexity is O(n1 * n2) due to the memoization table used in DFS.
- Additionally, the sorted `arr2` takes O(n2) space.
- Total space complexity: O(n1 * n2).
"""

# Topic: Dynamic Programming (DP)