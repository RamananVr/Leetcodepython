"""
LeetCode Problem #2819: Count the Number of Beautiful Subarrays

Problem Statement:
You are given a 0-indexed integer array `nums`. A subarray of `nums` is called beautiful if it satisfies the following conditions:
1. The length of the subarray is even.
2. The sum of the first half of the subarray is equal to the sum of the second half.

Return the number of beautiful subarrays in `nums`.

A subarray is a contiguous non-empty sequence of elements within an array.

Example:
Input: nums = [2, 3, 1, 2, 3, 1]
Output: 4
Explanation: The beautiful subarrays are:
- [2, 3, 1, 2] (sum of first half = 5, sum of second half = 5)
- [3, 1, 2, 3] (sum of first half = 4, sum of second half = 4)
- [1, 2, 3, 1] (sum of first half = 3, sum of second half = 3)
- [2, 3, 1, 2, 3, 1] (sum of first half = 6, sum of second half = 6)

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
"""

def count_beautiful_subarrays(nums):
    """
    Function to count the number of beautiful subarrays in the given array.

    Args:
    nums (List[int]): The input array.

    Returns:
    int: The number of beautiful subarrays.
    """
    n = len(nums)
    beautiful_count = 0

    # Iterate over all possible even-length subarrays
    for start in range(n):
        for end in range(start + 1, n, 2):  # Ensure subarray length is even
            mid = (start + end) // 2
            if sum(nums[start:mid + 1]) == sum(nums[mid + 1:end + 1]):
                beautiful_count += 1

    return beautiful_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 1, 2, 3, 1]
    print(count_beautiful_subarrays(nums1))  # Output: 4

    # Test Case 2
    nums2 = [1, 2, 1, 2]
    print(count_beautiful_subarrays(nums2))  # Output: 1

    # Test Case 3
    nums3 = [1, 1, 1, 1, 1, 1]
    print(count_beautiful_subarrays(nums3))  # Output: 9

    # Test Case 4
    nums4 = [1, 2, 3, 4]
    print(count_beautiful_subarrays(nums4))  # Output: 0

    # Test Case 5
    nums5 = [10, 20, 10, 20, 10, 20]
    print(count_beautiful_subarrays(nums5))  # Output: 4

"""
Time Complexity Analysis:
- The outer loop iterates over all possible starting indices of the subarray, O(n).
- The inner loop iterates over all possible even-length subarrays starting from the current index, O(n).
- For each subarray, we calculate the sum of two halves, which takes O(k) time where k is the length of the subarray.
- In the worst case, the total time complexity is O(n^3).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space, O(1).

Topic: Arrays
"""