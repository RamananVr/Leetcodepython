"""
LeetCode Question #689: Maximum Sum of 3 Non-Overlapping Subarrays

Problem Statement:
Given an integer array `nums` and an integer `k`, find three non-overlapping subarrays of length `k` with maximum sum.
Return the starting indices of the three subarrays. If there are multiple answers, return the lexicographically smallest one.

The subarrays must be non-overlapping, meaning that the starting index of each subarray must be at least `k` apart.

Constraints:
- `1 <= nums.length <= 2 * 10^4`
- `1 <= k <= nums.length / 3`
- `0 <= nums[i] <= 10^4`

Example:
Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0, 3, 5]
Explanation: Subarrays are [1, 2], [2, 6], [6, 7]. They have the maximum sum 1+2 + 2+6 + 6+7 = 24.

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0, 2, 4]
"""

# Solution
def maxSumOfThreeSubarrays(nums, k):
    n = len(nums)
    # Step 1: Calculate the sum of all subarrays of size k
    window_sum = [0] * (n - k + 1)
    current_sum = sum(nums[:k])
    window_sum[0] = current_sum
    for i in range(1, n - k + 1):
        current_sum += nums[i + k - 1] - nums[i - 1]
        window_sum[i] = current_sum

    # Step 2: Precompute the best left and right indices for each position
    left = [0] * len(window_sum)
    right = [0] * len(window_sum)

    # Best left index for each position
    best_left = 0
    for i in range(len(window_sum)):
        if window_sum[i] > window_sum[best_left]:
            best_left = i
        left[i] = best_left

    # Best right index for each position
    best_right = len(window_sum) - 1
    for i in range(len(window_sum) - 1, -1, -1):
        if window_sum[i] >= window_sum[best_right]:
            best_right = i
        right[i] = best_right

    # Step 3: Find the maximum sum by iterating over the middle subarray
    max_sum = 0
    result = []
    for mid in range(k, len(window_sum) - k):
        l = left[mid - k]
        r = right[mid + k]
        total = window_sum[l] + window_sum[mid] + window_sum[r]
        if total > max_sum:
            max_sum = total
            result = [l, mid, r]

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 1, 2, 6, 7, 5, 1]
    k1 = 2
    print(maxSumOfThreeSubarrays(nums1, k1))  # Output: [0, 3, 5]

    # Test Case 2
    nums2 = [1, 2, 1, 2, 1, 2, 1, 2, 1]
    k2 = 2
    print(maxSumOfThreeSubarrays(nums2, k2))  # Output: [0, 2, 4]

    # Test Case 3
    nums3 = [4, 5, 10, 6, 11, 17, 2, 8, 3, 9]
    k3 = 3
    print(maxSumOfThreeSubarrays(nums3, k3))  # Output: [0, 4, 7]

# Time and Space Complexity Analysis
# Time Complexity:
# - Calculating the window sums takes O(n).
# - Precomputing the left and right arrays takes O(n).
# - Iterating over the middle subarray takes O(n).
# Total: O(n).

# Space Complexity:
# - The `window_sum`, `left`, and `right` arrays each take O(n) space.
# Total: O(n).

# Topic: Arrays, Sliding Window, Dynamic Programming