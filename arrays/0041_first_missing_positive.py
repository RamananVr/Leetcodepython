"""
LeetCode Question #41: First Missing Positive

Problem Statement:
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
"""

def firstMissingPositive(nums):
    """
    Finds the smallest missing positive integer in an unsorted array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The smallest missing positive integer.
    """
    n = len(nums)
    
    # Step 1: Place each number in its correct index position if possible
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap nums[i] with nums[nums[i] - 1]
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
    # Step 2: Identify the first missing positive integer
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    # If all numbers are in their correct positions, return n + 1
    return n + 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 0]
    print(firstMissingPositive(nums1))  # Output: 3

    # Test Case 2
    nums2 = [3, 4, -1, 1]
    print(firstMissingPositive(nums2))  # Output: 2

    # Test Case 3
    nums3 = [7, 8, 9, 11, 12]
    print(firstMissingPositive(nums3))  # Output: 1

    # Test Case 4
    nums4 = [1]
    print(firstMissingPositive(nums4))  # Output: 2

    # Test Case 5
    nums5 = [2, 1]
    print(firstMissingPositive(nums5))  # Output: 3

"""
Time Complexity:
- The algorithm runs in O(n) time because each number is swapped at most once, and the loop iterates through the array a constant number of times.

Space Complexity:
- The algorithm uses O(1) extra space since it modifies the input array in place and does not use any additional data structures.

Topic: Arrays
"""