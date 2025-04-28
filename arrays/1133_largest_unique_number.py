"""
LeetCode Question #1133: Largest Unique Number

Problem Statement:
Given an integer array `nums`, return the largest integer that only occurs once. 
If no integer occurs once, return -1.

Example 1:
Input: nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]
Output: 8
Explanation: The maximum integer in the array that only occurs once is 8.

Example 2:
Input: nums = [9, 9, 8, 8]
Output: -1
Explanation: There is no integer that occurs once.

Constraints:
- 1 <= nums.length <= 2000
- 0 <= nums[i] <= 1000
"""

# Python Solution
def largestUniqueNumber(nums):
    """
    Finds the largest integer in the array that occurs only once.

    :param nums: List[int] - List of integers
    :return: int - Largest unique integer or -1 if none exists
    """
    from collections import Counter

    # Count the frequency of each number
    freq = Counter(nums)

    # Filter numbers that occur only once
    unique_numbers = [num for num, count in freq.items() if count == 1]

    # Return the maximum unique number or -1 if no unique numbers exist
    return max(unique_numbers) if unique_numbers else -1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [5, 7, 3, 9, 4, 9, 8, 3, 1]
    print(largestUniqueNumber(nums1))  # Output: 8

    # Test Case 2
    nums2 = [9, 9, 8, 8]
    print(largestUniqueNumber(nums2))  # Output: -1

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(largestUniqueNumber(nums3))  # Output: 5

    # Test Case 4
    nums4 = [10, 10, 20, 30, 30]
    print(largestUniqueNumber(nums4))  # Output: 20

    # Test Case 5
    nums5 = [1000, 1000, 999, 998, 998]
    print(largestUniqueNumber(nums5))  # Output: 999


"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of elements using `Counter` takes O(n), where n is the length of the input array.
- Filtering unique numbers takes O(n).
- Finding the maximum of the unique numbers takes O(k), where k is the number of unique numbers.
- Overall, the time complexity is O(n).

Space Complexity:
- The `Counter` object stores the frequency of each number, which takes O(u) space, where u is the number of unique elements in the array.
- The list `unique_numbers` also takes O(u) space.
- Overall, the space complexity is O(u).

Topic: Arrays
"""