"""
LeetCode Problem #2461: Maximum Sum of Distinct Subarrays With Length K

Problem Statement:
You are given an integer array `nums` and an integer `k`. Find the maximum sum of any subarray of size `k` such that all the elements of the subarray are distinct.

Return the maximum sum of the subarray, or 0 if no such subarray exists.

Constraints:
- `1 <= k <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
"""

def maximumSubarraySum(nums, k):
    """
    Finds the maximum sum of any subarray of size k with distinct elements.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The size of the subarray.

    Returns:
    int: The maximum sum of a subarray of size k with distinct elements, or 0 if no such subarray exists.
    """
    from collections import defaultdict

    # Initialize variables
    max_sum = 0
    current_sum = 0
    window_start = 0
    freq_map = defaultdict(int)

    for window_end in range(len(nums)):
        # Add the current element to the window
        current_num = nums[window_end]
        freq_map[current_num] += 1
        current_sum += current_num

        # If the window size exceeds k, shrink it from the left
        if window_end - window_start + 1 > k:
            left_num = nums[window_start]
            freq_map[left_num] -= 1
            if freq_map[left_num] == 0:
                del freq_map[left_num]
            current_sum -= left_num
            window_start += 1

        # Check if the current window is valid (all elements are distinct)
        if window_end - window_start + 1 == k and len(freq_map) == k:
            max_sum = max(max_sum, current_sum)

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    k1 = 3
    print(maximumSubarraySum(nums1, k1))  # Expected Output: 12 (subarray [3, 4, 5])

    # Test Case 2
    nums2 = [4, 4, 4]
    k2 = 2
    print(maximumSubarraySum(nums2, k2))  # Expected Output: 0 (no valid subarray)

    # Test Case 3
    nums3 = [1, 2, 1, 2, 3]
    k3 = 3
    print(maximumSubarraySum(nums3, k3))  # Expected Output: 6 (subarray [1, 2, 3])

    # Test Case 4
    nums4 = [5, 9, 7, 9, 10]
    k4 = 2
    print(maximumSubarraySum(nums4, k4))  # Expected Output: 16 (subarray [7, 9] or [9, 10])

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5, 6]
    k5 = 6
    print(maximumSubarraySum(nums5, k5))  # Expected Output: 21 (subarray [1, 2, 3, 4, 5, 6])

"""
Time Complexity Analysis:
- The algorithm uses a sliding window approach, where each element is added to and removed from the window at most once.
- The operations on the frequency map (insertion, deletion, and lookup) are O(1) on average.
- Therefore, the overall time complexity is O(n), where n is the length of the input array `nums`.

Space Complexity Analysis:
- The space complexity is O(k), as the frequency map can store at most `k` distinct elements at any given time.

Topic: Sliding Window, Hash Map
"""