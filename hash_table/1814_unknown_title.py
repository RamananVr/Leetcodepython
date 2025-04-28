"""
LeetCode Problem #1814: Count Nice Pairs in an Array

Problem Statement:
You are given an array `nums` that consists of non-negative integers. Let `rev(x)` be the reverse of the integer `x`. For example, `rev(123) = 321`, `rev(120) = 21`. A pair of indices `(i, j)` is called a nice pair if `i < j` and `nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])`.

Return the number of nice pairs in `nums`. Since the answer may be very large, return it modulo `10^9 + 7`.

Example 1:
Input: nums = [42, 11, 1, 97]
Output: 2
Explanation: The two nice pairs are:
- (0, 1): nums[0] + rev(nums[1]) = 42 + 11 = 11 + 42 = nums[1] + rev(nums[0])
- (1, 2): nums[1] + rev(nums[2]) = 11 + 1 = 1 + 11 = nums[2] + rev(nums[1])

Example 2:
Input: nums = [13, 10, 35, 24, 76]
Output: 4

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
"""

# Python Solution
from collections import Counter

def countNicePairs(nums):
    MOD = 10**9 + 7

    def rev(x):
        return int(str(x)[::-1])

    # Calculate the difference between nums[i] and rev(nums[i])
    diff = [num - rev(num) for num in nums]

    # Count the frequency of each difference
    freq = Counter(diff)

    # Calculate the number of nice pairs using combination formula
    nice_pairs = sum(count * (count - 1) // 2 for count in freq.values())

    return nice_pairs % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [42, 11, 1, 97]
    print(countNicePairs(nums1))  # Output: 2

    # Test Case 2
    nums2 = [13, 10, 35, 24, 76]
    print(countNicePairs(nums2))  # Output: 4

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(countNicePairs(nums3))  # Output: 0

    # Test Case 4
    nums4 = [100, 101, 102, 103]
    print(countNicePairs(nums4))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating `rev(x)` for each number in `nums` takes O(K), where K is the number of digits in the number.
- Iterating through `nums` to compute the `diff` array takes O(N), where N is the length of `nums`.
- Counting frequencies using `Counter` takes O(N).
- Calculating the number of nice pairs from the frequency counts takes O(M), where M is the number of unique differences.
Overall, the time complexity is O(N * K), where K is the average number of digits in the numbers.

Space Complexity:
- The `diff` array takes O(N) space.
- The `Counter` object takes O(M) space, where M is the number of unique differences.
Overall, the space complexity is O(N + M).

Topic: Hash Table
"""