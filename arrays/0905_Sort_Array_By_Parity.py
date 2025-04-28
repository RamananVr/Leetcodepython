"""
LeetCode Problem #905: Sort Array By Parity

Problem Statement:
Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], etc. would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
- 1 <= nums.length <= 5000
- 0 <= nums[i] <= 10^4
"""

# Solution
def sortArrayByParity(nums):
    """
    Sorts the array by parity, placing even numbers first followed by odd numbers.

    :param nums: List[int] - The input array of integers.
    :return: List[int] - The array sorted by parity.
    """
    return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 != 0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 1, 2, 4]
    print(sortArrayByParity(nums1))  # Output: [2, 4, 3, 1] (or any valid permutation)

    # Test Case 2
    nums2 = [0]
    print(sortArrayByParity(nums2))  # Output: [0]

    # Test Case 3
    nums3 = [1, 3, 5, 7]
    print(sortArrayByParity(nums3))  # Output: [1, 3, 5, 7] (no even numbers)

    # Test Case 4
    nums4 = [2, 4, 6, 8]
    print(sortArrayByParity(nums4))  # Output: [2, 4, 6, 8] (all even numbers)

    # Test Case 5
    nums5 = [5, 2, 9, 4, 7, 6]
    print(sortArrayByParity(nums5))  # Output: [2, 4, 6, 5, 9, 7] (or any valid permutation)

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the array twice: once to collect even numbers and once to collect odd numbers.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The solution creates two new lists to store even and odd numbers, which together have a size equal to the input array.
- Therefore, the space complexity is O(n).
"""

# Topic: Arrays