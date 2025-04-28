"""
LeetCode Problem #2419: Longest Subarray With Maximum Bitwise AND

Problem Statement:
You are given an integer array `nums` of size `n`.

Consider a non-empty subarray from `nums` that has the maximum possible bitwise AND value. 
- A subarray is a contiguous sequence of elements within an array.

Return the length of the longest such subarray.

Example:
Input: nums = [1, 2, 3, 3, 2, 2]
Output: 2
Explanation: The maximum bitwise AND value is 3. The subarray [3, 3] has the maximum AND value and its length is 2.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""

def longest_subarray(nums):
    """
    Finds the length of the longest subarray with the maximum bitwise AND value.

    :param nums: List[int] - The input array of integers.
    :return: int - The length of the longest subarray with the maximum AND value.
    """
    # Step 1: Find the maximum value in the array
    max_val = max(nums)
    
    # Step 2: Initialize variables to track the longest subarray
    max_length = 0
    current_length = 0
    
    # Step 3: Iterate through the array to find the longest subarray with max_val
    for num in nums:
        if num == max_val:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    
    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 3, 2, 2]
    print(longest_subarray(nums1))  # Output: 2

    # Test Case 2
    nums2 = [1, 1, 1, 1]
    print(longest_subarray(nums2))  # Output: 4

    # Test Case 3
    nums3 = [5, 5, 5, 1, 2, 5, 5]
    print(longest_subarray(nums3))  # Output: 3

    # Test Case 4
    nums4 = [10, 10, 10, 10, 10]
    print(longest_subarray(nums4))  # Output: 5

    # Test Case 5
    nums5 = [1, 2, 4, 8, 16]
    print(longest_subarray(nums5))  # Output: 1

"""
Time Complexity Analysis:
- Finding the maximum value in the array takes O(n), where n is the length of the array.
- Iterating through the array to find the longest subarray also takes O(n).
- Overall time complexity: O(n).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space (variables like max_val, max_length, and current_length).
- Overall space complexity: O(1).

Topic: Arrays
"""