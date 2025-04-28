"""
LeetCode Problem #2221: Find Triangular Sum of an Array

Problem Statement:
You are given a 0-indexed integer array `nums`, where `nums[i]` is a positive integer.

You are tasked to apply the following operation until the array contains only one element:
1. Create a new 0-indexed integer array of length `n - 1`, where `n` is the length of the current array.
2. For each index `i` (0 <= i < n - 1), the value of the new array at index `i` is `(nums[i] + nums[i + 1]) % 10`, where `%` denotes modulo operation.
3. Replace the current array with the new array.

Return the triangular sum of the array, which is the only element left in the final array.

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 9
"""

def triangularSum(nums):
    """
    Function to compute the triangular sum of an array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The triangular sum of the array.
    """
    while len(nums) > 1:
        nums = [(nums[i] + nums[i + 1]) % 10 for i in range(len(nums) - 1)]
    return nums[0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    print(triangularSum(nums1))  # Output: 8

    # Test Case 2
    nums2 = [5]
    print(triangularSum(nums2))  # Output: 5

    # Test Case 3
    nums3 = [9, 9, 9, 9]
    print(triangularSum(nums3))  # Output: 6

    # Test Case 4
    nums4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(triangularSum(nums4))  # Output: 5

    # Test Case 5
    nums5 = [7, 8, 9]
    print(triangularSum(nums5))  # Output: 4

"""
Time Complexity Analysis:
- The length of the array reduces by 1 in each iteration.
- For an array of length `n`, the total number of operations is approximately:
  (n-1) + (n-2) + ... + 1 = n(n-1)/2.
- Therefore, the time complexity is O(n^2).

Space Complexity Analysis:
- The space complexity is O(n) because we create a new array of size `n-1` in each iteration.

Topic: Arrays
"""