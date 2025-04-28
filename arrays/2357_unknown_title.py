"""
LeetCode Problem #2357: Make Array Zero by Subtracting Equal Amounts

Problem Statement:
You are given a non-negative integer array nums. In one operation, you must:
- Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
- Subtract x from every positive element in nums.

Return the minimum number of operations required to make every element in nums equal to 0.

Example 1:
Input: nums = [3, 3, 2, 2, 4]
Output: 3
Explanation:
- In the first operation, choose x = 2. After subtracting, nums = [1, 1, 0, 0, 2].
- In the second operation, choose x = 1. After subtracting, nums = [0, 0, 0, 0, 1].
- In the third operation, choose x = 1. After subtracting, nums = [0, 0, 0, 0, 0].

Example 2:
Input: nums = [0]
Output: 0
Explanation: All elements are already 0, so no operations are needed.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100
"""

# Python Solution
def minimumOperations(nums):
    """
    Returns the minimum number of operations required to make all elements in nums equal to 0.

    :param nums: List[int] - A list of non-negative integers.
    :return: int - Minimum number of operations.
    """
    # Use a set to find unique non-zero elements
    return len(set(nums) - {0})

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 3, 2, 2, 4]
    print(minimumOperations(nums1))  # Output: 3

    # Test Case 2
    nums2 = [0]
    print(minimumOperations(nums2))  # Output: 0

    # Test Case 3
    nums3 = [1, 5, 0, 3, 5]
    print(minimumOperations(nums3))  # Output: 3

    # Test Case 4
    nums4 = [0, 0, 0, 0]
    print(minimumOperations(nums4))  # Output: 0

    # Test Case 5
    nums5 = [7, 7, 7, 7]
    print(minimumOperations(nums5))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses a set to find unique non-zero elements in the array.
- Constructing a set from the array takes O(n), where n is the length of nums.
- Therefore, the time complexity is O(n).

Space Complexity:
- The solution uses a set to store unique non-zero elements.
- In the worst case, the set will contain all elements of nums (if all are non-zero).
- Therefore, the space complexity is O(n).

Topic: Arrays
"""