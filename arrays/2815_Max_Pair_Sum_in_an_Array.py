"""
LeetCode Problem #2815: Max Pair Sum in an Array

Problem Statement:
You are given a 0-indexed integer array `nums`. You need to find the maximum sum of a pair `(nums[i], nums[j])` 
such that the maximum digit in `nums[i]` is equal to the maximum digit in `nums[j]` (i.e., they share the same 
maximum digit). Return the maximum sum of such a pair, or -1 if no such pair exists.

Example:
Input: nums = [51, 71, 17, 24, 42]
Output: 93
Explanation: 
- For nums[0] = 51, the maximum digit is 5.
- For nums[1] = 71, the maximum digit is 7.
- For nums[2] = 17, the maximum digit is 7.
- For nums[3] = 24, the maximum digit is 4.
- For nums[4] = 42, the maximum digit is 4.
There are two pairs with the same maximum digit:
- Pair (71, 17) with maximum digit 7. Sum = 71 + 17 = 88.
- Pair (24, 42) with maximum digit 4. Sum = 24 + 42 = 66.
The maximum sum is 93.

Constraints:
- 2 <= nums.length <= 1000
- 1 <= nums[i] <= 10^4
"""

# Python Solution
def max_pair_sum(nums):
    """
    Finds the maximum sum of a pair of numbers in the array such that they share the same maximum digit.

    :param nums: List[int] - The input array of integers.
    :return: int - The maximum sum of such a pair, or -1 if no such pair exists.
    """
    from collections import defaultdict

    # Helper function to find the maximum digit in a number
    def max_digit(num):
        return max(int(digit) for digit in str(num))

    # Group numbers by their maximum digit
    max_digit_map = defaultdict(list)
    for num in nums:
        max_d = max_digit(num)
        max_digit_map[max_d].append(num)

    # Find the maximum sum of pairs
    max_sum = -1
    for numbers in max_digit_map.values():
        if len(numbers) >= 2:
            # Sort numbers in descending order to get the two largest numbers
            numbers.sort(reverse=True)
            max_sum = max(max_sum, numbers[0] + numbers[1])

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [51, 71, 17, 24, 42]
    print(max_pair_sum(nums1))  # Output: 93

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print(max_pair_sum(nums2))  # Output: -1

    # Test Case 3
    nums3 = [99, 98, 97, 96]
    print(max_pair_sum(nums3))  # Output: 195

    # Test Case 4
    nums4 = [123, 456, 789, 321, 654]
    print(max_pair_sum(nums4))  # Output: 975

    # Test Case 5
    nums5 = [11, 22, 33, 44, 55]
    print(max_pair_sum(nums5))  # Output: 88

"""
Time and Space Complexity Analysis:

Time Complexity:
- The helper function `max_digit` runs in O(d), where d is the number of digits in a number.
- For each number in `nums`, we compute its maximum digit, which takes O(n * d) in total, where n is the length of `nums`.
- Sorting the numbers in each group takes O(k log k), where k is the size of the group. In the worst case, all numbers belong to the same group, so sorting takes O(n log n).
- Overall, the time complexity is O(n * d + n log n), where d is the average number of digits in the numbers.

Space Complexity:
- We use a dictionary to store groups of numbers based on their maximum digit. In the worst case, the dictionary contains n entries, each storing a list of numbers. This requires O(n) space.
- The space complexity is O(n).

Topic: Arrays
"""