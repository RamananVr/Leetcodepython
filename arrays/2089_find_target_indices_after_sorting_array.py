"""
LeetCode Question #2089: Find Target Indices After Sorting Array

Problem Statement:
You are given a 0-indexed integer array `nums` and a target integer `target`.

First, sort `nums` in non-decreasing order, then find the indices of the target in the sorted array. 
Return a list of the target indices of `nums` after sorting. If there are no target indices, return an empty list. 
The returned list must be sorted in increasing order.

Example 1:
Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums becomes [1,2,2,3,5].
The indices where 2 occurs are 1 and 2.

Example 2:
Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums becomes [1,2,2,3,5].
The index where 3 occurs is 3.

Example 3:
Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums becomes [1,2,2,3,5].
The index where 5 occurs is 4.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i], target <= 100
"""

# Python Solution
def targetIndices(nums, target):
    """
    Finds the indices of the target in the sorted array.

    Args:
    nums (List[int]): The input array of integers.
    target (int): The target integer to find.

    Returns:
    List[int]: A list of indices where the target occurs in the sorted array.
    """
    # Step 1: Sort the array
    nums.sort()
    
    # Step 2: Find indices of the target
    result = []
    for i in range(len(nums)):
        if nums[i] == target:
            result.append(i)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 5, 2, 3]
    target1 = 2
    print(targetIndices(nums1, target1))  # Output: [1, 2]

    # Test Case 2
    nums2 = [1, 2, 5, 2, 3]
    target2 = 3
    print(targetIndices(nums2, target2))  # Output: [3]

    # Test Case 3
    nums3 = [1, 2, 5, 2, 3]
    target3 = 5
    print(targetIndices(nums3, target3))  # Output: [4]

    # Test Case 4 (Edge Case: No target in array)
    nums4 = [1, 2, 5, 2, 3]
    target4 = 4
    print(targetIndices(nums4, target4))  # Output: []

    # Test Case 5 (Edge Case: Single element array)
    nums5 = [5]
    target5 = 5
    print(targetIndices(nums5, target5))  # Output: [0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- Iterating through the array to find the target indices takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- Sorting is done in-place, so no additional space is used.
- The result list takes O(k) space, where k is the number of occurrences of the target.
- Overall space complexity: O(k).
"""

# Topic: Arrays