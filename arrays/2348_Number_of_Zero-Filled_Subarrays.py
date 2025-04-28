"""
LeetCode Problem #2348: Number of Zero-Filled Subarrays

Problem Statement:
Given an integer array `nums`, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0.
Therefore, we return 6.

Example 2:
Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 6 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
Therefore, we return 9.

Example 3:
Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

def zero_filled_subarray(nums):
    """
    Function to calculate the number of zero-filled subarrays in the given array.

    :param nums: List[int] - The input array of integers.
    :return: int - The number of zero-filled subarrays.
    """
    count = 0
    current_zeros = 0

    for num in nums:
        if num == 0:
            current_zeros += 1
            count += current_zeros
        else:
            current_zeros = 0

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 0, 0, 2, 0, 0, 4]
    print(zero_filled_subarray(nums1))  # Output: 6

    # Test Case 2
    nums2 = [0, 0, 0, 2, 0, 0]
    print(zero_filled_subarray(nums2))  # Output: 9

    # Test Case 3
    nums3 = [2, 10, 2019]
    print(zero_filled_subarray(nums3))  # Output: 0

    # Test Case 4
    nums4 = [0, 0, 0, 0]
    print(zero_filled_subarray(nums4))  # Output: 10

    # Test Case 5
    nums5 = [1, 0, 1, 0, 0, 1, 0]
    print(zero_filled_subarray(nums5))  # Output: 4

"""
Time Complexity:
- The algorithm iterates through the array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses a constant amount of extra space (two integer variables: `count` and `current_zeros`).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""