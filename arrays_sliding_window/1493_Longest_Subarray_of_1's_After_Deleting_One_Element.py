"""
LeetCode Problem #1493: Longest Subarray of 1's After Deleting One Element

Problem Statement:
Given a binary array `nums`, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the 0, the longest subarray is [1,1,1], with length 3.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting one 0, the longest subarray is [1,1,1,1,1], with length 5.

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element, so the longest subarray is [1,1], with length 2.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
"""

def longest_subarray(nums):
    """
    Finds the length of the longest subarray of 1's after deleting one element.

    :param nums: List[int] - Binary array
    :return: int - Length of the longest subarray of 1's
    """
    max_length = 0
    left = 0
    zero_count = 0

    for right in range(len(nums)):
        # Count zeros in the current window
        if nums[right] == 0:
            zero_count += 1

        # If there are more than one zero, shrink the window from the left
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # Calculate the length of the current window
        max_length = max(max_length, right - left)

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 0, 1]
    print(longest_subarray(nums1))  # Output: 3

    # Test Case 2
    nums2 = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    print(longest_subarray(nums2))  # Output: 5

    # Test Case 3
    nums3 = [1, 1, 1]
    print(longest_subarray(nums3))  # Output: 2

    # Test Case 4
    nums4 = [0, 0, 0]
    print(longest_subarray(nums4))  # Output: 0

    # Test Case 5
    nums5 = [1, 0, 1, 1, 0, 1]
    print(longest_subarray(nums5))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses a sliding window approach, where the `right` pointer iterates through the array once.
- The `left` pointer adjusts as needed, but each element is processed at most twice (once by `right` and once by `left`).
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses a constant amount of extra space (variables `max_length`, `left`, and `zero_count`).
- No additional data structures are used.
- Therefore, the space complexity is O(1).

Topic: Arrays, Sliding Window
"""