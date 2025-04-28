"""
LeetCode Problem #1590: Make Sum Divisible by P

Problem Statement:
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the entire array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

Example 1:
Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the array is 10, and 10 % 6 = 4. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

Example 2:
Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: The sum of the array is 16, and 16 % 9 = 7. We can remove the subarray [5,2], and the sum of the remaining elements is 9, which is divisible by 9.

Example 3:
Input: nums = [1,2,3], p = 3
Output: 0
Explanation: The sum of the array is 6, which is already divisible by 3. Thus, we do not need to remove any subarray.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= p <= 10^9
"""

# Python Solution
def minSubarray(nums, p):
    total_sum = sum(nums)
    remainder = total_sum % p
    if remainder == 0:
        return 0  # No need to remove any subarray

    prefix_sum = 0
    min_length = len(nums)
    prefix_map = {0: -1}  # Maps prefix_sum % p to its index

    for i, num in enumerate(nums):
        prefix_sum += num
        prefix_mod = prefix_sum % p
        target_mod = (prefix_mod - remainder) % p

        if target_mod in prefix_map:
            min_length = min(min_length, i - prefix_map[target_mod])

        prefix_map[prefix_mod] = i

    return min_length if min_length < len(nums) else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 1, 4, 2]
    p1 = 6
    print(minSubarray(nums1, p1))  # Output: 1

    # Test Case 2
    nums2 = [6, 3, 5, 2]
    p2 = 9
    print(minSubarray(nums2, p2))  # Output: 2

    # Test Case 3
    nums3 = [1, 2, 3]
    p3 = 3
    print(minSubarray(nums3, p3))  # Output: 0

    # Test Case 4
    nums4 = [1, 2, 3]
    p4 = 7
    print(minSubarray(nums4, p4))  # Output: -1

    # Test Case 5
    nums5 = [1000000000, 1000000000, 1000000000]
    p5 = 3
    print(minSubarray(nums5, p5))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once, making it O(n), where n is the length of nums.
- Hash map operations (insert and lookup) are O(1) on average.

Space Complexity:
- The space complexity is O(n) due to the hash map storing prefix sums modulo p.

Overall:
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Topic: Arrays, Prefix Sum, Hash Map