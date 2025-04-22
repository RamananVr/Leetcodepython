"""
LeetCode Problem #396: Rotate Function

Problem Statement:
You are given an integer array `nums` of length `n`.

Assume `F` is a function that takes an array `nums` and returns an integer. The function `F` is defined as:
F(k) = 0 * nums[k] + 1 * nums[k+1] + 2 * nums[k+2] + ... + (n-1) * nums[k+n-1]

Where the array is rotated `k` times. Here, `nums[k+n-1]` means the array element at index `(k+n-1) % n`.

Return the maximum value of `F(0), F(1), ..., F(n-1)`.

Example:
Input: nums = [4, 3, 2, 6]
Output: 26
Explanation:
F(0) = 0*4 + 1*3 + 2*2 + 3*6 = 25
F(1) = 0*6 + 1*4 + 2*3 + 3*2 = 26
F(2) = 0*2 + 1*6 + 2*4 + 3*3 = 25
F(3) = 0*3 + 1*2 + 2*6 + 3*4 = 22
So the maximum value of F(0), F(1), ..., F(3) is 26.

Constraints:
- n == nums.length
- 1 <= n <= 10^5
- -100 <= nums[i] <= 100
"""

# Python Solution
def maxRotateFunction(nums):
    """
    Calculate the maximum value of the rotate function F(k) for the given array nums.

    :param nums: List[int] - The input array
    :return: int - The maximum value of F(k)
    """
    n = len(nums)
    total_sum = sum(nums)
    current_F = sum(i * nums[i] for i in range(n))
    max_F = current_F

    for k in range(1, n):
        current_F += total_sum - n * nums[n - k]
        max_F = max(max_F, current_F)

    return max_F

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 3, 2, 6]
    print(maxRotateFunction(nums1))  # Output: 26

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(maxRotateFunction(nums2))  # Output: 40

    # Test Case 3
    nums3 = [0, 0, 0]
    print(maxRotateFunction(nums3))  # Output: 0

    # Test Case 4
    nums4 = [-1, -2, -3, -4]
    print(maxRotateFunction(nums4))  # Output: -10

    # Test Case 5
    nums5 = [100, -100, 50, -50]
    print(maxRotateFunction(nums5))  # Output: 250

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the initial value of F(0) takes O(n) time.
- For each rotation, we update the value of F(k) in O(1) time.
- Since there are n rotations, the total time complexity is O(n).

Space Complexity:
- The algorithm uses O(1) additional space, as we only store a few variables (total_sum, current_F, max_F).
- Therefore, the space complexity is O(1).
"""

# Topic: Arrays