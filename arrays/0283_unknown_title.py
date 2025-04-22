"""
LeetCode Problem #283: Move Zeroes

Problem Statement:
Given an integer array `nums`, move all `0`s to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you minimize the total number of operations done?
"""

def moveZeroes(nums):
    """
    Moves all zeroes in the array to the end while maintaining the relative order of non-zero elements.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    None: The function modifies the input array in-place.
    """
    # Initialize a pointer for the position of the next non-zero element
    non_zero_index = 0

    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is non-zero, swap it with the element at non_zero_index
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [0, 1, 0, 3, 12]
    moveZeroes(nums1)
    print(nums1)  # Output: [1, 3, 12, 0, 0]

    # Test Case 2
    nums2 = [0]
    moveZeroes(nums2)
    print(nums2)  # Output: [0]

    # Test Case 3
    nums3 = [1, 0, 2, 0, 3, 0, 4]
    moveZeroes(nums3)
    print(nums3)  # Output: [1, 2, 3, 4, 0, 0, 0]

    # Test Case 4
    nums4 = [0, 0, 0, 0, 0]
    moveZeroes(nums4)
    print(nums4)  # Output: [0, 0, 0, 0, 0]

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5]
    moveZeroes(nums5)
    print(nums5)  # Output: [1, 2, 3, 4, 5]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array once, performing swaps when necessary.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space (the `non_zero_index` variable).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""