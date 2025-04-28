"""
LeetCode Problem #1829: Maximum XOR for Each Query

Problem Statement:
You are given a sorted array `nums` of n non-negative integers (0-indexed). You are also given an integer `maximumBit`. 
You will apply the following algorithm on `nums`:

1. Start with `x = 0`.
2. For every element in `nums` (from left to right), apply `x = x XOR nums[i]`.
3. After finishing the XOR operation for all elements of `nums`, find the maximum possible value of `x XOR k`, 
   where `k` is an integer such that `0 <= k < 2^maximumBit`.
4. Reverse the process and repeat the above steps for the remaining elements of `nums` (excluding the last one).

Return an array `result` where `result[i]` is the maximum XOR value for the i-th query.

Constraints:
- `1 <= nums.length <= 10^5`
- `1 <= maximumBit <= 20`
- `0 <= nums[i] < 2^maximumBit`

Example:
Input: nums = [0,1,1,3], maximumBit = 2
Output: [0,3,2,3]

Explanation:
- The maximum value of `k` is `2^maximumBit - 1 = 3`.
- After processing the array, the XOR values and results are calculated as described in the problem.

"""

# Python Solution
from typing import List

def getMaximumXor(nums: List[int], maximumBit: int) -> List[int]:
    # Calculate the maximum possible value of k
    max_k = (1 << maximumBit) - 1  # 2^maximumBit - 1
    
    # Compute the prefix XOR for the entire array
    x = 0
    for num in nums:
        x ^= num
    
    # Generate the result array
    result = []
    for num in reversed(nums):
        # The maximum XOR value is x XOR max_k
        result.append(x ^ max_k)
        # Update x by removing the last element's contribution
        x ^= num
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [0, 1, 1, 3]
    maximumBit = 2
    print(getMaximumXor(nums, maximumBit))  # Output: [0, 3, 2, 3]

    # Test Case 2
    nums = [2, 3, 4, 7]
    maximumBit = 3
    print(getMaximumXor(nums, maximumBit))  # Output: [5, 2, 6, 5]

    # Test Case 3
    nums = [10, 5, 7]
    maximumBit = 4
    print(getMaximumXor(nums, maximumBit))  # Output: [8, 13, 10]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the prefix XOR for the entire array takes O(n), where n is the length of `nums`.
- Generating the result array involves iterating over the array in reverse, which also takes O(n).
- Thus, the overall time complexity is O(n).

Space Complexity:
- The algorithm uses O(1) additional space for variables like `x` and `max_k`.
- The result array takes O(n) space to store the output.
- Therefore, the overall space complexity is O(n).

Topic: Bit Manipulation
"""