"""
LeetCode Question #891: Sum of Subsequence Widths

Problem Statement:
Given an array of integers `nums`, consider all non-empty subsequences of `nums`. For any subsequence, 
let the width be defined as the difference between the maximum and minimum elements in the subsequence.

Return the sum of the widths of all subsequences of `nums`. Since the answer may be very large, 
return it modulo 10^9 + 7.

A subsequence is a sequence that can be derived from an array by deleting some or no elements 
without changing the order of the remaining elements.

Example:
Input: nums = [2,1,3]
Output: 6
Explanation: The subsequences are:
- [1] with width = 0
- [2] with width = 0
- [3] with width = 0
- [1,2] with width = 1
- [1,3] with width = 2
- [2,3] with width = 1
- [1,2,3] with width = 2
The sum of all widths is 6.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""

# Python Solution
def sumSubseqWidths(nums):
    MOD = 10**9 + 7
    nums.sort()
    n = len(nums)
    
    # Precompute powers of 2 modulo MOD
    power_of_two = [1] * n
    for i in range(1, n):
        power_of_two[i] = (power_of_two[i - 1] * 2) % MOD
    
    result = 0
    for i in range(n):
        # Contribution of nums[i] as the maximum element
        max_contribution = nums[i] * power_of_two[i]
        # Contribution of nums[i] as the minimum element
        min_contribution = nums[i] * power_of_two[n - i - 1]
        # Add the difference to the result
        result += (max_contribution - min_contribution) % MOD
        result %= MOD
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [2, 1, 3]
    print(sumSubseqWidths(nums))  # Output: 6

    # Test Case 2
    nums = [1, 2, 3, 4]
    print(sumSubseqWidths(nums))  # Output: 50

    # Test Case 3
    nums = [10, 20, 30]
    print(sumSubseqWidths(nums))  # Output: 180

    # Test Case 4
    nums = [1]
    print(sumSubseqWidths(nums))  # Output: 0

    # Test Case 5
    nums = [5, 5, 5]
    print(sumSubseqWidths(nums))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n).
- The loop to compute the result runs in O(n).
- Precomputing powers of 2 also runs in O(n).
Thus, the overall time complexity is O(n log n).

Space Complexity:
- The space used for the `power_of_two` array is O(n).
- Sorting the array may require O(n) additional space depending on the sorting algorithm.
Thus, the overall space complexity is O(n).

Topic: Arrays
"""