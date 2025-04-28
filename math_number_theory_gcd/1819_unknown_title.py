"""
LeetCode Problem #1819: Number of Different Subsequences GCDs

Problem Statement:
You are given an array nums that consists of positive integers.

The GCD of a sequence of numbers is defined as the greatest integer that divides all the numbers in the sequence.

- A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
- For example, [2,5,10] is a subsequence of [1,2,1,2,5,10].

Return the number of different GCDs among all non-empty subsequences of nums.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 2 * 10^5
"""

# Solution
from math import gcd
from typing import List

def countDifferentSubsequenceGCDs(nums: List[int]) -> int:
    max_num = max(nums)
    present = [False] * (max_num + 1)
    
    # Mark all numbers that are present in the array
    for num in nums:
        present[num] = True
    
    count = 0
    
    # Iterate over all possible GCDs
    for x in range(1, max_num + 1):
        current_gcd = 0
        # Check multiples of x
        for multiple in range(x, max_num + 1, x):
            if present[multiple]:
                current_gcd = gcd(current_gcd, multiple)
                # If the current GCD equals x, we can stop early
                if current_gcd == x:
                    count += 1
                    break
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [6, 10, 3]
    print(countDifferentSubsequenceGCDs(nums1))  # Expected Output: 5

    # Test Case 2
    nums2 = [5, 15, 40, 5, 6]
    print(countDifferentSubsequenceGCDs(nums2))  # Expected Output: 7

    # Test Case 3
    nums3 = [2, 4, 8, 16]
    print(countDifferentSubsequenceGCDs(nums3))  # Expected Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop iterates over all possible values of x from 1 to max_num.
- For each x, the inner loop iterates over all multiples of x up to max_num.
- In the worst case, the number of iterations is proportional to max_num * (log(max_num)), where log(max_num) comes from the gcd computation.
- Therefore, the time complexity is approximately O(max_num * log(max_num)).

Space Complexity:
- We use an array `present` of size max_num + 1 to mark the presence of numbers in nums.
- The space complexity is O(max_num).

Topic: Math, Number Theory, GCD
"""