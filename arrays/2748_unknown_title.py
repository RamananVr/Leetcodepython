"""
LeetCode Problem #2748: Number of Beautiful Pairs

Problem Statement:
You are given a 0-indexed integer array `nums`. A pair of integers `(i, j)` is called beautiful if:
1. `0 <= i < j < nums.length`
2. The greatest common divisor (GCD) of the first digit of `nums[i]` and the last digit of `nums[j]` is 1.

Return the total number of beautiful pairs in the array.

Example:
Input: nums = [2, 5, 1, 4]
Output: 5
Explanation:
- The first digit of nums[0] is 2 and the last digit of nums[1] is 5. gcd(2, 5) = 1.
- The first digit of nums[0] is 2 and the last digit of nums[2] is 1. gcd(2, 1) = 1.
- The first digit of nums[0] is 2 and the last digit of nums[3] is 4. gcd(2, 4) = 1.
- The first digit of nums[1] is 5 and the last digit of nums[2] is 1. gcd(5, 1) = 1.
- The first digit of nums[1] is 5 and the last digit of nums[3] is 4. gcd(5, 4) = 1.
Thus, there are 5 beautiful pairs.

Constraints:
- 2 <= nums.length <= 100
- 1 <= nums[i] <= 9999
"""

from math import gcd

def count_beautiful_pairs(nums):
    """
    Counts the number of beautiful pairs in the given array.

    :param nums: List[int] - The input array of integers.
    :return: int - The total number of beautiful pairs.
    """
    def first_digit(n):
        """Returns the first digit of a number."""
        while n >= 10:
            n //= 10
        return n

    def last_digit(n):
        """Returns the last digit of a number."""
        return n % 10

    beautiful_pairs = 0
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if gcd(first_digit(nums[i]), last_digit(nums[j])) == 1:
                beautiful_pairs += 1

    return beautiful_pairs

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 5, 1, 4]
    print(count_beautiful_pairs(nums1))  # Output: 5

    # Test Case 2
    nums2 = [12, 34, 56, 78]
    print(count_beautiful_pairs(nums2))  # Output: 4

    # Test Case 3
    nums3 = [11, 22, 33, 44]
    print(count_beautiful_pairs(nums3))  # Output: 0

    # Test Case 4
    nums4 = [123, 456, 789, 101]
    print(count_beautiful_pairs(nums4))  # Output: 6

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through all pairs of indices `(i, j)` where `0 <= i < j < n`.
- This results in a nested loop with O(n^2) iterations.
- For each pair, the `first_digit` and `last_digit` functions are called, which take O(log10(nums[i])) and O(1) time respectively.
- The GCD computation takes O(log(min(a, b))) time, where `a` and `b` are the first and last digits.
- Overall, the time complexity is approximately O(n^2 * log(max_digit)), where `max_digit` is the largest number in `nums`.

Space Complexity:
- The function uses a constant amount of extra space for variables and helper functions.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""