"""
LeetCode Problem #414: Third Maximum Number

Problem Statement:
Given an integer array `nums`, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3, 2, 1]
Output: 1
Explanation: The first distinct maximum is 3, the second is 2, and the third is 1.

Example 2:
Input: nums = [1, 2]
Output: 2
Explanation: The first distinct maximum is 2, and the second is 1. Since the third maximum does not exist, return the maximum (2).

Example 3:
Input: nums = [2, 2, 3, 1]
Output: 1
Explanation: The first distinct maximum is 3, the second is 2 (both 2s are considered the same), and the third is 1.

Constraints:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

Follow up: Can you find an O(n) solution?
"""

# Clean and Correct Python Solution
def thirdMax(nums):
    # Use a set to store distinct numbers
    distinct_nums = set(nums)
    
    # If there are less than 3 distinct numbers, return the maximum
    if len(distinct_nums) < 3:
        return max(distinct_nums)
    
    # Otherwise, remove the largest two numbers and return the third maximum
    distinct_nums.remove(max(distinct_nums))
    distinct_nums.remove(max(distinct_nums))
    return max(distinct_nums)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 2, 1]
    print(thirdMax(nums1))  # Output: 1

    # Test Case 2
    nums2 = [1, 2]
    print(thirdMax(nums2))  # Output: 2

    # Test Case 3
    nums3 = [2, 2, 3, 1]
    print(thirdMax(nums3))  # Output: 1

    # Test Case 4
    nums4 = [1, 1, 1]
    print(thirdMax(nums4))  # Output: 1

    # Test Case 5
    nums5 = [5, 2, 2]
    print(thirdMax(nums5))  # Output: 5

# Time and Space Complexity Analysis
"""
Time Complexity:
- The time complexity is O(n), where n is the length of the input array `nums`.
  - Converting the list to a set takes O(n).
  - Finding the maximum value in the set takes O(1) (amortized constant time for small sets).
  - Removing two maximum values also takes O(1) each.

Space Complexity:
- The space complexity is O(n) due to the use of a set to store distinct elements from the input array.
"""

# Topic: Arrays