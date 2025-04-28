"""
LeetCode Problem #2674: Split Array Into Maximum Number of Subarrays

Problem Statement:
You are given an integer array nums. You want to split nums into the maximum number of subarrays such that:
1. Each subarray is non-empty.
2. The bitwise AND of the elements of each subarray is 0.

Return the maximum number of subarrays you can achieve.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^6
"""

# Solution
def maxSubarrays(nums):
    """
    Function to calculate the maximum number of subarrays such that the bitwise AND of each subarray is 0.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The maximum number of subarrays.
    """
    # Initialize variables
    current_and = -1  # Start with all bits set (bitwise AND identity)
    subarray_count = 0

    # Iterate through the array
    for num in nums:
        current_and &= num  # Update the current AND value
        if current_and == 0:  # If the AND becomes 0, we can split here
            subarray_count += 1
            current_and = -1  # Reset the AND for the next subarray

    # If no subarray was formed, return 1 (the entire array is one subarray)
    return subarray_count if subarray_count > 0 else 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 0, 2, 0, 3]
    print(maxSubarrays(nums1))  # Expected Output: 4

    # Test Case 2
    nums2 = [5, 7, 9]
    print(maxSubarrays(nums2))  # Expected Output: 1

    # Test Case 3
    nums3 = [0, 0, 0]
    print(maxSubarrays(nums3))  # Expected Output: 3

    # Test Case 4
    nums4 = [1, 2, 4, 8, 16]
    print(maxSubarrays(nums4))  # Expected Output: 1

    # Test Case 5
    nums5 = [0, 1, 0, 1, 0]
    print(maxSubarrays(nums5))  # Expected Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the array once, performing a constant-time operation (bitwise AND) for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The function uses a constant amount of extra space for variables (current_and and subarray_count).
- Therefore, the space complexity is O(1).

Topic: Arrays, Bit Manipulation
"""