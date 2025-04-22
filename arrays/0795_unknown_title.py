"""
LeetCode Problem #795: Number of Subarrays with Bounded Maximum

Problem Statement:
Given an integer array `nums` and two integers `left` and `right`, return the number of contiguous subarrays 
where the value of the maximum array element is in the range `[left, right]`.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [2, 1, 4, 3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

Example 2:
Input: nums = [2, 9, 2, 5, 6], left = 2, right = 8
Output: 7

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 0 <= left <= right <= 10^9
"""

def numSubarrayBoundedMax(nums, left, right):
    """
    Function to count the number of subarrays with bounded maximum.

    Args:
    nums (List[int]): The input array of integers.
    left (int): The lower bound of the range.
    right (int): The upper bound of the range.

    Returns:
    int: The number of subarrays where the maximum element is in the range [left, right].
    """
    def countSubarrays(bound):
        count = 0
        current = 0
        for num in nums:
            if num <= bound:
                current += 1
                count += current
            else:
                current = 0
        return count

    return countSubarrays(right) - countSubarrays(left - 1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 1, 4, 3]
    left1 = 2
    right1 = 3
    print(numSubarrayBoundedMax(nums1, left1, right1))  # Output: 3

    # Test Case 2
    nums2 = [2, 9, 2, 5, 6]
    left2 = 2
    right2 = 8
    print(numSubarrayBoundedMax(nums2, left2, right2))  # Output: 7

    # Test Case 3
    nums3 = [1, 4, 2, 3]
    left3 = 2
    right3 = 4
    print(numSubarrayBoundedMax(nums3, left3, right3))  # Output: 8

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    left4 = 1
    right4 = 1
    print(numSubarrayBoundedMax(nums4, left4, right4))  # Output: 10

"""
Time Complexity:
- The function `countSubarrays` iterates through the array once, making it O(n) for each call.
- Since we call `countSubarrays` twice, the overall time complexity is O(n).

Space Complexity:
- The algorithm uses O(1) additional space as it only uses a few variables for computation.

Topic: Arrays
"""