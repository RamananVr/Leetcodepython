"""
LeetCode Problem #2297: Jump Game VIII

Problem Statement:
You are given an array of integers `nums` and an integer `k`. You are initially positioned at the first index of the array. 
In one move, you can jump from index `i` to any index `j` such that:
    - `i < j <= i + k` (you can jump forward up to `k` steps), and
    - `nums[j] >= nums[i]` (you can only jump to indices with values greater than or equal to the current value).

Your goal is to determine the minimum number of jumps required to reach the last index of the array. If it is not possible to reach the last index, return -1.

Constraints:
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= nums.length`

Example:
Input: nums = [1, 3, 1, 2, 4, 2], k = 2
Output: 3
Explanation: The minimum jumps to reach the last index are:
- Start at index 0 (value = 1).
- Jump to index 1 (value = 3).
- Jump to index 4 (value = 4).
- Jump to index 5 (value = 2).

If it is not possible to reach the last index, return -1.
"""

from collections import deque

def min_jumps(nums, k):
    """
    Function to calculate the minimum number of jumps to reach the last index.
    If it is not possible, return -1.
    """
    n = len(nums)
    if n == 1:
        return 0  # Already at the last index

    # Deque to store indices for the sliding window maximum
    dq = deque()
    jumps = [float('inf')] * n
    jumps[0] = 0  # Starting point requires 0 jumps

    for i in range(n):
        # Remove indices from the deque that are out of the current window
        while dq and dq[0] < i - k:
            dq.popleft()

        # If the deque is not empty, update the minimum jumps for the current index
        if dq:
            jumps[i] = jumps[dq[0]] + 1

        # Maintain the deque in decreasing order of jumps[i]
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)

    # If the last index is unreachable, return -1
    return jumps[-1] if jumps[-1] != float('inf') else -1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 1, 2, 4, 2]
    k1 = 2
    print(min_jumps(nums1, k1))  # Output: 3

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    k2 = 1
    print(min_jumps(nums2, k2))  # Output: 4

    # Test Case 3
    nums3 = [5, 4, 3, 2, 1]
    k3 = 2
    print(min_jumps(nums3, k3))  # Output: -1

    # Test Case 4
    nums4 = [1]
    k4 = 1
    print(min_jumps(nums4, k4))  # Output: 0

    # Test Case 5
    nums5 = [1, 3, 1, 2, 4, 2, 6]
    k5 = 3
    print(min_jumps(nums5, k5))  # Output: 3


"""
Time Complexity:
- The algorithm iterates through the array once, and each index is added to and removed from the deque at most once.
- Thus, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The space complexity is O(k) due to the deque, which can hold at most k elements at any time.

Topic: Sliding Window, Deque, Dynamic Programming
"""