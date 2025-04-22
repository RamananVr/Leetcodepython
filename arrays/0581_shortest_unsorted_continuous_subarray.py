"""
LeetCode Question #581: Shortest Unsorted Continuous Subarray

Problem Statement:
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, 
then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6,4,8,10,9] in ascending order to make the whole array sorted in ascending order.

Example 2:
Input: nums = [1,2,3,4]
Output: 0
Explanation: The array is already sorted, so no subarray needs to be sorted.

Example 3:
Input: nums = [1]
Output: 0
Explanation: The array is already sorted, so no subarray needs to be sorted.

Constraints:
- 1 <= nums.length <= 10^4
- -10^5 <= nums[i] <= 10^5

Follow up: Can you solve it in O(n) time complexity?
"""

# Python Solution
def findUnsortedSubarray(nums):
    """
    Finds the length of the shortest unsorted continuous subarray.
    
    :param nums: List[int] - The input array
    :return: int - Length of the shortest unsorted subarray
    """
    n = len(nums)
    left, right = 0, n - 1

    # Find the first element out of order from the left
    while left < n - 1 and nums[left] <= nums[left + 1]:
        left += 1

    # If the array is already sorted
    if left == n - 1:
        return 0

    # Find the first element out of order from the right
    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1

    # Find the min and max in the unsorted subarray
    subarray_min = min(nums[left:right + 1])
    subarray_max = max(nums[left:right + 1])

    # Expand the left boundary
    while left > 0 and nums[left - 1] > subarray_min:
        left -= 1

    # Expand the right boundary
    while right < n - 1 and nums[right + 1] < subarray_max:
        right += 1

    return right - left + 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 6, 4, 8, 10, 9, 15]
    print(findUnsortedSubarray(nums1))  # Output: 5

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print(findUnsortedSubarray(nums2))  # Output: 0

    # Test Case 3
    nums3 = [1]
    print(findUnsortedSubarray(nums3))  # Output: 0

    # Test Case 4
    nums4 = [1, 3, 2, 2, 2]
    print(findUnsortedSubarray(nums4))  # Output: 4

    # Test Case 5
    nums5 = [2, 1]
    print(findUnsortedSubarray(nums5))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm involves a single pass to find the left and right boundaries of the unsorted subarray (O(n)).
- It then calculates the minimum and maximum values in the unsorted subarray (O(n)).
- Finally, it adjusts the boundaries by expanding them (O(n)).
- Overall, the time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables (O(1)).
- No additional data structures are used.
- Overall, the space complexity is O(1).

Topic: Arrays
"""