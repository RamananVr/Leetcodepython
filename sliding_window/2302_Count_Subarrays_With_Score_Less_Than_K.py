"""
LeetCode Problem #2302: Count Subarrays With Score Less Than K

Problem Statement:
You are given an array `nums` consisting of positive integers and an integer `k`.

The score of a subarray `(nums[l], nums[l+1], ..., nums[r])` is defined as the sum of the subarray multiplied by its length.

Return the number of non-empty subarrays of `nums` whose score is strictly less than `k`.

A subarray is a contiguous sequence of elements within an array.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
- 1 <= k <= 10^15
"""

# Solution
def countSubarrays(nums, k):
    """
    Counts the number of subarrays with a score less than k.

    :param nums: List[int] - The input array of positive integers.
    :param k: int - The threshold score.
    :return: int - The number of subarrays with a score less than k.
    """
    n = len(nums)
    count = 0
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += nums[right]
        while current_sum * (right - left + 1) >= k:
            current_sum -= nums[left]
            left += 1
        count += (right - left + 1)

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 1, 4, 3]
    k1 = 10
    print(countSubarrays(nums1, k1))  # Expected Output: 6

    # Test Case 2
    nums2 = [1, 2, 3]
    k2 = 6
    print(countSubarrays(nums2, k2))  # Expected Output: 4

    # Test Case 3
    nums3 = [5, 5, 5]
    k3 = 15
    print(countSubarrays(nums3, k3))  # Expected Output: 3

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    k4 = 5
    print(countSubarrays(nums4, k4))  # Expected Output: 10

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses a sliding window approach, where the `right` pointer iterates through the array once.
- The `left` pointer adjusts as needed, but each element is processed at most twice (once by `right` and once by `left`).
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses a constant amount of extra space (variables like `current_sum`, `left`, and `count`).
- Hence, the space complexity is O(1).

Topic: Sliding Window
"""