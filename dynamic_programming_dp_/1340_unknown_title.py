"""
LeetCode Problem #1340: Jump Game V

Problem Statement:
Given an array of integers `arr` and an integer `d`. In one step, you can jump from index `i` to index:
- `i + k` where: `i < i + k <= i + d` and `arr[i] > arr[i + k]`, or
- `i - k` where: `i - d <= i - k < i` and `arr[i] > arr[i - k]`.

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.

Constraints:
- `1 <= arr.length <= 1000`
- `1 <= arr[i] <= 10^5`
- `1 <= d <= arr.length`
"""

from functools import lru_cache

def maxJumps(arr, d):
    """
    Function to calculate the maximum number of indices you can visit starting from any index.

    :param arr: List[int] - The array of integers.
    :param d: int - The maximum distance you can jump.
    :return: int - The maximum number of indices you can visit.
    """
    n = len(arr)

    @lru_cache(None)
    def dfs(i):
        # Start with the current index as the only visited index
        max_reachable = 1

        # Check jumps to the right
        for k in range(1, d + 1):
            if i + k >= n or arr[i + k] >= arr[i]:
                break
            max_reachable = max(max_reachable, 1 + dfs(i + k))

        # Check jumps to the left
        for k in range(1, d + 1):
            if i - k < 0 or arr[i - k] >= arr[i]:
                break
            max_reachable = max(max_reachable, 1 + dfs(i - k))

        return max_reachable

    # Compute the maximum jumps starting from any index
    return max(dfs(i) for i in range(n))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12]
    d1 = 2
    print(maxJumps(arr1, d1))  # Expected Output: 4

    # Test Case 2
    arr2 = [3, 3, 3, 3, 3]
    d2 = 3
    print(maxJumps(arr2, d2))  # Expected Output: 1

    # Test Case 3
    arr3 = [7, 6, 5, 4, 3, 2, 1]
    d3 = 1
    print(maxJumps(arr3, d3))  # Expected Output: 7

    # Test Case 4
    arr4 = [7, 1, 7, 1, 7, 1]
    d4 = 2
    print(maxJumps(arr4, d4))  # Expected Output: 2

    # Test Case 5
    arr5 = [66]
    d5 = 1
    print(maxJumps(arr5, d5))  # Expected Output: 1


"""
Time Complexity Analysis:
- The function `dfs` is called once for each index in the array, and each call explores up to `d` indices to the left and `d` indices to the right.
- Thus, the time complexity is O(n * d), where `n` is the length of the array and `d` is the maximum jump distance.
- The use of `lru_cache` ensures that each index is processed only once.

Space Complexity Analysis:
- The space complexity is O(n) for the recursion stack and O(n) for the `lru_cache`, resulting in a total space complexity of O(n).

Topic: Dynamic Programming (DP)
"""