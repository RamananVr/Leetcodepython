"""
LeetCode Problem #775: Global and Local Inversions

Problem Statement:
You are given an integer array `nums` where `nums` is a permutation of the first `n` positive integers.
You need to determine if the number of global inversions is equal to the number of local inversions.

A global inversion is defined as a pair `(i, j)` where:
- `0 <= i < j < n`
- `nums[i] > nums[j]`

A local inversion is defined as a pair `(i, i+1)` where:
- `0 <= i < n-1`
- `nums[i] > nums[i+1]`

Return `true` if the number of global inversions is equal to the number of local inversions, otherwise return `false`.

Constraints:
- `n == nums.length`
- `1 <= n <= 10^5`
- All the integers of `nums` are unique and in the range `[1, n]`.

Example 1:
Input: nums = [1, 0, 2]
Output: true

Example 2:
Input: nums = [1, 2, 0]
Output: false

Follow-up:
Can you solve the problem in O(n) time complexity?
"""

def isIdealPermutation(nums):
    """
    Determines if the number of global inversions is equal to the number of local inversions.

    Args:
    nums (List[int]): A permutation of the first n positive integers.

    Returns:
    bool: True if the number of global inversions equals the number of local inversions, False otherwise.
    """
    for i in range(len(nums)):
        # Check if any number is more than 1 position away from its original position
        if abs(nums[i] - i) > 1:
            return False
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 0, 2]
    print(isIdealPermutation(nums1))  # Output: True

    # Test Case 2
    nums2 = [1, 2, 0]
    print(isIdealPermutation(nums2))  # Output: False

    # Test Case 3
    nums3 = [0, 1, 2, 3]
    print(isIdealPermutation(nums3))  # Output: True

    # Test Case 4
    nums4 = [2, 0, 1]
    print(isIdealPermutation(nums4))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the array once, performing a constant-time check for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The function uses only a constant amount of extra space (no additional data structures are used).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""