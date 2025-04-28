"""
LeetCode Problem #2441: Largest Positive Integer That Exists With Its Negative

Problem Statement:
Given an integer array `nums` that does not contain any zeros, find the largest positive integer `k` such that `-k` also exists in the array. 
Return the positive integer `k`. If there is no such integer, return -1.

Example 1:
Input: nums = [-1, 2, -3, 3]
Output: 3
Explanation: 3 is the largest positive integer that exists with its negative -3.

Example 2:
Input: nums = [-1, 10, 6, 7, -7, 1]
Output: 7
Explanation: 7 is the largest positive integer that exists with its negative -7.

Example 3:
Input: nums = [-10, 8, 6, 7, -2, -3]
Output: -1
Explanation: There is no positive integer that exists with its negative.

Constraints:
- 1 <= nums.length <= 1000
- -1000 <= nums[i] <= 1000
- nums[i] != 0
"""

# Python Solution
def findMaxK(nums):
    """
    Finds the largest positive integer k such that both k and -k exist in the array.

    :param nums: List[int] - List of integers
    :return: int - The largest positive integer k, or -1 if no such k exists
    """
    num_set = set(nums)
    max_k = -1

    for num in nums:
        if num > 0 and -num in num_set:
            max_k = max(max_k, num)

    return max_k

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [-1, 2, -3, 3]
    print(findMaxK(nums1))  # Output: 3

    # Test Case 2
    nums2 = [-1, 10, 6, 7, -7, 1]
    print(findMaxK(nums2))  # Output: 7

    # Test Case 3
    nums3 = [-10, 8, 6, 7, -2, -3]
    print(findMaxK(nums3))  # Output: -1

    # Test Case 4 (Edge Case: No valid k)
    nums4 = [1, 2, 3, 4]
    print(findMaxK(nums4))  # Output: -1

    # Test Case 5 (Edge Case: Single pair)
    nums5 = [5, -5]
    print(findMaxK(nums5))  # Output: 5

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the set from the input list takes O(n), where n is the length of the input list.
- Iterating through the list and checking for the existence of -num in the set takes O(n) in the worst case.
- Thus, the overall time complexity is O(n).

Space Complexity:
- The space complexity is O(n) due to the set used to store the elements of the input list.
"""

# Topic: Arrays, Hashing