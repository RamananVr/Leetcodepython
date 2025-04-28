"""
LeetCode Problem #665: Non-decreasing Array

Problem Statement:
Given an array nums with n integers, your task is to check if it could become non-decreasing 
by modifying at most one element.

We define an array as non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) 
such that (0 <= i <= n - 2).

Example 1:
Input: nums = [4, 2, 3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: nums = [4, 2, 1]
Output: false
Explanation: You can't get a non-decreasing array by modifying at most one element.

Constraints:
- n == nums.length
- 1 <= n <= 10^4
- -10^5 <= nums[i] <= 10^5
"""

def checkPossibility(nums):
    """
    Function to check if the array can be made non-decreasing by modifying at most one element.

    :param nums: List[int] - The input array of integers
    :return: bool - True if the array can be made non-decreasing, False otherwise
    """
    count = 0  # To track the number of modifications
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            # If more than one modification is needed, return False
            if count == 1:
                return False
            count += 1
            # Modify nums[i] or nums[i+1] to maintain non-decreasing order
            if i == 0 or nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i + 1]  # Modify nums[i]
            else:
                nums[i + 1] = nums[i]  # Modify nums[i+1]
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 2, 3]
    print(checkPossibility(nums1))  # Output: True

    # Test Case 2
    nums2 = [4, 2, 1]
    print(checkPossibility(nums2))  # Output: False

    # Test Case 3
    nums3 = [3, 4, 2, 3]
    print(checkPossibility(nums3))  # Output: False

    # Test Case 4
    nums4 = [5, 7, 1, 8]
    print(checkPossibility(nums4))  # Output: True

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5]
    print(checkPossibility(nums5))  # Output: True

"""
Time Complexity Analysis:
- The function iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The function uses a constant amount of extra space (only a few variables).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""