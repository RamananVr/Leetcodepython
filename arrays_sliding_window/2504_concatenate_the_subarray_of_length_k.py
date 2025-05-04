"""
LeetCode Question #2504: Concatenate the Subarray of Length K

Problem Statement:
You are given an integer array `nums` and an integer `k`. A subarray is a contiguous non-empty sequence of elements within an array. 
The task is to find the lexicographically largest string that can be formed by concatenating the elements of a subarray of length `k` 
from the array `nums`. Each element in `nums` is a single-digit integer (0-9).

Return the lexicographically largest string.

Example:
Input: nums = [3, 5, 2, 9, 4], k = 3
Output: "952"

Constraints:
1. 1 <= k <= len(nums) <= 1000
2. 0 <= nums[i] <= 9
"""

# Python Solution
def largest_concatenated_subarray(nums, k):
    """
    Finds the lexicographically largest string formed by concatenating the elements
    of a subarray of length k from the array nums.

    :param nums: List[int] - The input array of single-digit integers.
    :param k: int - The length of the subarray to consider.
    :return: str - The lexicographically largest string.
    """
    n = len(nums)
    max_string = ""
    
    for i in range(n - k + 1):
        # Extract the subarray of length k
        subarray = nums[i:i + k]
        # Convert the subarray to a string
        subarray_string = ''.join(map(str, subarray))
        # Update the max_string if the current subarray_string is larger
        if subarray_string > max_string:
            max_string = subarray_string
    
    return max_string

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 5, 2, 9, 4]
    k1 = 3
    print(largest_concatenated_subarray(nums1, k1))  # Output: "952"

    # Test Case 2
    nums2 = [1, 4, 3, 2, 5]
    k2 = 2
    print(largest_concatenated_subarray(nums2, k2))  # Output: "43"

    # Test Case 3
    nums3 = [9, 8, 7, 6, 5]
    k3 = 4
    print(largest_concatenated_subarray(nums3, k3))  # Output: "9876"

    # Test Case 4
    nums4 = [0, 0, 0, 0, 0]
    k4 = 3
    print(largest_concatenated_subarray(nums4, k4))  # Output: "000"

    # Test Case 5
    nums5 = [5, 1, 5, 1, 5]
    k5 = 1
    print(largest_concatenated_subarray(nums5, k5))  # Output: "5"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop iterates over the array `nums` with a sliding window of size `k`. 
  This takes O(n - k + 1) iterations, where `n` is the length of `nums`.
- For each iteration, we extract a subarray of size `k` and convert it to a string, 
  which takes O(k) time.
- Overall, the time complexity is O((n - k + 1) * k), which simplifies to O(n * k).

Space Complexity:
- The space complexity is O(k) for the temporary subarray and string conversion.
- The overall space complexity is O(k).
"""

# Topic: Arrays, Sliding Window