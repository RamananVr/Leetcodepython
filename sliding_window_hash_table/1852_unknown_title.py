"""
LeetCode Problem #1852: Distinct Numbers in Each Subarray

Problem Statement:
You are given an integer array `nums` and an integer `k`. Find the number of distinct integers in each sliding window of size `k` and return an array of these numbers.

The sliding window moves from the very left of the array to the very right. A sliding window is a subarray of length `k` where we only consider the elements in the window. Each time the sliding window moves right by one position.

Return the result as an array.

Example 1:
Input: nums = [1,2,3,2,2,1,4,5], k = 3
Output: [3,2,2,2,3,3]

Example 2:
Input: nums = [1,1,1,1,1], k = 1
Output: [1,1,1,1,1]

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
- 1 <= k <= nums.length
"""

from collections import Counter

def distinctNumbers(nums, k):
    """
    Function to calculate the number of distinct integers in each sliding window of size k.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The size of the sliding window.

    Returns:
    List[int]: A list of integers representing the number of distinct integers in each sliding window.
    """
    # Initialize the result list and a Counter to track the frequency of elements in the current window
    result = []
    window_count = Counter(nums[:k])  # Count the first window of size k
    result.append(len(window_count))  # Add the count of distinct elements in the first window

    # Slide the window across the array
    for i in range(k, len(nums)):
        # Remove the element that is sliding out of the window
        outgoing = nums[i - k]
        window_count[outgoing] -= 1
        if window_count[outgoing] == 0:
            del window_count[outgoing]

        # Add the new element that is sliding into the window
        incoming = nums[i]
        window_count[incoming] += 1

        # Append the count of distinct elements in the current window
        result.append(len(window_count))

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 2, 2, 1, 4, 5]
    k1 = 3
    print(distinctNumbers(nums1, k1))  # Output: [3, 2, 2, 2, 3, 3]

    # Test Case 2
    nums2 = [1, 1, 1, 1, 1]
    k2 = 1
    print(distinctNumbers(nums2, k2))  # Output: [1, 1, 1, 1, 1]

    # Test Case 3
    nums3 = [4, 5, 6, 7, 8, 9]
    k3 = 2
    print(distinctNumbers(nums3, k3))  # Output: [2, 2, 2, 2, 2]

    # Test Case 4
    nums4 = [1, 2, 1, 3, 4, 2, 3]
    k4 = 4
    print(distinctNumbers(nums4, k4))  # Output: [3, 4, 4, 3]

# Time Complexity Analysis:
# - The sliding window is processed in O(n) time, where n is the length of the array `nums`.
# - Each operation on the Counter (increment, decrement, and deletion) is O(1) on average.
# - Thus, the overall time complexity is O(n).

# Space Complexity Analysis:
# - The Counter stores at most `k` elements at any time, so the space complexity is O(k).
# - The result list requires O(n) space to store the output.
# - Therefore, the total space complexity is O(n + k).

# Topic: Sliding Window, Hash Table