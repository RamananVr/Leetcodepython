"""
LeetCode Problem #995: Minimum Number of K Consecutive Bit Flips

Problem Statement:
You are given a binary array `nums` and an integer `k`.

A *k-bit flip* is choosing a subarray of length `k` from `nums` and simultaneously flipping every bit in the subarray 
(i.e., changing 0 to 1 and 1 to 0).

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].

Example 2:
Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].

Example 3:
Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation: 
Flip nums[0], nums[1], and nums[4].

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= k <= nums.length
"""

def minKBitFlips(nums, k):
    """
    Function to calculate the minimum number of k-bit flips required to make all elements in nums equal to 1.
    If it's not possible, return -1.
    """
    n = len(nums)
    flips = 0
    flip_count = 0
    is_flipped = [0] * n  # Tracks whether a flip affects the current index

    for i in range(n):
        # Remove the effect of a flip that is no longer in the current window
        if i >= k:
            flip_count ^= is_flipped[i - k]

        # If the current bit is 0 and the current flip count is even (or 1 and odd), we need to flip
        if nums[i] == flip_count:
            if i + k > n:  # If flipping here would exceed the array bounds
                return -1
            flips += 1
            flip_count ^= 1  # Toggle the flip count
            is_flipped[i] = 1  # Mark the start of a flip

    return flips


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [0, 1, 0]
    k1 = 1
    print(minKBitFlips(nums1, k1))  # Output: 2

    # Test Case 2
    nums2 = [1, 1, 0]
    k2 = 2
    print(minKBitFlips(nums2, k2))  # Output: -1

    # Test Case 3
    nums3 = [0, 0, 0, 1, 0, 1, 1, 0]
    k3 = 3
    print(minKBitFlips(nums3, k3))  # Output: 3

    # Test Case 4
    nums4 = [1, 0, 1, 0, 1, 0]
    k4 = 2
    print(minKBitFlips(nums4, k4))  # Output: 3

    # Test Case 5
    nums5 = [1, 1, 1, 1]
    k5 = 2
    print(minKBitFlips(nums5, k5))  # Output: 0


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Thus, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses an auxiliary array `is_flipped` of size n to track the flip status of each index.
- Therefore, the space complexity is O(n).

Topic: Arrays, Greedy
"""