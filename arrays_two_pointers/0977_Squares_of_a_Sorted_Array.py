"""
LeetCode Problem #977: Squares of a Sorted Array

Problem Statement:
Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number 
sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100]. After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order.

Follow up:
Try to implement the solution with O(n) time complexity.
"""

def sortedSquares(nums):
    """
    This function takes a sorted array of integers, squares each number, and returns a sorted array of the squares.

    :param nums: List[int] - A sorted list of integers
    :return: List[int] - A sorted list of the squares of the integers
    """
    # Two-pointer approach
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1

        pos -= 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [-4, -1, 0, 3, 10]
    print(sortedSquares(nums1))  # Output: [0, 1, 9, 16, 100]

    # Test Case 2
    nums2 = [-7, -3, 2, 3, 11]
    print(sortedSquares(nums2))  # Output: [4, 9, 9, 49, 121]

    # Test Case 3
    nums3 = [-5, -3, -2, -1]
    print(sortedSquares(nums3))  # Output: [1, 4, 9, 25]

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    print(sortedSquares(nums4))  # Output: [1, 4, 9, 16, 25]

    # Test Case 5
    nums5 = [-1]
    print(sortedSquares(nums5))  # Output: [1]

"""
Time Complexity Analysis:
- The algorithm uses a two-pointer approach to traverse the array once, so the time complexity is O(n), 
  where n is the length of the input array.

Space Complexity Analysis:
- The algorithm uses an additional array `result` of size n to store the squared values, so the space complexity is O(n).

Topic: Arrays, Two Pointers
"""