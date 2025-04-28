"""
LeetCode Question #2025: Maximum Number of Ways to Partition an Array

Problem Statement:
You are given a 0-indexed integer array nums of length n. The array nums can be partitioned at index i (where 0 <= i < n) into two arrays:
    - nums_left which contains the first i + 1 elements of nums, and
    - nums_right which contains the remaining elements of nums.

The partition is called valid if:
    - The sum of nums_left is equal to the sum of nums_right.

You are also given an integer k. You can choose to change the value of one element of nums to k. Return the maximum number of valid partitions that can be obtained after changing at most one element of nums.

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^5 <= nums[i], k <= 10^5
"""

# Solution
def waysToPartition(nums, k):
    from collections import defaultdict

    n = len(nums)
    total_sum = sum(nums)
    prefix_sum = 0
    prefix_count = defaultdict(int)
    suffix_count = defaultdict(int)

    # Count prefix sums and suffix sums
    for i in range(n - 1):
        prefix_sum += nums[i]
        suffix_count[prefix_sum] += 1

    max_partitions = suffix_count[total_sum // 2] if total_sum % 2 == 0 else 0

    prefix_sum = 0
    for i in range(n):
        # Update prefix and suffix counts
        if i > 0:
            prefix_sum += nums[i - 1]
            suffix_count[prefix_sum] -= 1

        # Check partitions without changing any element
        if total_sum % 2 == 0:
            max_partitions = max(max_partitions, prefix_count[total_sum // 2] + suffix_count[total_sum // 2])

        # Check partitions after changing nums[i] to k
        new_total_sum = total_sum - nums[i] + k
        if new_total_sum % 2 == 0:
            target = new_total_sum // 2
            max_partitions = max(max_partitions, prefix_count[target] + suffix_count[target])

        # Update prefix count
        prefix_count[prefix_sum] += 1

    return max_partitions

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [2, -1, 2]
    k = 3
    print(waysToPartition(nums, k))  # Output: 1

    # Test Case 2
    nums = [0, 0, 0]
    k = 1
    print(waysToPartition(nums, k))  # Output: 2

    # Test Case 3
    nums = [1, 2, 3, 4]
    k = 5
    print(waysToPartition(nums, k))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the total sum of the array takes O(n).
- Iterating through the array to calculate prefix and suffix counts takes O(n).
- For each element, we check partitions without and with changing the element, which is O(1) per element.
- Overall, the time complexity is O(n).

Space Complexity:
- We use two hash maps (prefix_count and suffix_count) to store prefix and suffix sums, which can have at most O(n) unique keys.
- The space complexity is O(n).
"""

# Topic: Arrays, Prefix Sum, Hash Map