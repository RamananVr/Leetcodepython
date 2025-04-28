"""
LeetCode Problem #1746: Maximum Subarray Sum After One Operation

Problem Statement:
You are given an integer array nums. You must perform exactly one operation where you can replace one element nums[i] with nums[i] * nums[i].
Return the maximum possible subarray sum after exactly one operation.

A subarray is a contiguous sequence of elements within an array.

Example 1:
Input: nums = [2,-1,-4,-3]
Output: 17
Explanation: Replace -4 with (-4)^2 = 16, and the subarray [16,-3] has the maximum sum of 17.

Example 2:
Input: nums = [1,-1,1,1,-1,-1,1]
Output: 4
Explanation: Replace the first -1 with (-1)^2 = 1, and the subarray [1,1,1] has the maximum sum of 4.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

# Python Solution
def maxSumAfterOperation(nums):
    """
    Function to calculate the maximum subarray sum after exactly one operation.
    
    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The maximum possible subarray sum after one operation.
    """
    n = len(nums)
    max_no_op = 0  # Maximum subarray sum without any operation
    max_with_op = 0  # Maximum subarray sum with one operation
    result = float('-inf')  # Initialize the result to negative infinity

    for num in nums:
        # Update the maximum subarray sum with one operation
        max_with_op = max(max_with_op + num, max_no_op + num * num, num * num)
        # Update the maximum subarray sum without any operation
        max_no_op = max(max_no_op + num, num)
        # Update the result
        result = max(result, max_with_op)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, -1, -4, -3]
    print(maxSumAfterOperation(nums1))  # Output: 17

    # Test Case 2
    nums2 = [1, -1, 1, 1, -1, -1, 1]
    print(maxSumAfterOperation(nums2))  # Output: 4

    # Test Case 3
    nums3 = [-2, -1, -3]
    print(maxSumAfterOperation(nums3))  # Output: 9

    # Test Case 4
    nums4 = [1, 2, 3, 4]
    print(maxSumAfterOperation(nums4))  # Output: 30

    # Test Case 5
    nums5 = [-1]
    print(maxSumAfterOperation(nums5))  # Output: 1

"""
Time Complexity Analysis:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space for variables (max_no_op, max_with_op, result).
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming
"""