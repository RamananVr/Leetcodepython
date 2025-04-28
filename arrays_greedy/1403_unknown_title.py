"""
LeetCode Problem #1403: Minimum Subsequence in Non-Increasing Order

Problem Statement:
Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non-included elements in such subsequence. 

If there are multiple solutions, return the subsequence with the maximum size and if there still exist multiple solutions, return the subsequence with the maximum sum of elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.

Note that the solution with the maximum sum of elements is unique. Also, the returned answer should be sorted in non-increasing order.

Example 1:
Input: nums = [4,3,10,9,8]
Output: [10,9]

Example 2:
Input: nums = [4,4,7,6,7]
Output: [7,7,6]

Example 3:
Input: nums = [6]
Output: [6]

Constraints:
- 1 <= nums.length <= 500
- 1 <= nums[i] <= 100
"""

# Python Solution
from typing import List

def minSubsequence(nums: List[int]) -> List[int]:
    # Sort the array in descending order
    nums.sort(reverse=True)
    
    # Calculate the total sum of the array
    total_sum = sum(nums)
    
    # Initialize variables for the subsequence and its sum
    subsequence = []
    subsequence_sum = 0
    
    # Iterate through the sorted array
    for num in nums:
        subsequence.append(num)
        subsequence_sum += num
        # Check if the subsequence sum is greater than the remaining sum
        if subsequence_sum > total_sum - subsequence_sum:
            break
    
    return subsequence

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 3, 10, 9, 8]
    print(minSubsequence(nums1))  # Output: [10, 9]

    # Test Case 2
    nums2 = [4, 4, 7, 6, 7]
    print(minSubsequence(nums2))  # Output: [7, 7, 6]

    # Test Case 3
    nums3 = [6]
    print(minSubsequence(nums3))  # Output: [6]

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    print(minSubsequence(nums4))  # Output: [5, 4]

    # Test Case 5
    nums5 = [10, 10, 10, 10]
    print(minSubsequence(nums5))  # Output: [10, 10]

"""
Time Complexity Analysis:
- Sorting the array takes O(n log n), where n is the length of the array.
- Iterating through the array to build the subsequence takes O(n).
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- The space complexity is O(n) due to the storage of the subsequence list.
- Overall space complexity: O(n).

Topic: Arrays, Greedy
"""