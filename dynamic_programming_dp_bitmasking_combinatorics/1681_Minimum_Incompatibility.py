"""
LeetCode Problem #1681: Minimum Incompatibility

Problem Statement:
You are given an integer array `nums` and an integer `k`. The array contains `n` elements, where `n` is divisible by `k`, that is, `n % k == 0`.

Divide the array into `k` subsets of equal size such that the incompatibility of the subsets is minimized.

The incompatibility of a subset is defined as the difference between the maximum and minimum elements in the subset.

Return the minimum possible sum of incompatibilities of the `k` subsets after dividing the array, or return -1 if it is not possible to divide the array as described.

Example 1:
Input: nums = [1,2,1,4], k = 2
Output: 4
Explanation: The optimal way to divide the array is [1,2] and [1,4]. The incompatibility is (2-1) + (4-1) = 4.

Example 2:
Input: nums = [6,3,8,1,3,1,2,2], k = 4
Output: 6
Explanation: The optimal way to divide the array is [1,2], [2,3], [1,3], and [6,8]. The incompatibility is (2-1) + (3-2) + (3-1) + (8-6) = 6.

Example 3:
Input: nums = [5,3,3,6,3,3], k = 3
Output: -1
Explanation: It is impossible to divide the array into 3 subsets of size 2 each.

Constraints:
- `n == nums.length`
- `1 <= k <= n <= 16`
- `n % k == 0`
- `1 <= nums[i] <= 16`

"""

from itertools import combinations
from functools import lru_cache

def minimumIncompatibility(nums, k):
    n = len(nums)
    subset_size = n // k

    # If there are duplicates that cannot fit into k subsets, return -1
    if any(nums.count(x) > k for x in nums):
        return -1

    # Precompute all valid subsets of size `subset_size` and their incompatibilities
    valid_subsets = {}
    for subset in combinations(nums, subset_size):
        if len(set(subset)) == subset_size:  # Ensure no duplicates in the subset
            valid_subsets[subset] = max(subset) - min(subset)

    # Use bitmask DP to find the minimum incompatibility
    @lru_cache(None)
    def dp(mask):
        if mask == 0:
            return 0

        min_incompatibility = float('inf')
        remaining_elements = [i for i in range(n) if mask & (1 << i)]

        # Try forming a subset from the remaining elements
        for subset in combinations(remaining_elements, subset_size):
            subset_mask = sum(1 << i for i in subset)
            subset_tuple = tuple(nums[i] for i in subset)

            if subset_tuple in valid_subsets:
                min_incompatibility = min(
                    min_incompatibility,
                    valid_subsets[subset_tuple] + dp(mask ^ subset_mask)
                )

        return min_incompatibility

    full_mask = (1 << n) - 1
    result = dp(full_mask)
    return result if result != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 1, 4]
    k1 = 2
    print(minimumIncompatibility(nums1, k1))  # Output: 4

    # Test Case 2
    nums2 = [6, 3, 8, 1, 3, 1, 2, 2]
    k2 = 4
    print(minimumIncompatibility(nums2, k2))  # Output: 6

    # Test Case 3
    nums3 = [5, 3, 3, 6, 3, 3]
    k3 = 3
    print(minimumIncompatibility(nums3, k3))  # Output: -1

# Time Complexity Analysis:
# - The number of subsets of size `subset_size` is O(C(n, subset_size)), where C(n, k) is the binomial coefficient.
# - The DP function iterates over all possible bitmasks (2^n) and subsets, leading to a time complexity of O(2^n * C(n, subset_size)).
# - Overall, the time complexity is exponential in the size of `nums`.

# Space Complexity Analysis:
# - The space complexity is O(2^n) for the DP cache and O(C(n, subset_size)) for storing valid subsets.
# - Overall, the space complexity is O(2^n + C(n, subset_size)).

# Topic: Dynamic Programming (DP), Bitmasking, Combinatorics