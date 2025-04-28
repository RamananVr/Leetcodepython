"""
LeetCode Problem #2404: Most Frequent Even Element

Problem Statement:
Given an integer array `nums`, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.

Example 1:
Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
- The even elements are [0, 2, 2, 4, 4].
- The frequencies of the even elements are:
  0 -> 1
  2 -> 2
  4 -> 2.
- Since 2 and 4 both have the same highest frequency, return the smallest one, which is 2.

Example 2:
Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element with the highest frequency.

Example 3:
Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element in the array.

Constraints:
- 1 <= nums.length <= 2000
- 0 <= nums[i] <= 10^5
"""

from collections import Counter

def mostFrequentEven(nums):
    """
    Finds the most frequent even element in the array.
    If there is a tie, returns the smallest one.
    If no even element exists, returns -1.

    :param nums: List[int] - The input array of integers.
    :return: int - The most frequent even element or -1 if no even element exists.
    """
    # Filter out only even numbers
    even_nums = [num for num in nums if num % 2 == 0]
    
    # If no even numbers exist, return -1
    if not even_nums:
        return -1
    
    # Count the frequency of each even number
    freq = Counter(even_nums)
    
    # Find the most frequent even number with a tie-breaking rule for the smallest number
    return min(freq.keys(), key=lambda x: (-freq[x], x))


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
    print(mostFrequentEven(nums4))  # Output: 2

    # Test Case 5
    nums5 = [10, 10, 20, 20, 30, 30, 30]
    print(mostFrequentEven(nums5))  # Output: 30


"""
Time Complexity Analysis:
1. Filtering even numbers: O(n), where n is the length of the input array `nums`.
2. Counting frequencies using Counter: O(n).
3. Finding the minimum with a custom key: O(k), where k is the number of unique even numbers.
   In the worst case, k = n, so this step is O(n).
Overall time complexity: O(n).

Space Complexity Analysis:
1. Space for the filtered list of even numbers: O(n) in the worst case.
2. Space for the Counter dictionary: O(k), where k is the number of unique even numbers.
Overall space complexity: O(n).

Topic: Arrays, Hash Table
"""