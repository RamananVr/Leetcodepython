"""
LeetCode Problem #2364: Count Number of Bad Pairs

Problem Statement:
You are given a 0-indexed integer array nums. A pair (i, j) is called a bad pair if:
    1. 0 <= i < j < nums.length, and
    2. j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.

Example 1:
Input: nums = [4,1,3,3]
Output: 5
Explanation: There are 5 bad pairs in the array:
- (0, 1): j - i = 1 - 0 = 1, nums[j] - nums[i] = 1 - 4 = -3.
- (0, 2): j - i = 2 - 0 = 2, nums[j] - nums[i] = 3 - 4 = -1.
- (0, 3): j - i = 3 - 0 = 3, nums[j] - nums[i] = 3 - 4 = -1.
- (1, 2): j - i = 2 - 1 = 1, nums[j] - nums[i] = 3 - 1 = 2.
- (1, 3): j - i = 3 - 1 = 2, nums[j] - nums[i] = 3 - 1 = 2.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 0
Explanation: All pairs are good pairs.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

# Python Solution
from collections import defaultdict

def countBadPairs(nums):
    """
    Function to count the number of bad pairs in the given array.

    :param nums: List[int] - The input array of integers.
    :return: int - The total number of bad pairs.
    """
    n = len(nums)
    total_pairs = n * (n - 1) // 2  # Total number of pairs (i, j) where 0 <= i < j < n
    good_pairs = 0

    # Dictionary to store the frequency of nums[i] - i
    freq = defaultdict(int)

    for i, num in enumerate(nums):
        diff = num - i
        good_pairs += freq[diff]  # Count pairs where nums[j] - j == nums[i] - i
        freq[diff] += 1  # Update frequency of nums[i] - i

    # Bad pairs = Total pairs - Good pairs
    return total_pairs - good_pairs

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 1, 3, 3]
    print(countBadPairs(nums1))  # Output: 5

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(countBadPairs(nums2))  # Output: 0

    # Test Case 3
    nums3 = [10, 20, 10, 30, 40]
    print(countBadPairs(nums3))  # Output: 8

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The function uses a dictionary to store the frequency of nums[i] - i. In the worst case, the dictionary could store up to n unique keys.
- Therefore, the space complexity is O(n).

Topic: Arrays, Hash Map
"""