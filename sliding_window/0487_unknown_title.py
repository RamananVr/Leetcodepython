"""
LeetCode Problem #487: Max Consecutive Ones II

Problem Statement:
Given a binary array `nums`, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

Example 1:
Input: nums = [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero to get [1,1,1,1,0], which has a maximum of 4 consecutive 1's.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation: Flip the first zero to get [1,1,1,1,0,1], which has a maximum of 4 consecutive 1's.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.

Follow-up:
What if the input numbers come in a stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?
"""

def findMaxConsecutiveOnes(nums):
    """
    Function to find the maximum number of consecutive 1's in the array
    if you can flip at most one 0.
    """
    max_ones = 0
    left = 0
    zero_count = 0

    for right in range(len(nums)):
        # If we encounter a zero, increment the zero_count
        if nums[right] == 0:
            zero_count += 1

        # If zero_count exceeds 1, shrink the window from the left
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # Update the maximum length of consecutive 1's
        max_ones = max(max_ones, right - left + 1)

    return max_ones

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 0, 1, 1, 0]
    print(findMaxConsecutiveOnes(nums1))  # Output: 4

    # Test Case 2
    nums2 = [1, 0, 1, 1, 0, 1]
    print(findMaxConsecutiveOnes(nums2))  # Output: 4

    # Test Case 3
    nums3 = [1, 1, 1, 1, 1]
    print(findMaxConsecutiveOnes(nums3))  # Output: 5

    # Test Case 4
    nums4 = [0, 0, 0, 0]
    print(findMaxConsecutiveOnes(nums4))  # Output: 1

    # Test Case 5
    nums5 = [1, 0, 1, 0, 1, 0, 1]
    print(findMaxConsecutiveOnes(nums5))  # Output: 3

"""
Time Complexity:
- The algorithm processes each element of the array exactly once, as the `right` pointer iterates through the array and the `left` pointer only moves forward. 
- Thus, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses a constant amount of extra space (variables like `left`, `right`, `zero_count`, and `max_ones`).
- Thus, the space complexity is O(1).

Topic: Sliding Window
"""