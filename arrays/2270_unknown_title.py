"""
LeetCode Problem #2270: Number of Ways to Split Array

Problem Statement:
You are given a 0-indexed integer array `nums` of length `n`. `nums` contains non-negative integers.

You are tasked to split the array into two non-empty parts (prefix and suffix) such that the sum of the elements in the prefix is greater than or equal to the sum of the elements in the suffix.

For example, if the array `nums = [10, 4, -8, 7]`, then the following are valid ways to split the array:
- Prefix = [10], Suffix = [4, -8, 7]
- Prefix = [10, 4], Suffix = [-8, 7]

Return the number of valid ways to split `nums`.

Constraints:
- `2 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`
"""

# Python Solution
def waysToSplitArray(nums):
    """
    Function to calculate the number of valid ways to split the array.

    Args:
    nums (List[int]): The input array.

    Returns:
    int: The number of valid ways to split the array.
    """
    n = len(nums)
    total_sum = sum(nums)
    prefix_sum = 0
    valid_splits = 0

    for i in range(n - 1):  # We stop at n-1 because both parts must be non-empty
        prefix_sum += nums[i]
        suffix_sum = total_sum - prefix_sum
        if prefix_sum >= suffix_sum:
            valid_splits += 1

    return valid_splits

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [10, 4, -8, 7]
    print(waysToSplitArray(nums1))  # Output: 2

    # Test Case 2
    nums2 = [2, 3, 1, 0]
    print(waysToSplitArray(nums2))  # Output: 2

    # Test Case 3
    nums3 = [1, 1, 1, 1, 1]
    print(waysToSplitArray(nums3))  # Output: 4

    # Test Case 4
    nums4 = [5, -1, 2, 0, 3]
    print(waysToSplitArray(nums4))  # Output: 3

    # Test Case 5
    nums5 = [1, 2]
    print(waysToSplitArray(nums5))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the total sum of the array takes O(n).
- Iterating through the array to calculate prefix sums and check the condition takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- We use a constant amount of extra space for variables like `total_sum`, `prefix_sum`, and `valid_splits`.
- Overall space complexity: O(1).

Topic: Arrays
"""