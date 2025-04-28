"""
LeetCode Problem #1248: Count Number of Nice Subarrays

Problem Statement:
Given an array of integers `nums` and an integer `k`. A subarray is called nice if there are exactly `k` odd numbers in it.

Return the number of nice subarrays.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only subarrays with exactly 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no subarray with exactly 1 odd number.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

Constraints:
- 1 <= nums.length <= 50000
- 1 <= nums[i] <= 10^5
- 1 <= k <= nums.length
"""

# Python Solution
def numberOfSubarrays(nums, k):
    """
    Count the number of nice subarrays with exactly k odd numbers.

    :param nums: List[int] - The input array of integers.
    :param k: int - The number of odd numbers required in a subarray.
    :return: int - The count of nice subarrays.
    """
    def atMostK(k):
        count = 0
        left = 0
        odd_count = 0

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1

            while odd_count > k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1

            count += right - left + 1

        return count

    return atMostK(k) - atMostK(k - 1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 2, 1, 1]
    k1 = 3
    print(numberOfSubarrays(nums1, k1))  # Output: 2

    # Test Case 2
    nums2 = [2, 4, 6]
    k2 = 1
    print(numberOfSubarrays(nums2, k2))  # Output: 0

    # Test Case 3
    nums3 = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    k3 = 2
    print(numberOfSubarrays(nums3, k3))  # Output: 16

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    k4 = 1
    print(numberOfSubarrays(nums4, k4))  # Output: 5

    # Test Case 5
    nums5 = [1, 1, 1, 1, 1]
    k5 = 2
    print(numberOfSubarrays(nums5, k5))  # Output: 6

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function `atMostK` iterates through the array once, with a sliding window approach.
- Each element is processed at most twice (once when expanding the window and once when contracting it).
- Therefore, the time complexity is O(n), where n is the length of the array.
- Since we call `atMostK` twice, the overall time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Arrays, Sliding Window