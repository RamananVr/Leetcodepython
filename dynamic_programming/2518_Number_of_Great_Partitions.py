"""
LeetCode Problem #2518: Number of Great Partitions

Problem Statement:
You are given an array `nums` consisting of positive integers and an integer `k`.

A partition of the array `nums` is called great if the sum of elements in each of the two partitions is greater than or equal to `k`.

Return the number of distinct great partitions. Since the answer may be too large, return it modulo `10^9 + 7`.

A partition of `nums` is defined as two non-empty subsets `s1` and `s2` such that every element in `nums` is in either `s1` or `s2`. Elements can only belong to one subset, and each element must belong to exactly one subset.

Constraints:
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`
"""

# Solution
from functools import lru_cache

def countPartitions(nums, k):
    MOD = 10**9 + 7
    total_sum = sum(nums)
    
    # If the total sum of the array is less than 2 * k, it's impossible to create a great partition
    if total_sum < 2 * k:
        return 0

    # Helper function to count subsets with sum less than k
    @lru_cache(None)
    def count_subsets(index, current_sum):
        if current_sum >= k:
            return 0
        if index == len(nums):
            return 1
        # Include the current number or exclude it
        include = count_subsets(index + 1, current_sum + nums[index])
        exclude = count_subsets(index + 1, current_sum)
        return (include + exclude) % MOD

    # Count subsets with sum less than k
    subsets_with_sum_less_than_k = count_subsets(0, 0)
    
    # Total subsets = 2^n
    total_subsets = pow(2, len(nums), MOD)
    
    # Subtract invalid partitions (those where one subset has sum < k)
    invalid_partitions = (2 * subsets_with_sum_less_than_k) % MOD
    result = (total_subsets - invalid_partitions + MOD) % MOD
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    k1 = 4
    print(countPartitions(nums1, k1))  # Expected Output: 6

    # Test Case 2
    nums2 = [3, 3, 3]
    k2 = 4
    print(countPartitions(nums2, k2))  # Expected Output: 0

    # Test Case 3
    nums3 = [6, 6, 6]
    k3 = 6
    print(countPartitions(nums3, k3))  # Expected Output: 7

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    k4 = 2
    print(countPartitions(nums4, k4))  # Expected Output: 14

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `count_subsets` function uses memoization to avoid redundant calculations. It has a time complexity of O(n * k), where `n` is the length of the array and `k` is the target sum.
- Calculating `total_subsets` is O(1) since it uses modular exponentiation.
- Overall time complexity: O(n * k).

Space Complexity:
- The space complexity is O(n * k) due to the memoization table used in the `count_subsets` function.
- Additional space is used for the recursion stack, which is O(n) in the worst case.
- Overall space complexity: O(n * k).

Topic: Dynamic Programming
"""