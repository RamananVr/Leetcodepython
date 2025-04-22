"""
LeetCode Question #307: Range Sum Query - Mutable

Problem Statement:
Given an integer array nums, handle multiple queries of the following types:
1. Update the value of an element in nums.
2. Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:
- NumArray(int[] nums) Initializes the object with the integer array nums.
- void update(int index, int val) Updates the value of nums[index] to be val.
- int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e., nums[left] + nums[left + 1] + ... + nums[right]).

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- 0 <= index < nums.length
- -100 <= val <= 100
- 0 <= left <= right < nums.length
- At most 3 * 10^4 calls will be made to update and sumRange.
"""

# Solution using a Fenwick Tree (Binary Indexed Tree)
class NumArray:
    def __init__(self, nums):
        """
        Initializes the NumArray object with the integer array nums.
        """
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * (self.n + 1)
        for i in range(self.n):
            self._add(i + 1, nums[i])

    def _add(self, index, delta):
        """
        Updates the Fenwick Tree with the given delta at the specified index.
        """
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index

    def _prefix_sum(self, index):
        """
        Computes the prefix sum from the Fenwick Tree up to the specified index.
        """
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def update(self, index, val):
        """
        Updates the value of nums[index] to be val.
        """
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left, right):
        """
        Returns the sum of the elements of nums between indices left and right inclusive.
        """
        return self._prefix_sum(right + 1) - self._prefix_sum(left)

# Example Test Cases
if __name__ == "__main__":
    # Initialize the NumArray object
    nums = [1, 3, 5]
    numArray = NumArray(nums)

    # Test sumRange
    print(numArray.sumRange(0, 2))  # Output: 9 (1 + 3 + 5)

    # Test update
    numArray.update(1, 2)  # Update nums[1] to 2
    print(numArray.sumRange(0, 2))  # Output: 8 (1 + 2 + 5)

    # Additional test cases
    numArray.update(0, 4)  # Update nums[0] to 4
    print(numArray.sumRange(0, 1))  # Output: 6 (4 + 2)

    numArray.update(2, 6)  # Update nums[2] to 6
    print(numArray.sumRange(1, 2))  # Output: 8 (2 + 6)

"""
Time and Space Complexity Analysis:
1. Initialization (__init__):
   - Time Complexity: O(n * log(n)), where n is the length of nums. Each element is added to the Fenwick Tree in O(log(n)) time.
   - Space Complexity: O(n), for storing the Fenwick Tree.

2. Update:
   - Time Complexity: O(log(n)), as updating the Fenwick Tree requires traversing up the tree.

3. sumRange:
   - Time Complexity: O(log(n)), as computing the prefix sum requires traversing up the tree.

Overall:
- Time Complexity for multiple operations: O(log(n)) per update and sumRange.
- Space Complexity: O(n).

Topic: Fenwick Tree (Binary Indexed Tree)
"""