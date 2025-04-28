"""
LeetCode Problem #485: Max Consecutive Ones

Problem Statement:
Given a binary array `nums`, return the maximum number of consecutive 1s in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits and the last three digits form consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
"""

# Solution
def findMaxConsecutiveOnes(nums):
    """
    Function to find the maximum number of consecutive 1s in a binary array.

    :param nums: List[int] - A binary array containing only 0s and 1s.
    :return: int - The maximum number of consecutive 1s.
    """
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 0, 1, 1, 1]
    print(findMaxConsecutiveOnes(nums1))  # Output: 3

    # Test Case 2
    nums2 = [1, 0, 1, 1, 0, 1]
    print(findMaxConsecutiveOnes(nums2))  # Output: 2

    # Test Case 3
    nums3 = [0, 0, 0, 0]
    print(findMaxConsecutiveOnes(nums3))  # Output: 0

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    print(findMaxConsecutiveOnes(nums4))  # Output: 4

    # Test Case 5
    nums5 = [1, 0, 0, 1, 0, 1, 1, 1, 0, 1]
    print(findMaxConsecutiveOnes(nums5))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
The function iterates through the array once, performing constant-time operations for each element.
Thus, the time complexity is O(n), where n is the length of the array.

Space Complexity:
The function uses a constant amount of extra space (two integer variables: `max_count` and `current_count`).
Thus, the space complexity is O(1).
"""

# Topic: Arrays