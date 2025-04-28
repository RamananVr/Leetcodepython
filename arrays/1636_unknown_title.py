"""
LeetCode Problem #1636: Sort Array by Increasing Frequency

Problem Statement:
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. 
If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

Example 1:
Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Example 2:
Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '1', '2', and '3' all have a frequency of 2. 
Since '1' is the smallest, it comes first. 
Since '3' is larger than '2', it comes next, followed by '2'.

Example 3:
Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]

Constraints:
- 1 <= nums.length <= 100
- -100 <= nums[i] <= 100
"""

# Python Solution
from collections import Counter

def frequencySort(nums):
    """
    Sorts the array based on frequency in increasing order. If frequencies are equal, sorts by value in decreasing order.

    :param nums: List[int] - Input array of integers
    :return: List[int] - Sorted array
    """
    # Count the frequency of each number
    freq = Counter(nums)
    
    # Sort the array based on frequency (ascending), and by value (descending) for ties
    return sorted(nums, key=lambda x: (freq[x], -x))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 2, 2, 2, 3]
    print(frequencySort(nums1))  # Output: [3, 1, 1, 2, 2, 2]

    # Test Case 2
    nums2 = [2, 3, 1, 3, 2]
    print(frequencySort(nums2))  # Output: [1, 3, 3, 2, 2]

    # Test Case 3
    nums3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    print(frequencySort(nums3))  # Output: [5, -1, 4, 4, -6, -6, 1, 1, 1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting frequencies using Counter takes O(n), where n is the length of nums.
- Sorting the array takes O(n log n) due to the sorting algorithm.
- Overall time complexity: O(n log n).

Space Complexity:
- The Counter object uses O(k) space, where k is the number of unique elements in nums.
- The sorted function creates a new list, which also uses O(n) space.
- Overall space complexity: O(n + k), which is O(n) in the worst case when all elements are unique.
"""

# Topic: Arrays