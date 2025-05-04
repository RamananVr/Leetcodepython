"""
LeetCode Problem #1004: Max Consecutive Ones III

Problem Statement:
Given a binary array `nums` and an integer `k`, you can flip at most `k` 0s to 1s. 
Return the maximum number of consecutive 1s in the array after performing the flips.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1] -> The maximum number of consecutive 1s is 6.

Example 2:
Input: nums = [0,0,1,1,1,0,0], k = 0
Output: 3
Explanation: [0,0,1,1,1,0,0] -> The maximum number of consecutive 1s is 3.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
- 0 <= k <= nums.length
"""

# Python Solution
def longestOnes(nums, k):
    """
    Finds the maximum number of consecutive 1s in the binary array `nums` after flipping at most `k` 0s to 1s.

    :param nums: List[int] - Binary array consisting of 0s and 1s.
    :param k: int - Maximum number of 0s that can be flipped to 1s.
    :return: int - Maximum number of consecutive 1s.
    """
    left = 0
    max_length = 0
    zero_count = 0

    for right in range(len(nums)):
        # Expand the window by including nums[right]
        if nums[right] == 0:
            zero_count += 1

        # Shrink the window if the number of 0s exceeds k
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # Update the maximum length of the window
        max_length = max(max_length, right - left + 1)

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1,1,1,0,0,0,1,1,1,1,0]
    k1 = 2
    print(longestOnes(nums1, k1))  # Output: 6

    # Test Case 2
    nums2 = [0,0,1,1,1,0,0]
    k2 = 0
    print(longestOnes(nums2, k2))  # Output: 3

    # Test Case 3
    nums3 = [1,0,1,0,1,0,1]
    k3 = 3
    print(longestOnes(nums3, k3))  # Output: 7

    # Test Case 4
    nums4 = [0,0,0,0,0]
    k4 = 2
    print(longestOnes(nums4, k4))  # Output: 2

    # Test Case 5
    nums5 = [1,1,1,1,1]
    k5 = 0
    print(longestOnes(nums5, k5))  # Output: 5

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm uses a sliding window approach where the `right` pointer iterates through the array once.
- The `left` pointer also moves forward, but each element is processed at most once.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space (variables `left`, `right`, `zero_count`, and `max_length`).
- Hence, the space complexity is O(1).
"""

# Topic: Arrays, Sliding Window