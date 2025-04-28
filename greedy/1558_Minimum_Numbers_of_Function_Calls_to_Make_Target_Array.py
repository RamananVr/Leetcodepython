"""
LeetCode Problem #1558: Minimum Numbers of Function Calls to Make Target Array

Problem Statement:
You are given an integer array `nums`. You can perform the following operations on the array any number of times:

1. Increment: Choose any element of the array and increment it by 1.
2. Double: Double all the elements of the array.

Your goal is to make the array equal to `nums` using the minimum number of operations. Return the minimum number of operations needed.

Example:
Input: nums = [1, 5]
Output: 5
Explanation: Increment 0 to 1, increment 0 to 5, double the array once.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
"""

# Solution
def minOperations(nums):
    """
    Calculate the minimum number of operations to make the target array `nums`.

    :param nums: List[int] - The target array
    :return: int - Minimum number of operations
    """
    max_double_operations = 0
    increment_operations = 0

    for num in nums:
        current_double_operations = 0
        while num > 0:
            if num % 2 == 1:
                increment_operations += 1
                num -= 1
            else:
                current_double_operations += 1
                num //= 2
        max_double_operations = max(max_double_operations, current_double_operations)

    return increment_operations + max_double_operations


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 5]
    print(minOperations(nums1))  # Output: 5

    # Test Case 2
    nums2 = [2, 2]
    print(minOperations(nums2))  # Output: 3

    # Test Case 3
    nums3 = [3, 2, 2]
    print(minOperations(nums3))  # Output: 5

    # Test Case 4
    nums4 = [0]
    print(minOperations(nums4))  # Output: 0

    # Test Case 5
    nums5 = [8, 4, 2]
    print(minOperations(nums5))  # Output: 6


"""
Time and Space Complexity Analysis:

Time Complexity:
- For each number in the array, we repeatedly divide it by 2 until it becomes 0. 
  This takes O(log(nums[i])) time for each number `nums[i]`.
- Summing up for all numbers in the array, the total time complexity is O(n * log(max(nums))),
  where `n` is the length of the array and `max(nums)` is the largest number in the array.

Space Complexity:
- The algorithm uses O(1) additional space, as it only uses a few variables to track operations.

Topic: Greedy
"""