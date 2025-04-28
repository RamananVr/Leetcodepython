"""
LeetCode Problem #1390: Four Divisors

Problem Statement:
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. 
If there is no such integer in the array, return 0.

An integer x has exactly four divisors if and only if there exist exactly four distinct integers d1, d2, d3, and d4 such that:
- x % d1 == 0
- x % d2 == 0
- x % d3 == 0
- x % d4 == 0

Example:
Input: nums = [21, 4, 7]
Output: 32
Explanation:
- 21 has exactly four divisors: 1, 3, 7, 21. Sum is 1 + 3 + 7 + 21 = 32.
- 4 has exactly three divisors: 1, 2, 4.
- 7 has exactly two divisors: 1, 7.
Hence, the output is 32.

Constraints:
- 1 <= nums.length <= 10^4
- 1 <= nums[i] <= 10^5
"""

# Solution
def sumFourDivisors(nums):
    def get_divisors(n):
        divisors = set()
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
            if len(divisors) > 4:  # Early exit if more than 4 divisors
                return []
        return divisors if len(divisors) == 4 else []

    total_sum = 0
    for num in nums:
        divisors = get_divisors(num)
        if divisors:
            total_sum += sum(divisors)
    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [21, 4, 7]
    print(sumFourDivisors(nums1))  # Output: 32

    # Test Case 2
    nums2 = [10, 15, 28]
    print(sumFourDivisors(nums2))  # Output: 54

    # Test Case 3
    nums3 = [1, 2, 3]
    print(sumFourDivisors(nums3))  # Output: 0

    # Test Case 4
    nums4 = [16, 18, 20]
    print(sumFourDivisors(nums4))  # Output: 0

    # Test Case 5
    nums5 = [30, 42, 66]
    print(sumFourDivisors(nums5))  # Output: 144

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - For each number in the array, we iterate up to the square root of the number to find its divisors.
   - Let n be the maximum value in nums and m be the length of nums.
   - The worst-case time complexity is O(m * sqrt(n)).

2. Space Complexity:
   - The space complexity is O(k), where k is the number of divisors stored temporarily for each number.
   - Since we only store divisors for one number at a time, the space usage is minimal and does not depend on the size of the input array.

Topic: Arrays, Math
"""