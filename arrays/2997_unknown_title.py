"""
LeetCode Problem #2997: Full Problem Statement

Problem:
You are given a list of integers `nums` and an integer `target`. Your task is to find all unique quadruplets 
in the array which gives the sum of `target`.

The solution set must not contain duplicate quadruplets.

Example:
Input: nums = [1, 0, -1, 0, -2, 2], target = 0
Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

Constraints:
1. 1 <= nums.length <= 200
2. -10^9 <= nums[i] <= 10^9
3. -10^9 <= target <= 10^9
"""

# Python Solution
def fourSum(nums, target):
    """
    Finds all unique quadruplets in the array that sum up to the target.

    :param nums: List[int] - List of integers
    :param target: int - Target sum
    :return: List[List[int]] - List of quadruplets
    """
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 3):
        # Skip duplicate values for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            # Skip duplicate values for the second number
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate values for the third and fourth numbers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    print(fourSum(nums1, target1))  # Expected Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    # Test Case 2
    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    print(fourSum(nums2, target2))  # Expected Output: [[2, 2, 2, 2]]

    # Test Case 3
    nums3 = [-3, -2, -1, 0, 0, 1, 2, 3]
    target3 = 0
    print(fourSum(nums3, target3))  # Expected Output: [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    # Test Case 4
    nums4 = [0, 0, 0, 0]
    target4 = 0
    print(fourSum(nums4, target4))  # Expected Output: [[0, 0, 0, 0]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n).
- The nested loops iterate over the array with two pointers, resulting in O(n^3) in the worst case.
- Overall time complexity: O(n^3).

Space Complexity:
- The space complexity is O(1) for the sorting and pointer manipulation.
- The result list may grow in size depending on the number of quadruplets found, but this is not considered auxiliary space.
- Overall space complexity: O(1) (excluding the output).

Topic: Arrays
"""