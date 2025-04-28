"""
LeetCode Problem #2006: Count Number of Pairs With Absolute Difference K

Problem Statement:
Given an integer array `nums` and an integer `k`, return the number of pairs `(i, j)` 
where `i < j` such that `|nums[i] - nums[j]| == k`.

The value of `|x|` is defined as:
- `x` if `x >= 0`.
- `-x` if `x < 0`.

Example 1:
Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- (0, 1): |1 - 2| = 1
- (0, 2): |1 - 2| = 1
- (1, 3): |2 - 1| = 1
- (2, 3): |2 - 1| = 1

Example 2:
Input: nums = [1,3], k = 3
Output: 0
Explanation: There are no pairs with an absolute difference of 3.

Example 3:
Input: nums = [3,2,1,5,4], k = 2
Output: 3
Explanation: The pairs with an absolute difference of 2 are:
- (0, 2): |3 - 1| = 2
- (1, 4): |2 - 4| = 2
- (3, 4): |5 - 3| = 2

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100
- 1 <= k <= 99
"""

# Clean and Correct Python Solution
from collections import Counter

def countKDifference(nums, k):
    """
    Counts the number of pairs (i, j) where i < j and |nums[i] - nums[j]| == k.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The target absolute difference.

    Returns:
    int: The number of valid pairs.
    """
    count = 0
    freq = Counter()

    for num in nums:
        # Check for pairs that satisfy the condition
        count += freq[num - k] + freq[num + k]
        # Update the frequency of the current number
        freq[num] += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 2, 1]
    k1 = 1
    print(countKDifference(nums1, k1))  # Output: 4

    # Test Case 2
    nums2 = [1, 3]
    k2 = 3
    print(countKDifference(nums2, k2))  # Output: 0

    # Test Case 3
    nums3 = [3, 2, 1, 5, 4]
    k3 = 2
    print(countKDifference(nums3, k3))  # Output: 3

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    k4 = 0
    print(countKDifference(nums4, k4))  # Output: 0

    # Test Case 5
    nums5 = [1, 5, 3, 4, 2]
    k5 = 2
    print(countKDifference(nums5, k5))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `nums` array once, making it O(n), where n is the length of the array.
- The operations on the Counter (dictionary) are O(1) on average for both lookups and updates.
- Overall time complexity: O(n).

Space Complexity:
- The function uses a Counter (dictionary) to store the frequency of numbers, which can hold at most 100 keys (since 1 <= nums[i] <= 100).
- Therefore, the space complexity is O(1) (constant space) in terms of the input constraints.
"""

# Topic: Arrays, Hash Table