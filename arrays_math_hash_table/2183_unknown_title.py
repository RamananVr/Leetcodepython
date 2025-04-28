"""
LeetCode Problem #2183: Count Array Pairs Divisible by K

Problem Statement:
Given a 0-indexed integer array `nums` of length `n` and an integer `k`, return the number of pairs `(i, j)` such that:
- 0 <= i < j < n
- nums[i] * nums[j] is divisible by k.

Example:
Input: nums = [2, 3, 4, 6], k = 6
Output: 7
Explanation:
The 7 pairs of indices are:
- (0, 1): nums[0] * nums[1] = 2 * 3 = 6, divisible by 6
- (0, 2): nums[0] * nums[2] = 2 * 4 = 8, not divisible by 6
- (0, 3): nums[0] * nums[3] = 2 * 6 = 12, divisible by 6
- (1, 2): nums[1] * nums[2] = 3 * 4 = 12, divisible by 6
- (1, 3): nums[1] * nums[3] = 3 * 6 = 18, divisible by 6
- (2, 3): nums[2] * nums[3] = 4 * 6 = 24, divisible by 6

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i], k <= 10^5
"""

from collections import defaultdict
from math import gcd

def countPairs(nums, k):
    """
    Function to count the number of pairs (i, j) such that nums[i] * nums[j] is divisible by k.
    
    Args:
    nums (List[int]): The input array of integers.
    k (int): The divisor.
    
    Returns:
    int: The count of valid pairs.
    """
    freq = defaultdict(int)
    count = 0

    for num in nums:
        gcd_num = gcd(num, k)
        for gcd_other, freq_count in freq.items():
            if (gcd_num * gcd_other) % k == 0:
                count += freq_count
        freq[gcd_num] += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 4, 6]
    k1 = 6
    print(countPairs(nums1, k1))  # Output: 7

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    k2 = 2
    print(countPairs(nums2, k2))  # Output: 7

    # Test Case 3
    nums3 = [10, 20, 30, 40]
    k3 = 10
    print(countPairs(nums3, k3))  # Output: 6

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    k4 = 1
    print(countPairs(nums4, k4))  # Output: 6

    # Test Case 5
    nums5 = [5, 10, 15, 20]
    k5 = 5
    print(countPairs(nums5, k5))  # Output: 6

"""
Time Complexity:
- Calculating the gcd for each number takes O(log(min(num, k))).
- For each number in nums, we iterate over the keys in the frequency dictionary. 
  In the worst case, the number of keys in the dictionary is bounded by the number of divisors of k, which is O(sqrt(k)).
- Thus, the overall time complexity is O(n * log(min(num, k)) * sqrt(k)).

Space Complexity:
- The space complexity is O(sqrt(k)) due to the frequency dictionary storing gcd values.

Topic: Arrays, Math, Hash Table
"""