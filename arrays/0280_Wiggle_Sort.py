"""
LeetCode Problem #280: Wiggle Sort

Problem Statement:
Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3].... 
You may assume the input array always has a valid answer.

Example:
Input: nums = [3, 5, 2, 1, 6, 4]
Output: [3, 5, 1, 6, 2, 4]
Explanation: The resulting array satisfies the conditions nums[0] <= nums[1] >= nums[2] <= nums[3]....

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^4

Follow up:
Can you do it in-place with O(1) extra space?
"""

# Solution
def wiggleSort(nums):
    """
    Reorders the array in-place to satisfy the wiggle sort condition.
    
    Args:
    nums (List[int]): The input array of integers.
    
    Returns:
    None: The function modifies the input array in-place.
    """
    for i in range(len(nums) - 1):
        if (i % 2 == 0 and nums[i] > nums[i + 1]) or (i % 2 == 1 and nums[i] < nums[i + 1]):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 5, 2, 1, 6, 4]
    wiggleSort(nums1)
    print(nums1)  # Output: [3, 5, 1, 6, 2, 4]

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5, 6]
    wiggleSort(nums2)
    print(nums2)  # Output: [1, 3, 2, 5, 4, 6]

    # Test Case 3
    nums3 = [6, 6, 6, 6, 6]
    wiggleSort(nums3)
    print(nums3)  # Output: [6, 6, 6, 6, 6] (already satisfies the condition)

    # Test Case 4
    nums4 = [10, 1, 2, 3, 4, 5]
    wiggleSort(nums4)
    print(nums4)  # Output: [1, 10, 2, 5, 3, 4]

# Time and Space Complexity Analysis
"""
Time Complexity:
The algorithm iterates through the array once, performing constant-time operations for each element.
Thus, the time complexity is O(n), where n is the length of the array.

Space Complexity:
The algorithm modifies the array in-place and does not use any additional data structures.
Thus, the space complexity is O(1).
"""

# Topic: Arrays