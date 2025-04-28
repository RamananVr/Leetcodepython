"""
LeetCode Problem #2886: Find the Maximum Sum of a Subarray with a Fixed Length

Problem Statement:
You are given an integer array `nums` and an integer `k`. Your task is to find the maximum sum of any subarray of length `k`.

A subarray is a contiguous part of an array. Return the maximum sum of any subarray of length `k`.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
"""

def max_sum_subarray(nums, k):
    """
    Finds the maximum sum of any subarray of length k.

    :param nums: List[int] - The input array of integers.
    :param k: int - The fixed length of the subarray.
    :return: int - The maximum sum of any subarray of length k.
    """
    # Initialize the sum of the first window and the maximum sum
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # Use a sliding window to calculate the sum of subarrays of length k
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    k1 = 2
    print(max_sum_subarray(nums1, k1))  # Expected Output: 9 (subarray [4, 5])

    # Test Case 2
    nums2 = [2, 1, 5, 1, 3, 2]
    k2 = 3
    print(max_sum_subarray(nums2, k2))  # Expected Output: 9 (subarray [5, 1, 3])

    # Test Case 3
    nums3 = [-1, -2, -3, -4, -5]
    k3 = 2
    print(max_sum_subarray(nums3, k3))  # Expected Output: -3 (subarray [-1, -2])

    # Test Case 4
    nums4 = [10, -2, 3, 1, 5, -1]
    k4 = 4
    print(max_sum_subarray(nums4, k4))  # Expected Output: 17 (subarray [10, -2, 3, 1])

    # Test Case 5
    nums5 = [1]
    k5 = 1
    print(max_sum_subarray(nums5, k5))  # Expected Output: 1 (subarray [1])

"""
Time Complexity Analysis:
- Calculating the sum of the first `k` elements takes O(k).
- Sliding the window across the array takes O(n - k), where `n` is the length of the array.
- Overall, the time complexity is O(n).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Sliding Window
"""