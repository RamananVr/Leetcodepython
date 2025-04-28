"""
LeetCode Problem #1596: The Most Frequent Even Element

Problem Statement:
Given an integer array `nums`, return the most frequent even element.
If there is a tie, return the smallest one. If there is no such element, return -1.

Example 1:
Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation: 
- The even elements are [0, 2, 2, 4, 4].
- The frequencies of the even elements are:
  0 -> 1, 2 -> 2, 4 -> 2.
- Since 2 and 4 have the same frequency, the smallest one is returned.

Example 2:
Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 
- The even elements are [4, 4, 4, 2, 4].
- The frequencies of the even elements are:
  4 -> 4, 2 -> 1.
- 4 is the most frequent even element.

Example 3:
Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: 
- There are no even elements in the array.

Constraints:
- 1 <= nums.length <= 2000
- 0 <= nums[i] <= 10^5
"""

# Python Solution
from collections import Counter

def mostFrequentEven(nums):
    # Filter out even numbers and count their frequencies
    even_counts = Counter(num for num in nums if num % 2 == 0)
    
    if not even_counts:
        return -1  # No even numbers found
    
    # Find the most frequent even number, breaking ties by choosing the smallest number
    return min(even_counts.keys(), key=lambda x: (-even_counts[x], x))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [0, 1, 2, 2, 4, 4, 1]
    print(mostFrequentEven(nums1))  # Output: 2

    # Test Case 2
    nums2 = [4, 4, 4, 9, 2, 4]
    print(mostFrequentEven(nums2))  # Output: 4

    # Test Case 3
    nums3 = [29, 47, 21, 41, 13, 37, 25, 7]
    print(mostFrequentEven(nums3))  # Output: -1

    # Test Case 4
    nums4 = [2, 2, 2, 4, 4, 6, 6, 6]
    print(mostFrequentEven(nums4))  # Output: 6

    # Test Case 5
    nums5 = [1, 3, 5, 7, 9]
    print(mostFrequentEven(nums5))  # Output: -1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Filtering even numbers: O(n), where n is the length of the input array.
- Counting frequencies using Counter: O(n).
- Finding the minimum with a custom key: O(k), where k is the number of unique even numbers.
- Overall: O(n).

Space Complexity:
- The Counter object stores frequencies of even numbers, which takes O(k) space, where k is the number of unique even numbers.
- Overall: O(k).
"""

# Topic: Arrays