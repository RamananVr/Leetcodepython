"""
LeetCode Problem #698: Partition to K Equal Sum Subsets

Problem Statement:
You are given an integer array `nums` and an integer `k`. You want to divide the array into `k` non-empty subsets such that the sum of elements in each subset is equal.

Return `True` if it is possible to divide the array into `k` subsets with equal sum, otherwise return `False`.

Constraints:
- 1 <= k <= nums.length <= 16
- 0 <= nums[i] <= 10^4
- The sum of the elements in the array is guaranteed to be divisible by `k`.
"""

from typing import List

def canPartitionKSubsets(nums: List[int], k: int) -> bool:
    # Calculate the target sum for each subset
    total_sum = sum(nums)
    if total_sum % k != 0:
        return False
    target = total_sum // k

    # Sort the numbers in descending order to optimize backtracking
    nums.sort(reverse=True)

    # If the largest number is greater than the target, it's impossible to partition
    if nums[0] > target:
        return False

    # Initialize an array to track the sum of each subset
    subsets = [0] * k

    # Helper function for backtracking
    def backtrack(index: int) -> bool:
        if index == len(nums):
            # Check if all subsets have reached the target sum
            return all(s == target for s in subsets)

        for i in range(k):
            # Try to place nums[index] in subset i
            if subsets[i] + nums[index] <= target:
                subsets[i] += nums[index]
                if backtrack(index + 1):
                    return True
                subsets[i] -= nums[index]

            # If the current subset is empty, no need to try other empty subsets
            if subsets[i] == 0:
                break

        return False

    # Start backtracking from the first number
    return backtrack(0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 3, 2, 3, 5, 2, 1]
    k1 = 4
    print(canPartitionKSubsets(nums1, k1))  # Output: True

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    k2 = 3
    print(canPartitionKSubsets(nums2, k2))  # Output: False

    # Test Case 3
    nums3 = [2, 2, 2, 2, 3, 4, 5]
    k3 = 4
    print(canPartitionKSubsets(nums3, k3))  # Output: False

"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The backtracking function explores all possible ways to partition the array into k subsets.
  In the worst case, there are k^n states to explore, where n is the number of elements in the array.
  However, pruning significantly reduces the number of states explored.
- Overall, the time complexity is approximately O(k^n), but with pruning, it is much faster in practice.

Space Complexity:
- The space complexity is O(k + n), where:
  - O(k) is for the `subsets` array to track the sum of each subset.
  - O(n) is for the recursion stack in the backtracking function.

Topic: Backtracking
"""