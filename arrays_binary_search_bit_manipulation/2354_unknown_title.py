"""
LeetCode Problem #2354: Number of Excellent Pairs

Problem Statement:
You are given a 0-indexed positive integer array `nums` and a positive integer `k`.

An excellent pair is a pair of indices `(i, j)` such that the bitwise OR of `nums[i]` and `nums[j]` has at least `k` set bits.

Return the number of distinct excellent pairs.

Two pairs `(i, j)` and `(i', j')` are considered distinct if either `i != i'` or `j != j'`.

Note:
- The bitwise OR of two integers is an operation that takes the binary representation of each integer and performs the bitwise OR operation on each pair of corresponding bits. The result in each position is 1 if either of the bits is 1, otherwise, it is 0.
- The number of set bits in an integer is the number of 1s in its binary representation.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 60
"""

from collections import Counter
from bisect import bisect_left

def countExcellentPairs(nums, k):
    """
    Function to count the number of excellent pairs in the array `nums` with the given threshold `k`.
    """
    # Remove duplicates from nums
    nums = list(set(nums))
    
    # Count the number of set bits for each number in nums
    set_bits = [bin(num).count('1') for num in nums]
    
    # Sort the set bits array
    set_bits.sort()
    
    # Initialize the count of excellent pairs
    count = 0
    
    # For each set bit count, find the number of valid pairs
    for bits in set_bits:
        # Find the smallest index where the sum of set bits is >= k
        idx = bisect_left(set_bits, k - bits)
        count += len(set_bits) - idx
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 2, 3]
    k1 = 3
    print(countExcellentPairs(nums1, k1))  # Expected Output: 3

    # Test Case 2
    nums2 = [5, 1, 1]
    k2 = 2
    print(countExcellentPairs(nums2, k2))  # Expected Output: 6

    # Test Case 3
    nums3 = [1, 2, 4, 8]
    k3 = 4
    print(countExcellentPairs(nums3, k3))  # Expected Output: 4

"""
Time Complexity Analysis:
- Removing duplicates from `nums` takes O(n), where n is the length of `nums`.
- Calculating the number of set bits for each number takes O(n * log(max(nums))) since the binary representation of a number has at most log(max(nums)) bits.
- Sorting the `set_bits` array takes O(n * log(n)).
- For each element in `set_bits`, performing a binary search takes O(log(n)), and this is done for all n elements, resulting in O(n * log(n)).
- Overall time complexity: O(n * log(max(nums)) + n * log(n)).

Space Complexity Analysis:
- The space used to store the `set_bits` array is O(n).
- The space complexity is O(n).

Topic: Arrays, Binary Search, Bit Manipulation
"""