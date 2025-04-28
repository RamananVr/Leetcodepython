"""
LeetCode Question #1438: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Problem Statement:
Given an array of integers `nums` and an integer `limit`, return the size of the longest continuous subarray 
such that the absolute difference between any two elements of this subarray is less than or equal to `limit`.

If there is no such subarray, return 0.

Example 1:
Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
- [8] with maximum absolute diff |8-8| = 0 <= 4.
- [2] with maximum absolute diff |2-2| = 0 <= 4.
- [4] with maximum absolute diff |4-4| = 0 <= 4.
- [7] with maximum absolute diff |7-7| = 0 <= 4.
- [8,2] with maximum absolute diff |8-2| = 6 > 4.
- [2,4] with maximum absolute diff |2-4| = 2 <= 4.
- [4,7] with maximum absolute diff |4-7| = 3 <= 4.
Therefore, the size of the longest subarray is 2.

Example 2:
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest subarray where the absolute difference between any two elements is <= 5.

Example 3:
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
Explanation: The subarray [2,2,2] is the longest subarray where the absolute difference between any two elements is <= 0.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 0 <= limit <= 10^9
"""

from collections import deque

def longestSubarray(nums, limit):
    """
    Finds the size of the longest continuous subarray such that the absolute difference 
    between any two elements of this subarray is less than or equal to the given limit.

    :param nums: List[int] - The input array of integers.
    :param limit: int - The maximum allowed absolute difference between any two elements.
    :return: int - The size of the longest subarray.
    """
    max_deque = deque()  # Stores indices of elements in decreasing order
    min_deque = deque()  # Stores indices of elements in increasing order
    left = 0  # Left pointer of the sliding window
    result = 0  # Maximum length of the subarray

    for right in range(len(nums)):
        # Maintain max_deque for the maximum element in the current window
        while max_deque and nums[max_deque[-1]] <= nums[right]:
            max_deque.pop()
        max_deque.append(right)

        # Maintain min_deque for the minimum element in the current window
        while min_deque and nums[min_deque[-1]] >= nums[right]:
            min_deque.pop()
        min_deque.append(right)

        # Check if the current window satisfies the condition
        while nums[max_deque[0]] - nums[min_deque[0]] > limit:
            left += 1
            # Remove elements outside the current window from both deques
            if max_deque[0] < left:
                max_deque.popleft()
            if min_deque[0] < left:
                min_deque.popleft()

        # Update the result with the size of the current valid window
        result = max(result, right - left + 1)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [8, 2, 4, 7]
    limit1 = 4
    print(longestSubarray(nums1, limit1))  # Output: 2

    # Test Case 2
    nums2 = [10, 1, 2, 4, 7, 2]
    limit2 = 5
    print(longestSubarray(nums2, limit2))  # Output: 4

    # Test Case 3
    nums3 = [4, 2, 2, 2, 4, 4, 2, 2]
    limit3 = 0
    print(longestSubarray(nums3, limit3))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once with the right pointer, and the left pointer moves as needed.
- Each element is added and removed from the deques at most once.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The space complexity is O(n) in the worst case due to the deques storing indices of elements.
- However, the deques typically store only a small subset of indices, making the space usage efficient.
"""

# Topic: Sliding Window, Deque