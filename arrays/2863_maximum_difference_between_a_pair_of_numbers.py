"""
LeetCode Question #2863: Maximum Difference Between a Pair of Numbers

Problem Statement:
You are given an integer array `nums`. The maximum difference between a pair of numbers is defined as the largest difference 
between any two numbers in the array such that the larger number comes after the smaller number in the array.

Return the maximum difference. If no such pair exists, return -1.

Example 1:
Input: nums = [7,1,5,4]
Output: 4
Explanation: The maximum difference occurs between 1 and 5, where 5 comes after 1.

Example 2:
Input: nums = [9,4,3,2]
Output: -1
Explanation: No pair exists where the larger number comes after the smaller number.

Example 3:
Input: nums = [1,5,2,10]
Output: 9
Explanation: The maximum difference occurs between 1 and 10, where 10 comes after 1.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^9
"""

# Python Solution
def maximumDifference(nums):
    """
    Function to calculate the maximum difference between a pair of numbers
    such that the larger number comes after the smaller number in the array.

    :param nums: List[int] - Input array of integers
    :return: int - Maximum difference or -1 if no valid pair exists
    """
    min_value = float('inf')
    max_diff = -1

    for num in nums:
        if num > min_value:
            max_diff = max(max_diff, num - min_value)
        min_value = min(min_value, num)

    return max_diff

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [7, 1, 5, 4]
    print(maximumDifference(nums1))  # Output: 4

    # Test Case 2
    nums2 = [9, 4, 3, 2]
    print(maximumDifference(nums2))  # Output: -1

    # Test Case 3
    nums3 = [1, 5, 2, 10]
    print(maximumDifference(nums3))  # Output: 9

    # Additional Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    print(maximumDifference(nums4))  # Output: 4

    # Additional Test Case 5
    nums5 = [5, 4, 3, 2, 1]
    print(maximumDifference(nums5))  # Output: -1

"""
Time and Space Complexity Analysis:

Time Complexity:
The function iterates through the array once, performing constant-time operations for each element. 
Thus, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
The function uses a constant amount of extra space (variables `min_value` and `max_diff`), 
so the space complexity is O(1).

Topic: Arrays
"""