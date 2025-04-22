"""
LeetCode Question #18: 4Sum

Problem Statement:
Given an array `nums` of `n` integers and an integer `target`, return all unique quadruplets 
[nums[a], nums[b], nums[c], nums[d]] such that:
    - 0 <= a, b, c, d < n
    - a, b, c, and d are distinct.
    - nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
- 1 <= nums.length <= 200
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- The solution set must not contain duplicate quadruplets.
"""

# Python Solution
def fourSum(nums, target):
    nums.sort()  # Sort the array to simplify duplicate handling and two-pointer approach
    n = len(nums)
    result = []

    for i in range(n - 3):
        # Skip duplicates for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            # Skip duplicates for the second number
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            # Two-pointer approach for the remaining two numbers
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    # Skip duplicates for the third and fourth numbers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
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

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n).
- The outer two loops iterate over the array, resulting in O(n^2).
- The two-pointer approach for the remaining two numbers takes O(n) in the worst case.
- Overall complexity: O(n^3).

Space Complexity:
- The space complexity is O(1) for the sorting and two-pointer approach.
- The result list may take up to O(k) space, where k is the number of unique quadruplets.
- Overall space complexity: O(k).
"""

# Topic: Arrays