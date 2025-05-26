# 1. Problem Statement for LeetCode Question #2640:
# As of my knowledge cutoff in October 2023, I do not have access to the exact problem statement for LeetCode Question #2640.
# If you have the problem statement, please provide it, and I can assist you further.
# For now, I will proceed with a placeholder problem statement and solution based on a hypothetical problem.

# Hypothetical Problem Statement:
# Given an array of integers `nums`, return an array `result` such that `result[i]` is the sum of all elements in `nums` 
# except `nums[i]`. Solve this problem without using division and in O(n) time complexity.

# 2. Python Solution:
def sum_except_self(nums):
    """
    Given an array nums, return an array result such that result[i] is the sum of all elements in nums except nums[i].
    """
    n = len(nums)
    result = [0] * n

    # Compute prefix sums
    prefix_sum = [0] * n
    for i in range(n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i] if i > 0 else nums[i]

    # Compute suffix sums
    suffix_sum = [0] * n
    for i in range(n - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + nums[i] if i < n - 1 else nums[i]

    # Compute result array
    for i in range(n):
        left_sum = prefix_sum[i - 1] if i > 0 else 0
        right_sum = suffix_sum[i + 1] if i < n - 1 else 0
        result[i] = left_sum + right_sum

    return result

# 3. Example Test Cases:
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print(sum_except_self(nums1))  # Expected Output: [9, 8, 7, 6]

    # Test Case 2
    nums2 = [5, 1, 3]
    print(sum_except_self(nums2))  # Expected Output: [4, 8, 6]

    # Test Case 3
    nums3 = [0, 0, 0]
    print(sum_except_self(nums3))  # Expected Output: [0, 0, 0]

    # Test Case 4
    nums4 = [10]
    print(sum_except_self(nums4))  # Expected Output: [0]

# 4. Time and Space Complexity Analysis:
# Time Complexity:
# - Computing prefix sums takes O(n).
# - Computing suffix sums takes O(n).
# - Computing the result array takes O(n).
# Overall time complexity: O(n).

# Space Complexity:
# - The prefix_sum and suffix_sum arrays each take O(n) space.
# - The result array takes O(n) space.
# Overall space complexity: O(n).

# 5. Topic: Arrays