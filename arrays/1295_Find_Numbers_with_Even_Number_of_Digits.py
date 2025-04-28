"""
LeetCode Problem #1295: Find Numbers with Even Number of Digits

Problem Statement:
Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:
Input: nums = [12, 345, 2, 6, 7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore, only 12 and 7896 contain an even number of digits.

Example 2:
Input: nums = [555, 901, 482, 1771]
Output: 1
Explanation: 
Only 1771 contains an even number of digits.

Constraints:
- 1 <= nums.length <= 500
- 1 <= nums[i] <= 10^5
"""

def findNumbers(nums):
    """
    Function to find the count of numbers with an even number of digits in the given list.

    :param nums: List[int] - List of integers
    :return: int - Count of numbers with an even number of digits
    """
    return sum(1 for num in nums if len(str(num)) % 2 == 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [12, 345, 2, 6, 7896]
    print(findNumbers(nums1))  # Output: 2

    # Test Case 2
    nums2 = [555, 901, 482, 1771]
    print(findNumbers(nums2))  # Output: 1

    # Test Case 3
    nums3 = [1, 22, 333, 4444, 55555]
    print(findNumbers(nums3))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the list `nums` once, and for each number, it converts the number to a string and checks its length.
- Converting a number to a string and checking its length is O(d), where d is the number of digits in the number.
- In the worst case, the total time complexity is O(n * d), where n is the length of the list and d is the average number of digits in the numbers.

Space Complexity:
- The function uses O(1) additional space since it does not use any extra data structures.
- The conversion of a number to a string is temporary and does not count towards space complexity.

Overall:
Time Complexity: O(n * d)
Space Complexity: O(1)

Topic: Arrays
"""