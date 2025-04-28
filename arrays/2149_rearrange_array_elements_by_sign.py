"""
LeetCode Question #2149: Rearrange Array Elements by Sign

Problem Statement:
You are given a 0-indexed integer array `nums` of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of `nums` such that the modified array follows these conditions:
1. Every consecutive pair of integers have opposite signs.
2. For all integers with the same sign, the order in which they were present in `nums` is preserved.

The rearranged array should be returned.

Example 1:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
- The positive integers in nums are [3,1,2].
- The negative integers in nums are [-2,-5,-4].
- The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].

Example 2:
Input: nums = [-1,1]
Output: [1,-1]
Explanation:
- The positive integers in nums are [1].
- The negative integers in nums are [-1].
- The only possible way to rearrange them such that they satisfy all conditions is [1,-1].

Constraints:
- 2 <= nums.length <= 2 * 10^5
- nums.length is even.
- 1 <= |nums[i]| <= 10^5
- nums consists of equal number of positive and negative integers.
"""

# Python Solution
def rearrangeArray(nums):
    """
    Rearranges the array such that every consecutive pair of integers have opposite signs
    while preserving the relative order of positive and negative integers.

    :param nums: List[int] - Input array of integers
    :return: List[int] - Rearranged array
    """
    # Separate positive and negative numbers
    positives = [num for num in nums if num > 0]
    negatives = [num for num in nums if num < 0]

    # Interleave positive and negative numbers
    result = []
    for p, n in zip(positives, negatives):
        result.append(p)
        result.append(n)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 1, -2, -5, 2, -4]
    print(rearrangeArray(nums1))  # Output: [3, -2, 1, -5, 2, -4]

    # Test Case 2
    nums2 = [-1, 1]
    print(rearrangeArray(nums2))  # Output: [1, -1]

    # Test Case 3
    nums3 = [4, -3, 2, -1, 6, -5]
    print(rearrangeArray(nums3))  # Output: [4, -3, 2, -1, 6, -5]

    # Test Case 4
    nums4 = [10, -10, 20, -20, 30, -30]
    print(rearrangeArray(nums4))  # Output: [10, -10, 20, -20, 30, -30]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Separating positive and negative numbers takes O(n), where n is the length of the input array.
- Interleaving the two lists also takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- We use two additional lists to store positive and negative numbers, each of size n/2.
- The result list also takes O(n) space.
- Overall space complexity: O(n).

Topic: Arrays
"""