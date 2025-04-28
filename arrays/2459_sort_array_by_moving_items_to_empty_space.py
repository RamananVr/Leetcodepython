"""
LeetCode Question #2459: Sort Array by Moving Items to Empty Space

Problem Statement:
You are given an integer array `nums` of size `n` where `nums` is a permutation of the integers in the range `[0, n - 1]`. You are also given an integer `k`.

You can perform the following operation on the array `nums` at most `k` times:
- Pick two indices `i` and `j` such that `nums[i]` and `nums[j]` are not in their correct positions, and swap `nums[i]` with `nums[j]`.

Return the minimum number of swaps required to sort the array `nums` such that all elements are in their correct positions.

Constraints:
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] < nums.length`
- `nums` is a permutation of integers in the range `[0, n - 1]`.
- `0 <= k <= 10^9`
"""

# Solution
def minimumSwaps(nums, k):
    """
    Calculate the minimum number of swaps required to sort the array `nums`.

    Args:
    nums (List[int]): The input array, a permutation of integers in the range [0, n-1].
    k (int): The maximum number of swaps allowed.

    Returns:
    int: The minimum number of swaps required to sort the array.
    """
    n = len(nums)
    swaps = 0
    visited = [False] * n

    for i in range(n):
        if visited[i] or nums[i] == i:
            continue

        cycle_size = 0
        j = i

        while not visited[j]:
            visited[j] = True
            j = nums[j]
            cycle_size += 1

        if cycle_size > 1:
            swaps += cycle_size - 1

    return swaps

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 3, 2, 1, 0]
    k1 = 10
    print(minimumSwaps(nums1, k1))  # Expected Output: 2

    # Test Case 2
    nums2 = [1, 0, 3, 2]
    k2 = 5
    print(minimumSwaps(nums2, k2))  # Expected Output: 2

    # Test Case 3
    nums3 = [0, 1, 2, 3, 4]
    k3 = 0
    print(minimumSwaps(nums3, k3))  # Expected Output: 0

    # Test Case 4
    nums4 = [2, 0, 1, 4, 3]
    k4 = 100
    print(minimumSwaps(nums4, k4))  # Expected Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
The algorithm iterates through the array once, and for each unvisited element, it traces a cycle of swaps. 
In the worst case, the entire array is one large cycle, resulting in O(n) operations. Thus, the time complexity is O(n).

Space Complexity:
The algorithm uses an auxiliary array `visited` of size `n` to keep track of visited elements. 
Thus, the space complexity is O(n).
"""

# Topic: Arrays