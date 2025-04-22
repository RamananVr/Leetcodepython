"""
LeetCode Problem #480: Sliding Window Median

Problem Statement:
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

- For example, `[2,3,4]`, the median is `3`.
- For example, `[2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Given an integer array `nums`, and an integer `k`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position, you need to output the median of the window.

You are required to implement the function `medianSlidingWindow(nums: List[int], k: int) -> List[float]`.

Constraints:
1. `1 <= k <= nums.length <= 10^5`
2. `-2^31 <= nums[i] <= 2^31 - 1`

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.0,-1.0,-1.0,3.0,5.0,6.0]
Explanation:
Window position                Median
---------------                -----
[1, 3, -1]                     1
[3, -1, -3]                    -1
[-1, -3, 5]                    -1
[-3, 5, 3]                     3
[5, 3, 6]                      5
[3, 6, 7]                      6

Example 2:
Input: nums = [1,2,3,4,2,3,1,4,2], k = 4
Output: [2.5, 3.0, 3.0, 2.5, 3.0, 2.5]

"""

from bisect import insort, bisect_left
from typing import List

def medianSlidingWindow(nums: List[int], k: int) -> List[float]:
    """
    Function to calculate the median of each sliding window of size k.
    """
    window = sorted(nums[:k])  # Initialize the first window
    medians = []

    for i in range(k, len(nums) + 1):
        # Calculate the median for the current window
        if k % 2 == 0:
            medians.append((window[k // 2 - 1] + window[k // 2]) / 2.0)
        else:
            medians.append(float(window[k // 2]))

        # Slide the window: remove the leftmost element and add the next element
        if i < len(nums):
            # Remove the element going out of the window
            out_idx = bisect_left(window, nums[i - k])
            window.pop(out_idx)
            # Add the new element into the window
            insort(window, nums[i])

    return medians

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3
    print(medianSlidingWindow(nums1, k1))  # Output: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]

    # Test Case 2
    nums2 = [1, 2, 3, 4, 2, 3, 1, 4, 2]
    k2 = 4
    print(medianSlidingWindow(nums2, k2))  # Output: [2.5, 3.0, 3.0, 2.5, 3.0, 2.5]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the initial window takes O(k log k).
- For each sliding window operation:
  - Removing an element from the sorted list takes O(log k) using `bisect_left`.
  - Inserting a new element into the sorted list takes O(log k) using `insort`.
- Since there are (n - k + 1) windows, the total time complexity is O(n log k).

Space Complexity:
- The space complexity is O(k) for storing the sliding window.

Topic: Arrays, Sliding Window, Sorting
"""