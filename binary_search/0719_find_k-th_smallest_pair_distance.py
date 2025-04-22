"""
LeetCode Question #719: Find K-th Smallest Pair Distance

Problem Statement:
The distance of a pair (A, B) is defined as the absolute difference between A and B.
Given an integer array `nums` and an integer `k`, return the k-th smallest distance among all the pairs (nums[i], nums[j]) where 0 <= i < j < nums.length.

Example 1:
Input: nums = [1, 3, 1], k = 1
Output: 0
Explanation: The pairs are (1, 3), (1, 1), and (3, 1). The distances are 2, 0, and 2. The 1st smallest distance is 0.

Example 2:
Input: nums = [1, 1, 1], k = 2
Output: 0

Example 3:
Input: nums = [1, 6, 1], k = 3
Output: 5

Constraints:
- 2 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^6
- 1 <= k <= nums.length * (nums.length - 1) // 2
"""

# Solution
from typing import List

def smallestDistancePair(nums: List[int], k: int) -> int:
    def count_pairs_with_distance_less_than_or_equal_to(mid: int) -> int:
        count = 0
        j = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] - nums[i] <= mid:
                j += 1
            count += j - i - 1
        return count

    nums.sort()
    left, right = 0, nums[-1] - nums[0]

    while left < right:
        mid = (left + right) // 2
        if count_pairs_with_distance_less_than_or_equal_to(mid) < k:
            left = mid + 1
        else:
            right = mid

    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 1]
    k1 = 1
    print(smallestDistancePair(nums1, k1))  # Output: 0

    # Test Case 2
    nums2 = [1, 1, 1]
    k2 = 2
    print(smallestDistancePair(nums2, k2))  # Output: 0

    # Test Case 3
    nums3 = [1, 6, 1]
    k3 = 3
    print(smallestDistancePair(nums3, k3))  # Output: 5

    # Additional Test Case
    nums4 = [1, 2, 3, 4]
    k4 = 3
    print(smallestDistancePair(nums4, k4))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of `nums`.
- The binary search runs for O(log(max_distance)), where max_distance is the difference between the largest and smallest elements in `nums`.
- For each binary search iteration, we count pairs with a distance less than or equal to `mid`, which takes O(n) using the two-pointer technique.
- Overall, the time complexity is O(n log n + n log(max_distance)).

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures apart from variables.

Topic: Binary Search
"""