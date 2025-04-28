"""
LeetCode Problem #2012: Sum of Beauty in the Array

Problem Statement:
You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2), the beauty of nums[i] equals:
- 2, if nums[i] is strictly greater than all elements to its left and strictly less than all elements to its right.
- 1, if nums[i] is strictly greater than all elements to its left or strictly less than all elements to its right.
- 0, otherwise.

Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.

Example 1:
Input: nums = [1,2,3]
Output: 2
Explanation: For nums[1] = 2, it is strictly greater than nums[0] = 1 and strictly less than nums[2] = 3. Hence, beauty of nums[1] is 2.

Example 2:
Input: nums = [2,4,6,4]
Output: 1
Explanation: For nums[1] = 4, it is strictly greater than nums[0] = 2 and strictly less than nums[2] = 6. Hence, beauty of nums[1] is 2.
For nums[2] = 6, it is not strictly less than nums[3] = 4. Hence, beauty of nums[2] is 0.

Example 3:
Input: nums = [3,2,1]
Output: 0
Explanation: For nums[1] = 2 and nums[2] = 1, neither of them is strictly greater than all elements to their left nor strictly less than all elements to their right. Hence, beauty of nums[1] and nums[2] is 0.

Constraints:
- 3 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

# Python Solution
def sumOfBeauties(nums):
    n = len(nums)
    left_max = [0] * n
    right_min = [0] * n

    # Compute left_max array
    left_max[0] = nums[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], nums[i])

    # Compute right_min array
    right_min[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], nums[i])

    # Calculate the sum of beauty
    beauty_sum = 0
    for i in range(1, n - 1):
        if left_max[i - 1] < nums[i] < right_min[i + 1]:
            beauty_sum += 2
        elif nums[i] > nums[i - 1] and nums[i] < nums[i + 1]:
            beauty_sum += 1

    return beauty_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    print(sumOfBeauties(nums1))  # Output: 2

    # Test Case 2
    nums2 = [2, 4, 6, 4]
    print(sumOfBeauties(nums2))  # Output: 1

    # Test Case 3
    nums3 = [3, 2, 1]
    print(sumOfBeauties(nums3))  # Output: 0

    # Additional Test Case
    nums4 = [1, 3, 2, 4, 5]
    print(sumOfBeauties(nums4))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- Computing the left_max array takes O(n) time.
- Computing the right_min array takes O(n) time.
- Iterating through the array to calculate the beauty sum takes O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- The left_max and right_min arrays each take O(n) space.
- Overall space complexity: O(n).

Topic: Arrays
"""