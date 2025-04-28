"""
LeetCode Problem #75: Sort Colors

Problem Statement:
Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

Follow-up:
Could you come up with a one-pass algorithm using only constant extra space?
"""

def sortColors(nums):
    """
    Sorts the input list `nums` in-place such that all 0s come first, followed by 1s, and then 2s.

    Args:
    nums (List[int]): List of integers where each integer is either 0, 1, or 2.

    Returns:
    None: The input list is modified in-place.
    """
    # Initialize pointers
    low, mid, high = 0, 0, len(nums) - 1

    # One-pass algorithm
    while mid <= high:
        if nums[mid] == 0:
            # Swap nums[low] and nums[mid], then increment both pointers
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # Move the mid pointer forward
            mid += 1
        else:  # nums[mid] == 2
            # Swap nums[mid] and nums[high], then decrement the high pointer
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 0, 2, 1, 1, 0]
    sortColors(nums1)
    print(nums1)  # Output: [0, 0, 1, 1, 2, 2]

    # Test Case 2
    nums2 = [2, 0, 1]
    sortColors(nums2)
    print(nums2)  # Output: [0, 1, 2]

    # Test Case 3
    nums3 = [0]
    sortColors(nums3)
    print(nums3)  # Output: [0]

    # Test Case 4
    nums4 = [1, 2, 0]
    sortColors(nums4)
    print(nums4)  # Output: [0, 1, 2]

"""
Time Complexity:
- The algorithm processes each element of the array exactly once, making it O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses constant extra space, O(1), as it modifies the input array in-place.

Topic: Arrays
"""