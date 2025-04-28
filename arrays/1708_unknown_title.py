"""
LeetCode Problem #1708: Largest Subarray Length K

Problem Statement:
You are given an integer array `nums` and an integer `k`. Find the largest subarray of length `k` and return it.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1, 4, 5, 2, 3], k = 3
Output: [5, 2, 3]
Explanation: The subarrays of length 3 are:
- [1, 4, 5]
- [4, 5, 2]
- [5, 2, 3]
Among these, [5, 2, 3] is the largest.

Example 2:
Input: nums = [1, 4, 5, 2, 3], k = 4
Output: [4, 5, 2, 3]
Explanation: The subarrays of length 4 are:
- [1, 4, 5, 2]
- [4, 5, 2, 3]
Among these, [4, 5, 2, 3] is the largest.

Constraints:
- 1 <= k <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

# Solution
def largest_subarray(nums, k):
    """
    Finds the largest subarray of length k.

    Args:
    nums (List[int]): The input array.
    k (int): The length of the subarray.

    Returns:
    List[int]: The largest subarray of length k.
    """
    # Initialize the starting index of the largest subarray
    max_start = 0
    
    # Iterate through the array to find the starting index of the largest subarray
    for i in range(1, len(nums) - k + 1):
        # Compare the current subarray starting at index i with the current largest subarray
        if nums[i:i + k] > nums[max_start:max_start + k]:
            max_start = i
    
    # Return the largest subarray
    return nums[max_start:max_start + k]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 4, 5, 2, 3]
    k1 = 3
    print(largest_subarray(nums1, k1))  # Output: [5, 2, 3]

    # Test Case 2
    nums2 = [1, 4, 5, 2, 3]
    k2 = 4
    print(largest_subarray(nums2, k2))  # Output: [4, 5, 2, 3]

    # Test Case 3
    nums3 = [10, 20, 30, 40, 50]
    k3 = 2
    print(largest_subarray(nums3, k3))  # Output: [40, 50]

    # Test Case 4
    nums4 = [5, 5, 5, 5, 5]
    k4 = 3
    print(largest_subarray(nums4, k4))  # Output: [5, 5, 5]

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5]
    k5 = 1
    print(largest_subarray(nums5, k5))  # Output: [5]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once, comparing subarrays of length k.
- Each comparison takes O(k) time.
- Therefore, the overall time complexity is O((n - k) * k), where n is the length of the array.
- However, in practice, slicing and comparing subarrays can be optimized by comparing elements directly, reducing the complexity to O(n).

Space Complexity:
- The algorithm uses O(1) additional space since it only stores indices and does not create new data structures.
- The output subarray is a slice of the input array, which does not require extra space.
- Therefore, the space complexity is O(1).
"""

# Topic: Arrays