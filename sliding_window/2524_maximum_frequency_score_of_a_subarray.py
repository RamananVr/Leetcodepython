"""
LeetCode Question #2524: Maximum Frequency Score of a Subarray

Problem Statement:
You are given an integer array `nums` and an integer `k`. A subarray of `nums` is a contiguous non-empty sequence of elements within `nums`.

The frequency score of a subarray is defined as the sum of the squares of the frequencies of each unique element in the subarray. For example, if the subarray is `[1, 2, 2, 3]`, the frequency score is `1^2 + 2^2 + 1^2 = 6`.

Return the maximum frequency score of any subarray of size `k`.

Constraints:
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`
"""

from collections import defaultdict

def maxFrequencyScore(nums, k):
    """
    Function to calculate the maximum frequency score of any subarray of size k.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The size of the subarray.

    Returns:
    int: The maximum frequency score of any subarray of size k.
    """
    # Dictionary to store the frequency of elements in the current window
    freq = defaultdict(int)
    current_score = 0
    max_score = 0

    # Initialize the first window of size k
    for i in range(k):
        freq[nums[i]] += 1
        current_score += freq[nums[i]] ** 2 - (freq[nums[i]] - 1) ** 2

    max_score = current_score

    # Slide the window across the array
    for i in range(k, len(nums)):
        # Add the new element to the window
        freq[nums[i]] += 1
        current_score += freq[nums[i]] ** 2 - (freq[nums[i]] - 1) ** 2

        # Remove the element that is sliding out of the window
        freq[nums[i - k]] -= 1
        current_score += freq[nums[i - k]] ** 2 - (freq[nums[i - k]] + 1) ** 2

        # Update the maximum score
        max_score = max(max_score, current_score)

    return max_score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 2, 3]
    k1 = 3
    print(maxFrequencyScore(nums1, k1))  # Expected Output: 6

    # Test Case 2
    nums2 = [1, 1, 1, 1]
    k2 = 2
    print(maxFrequencyScore(nums2, k2))  # Expected Output: 4

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    k3 = 2
    print(maxFrequencyScore(nums3, k3))  # Expected Output: 2

    # Test Case 4
    nums4 = [1, 2, 2, 1, 3, 3, 3]
    k4 = 4
    print(maxFrequencyScore(nums4, k4))  # Expected Output: 14

"""
Time Complexity Analysis:
- The algorithm uses a sliding window approach, where each element is added and removed from the frequency dictionary exactly once.
- Calculating the frequency score for each element involves constant time operations.
- Therefore, the time complexity is O(n), where n is the length of the input array `nums`.

Space Complexity Analysis:
- The space complexity is O(u), where u is the number of unique elements in the array `nums`.
- In the worst case, u can be equal to the size of the array, so the space complexity is O(n).

Topic: Sliding Window
"""