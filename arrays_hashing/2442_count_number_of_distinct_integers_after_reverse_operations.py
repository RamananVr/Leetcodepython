"""
LeetCode Question #2442: Count Number of Distinct Integers After Reverse Operations

Problem Statement:
You are given an array `nums` consisting of positive integers. You can perform the following operation any number of times:

1. Pick any integer from `nums` and reverse its digits.
2. Add the reversed integer to the array (it can be added multiple times).

Return the number of distinct integers in the final array.

Example:
Input: nums = [1, 13, 10, 12, 31]
Output: 6
Explanation: After reversing the digits of some numbers in the array, the final array contains [1, 13, 10, 12, 31, 3]. The distinct integers are [1, 3, 10, 12, 13, 31].

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""

# Clean and Correct Python Solution
def countDistinctIntegers(nums):
    """
    This function returns the number of distinct integers in the array after performing
    the reverse operation on the integers.

    :param nums: List[int] - The input array of positive integers
    :return: int - The number of distinct integers in the final array
    """
    distinct_set = set(nums)  # Start with the original numbers in a set
    for num in nums:
        reversed_num = int(str(num)[::-1])  # Reverse the digits of the number
        distinct_set.add(reversed_num)  # Add the reversed number to the set
    return len(distinct_set)  # The size of the set is the count of distinct integers

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 13, 10, 12, 31]
    print(countDistinctIntegers(nums1))  # Expected Output: 6

    # Test Case 2
    nums2 = [2, 2, 2]
    print(countDistinctIntegers(nums2))  # Expected Output: 2

    # Test Case 3
    nums3 = [123, 321, 456]
    print(countDistinctIntegers(nums3))  # Expected Output: 4

    # Test Case 4
    nums4 = [100, 200, 300]
    print(countDistinctIntegers(nums4))  # Expected Output: 6

    # Test Case 5
    nums5 = [111, 222, 333]
    print(countDistinctIntegers(nums5))  # Expected Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n = len(nums) and m = the average number of digits in nums[i].
- Reversing a number takes O(m) time.
- Iterating through the array and reversing each number takes O(n * m).
- Adding elements to a set and checking for duplicates is O(1) on average.
- Overall time complexity: O(n * m).

Space Complexity:
- The space complexity is O(n) for the set that stores the distinct integers.
- Overall space complexity: O(n).
"""

# Topic: Arrays, Hashing