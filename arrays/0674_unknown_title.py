"""
LeetCode Problem #674: Longest Continuous Increasing Subsequence

Problem Statement:
Given an unsorted array of integers `nums`, return the length of the longest continuous increasing subsequence (LCIS).

The subsequence must be strictly increasing, and the elements of the subsequence must be consecutive elements of the array.

Example 1:
Input: nums = [1, 3, 5, 4, 7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1, 3, 5] with length 3.

Example 2:
Input: nums = [2, 2, 2, 2, 2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1.

Constraints:
- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
"""

def findLengthOfLCIS(nums):
    """
    Function to find the length of the longest continuous increasing subsequence.

    :param nums: List[int] - The input array of integers.
    :return: int - The length of the longest continuous increasing subsequence.
    """
    if not nums:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 5, 4, 7]
    print(findLengthOfLCIS(nums1))  # Output: 3

    # Test Case 2
    nums2 = [2, 2, 2, 2, 2]
    print(findLengthOfLCIS(nums2))  # Output: 1

    # Test Case 3
    nums3 = [10, 20, 30, 10, 40, 50, 60]
    print(findLengthOfLCIS(nums3))  # Output: 4

    # Test Case 4
    nums4 = [1]
    print(findLengthOfLCIS(nums4))  # Output: 1

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5]
    print(findLengthOfLCIS(nums5))  # Output: 5

"""
Time Complexity Analysis:
- The function iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The function uses a constant amount of extra space for variables like `max_length` and `current_length`.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""