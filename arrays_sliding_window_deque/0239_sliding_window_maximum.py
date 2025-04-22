"""
LeetCode Question #239: Sliding Window Maximum

Problem Statement:
You are given an array of integers `nums`, and there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]       7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1, -1], k = 1
Output: [1, -1]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
"""

from collections import deque

def maxSlidingWindow(nums, k):
    """
    Finds the maximum value in each sliding window of size k in the array nums.

    :param nums: List[int] - The input array of integers.
    :param k: int - The size of the sliding window.
    :return: List[int] - A list of the maximum values for each sliding window.
    """
    if not nums or k == 0:
        return []

    # Deque to store indices of elements in the current window
    dq = deque()
    result = []

    for i in range(len(nums)):
        # Remove indices that are out of the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove indices of elements smaller than the current element
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Add the current element's index to the deque
        dq.append(i)

        # Append the maximum element of the current window to the result
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3
    print(maxSlidingWindow(nums1, k1))  # Output: [3, 3, 5, 5, 6, 7]

    # Test Case 2
    nums2 = [1]
    k2 = 1
    print(maxSlidingWindow(nums2, k2))  # Output: [1]

    # Test Case 3
    nums3 = [1, -1]
    k3 = 1
    print(maxSlidingWindow(nums3, k3))  # Output: [1, -1]

    # Test Case 4
    nums4 = [9, 11]
    k4 = 2
    print(maxSlidingWindow(nums4, k4))  # Output: [11]

    # Test Case 5
    nums5 = [4, -2]
    k5 = 2
    print(maxSlidingWindow(nums5, k5))  # Output: [4]

"""
Time Complexity:
- O(n): Each element is added to and removed from the deque at most once, resulting in linear time complexity.

Space Complexity:
- O(k): The deque stores at most k elements, where k is the size of the sliding window.

Topic: Arrays, Sliding Window, Deque
"""