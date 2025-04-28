"""
LeetCode Question #1918: Kth Smallest Subarray Sum

Problem Statement:
You are given an integer array nums and an integer k. A subarray is a contiguous part of an array. 
The sum of a subarray is the sum of all the elements in the subarray. Return the k-th smallest 
subarray sum.

Example:
Input: nums = [2, 1, 3], k = 4
Output: 3
Explanation: The sums of all subarrays are [2, 1, 3, 3, 4, 6]. The 4th smallest sum is 3.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
- 1 <= k <= nums.length * (nums.length + 1) // 2
"""

# Solution
def kthSmallestSubarraySum(nums, k):
    def countSubarraysWithSumLessThanOrEqual(target):
        count = 0
        current_sum = 0
        start = 0
        for end in range(len(nums)):
            current_sum += nums[end]
            while current_sum > target:
                current_sum -= nums[start]
                start += 1
            count += end - start + 1
        return count

    left, right = min(nums), sum(nums)
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if countSubarraysWithSumLessThanOrEqual(mid) >= k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [2, 1, 3]
    k = 4
    print(kthSmallestSubarraySum(nums, k))  # Output: 3

    # Test Case 2
    nums = [1, 2, 3, 4]
    k = 10
    print(kthSmallestSubarraySum(nums, k))  # Output: 6

    # Test Case 3
    nums = [5, 2, 1]
    k = 5
    print(kthSmallestSubarraySum(nums, k))  # Output: 7

    # Test Case 4
    nums = [1, 1, 1, 1]
    k = 6
    print(kthSmallestSubarraySum(nums, k))  # Output: 2

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The binary search runs in O(log(sum(nums))) iterations, where sum(nums) is the sum of all elements in the array.
   - For each iteration of binary search, we count the number of subarrays with sum <= mid using a sliding window approach, which takes O(n) time.
   - Therefore, the overall time complexity is O(n * log(sum(nums))).

2. Space Complexity:
   - The algorithm uses O(1) additional space, as it only uses a few variables for computation.

Topic: Binary Search, Sliding Window
"""