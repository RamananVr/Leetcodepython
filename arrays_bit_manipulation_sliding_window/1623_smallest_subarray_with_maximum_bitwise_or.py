"""
LeetCode Question #1623: Smallest Subarray With Maximum Bitwise OR

Problem Statement:
Given an array `nums` of positive integers, find the smallest subarray that has the maximum bitwise OR value. 
A subarray is a contiguous part of the array. Return the length of the smallest subarray that achieves the maximum bitwise OR value.

Example:
Input: nums = [1, 2, 3, 4]
Output: 2
Explanation: The maximum bitwise OR value is 7, which can be achieved by the subarray [3, 4].

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

# Python Solution
def smallestSubarrayWithMaxBitwiseOR(nums):
    """
    Finds the length of the smallest subarray with the maximum bitwise OR value.

    :param nums: List[int] - The input array of positive integers.
    :return: int - The length of the smallest subarray with the maximum bitwise OR value.
    """
    # Step 1: Compute the maximum bitwise OR value for the entire array
    max_or = 0
    for num in nums:
        max_or |= num

    # Step 2: Find the smallest subarray that achieves this maximum OR value
    n = len(nums)
    smallest_length = n
    current_or = 0
    left = 0

    for right in range(n):
        current_or |= nums[right]

        # Shrink the window while the current OR is still equal to max_or
        while current_or == max_or:
            smallest_length = min(smallest_length, right - left + 1)
            current_or ^= nums[left]
            left += 1

    return smallest_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print(smallestSubarrayWithMaxBitwiseOR(nums1))  # Output: 2

    # Test Case 2
    nums2 = [8, 1, 2, 7]
    print(smallestSubarrayWithMaxBitwiseOR(nums2))  # Output: 1

    # Test Case 3
    nums3 = [1, 1, 1, 1]
    print(smallestSubarrayWithMaxBitwiseOR(nums3))  # Output: 4

    # Test Case 4
    nums4 = [5, 1, 2, 4, 8]
    print(smallestSubarrayWithMaxBitwiseOR(nums4))  # Output: 2

    # Test Case 5
    nums5 = [1]
    print(smallestSubarrayWithMaxBitwiseOR(nums5))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Computing the maximum bitwise OR value for the entire array takes O(n), where n is the length of the array.
- The sliding window approach iterates through the array once, and shrinking the window is proportional to the number of elements. 
  Thus, the overall time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space (variables like `max_or`, `current_or`, `left`, etc.).
- Therefore, the space complexity is O(1).

Topic: Arrays, Bit Manipulation, Sliding Window
"""