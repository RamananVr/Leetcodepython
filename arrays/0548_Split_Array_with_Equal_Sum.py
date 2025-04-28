"""
LeetCode Problem #548: Split Array with Equal Sum

Problem Statement:
Given an integer array `nums`, split it into four non-empty contiguous subarrays 
`nums1`, `nums2`, `nums3`, and `nums4` such that the sum of the elements in 
`nums1`, `nums2`, and `nums3` are all equal. If such a split is possible, return `True`. 
Otherwise, return `False`.

Formally, find indices `i`, `j`, and `k` such that:
- `sum(nums[0:i]) == sum(nums[i+1:j]) == sum(nums[j+1:k])`
- `i < j < k`
- All subarrays are non-empty.

Constraints:
- 1 <= nums.length <= 2000
- -10^6 <= nums[i] <= 10^6
"""

def splitArray(nums):
    """
    Determines if the array can be split into four non-empty contiguous subarrays
    with equal sums.

    :param nums: List[int] - The input array
    :return: bool - True if the split is possible, False otherwise
    """
    n = len(nums)
    if n < 7:  # Minimum length required for four non-empty subarrays
        return False

    # Compute prefix sums
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    # Iterate over possible middle indices j
    for j in range(3, n - 3):
        seen_sums = set()
        # Check for valid i (left split)
        for i in range(1, j - 1):
            if prefix_sum[i - 1] == prefix_sum[j - 1] - prefix_sum[i]:
                seen_sums.add(prefix_sum[i - 1])
        # Check for valid k (right split)
        for k in range(j + 2, n - 1):
            if prefix_sum[k - 1] - prefix_sum[j] == prefix_sum[-1] - prefix_sum[k] and \
               prefix_sum[k - 1] - prefix_sum[j] in seen_sums:
                return True

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Split is possible
    nums1 = [1, 2, 1, 2, 1, 2, 1]
    print(splitArray(nums1))  # Expected output: True

    # Test Case 2: Split is not possible
    nums2 = [1, 2, 3, 4, 5, 6, 7]
    print(splitArray(nums2))  # Expected output: False

    # Test Case 3: Edge case with minimum length
    nums3 = [1, 1, 1, 1, 1, 1, 1]
    print(splitArray(nums3))  # Expected output: True

    # Test Case 4: Large numbers
    nums4 = [1000000, -1000000, 1000000, -1000000, 1000000, -1000000, 1000000]
    print(splitArray(nums4))  # Expected output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- Computing prefix sums takes O(n).
- The outer loop iterates over possible `j` values, which is O(n).
- For each `j`, the inner loops iterate over possible `i` and `k` values, which is O(n) each.
- Thus, the overall time complexity is O(n^2).

Space Complexity:
- The prefix_sum array requires O(n) space.
- The seen_sums set requires O(n) space in the worst case.
- Thus, the overall space complexity is O(n).

Topic: Arrays
"""