"""
LeetCode Problem #2841: Maximum Sum of Almost Unique Subarray

Problem Statement:
You are given an integer array `nums` and two integers `m` and `k`. 
A subarray is called "almost unique" if it contains at most `m` distinct elements.

Return the maximum sum of any almost unique subarray of length `k`. 
If no such subarray exists, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
- `1 <= nums.length <= 2 * 10^4`
- `1 <= nums[i] <= 10^6`
- `1 <= m <= nums.length`
- `1 <= k <= nums.length`
"""

from collections import defaultdict

def max_sum_of_almost_unique_subarray(nums, m, k):
    """
    Finds the maximum sum of any almost unique subarray of length k.

    Args:
    nums (List[int]): The input array of integers.
    m (int): The maximum number of distinct elements allowed in the subarray.
    k (int): The required length of the subarray.

    Returns:
    int: The maximum sum of any almost unique subarray of length k, or 0 if no such subarray exists.
    """
    n = len(nums)
    if k > n:
        return 0

    # Sliding window variables
    window_sum = 0
    max_sum = 0
    freq = defaultdict(int)
    distinct_count = 0

    for i in range(n):
        # Add the current element to the window
        window_sum += nums[i]
        freq[nums[i]] += 1
        if freq[nums[i]] == 1:
            distinct_count += 1

        # Remove the element that is sliding out of the window
        if i >= k:
            window_sum -= nums[i - k]
            freq[nums[i - k]] -= 1
            if freq[nums[i - k]] == 0:
                distinct_count -= 1

        # Check if the current window is valid and update the max_sum
        if i >= k - 1 and distinct_count <= m:
            max_sum = max(max_sum, window_sum)

    return max_sum


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [1, 2, 1, 2, 3]
    m = 2
    k = 3
    print(max_sum_of_almost_unique_subarray(nums, m, k))  # Output: 6

    # Test Case 2
    nums = [4, 4, 4, 4]
    m = 1
    k = 2
    print(max_sum_of_almost_unique_subarray(nums, m, k))  # Output: 8

    # Test Case 3
    nums = [1, 2, 3, 4, 5]
    m = 3
    k = 3
    print(max_sum_of_almost_unique_subarray(nums, m, k))  # Output: 12

    # Test Case 4
    nums = [1, 2, 3, 4, 5]
    m = 1
    k = 3
    print(max_sum_of_almost_unique_subarray(nums, m, k))  # Output: 0

    # Test Case 5
    nums = [10, 20, 30, 40, 50]
    m = 2
    k = 2
    print(max_sum_of_almost_unique_subarray(nums, m, k))  # Output: 90


"""
Time Complexity:
- The algorithm uses a sliding window approach, where each element is added and removed from the window at most once.
- Maintaining the frequency dictionary takes O(1) per operation.
- Therefore, the overall time complexity is O(n), where n is the length of the input array `nums`.

Space Complexity:
- The space complexity is O(m), where m is the maximum number of distinct elements allowed in the subarray.
- This is because the frequency dictionary can store at most m distinct elements at any given time.

Topic: Sliding Window, Hash Table
"""