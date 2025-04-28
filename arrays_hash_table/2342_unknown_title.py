"""
LeetCode Problem #2342: Max Sum of a Pair With Equal Sum of Digits

Problem Statement:
You are given a 0-indexed array `nums` consisting of positive integers. You can choose two indices `i` and `j` such that `i != j`, and the sum of digits of the number `nums[i]` is equal to the sum of digits of the number `nums[j]`.

Return the maximum value of `nums[i] + nums[j]` that you can obtain over all possible indices `i` and `j` that satisfy the condition. If no such indices exist, return `-1`.

Example:
Input: nums = [51, 71, 17, 42]
Output: 93
Explanation:
- The sum of digits of 51 is 5 + 1 = 6, and the sum of digits of 42 is 4 + 2 = 6.
- The sum of digits of 71 is 7 + 1 = 8, and the sum of digits of 17 is 1 + 7 = 8.
- The maximum sum of nums[i] + nums[j] where the sum of digits of nums[i] equals the sum of digits of nums[j] is 93 (51 + 42).

Constraints:
- 2 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

# Python Solution
from collections import defaultdict

def maximumSum(nums):
    """
    Finds the maximum sum of a pair of numbers in the array such that the sum of their digits is equal.

    :param nums: List[int] - List of positive integers
    :return: int - Maximum sum of such a pair, or -1 if no such pair exists
    """
    def digit_sum(n):
        """Helper function to calculate the sum of digits of a number."""
        return sum(int(d) for d in str(n))
    
    # Dictionary to store the maximum number for each digit sum
    digit_sum_map = defaultdict(int)
    max_sum = -1

    for num in nums:
        d_sum = digit_sum(num)
        if d_sum in digit_sum_map:
            # Calculate the sum of the current number and the stored maximum
            max_sum = max(max_sum, num + digit_sum_map[d_sum])
        # Update the maximum number for this digit sum
        digit_sum_map[d_sum] = max(digit_sum_map[d_sum], num)
    
    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [51, 71, 17, 42]
    print(maximumSum(nums1))  # Output: 93

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print(maximumSum(nums2))  # Output: -1

    # Test Case 3
    nums3 = [18, 43, 36, 13, 7]
    print(maximumSum(nums3))  # Output: 54

    # Test Case 4
    nums4 = [10, 12, 19, 14]
    print(maximumSum(nums4))  # Output: 31

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the digit sum for a number takes O(log10(n)) time, where n is the number of digits in the number.
- For all numbers in the array, the total time complexity is O(N * D), where N is the length of the array and D is the average number of digits in the numbers.
- In the worst case, D = log10(10^9) = 9, so the time complexity is approximately O(N).

Space Complexity:
- We use a dictionary to store the maximum number for each digit sum. In the worst case, there are at most 81 unique digit sums (since the maximum digit sum for a number ≤ 10^9 is 81).
- Thus, the space complexity is O(1) with respect to the size of the dictionary, and O(N) for the input array.
"""

# Topic: Arrays, Hash Table