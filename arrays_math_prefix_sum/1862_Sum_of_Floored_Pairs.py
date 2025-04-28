"""
LeetCode Problem #1862: Sum of Floored Pairs

Problem Statement:
Given an integer array nums, return the sum of floored pairs.

The floor of the pair (a, b) is the number of times b can be subtracted from a until a becomes less than b. 
The floor function is denoted as ⌊a/b⌋.

For example:
- floor(2/3) = 0 because 2 < 3.
- floor(10/3) = 3 because 10 - 3 - 3 - 3 = 1.

Return the sum of ⌊nums[i] / nums[j]⌋ for all pairs of indices i, j (1 <= i, j <= nums.length).

Since the answer may be very large, return it modulo 10^9 + 7.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

# Python Solution
from collections import Counter

def sumOfFlooredPairs(nums):
    MOD = 10**9 + 7
    max_num = max(nums)
    
    # Count the frequency of each number in nums
    freq = Counter(nums)
    
    # Create an array to store the prefix sum of floor values
    floor_sum = [0] * (max_num + 1)
    
    # Calculate the floor sums for all numbers up to max_num
    for num in range(1, max_num + 1):
        if freq[num] > 0:
            for multiple in range(num, max_num + 1, num):
                floor_sum[multiple] += freq[num] * (multiple // num)
    
    # Calculate the total sum of floored pairs
    result = sum(floor_sum[num] for num in nums) % MOD
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 5, 9]
    print(sumOfFlooredPairs(nums1))  # Expected Output: 10

    # Test Case 2
    nums2 = [1, 1, 1]
    print(sumOfFlooredPairs(nums2))  # Expected Output: 3

    # Test Case 3
    nums3 = [7, 7, 7, 7]
    print(sumOfFlooredPairs(nums3))  # Expected Output: 16

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    print(sumOfFlooredPairs(nums4))  # Expected Output: 19

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates over all numbers up to max_num (O(max_num)).
- For each number, it calculates floor values for its multiples, which is proportional to max_num / num.
- In the worst case, this results in O(max_num * log(max_num)) due to the harmonic series summation.

Space Complexity:
- The space complexity is O(max_num) for the floor_sum array and O(max_num) for the frequency counter.
- Total space complexity is O(max_num).

Topic: Arrays, Math, Prefix Sum
"""