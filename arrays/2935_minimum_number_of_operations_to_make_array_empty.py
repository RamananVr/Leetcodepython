"""
LeetCode Question #2935: Minimum Number of Operations to Make Array Empty

Problem Statement:
You are given an array `nums` consisting of positive integers. You can perform the following operation on the array any number of times:

- Choose any element `x` from the array and remove all occurrences of `x` from the array.

Return the minimum number of operations required to make the array empty.

Example:
Input: nums = [3,3,2,2,4,4,4]
Output: 3
Explanation: You can perform the following operations:
1. Remove all occurrences of 3.
2. Remove all occurrences of 2.
3. Remove all occurrences of 4.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

# Python Solution
from collections import Counter

def min_operations(nums):
    """
    Calculate the minimum number of operations to make the array empty.

    :param nums: List[int] - The input array of positive integers.
    :return: int - The minimum number of operations required.
    """
    # Count the frequency of each unique number in the array
    frequency = Counter(nums)
    
    # The minimum number of operations is equal to the number of unique elements
    return len(frequency)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 3, 2, 2, 4, 4, 4]
    print(min_operations(nums1))  # Output: 3

    # Test Case 2
    nums2 = [1, 1, 1, 1, 1]
    print(min_operations(nums2))  # Output: 1

    # Test Case 3
    nums3 = [5, 6, 7, 8, 9]
    print(min_operations(nums3))  # Output: 5

    # Test Case 4
    nums4 = [10, 10, 10, 20, 20, 30]
    print(min_operations(nums4))  # Output: 3

    # Test Case 5
    nums5 = [1]
    print(min_operations(nums5))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of elements using `Counter(nums)` takes O(n), where n is the length of the array.
- Calculating the length of the frequency dictionary takes O(1).
- Overall, the time complexity is O(n).

Space Complexity:
- The `Counter` object stores the frequency of each unique element, which requires O(u) space, where u is the number of unique elements in the array.
- In the worst case, u = n (all elements are unique), so the space complexity is O(n).

Topic: Arrays
"""