"""
LeetCode Question #442: Find All Duplicates in an Array

Problem Statement:
Given an integer array `nums` of length `n` where all the integers of `nums` are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appear twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []

Constraints:
- n == nums.length
- 1 <= n <= 10^5
- 1 <= nums[i] <= n
"""

# Solution
def findDuplicates(nums):
    """
    Finds all the integers that appear twice in the array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    List[int]: A list of integers that appear twice.
    """
    duplicates = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            duplicates.append(abs(num))
        else:
            nums[index] = -nums[index]
    return duplicates

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDuplicates(nums1))  # Output: [2, 3]

    # Test Case 2
    nums2 = [1, 1, 2]
    print(findDuplicates(nums2))  # Output: [1]

    # Test Case 3
    nums3 = [1]
    print(findDuplicates(nums3))  # Output: []

    # Test Case 4
    nums4 = [2, 2, 3, 3, 4, 4, 5, 5]
    print(findDuplicates(nums4))  # Output: [2, 3, 4, 5]

# Time and Space Complexity Analysis
"""
Time Complexity:
The algorithm iterates through the array twice:
1. First iteration to mark visited indices.
2. Second iteration to collect duplicates.
Thus, the time complexity is O(n), where n is the length of the array.

Space Complexity:
The algorithm uses constant extra space (O(1)) because it modifies the input array in-place and does not use any additional data structures.
"""

# Topic: Arrays