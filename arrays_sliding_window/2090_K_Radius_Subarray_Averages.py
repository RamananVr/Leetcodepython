"""
LeetCode Problem #2090: K Radius Subarray Averages

Problem Statement:
You are given a 0-indexed array `nums` of `n` integers, and an integer `k`.

The `k-radius average` for a subarray of `nums` centered at some index `i` with the radius `k` is the average of all elements in the subarray of length `2k + 1` where the subarray is centered at `i`. The subarray must exist entirely within the bounds of the array. If there is no such subarray, the `k-radius average` is `-1`.

Build and return an array `result` of length `n` where `result[i]` is the `k-radius average` for the subarray centered at index `i`.

The average of `x` elements is the sum of the `x` elements divided by `x`, using integer division. The integer division truncates toward zero, which means losing its fractional part.

For example, the integer division of `4/3 = 1` and `-4/3 = -1`.

Constraints:
- `n == nums.length`
- `1 <= n <= 10^5`
- 0 <= nums[i] <= 10^5
- 0 <= k <= n // 2
"""

# Python Solution
from typing import List

def getAverages(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    result = [-1] * n  # Initialize the result array with -1
    window_size = 2 * k + 1  # The size of the sliding window

    if window_size > n:
        return result  # If the window size is larger than the array, return all -1s

    # Calculate the sum of the first window
    window_sum = sum(nums[:window_size])

    # Iterate through the array and calculate the k-radius averages
    for i in range(k, n - k):
        result[i] = window_sum // window_size  # Compute the average using integer division
        if i + k + 1 < n:  # Slide the window to the right
            window_sum += nums[i + k + 1] - nums[i - k]

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [7, 4, 3, 9, 1, 8, 5, 2, 6]
    k1 = 3
    print(getAverages(nums1, k1))  # Expected: [-1, -1, -1, 5, 4, 4, -1, -1, -1]

    # Test Case 2
    nums2 = [100000]
    k2 = 0
    print(getAverages(nums2, k2))  # Expected: [100000]

    # Test Case 3
    nums3 = [8, 2, 4, 6, 10]
    k3 = 2
    print(getAverages(nums3, k3))  # Expected: [-1, -1, 6, -1, -1]

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    k4 = 1
    print(getAverages(nums4, k4))  # Expected: [-1, 2, 3, 4, -1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the sum of the first window takes O(window_size) = O(2k + 1).
- Sliding the window across the array takes O(n) since we add one element and remove one element for each step.
- Overall time complexity: O(n).

Space Complexity:
- The space complexity is O(1) for the sliding window sum and O(n) for the result array.
- Overall space complexity: O(n).
"""

# Topic: Arrays, Sliding Window