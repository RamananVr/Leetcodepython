"""
LeetCode Problem #179: Largest Number

Problem Statement:
Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it.
Since the result may be very large, return it as a string.

Example 1:
Input: nums = [10, 2]
Output: "210"

Example 2:
Input: nums = [3, 30, 34, 5, 9]
Output: "9534330"

Example 3:
Input: nums = [1]
Output: "1"

Example 4:
Input: nums = [10]
Output: "10"

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 10^9
"""

from functools import cmp_to_key

def largestNumber(nums):
    """
    Function to arrange numbers to form the largest number.

    Args:
    nums (List[int]): List of non-negative integers.

    Returns:
    str: The largest number formed by arranging the integers.
    """
    # Custom comparator to decide the order of concatenation
    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0

    # Convert integers to strings for comparison
    nums = list(map(str, nums))
    
    # Sort using the custom comparator
    nums.sort(key=cmp_to_key(compare))
    
    # Join the sorted numbers
    result = ''.join(nums)
    
    # Handle the case where the result is all zeros (e.g., [0, 0])
    return '0' if result[0] == '0' else result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [10, 2]
    print(largestNumber(nums1))  # Output: "210"

    # Test Case 2
    nums2 = [3, 30, 34, 5, 9]
    print(largestNumber(nums2))  # Output: "9534330"

    # Test Case 3
    nums3 = [1]
    print(largestNumber(nums3))  # Output: "1"

    # Test Case 4
    nums4 = [10]
    print(largestNumber(nums4))  # Output: "10"

    # Test Case 5
    nums5 = [0, 0]
    print(largestNumber(nums5))  # Output: "0"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array using a custom comparator takes O(n log n), where n is the length of the input list.
- The comparison function itself runs in O(k), where k is the average number of digits in the numbers.
- Overall time complexity: O(n log n * k).

Space Complexity:
- The space complexity is O(n) for storing the string representations of the numbers.
- Additional space is used for sorting, but it is negligible compared to the input size.
- Overall space complexity: O(n).

Topic: Arrays
"""