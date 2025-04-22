"""
LeetCode Question #152: Maximum Product Subarray

Problem Statement:
Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated such that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

# Clean and Correct Python Solution
def maxProduct(nums):
    """
    Finds the maximum product of a contiguous subarray.

    :param nums: List[int] - The input array of integers.
    :return: int - The maximum product of a contiguous subarray.
    """
    if not nums:
        return 0

    # Initialize variables to track the maximum and minimum product up to the current index
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]

        # If the current number is negative, swap max_product and min_product
        if num < 0:
            max_product, min_product = min_product, max_product

        # Update max_product and min_product
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)

        # Update the result with the maximum product found so far
        result = max(result, max_product)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, -2, 4]
    print(f"Test Case 1: {maxProduct(nums1)}")  # Expected Output: 6

    # Test Case 2
    nums2 = [-2, 0, -1]
    print(f"Test Case 2: {maxProduct(nums2)}")  # Expected Output: 0

    # Test Case 3
    nums3 = [0, 2]
    print(f"Test Case 3: {maxProduct(nums3)}")  # Expected Output: 2

    # Test Case 4
    nums4 = [-2, 3, -4]
    print(f"Test Case 4: {maxProduct(nums4)}")  # Expected Output: 24

    # Test Case 5
    nums5 = [2, -5, -2, -4, 3]
    print(f"Test Case 5: {maxProduct(nums5)}")  # Expected Output: 240

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses a constant amount of extra space to store variables (max_product, min_product, result).
- Therefore, the space complexity is O(1).
"""

# Topic: Dynamic Programming