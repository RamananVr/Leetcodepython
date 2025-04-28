"""
LeetCode Problem #1856: Maximum Subarray Min-Product

Problem Statement:
The min-product of an array is defined as the minimum value in the array multiplied by the array's sum.

- For example, the array [3,2,5] has a minimum value of 2 and a sum of 3 + 2 + 5 = 10. The min-product is 2 * 10 = 20.

Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 10^9 + 7.

Note that the min-product should be maximized before performing the modulo operation. Test cases are generated such that the answer fits in a 32-bit integer.

A subarray is a contiguous part of an array.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^7
"""

# Python Solution
def maxSumMinProduct(nums):
    """
    Function to calculate the maximum min-product of any subarray in nums.
    """
    MOD = 10**9 + 7
    n = len(nums)

    # Step 1: Compute prefix sums
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    # Step 2: Find the previous smaller and next smaller elements for each index
    prev_smaller = [-1] * n
    next_smaller = [n] * n

    # Monotonic stack for previous smaller
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            prev_smaller[i] = stack[-1]
        stack.append(i)

    # Monotonic stack for next smaller
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            next_smaller[i] = stack[-1]
        stack.append(i)

    # Step 3: Calculate the maximum min-product
    max_min_product = 0
    for i in range(n):
        left = prev_smaller[i] + 1
        right = next_smaller[i] - 1
        subarray_sum = prefix_sum[right + 1] - prefix_sum[left]
        min_product = nums[i] * subarray_sum
        max_min_product = max(max_min_product, min_product)

    return max_min_product % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 2]
    print(maxSumMinProduct(nums1))  # Expected Output: 14

    # Test Case 2
    nums2 = [2, 3, 3, 1, 2]
    print(maxSumMinProduct(nums2))  # Expected Output: 18

    # Test Case 3
    nums3 = [3, 1, 5, 6, 4, 2]
    print(maxSumMinProduct(nums3))  # Expected Output: 60

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating prefix sums takes O(n).
- Finding previous smaller and next smaller elements using monotonic stacks takes O(n).
- Calculating the maximum min-product involves iterating through the array once, which is O(n).
Overall, the time complexity is O(n).

Space Complexity:
- The prefix_sum array takes O(n) space.
- The prev_smaller and next_smaller arrays take O(n) space.
- The stack used for monotonic stack operations takes O(n) space in the worst case.
Overall, the space complexity is O(n).
"""

# Topic: Arrays, Monotonic Stack