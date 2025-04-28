"""
LeetCode Problem #238: Product of Array Except Self

Problem Statement:
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Follow-up:
Can you solve the problem in O(n) time complexity and without using division?
"""

# Solution
def productExceptSelf(nums):
    """
    Computes the product of all elements except the current index for each index in the array.

    Args:
    nums (List[int]): Input array of integers.

    Returns:
    List[int]: Array where each element is the product of all elements except itself.
    """
    n = len(nums)
    answer = [1] * n

    # Compute prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Compute suffix products and combine with prefix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print(productExceptSelf(nums1))  # Output: [24, 12, 8, 6]

    # Test Case 2
    nums2 = [-1, 1, 0, -3, 3]
    print(productExceptSelf(nums2))  # Output: [0, 0, 9, 0, 0]

    # Test Case 3
    nums3 = [5, 6, 7]
    print(productExceptSelf(nums3))  # Output: [42, 35, 30]

    # Test Case 4
    nums4 = [2, 3]
    print(productExceptSelf(nums4))  # Output: [3, 2]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array twice (once for prefix products and once for suffix products).
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses a single array `answer` of size n to store the results.
- No additional space is used apart from a few variables (prefix and suffix).
- Therefore, the space complexity is O(1) (excluding the output array).
"""

# Topic: Arrays