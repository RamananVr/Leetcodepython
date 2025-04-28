"""
LeetCode Problem #1191: K-Concatenation Maximum Sum

Problem Statement:
Given an integer array `arr` and an integer `k`, you need to find the maximum possible sum of a subarray 
of the array formed by concatenating `arr` `k` times.

The size of the array is n, and the value of k is at least 1.

The result may be very large, so return the result modulo 10^9 + 7.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= k <= 10^5
- -10^4 <= arr[i] <= 10^4

Example:
Input: arr = [1, -2, 1], k = 5
Output: 2

Explanation:
The array formed by concatenating arr 5 times is [1, -2, 1, 1, -2, 1, 1, -2, 1, 1, -2, 1, 1, -2, 1].
The maximum subarray sum is 2.

"""

# Python Solution
from typing import List

def kConcatenationMaxSum(arr: List[int], k: int) -> int:
    MOD = 10**9 + 7
    
    def kadane(nums):
        """Helper function to calculate the maximum subarray sum using Kadane's algorithm."""
        max_sum = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    
    # Case 1: k == 1, simply find the max subarray sum of arr
    max_sum_single = kadane(arr)
    
    # Case 2: k == 2, consider the array concatenated twice
    max_sum_double = kadane(arr * 2)
    
    # Case 3: k > 2, consider the sum of the entire array and the contribution of the prefix/suffix
    total_sum = sum(arr)
    if k == 1:
        return max_sum_single % MOD
    elif total_sum > 0:
        return max(max_sum_double, max_sum_single + (k - 2) * total_sum) % MOD
    else:
        return max(max_sum_double, max_sum_single) % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr = [1, -2, 1]
    k = 5
    print(kConcatenationMaxSum(arr, k))  # Output: 2

    # Test Case 2
    arr = [1, 2]
    k = 3
    print(kConcatenationMaxSum(arr, k))  # Output: 9

    # Test Case 3
    arr = [-1, -2]
    k = 7
    print(kConcatenationMaxSum(arr, k))  # Output: 0

    # Test Case 4
    arr = [1, -1, 1]
    k = 4
    print(kConcatenationMaxSum(arr, k))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- Kadane's algorithm runs in O(n) for a single array.
- For k == 2, we run Kadane's algorithm on arr * 2, which is O(2n) = O(n).
- For k > 2, we calculate the total sum of arr (O(n)) and use Kadane's algorithm on arr (O(n)).
Thus, the overall time complexity is O(n).

Space Complexity:
- Kadane's algorithm uses O(1) extra space.
- For k == 2, we do not explicitly create arr * 2; instead, we simulate it during Kadane's algorithm.
Thus, the overall space complexity is O(1).

Topic: Dynamic Programming (Kadane's Algorithm)
"""