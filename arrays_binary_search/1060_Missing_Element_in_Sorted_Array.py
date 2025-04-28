"""
LeetCode Problem #1060: Missing Element in Sorted Array

Problem Statement:
Given an integer array `nums` which is sorted in ascending order and all of its elements are unique, return the `k-th` missing number starting from the leftmost number of the array.

Example 1:
Input: nums = [4,7,9,10], k = 1
Output: 5
Explanation: The first missing number is 5.

Example 2:
Input: nums = [4,7,9,10], k = 3
Output: 8
Explanation: The missing numbers are [5,6,8], and the 3rd missing number is 8.

Example 3:
Input: nums = [1,2,4], k = 3
Output: 6
Explanation: The missing numbers are [3,5,6], and the 3rd missing number is 6.

Constraints:
- 1 <= nums.length <= 5 * 10^4
- 1 <= nums[i] <= 10^7
- nums is sorted in ascending order, and all the elements are unique.
- 1 <= k <= 10^8
"""

# Solution
def missingElement(nums, k):
    """
    Finds the k-th missing number in a sorted array.

    :param nums: List[int] - Sorted array of unique integers
    :param k: int - The k-th missing number to find
    :return: int - The k-th missing number
    """
    def missing_count(idx):
        # Helper function to calculate the number of missing numbers up to index idx
        return nums[idx] - nums[0] - idx

    n = len(nums)
    
    # If the k-th missing number is beyond the last element of the array
    if k > missing_count(n - 1):
        return nums[-1] + (k - missing_count(n - 1))
    
    # Binary search to find the smallest index where missing_count(idx) >= k
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if missing_count(mid) < k:
            left = mid + 1
        else:
            right = mid
    
    # The k-th missing number is between nums[left - 1] and nums[left]
    return nums[left - 1] + (k - missing_count(left - 1))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 7, 9, 10]
    k1 = 1
    print(missingElement(nums1, k1))  # Output: 5

    # Test Case 2
    nums2 = [4, 7, 9, 10]
    k2 = 3
    print(missingElement(nums2, k2))  # Output: 8

    # Test Case 3
    nums3 = [1, 2, 4]
    k3 = 3
    print(missingElement(nums3, k3))  # Output: 6

    # Test Case 4
    nums4 = [1, 3, 5, 7]
    k4 = 5
    print(missingElement(nums4, k4))  # Output: 9

    # Test Case 5
    nums5 = [10, 20, 30]
    k5 = 15
    print(missingElement(nums5, k5))  # Output: 45

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search runs in O(log n), where n is the length of the array.
- The missing_count function is O(1), as it involves simple arithmetic.
- Overall, the time complexity is O(log n).

Space Complexity:
- The algorithm uses O(1) additional space, as it only uses a few variables for computation.
- Therefore, the space complexity is O(1).

Topic: Arrays, Binary Search
"""