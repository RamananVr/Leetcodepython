"""
LeetCode Problem #1437: Check If All 1's Are at Least Length K Places Away

Problem Statement:
Given an array `nums` of 0s and 1s and an integer `k`, return `true` if all 1's are at least `k` places away from each other, otherwise return `false`.

In other words, if there are two 1's in the array at indices `i` and `j`, where `i < j`, then `j - i >= k + 1`.

Example 1:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1's are at least 2 places away from each other.

Example 2:
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second and third 1's are only one place apart.

Example 3:
Input: nums = [1,1,1,1,1], k = 0
Output: true

Example 4:
Input: nums = [0,1,0,1], k = 1
Output: true

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= k <= nums.length
- nums[i] is 0 or 1
"""

# Python Solution
def kLengthApart(nums, k):
    """
    Check if all 1's in the array are at least k places apart.

    :param nums: List[int] - Array of 0s and 1s
    :param k: int - Minimum distance between 1's
    :return: bool - True if all 1's are at least k places apart, False otherwise
    """
    prev_index = -1  # Initialize the index of the previous 1 to -1 (no 1 encountered yet)

    for i, num in enumerate(nums):
        if num == 1:
            if prev_index != -1 and i - prev_index <= k:
                return False
            prev_index = i  # Update the index of the last encountered 1

    return True


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 0, 0, 0, 1, 0, 0, 1]
    k1 = 2
    print(kLengthApart(nums1, k1))  # Output: True

    # Test Case 2
    nums2 = [1, 0, 0, 1, 0, 1]
    k2 = 2
    print(kLengthApart(nums2, k2))  # Output: False

    # Test Case 3
    nums3 = [1, 1, 1, 1, 1]
    k3 = 0
    print(kLengthApart(nums3, k3))  # Output: True

    # Test Case 4
    nums4 = [0, 1, 0, 1]
    k4 = 1
    print(kLengthApart(nums4, k4))  # Output: True

    # Test Case 5
    nums5 = [0, 0, 0, 0, 0]
    k5 = 3
    print(kLengthApart(nums5, k5))  # Output: True


# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the array `nums` once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The function uses a single integer variable `prev_index` to store the index of the last encountered 1.
- No additional data structures are used, so the space complexity is O(1).
"""

# Topic: Arrays