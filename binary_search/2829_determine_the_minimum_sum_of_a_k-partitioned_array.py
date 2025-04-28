"""
LeetCode Question #2829: Determine the Minimum Sum of a k-Partitioned Array

Problem Statement:
You are given an integer array `nums` and an integer `k`. Partition the array into `k` non-empty subsets such that the sum of the elements in each subset is minimized. Return the minimum possible sum of the largest subset.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^6
- 1 <= k <= nums.length
"""

# Solution
from typing import List

def minimizeLargestSum(nums: List[int], k: int) -> int:
    def canPartition(maxSum):
        # Helper function to check if we can partition the array into k subsets
        # such that the sum of each subset is <= maxSum.
        currentSum = 0
        partitions = 1
        for num in nums:
            if currentSum + num > maxSum:
                partitions += 1
                currentSum = num
                if partitions > k:
                    return False
            else:
                currentSum += num
        return True

    # Sort the array to optimize the binary search
    nums.sort(reverse=True)
    
    # Binary search for the minimum possible largest sum
    left, right = max(nums), sum(nums)
    result = right
    while left <= right:
        mid = (left + right) // 2
        if canPartition(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [7, 2, 5, 10, 8]
    k1 = 2
    print(minimizeLargestSum(nums1, k1))  # Output: 18

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    k2 = 2
    print(minimizeLargestSum(nums2, k2))  # Output: 9

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k3 = 3
    print(minimizeLargestSum(nums3, k3))  # Output: 17

    # Test Case 4
    nums4 = [10, 20, 30, 40, 50]
    k4 = 5
    print(minimizeLargestSum(nums4, k4))  # Output: 50

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The binary search runs for O(log(sum(nums) - max(nums))) iterations.
- For each iteration of binary search, we traverse the array to check if the partition is valid, which takes O(n).
- Overall time complexity: O(n log n + n log(sum(nums) - max(nums))).

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures.

Topic: Binary Search
"""