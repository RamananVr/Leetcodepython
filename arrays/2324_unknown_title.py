"""
LeetCode Problem #2324: Product of Array Except Self

Problem Statement:
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

Follow-up:
Can you solve the problem in O(1) extra space complexity (excluding the output array)?
"""

# Python Solution
def productExceptSelf(nums):
    """
    This function calculates the product of all elements in the array except the current element
    for each index, without using division and in O(n) time complexity.

    :param nums: List[int] - Input array of integers
    :return: List[int] - Output array where each element is the product of all other elements
    """
    n = len(nums)
    answer = [1] * n

    # Calculate prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Calculate suffix products and multiply with prefix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print("Input:", nums1)
    print("Output:", productExceptSelf(nums1))  # Expected: [24, 12, 8, 6]

    # Test Case 2
    nums2 = [-1, 1, 0, -3, 3]
    print("Input:", nums2)
    print("Output:", productExceptSelf(nums2))  # Expected: [0, 0, 9, 0, 0]

    # Test Case 3
    nums3 = [2, 3, 4, 5]
    print("Input:", nums3)
    print("Output:", productExceptSelf(nums3))  # Expected: [60, 40, 30, 24]

    # Test Case 4
    nums4 = [10, 3, 5, 6, 2]
    print("Input:", nums4)
    print("Output:", productExceptSelf(nums4))  # Expected: [180, 600, 360, 300, 900]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array twice (once for prefix and once for suffix), making it O(n).

Space Complexity:
- The algorithm uses O(1) extra space for the prefix and suffix variables.
- The output array `answer` is not considered extra space as it is part of the required output.
- Therefore, the space complexity is O(1).
"""

# Topic: Arrays