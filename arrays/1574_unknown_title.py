"""
LeetCode Problem #1574: Shortest Subarray to be Removed to Make Array Sorted

Problem Statement:
Given an integer array `arr`, remove a subarray (can be empty) from `arr` such that the remaining elements in `arr` are non-decreasing. 
A subarray is a contiguous subsequence of the array.

Return the length of the shortest subarray to remove.

Example 1:
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2]. The resulting array would be [1,2,3,3,5], which is sorted.

Example 2:
Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the entire array is strictly decreasing, we can only keep a single element. The shortest subarray to remove is [4,3,2,1].

Example 3:
Input: arr = [1,2,3]
Output: 0
Explanation: The array is already sorted, so we don't need to remove anything.

Constraints:
- 1 <= arr.length <= 10^5
- 0 <= arr[i] <= 10^9
"""

def findLengthOfShortestSubarray(arr):
    """
    Function to find the length of the shortest subarray to remove to make the array sorted.
    """
    n = len(arr)
    
    # Find the leftmost sorted part
    left = 0
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1
    
    # If the entire array is already sorted
    if left == n - 1:
        return 0
    
    # Find the rightmost sorted part
    right = n - 1
    while right > 0 and arr[right - 1] <= arr[right]:
        right -= 1
    
    # Minimum removal is to remove everything between left and right
    min_removal = min(n - left - 1, right)
    
    # Try to merge the left and right sorted parts
    i, j = 0, right
    while i <= left and j < n:
        if arr[i] <= arr[j]:
            min_removal = min(min_removal, j - i - 1)
            i += 1
        else:
            j += 1
    
    return min_removal

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 3, 10, 4, 2, 3, 5]
    print(findLengthOfShortestSubarray(arr1))  # Output: 3

    # Test Case 2
    arr2 = [5, 4, 3, 2, 1]
    print(findLengthOfShortestSubarray(arr2))  # Output: 4

    # Test Case 3
    arr3 = [1, 2, 3]
    print(findLengthOfShortestSubarray(arr3))  # Output: 0

    # Test Case 4
    arr4 = [1]
    print(findLengthOfShortestSubarray(arr4))  # Output: 0

    # Test Case 5
    arr5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(findLengthOfShortestSubarray(arr5))  # Output: 0

"""
Time Complexity:
- Finding the leftmost sorted part: O(n)
- Finding the rightmost sorted part: O(n)
- Merging the left and right sorted parts: O(n)
Overall: O(n)

Space Complexity:
- The algorithm uses constant extra space: O(1)

Topic: Arrays
"""