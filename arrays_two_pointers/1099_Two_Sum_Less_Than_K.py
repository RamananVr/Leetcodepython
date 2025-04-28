"""
LeetCode Problem #1099: Two Sum Less Than K

Problem Statement:
Given an array `nums` of integers and an integer `k`, return the maximum sum such that there exists `i < j` with `nums[i] + nums[j] < k`. If no such `i, j` exists, return `-1`.

Example 1:
Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 23 to sum 57 which is less than 60. The maximum is 58.

Example 2:
Input: nums = [10,20,30], k = 15
Output: -1
Explanation: In this case, no two numbers sum less than 15, so we return -1.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 1000
- 1 <= k <= 2000
"""

# Clean and Correct Python Solution
def twoSumLessThanK(nums, k):
    """
    Finds the maximum sum of two numbers in the array such that their sum is less than k.

    :param nums: List[int] - List of integers
    :param k: int - Target integer
    :return: int - Maximum sum less than k, or -1 if no such pair exists
    """
    nums.sort()  # Sort the array to use two-pointer technique
    left, right = 0, len(nums) - 1
    max_sum = -1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum < k:
            max_sum = max(max_sum, current_sum)
            left += 1  # Move the left pointer to try a larger sum
        else:
            right -= 1  # Move the right pointer to try a smaller sum

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [34, 23, 1, 24, 75, 33, 54, 8]
    k1 = 60
    print(twoSumLessThanK(nums1, k1))  # Expected Output: 58

    # Test Case 2
    nums2 = [10, 20, 30]
    k2 = 15
    print(twoSumLessThanK(nums2, k2))  # Expected Output: -1

    # Test Case 3
    nums3 = [5, 1, 2, 3, 4]
    k3 = 10
    print(twoSumLessThanK(nums3, k3))  # Expected Output: 9

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    k4 = 8
    print(twoSumLessThanK(nums4, k4))  # Expected Output: 7

    # Test Case 5
    nums5 = [100, 200, 300]
    k5 = 500
    print(twoSumLessThanK(nums5, k5))  # Expected Output: 400

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The two-pointer traversal takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation is in-place, so no additional space is used apart from a few variables.
- Overall space complexity: O(1).
"""

# Topic: Arrays, Two Pointers