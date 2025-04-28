"""
LeetCode Problem #1748: Sum of Unique Elements

Problem Statement:
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Example 3:
Input: nums = [1,2,3,4,5]
Output: 15
Explanation: All the elements are unique, and the sum is 15.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

# Solution
def sumOfUnique(nums):
    """
    Function to calculate the sum of unique elements in the array.

    :param nums: List[int] - Input array of integers
    :return: int - Sum of unique elements
    """
    from collections import Counter

    # Count the frequency of each element in the array
    freq = Counter(nums)

    # Sum up elements that appear exactly once
    return sum(num for num, count in freq.items() if count == 1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 2]
    print(sumOfUnique(nums1))  # Output: 4

    # Test Case 2
    nums2 = [1, 1, 1, 1, 1]
    print(sumOfUnique(nums2))  # Output: 0

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(sumOfUnique(nums3))  # Output: 15

    # Additional Test Case 4
    nums4 = [10, 20, 10, 30, 40, 30]
    print(sumOfUnique(nums4))  # Output: 60

    # Additional Test Case 5
    nums5 = [100]
    print(sumOfUnique(nums5))  # Output: 100

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting the frequency of elements using `Counter` takes O(n), where n is the length of the input array.
- Summing up the unique elements involves iterating over the frequency dictionary, which takes O(k), where k is the number of unique elements.
- Overall, the time complexity is O(n).

Space Complexity:
- The `Counter` object stores the frequency of each element, which requires O(k) space, where k is the number of unique elements.
- The space complexity is O(k).

Topic: Arrays
"""