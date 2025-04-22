"""
LeetCode Question #697: Degree of an Array

Problem Statement:
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: nums = [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
- [1, 2, 2, 3, 1] (length 5)
- [2, 2] (length 2)
The shortest length is 2.

Example 2:
Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation:
The degree is 3 because the element 2 appears three times.
The shortest subarray with degree 3 is [2,2,3,1,4,2], which has length 6.

Constraints:
- nums.length will be between 1 and 50,000.
- nums[i] will be an integer between 0 and 49,999.
"""

# Python Solution
def findShortestSubarray(nums):
    """
    Finds the smallest length of a contiguous subarray with the same degree as the input array.

    :param nums: List[int] - The input array of integers.
    :return: int - The length of the shortest subarray with the same degree.
    """
    # Dictionary to store the frequency, first occurrence, and last occurrence of each number
    num_info = {}
    degree = 0
    min_length = float('inf')

    for i, num in enumerate(nums):
        if num not in num_info:
            num_info[num] = [1, i, i]  # [frequency, first_index, last_index]
        else:
            num_info[num][0] += 1
            num_info[num][2] = i

        # Update the degree of the array
        degree = max(degree, num_info[num][0])

    # Find the minimum length of subarray with the same degree
    for freq, first, last in num_info.values():
        if freq == degree:
            min_length = min(min_length, last - first + 1)

    return min_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 2, 3, 1]
    print(findShortestSubarray(nums1))  # Output: 2

    # Test Case 2
    nums2 = [1, 2, 2, 3, 1, 4, 2]
    print(findShortestSubarray(nums2))  # Output: 6

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(findShortestSubarray(nums3))  # Output: 1

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1]
    print(findShortestSubarray(nums4))  # Output: 5

    # Test Case 5
    nums5 = [2, 2, 2, 1, 1, 1, 2]
    print(findShortestSubarray(nums5))  # Output: 7

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once to populate the num_info dictionary, which takes O(n) time.
- Then, it iterates through the values of the dictionary to find the minimum length, which also takes O(n) time.
- Overall, the time complexity is O(n).

Space Complexity:
- The algorithm uses a dictionary to store information about each unique number in the array. In the worst case, the dictionary will have as many entries as there are unique numbers in the array.
- Therefore, the space complexity is O(u), where u is the number of unique elements in the array.
- In the worst case, u = n, so the space complexity is O(n).
"""

# Topic: Arrays