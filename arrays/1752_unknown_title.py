"""
LeetCode Problem #1752: Check if Array Is Sorted and Rotated

Problem Statement:
Given an array nums, return true if the array was originally sorted in non-decreasing order, 
then rotated some number of positions (including zero). Otherwise, return false.

An array A is considered "rotated" if:
- It can be obtained by taking a sorted array and rotating it some number of times.
- For example, A = [3, 4, 5, 1, 2] is considered rotated because it is derived from the sorted array [1, 2, 3, 4, 5] by rotating it 3 positions.

Note:
- The array may contain duplicates.
- A sorted array is considered rotated by 0 positions.

Constraints:
- 1 <= nums.length <= 100
- -100 <= nums[i] <= 100
"""

def check(nums):
    """
    Function to check if the array is sorted and rotated.

    :param nums: List[int] - Input array
    :return: bool - True if the array is sorted and rotated, False otherwise
    """
    count_breaks = 0
    n = len(nums)
    
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count_breaks += 1
    
    return count_breaks <= 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Rotated sorted array
    nums1 = [3, 4, 5, 1, 2]
    print(check(nums1))  # Expected output: True

    # Test Case 2: Sorted array (not rotated)
    nums2 = [1, 2, 3, 4, 5]
    print(check(nums2))  # Expected output: True

    # Test Case 3: Not sorted or rotated
    nums3 = [2, 1, 3, 4, 5]
    print(check(nums3))  # Expected output: False

    # Test Case 4: Single element array
    nums4 = [1]
    print(check(nums4))  # Expected output: True

    # Test Case 5: Array with duplicates
    nums5 = [2, 2, 2, 1, 2]
    print(check(nums5))  # Expected output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The function uses a constant amount of extra space (count_breaks and n variables).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""