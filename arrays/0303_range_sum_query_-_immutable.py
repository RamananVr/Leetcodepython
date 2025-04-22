"""
LeetCode Question #303: Range Sum Query - Immutable

Problem Statement:
Given an integer array `nums`, handle multiple queries of the following type:
- Calculate the sum of the elements of `nums` between indices `left` and `right` inclusive, where `left <= right`.

Implement the `NumArray` class:
- `NumArray(int[] nums)` Initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)` Returns the sum of the elements of `nums` between indices `left` and `right` inclusive (i.e., `nums[left] + nums[left + 1] + ... + nums[right]`).

Example:
Input:
    ["NumArray", "sumRange", "sumRange", "sumRange"]
    [[[1, 2, 3, 4, 5]], [0, 2], [1, 3], [0, 4]]
Output:
    [null, 6, 9, 15]

Explanation:
    NumArray numArray = new NumArray([1, 2, 3, 4, 5]);
    numArray.sumRange(0, 2); // return 6 (1 + 2 + 3)
    numArray.sumRange(1, 3); // return 9 (2 + 3 + 4)
    numArray.sumRange(0, 4); // return 15 (1 + 2 + 3 + 4 + 5)
"""

# Python Solution
class NumArray:
    def __init__(self, nums):
        """
        Initialize the NumArray object with the given integer array `nums`.
        Precompute the prefix sum array to allow efficient range sum queries.
        """
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left, right):
        """
        Return the sum of the elements of `nums` between indices `left` and `right` inclusive.
        """
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# Example Test Cases
if __name__ == "__main__":
    # Initialize the NumArray object
    numArray = NumArray([1, 2, 3, 4, 5])

    # Test cases
    print(numArray.sumRange(0, 2))  # Output: 6 (1 + 2 + 3)
    print(numArray.sumRange(1, 3))  # Output: 9 (2 + 3 + 4)
    print(numArray.sumRange(0, 4))  # Output: 15 (1 + 2 + 3 + 4 + 5)

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Initialization (`__init__`): O(n), where `n` is the length of the input array `nums`. This is because we compute the prefix sum array in a single pass.
   - Query (`sumRange`): O(1), as we simply perform two lookups and a subtraction in the prefix sum array.

2. Space Complexity:
   - O(n), where `n` is the length of the input array `nums`. This is due to the storage of the prefix sum array.

Topic: Arrays
"""