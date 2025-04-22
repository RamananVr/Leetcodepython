"""
LeetCode Problem #565: Array Nesting

Problem Statement:
You are given an integer array `nums` of length `n` where `nums` is a permutation of the numbers in the range `[0, n - 1]`.
You should build a set `s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... }` subjected to the following rule:
- The first element in `s[k]` starts with the selection of the element `nums[k]` of `nums`.
- The next element in `s[k]` should be `nums[nums[k]]`, and then `nums[nums[nums[k]]]`, and so on.
- Stop adding right before a duplicate element occurs in `s[k]`.

Return the size of the largest set `s[k]` you can form.

Example 1:
Input: nums = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
nums[0] = 5, nums[5] = 6, nums[6] = 2, nums[2] = 0, therefore, s[0] = {5, 6, 2, 0}.
The size of s[0] is 4.

Example 2:
Input: nums = [0,1,2]
Output: 1
Explanation:
Each element forms its own set, so the largest set size is 1.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] < nums.length
- All the values of nums are unique.

"""

def arrayNesting(nums):
    """
    Function to find the size of the largest set s[k] that can be formed.

    :param nums: List[int] - Input array of integers
    :return: int - Size of the largest set
    """
    n = len(nums)
    visited = [False] * n
    max_size = 0

    for i in range(n):
        if not visited[i]:
            size = 0
            current = i
            while not visited[current]:
                visited[current] = True
                current = nums[current]
                size += 1
            max_size = max(max_size, size)

    return max_size

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [5, 4, 0, 3, 1, 6, 2]
    print(arrayNesting(nums1))  # Output: 4

    # Test Case 2
    nums2 = [0, 1, 2]
    print(arrayNesting(nums2))  # Output: 1

    # Test Case 3
    nums3 = [1, 0, 3, 4, 2]
    print(arrayNesting(nums3))  # Output: 3

    # Test Case 4
    nums4 = [2, 0, 1]
    print(arrayNesting(nums4))  # Output: 3

"""
Time Complexity Analysis:
- Each element in the array is visited at most once. Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity Analysis:
- The `visited` array requires O(n) space. Other variables use O(1) space. Hence, the space complexity is O(n).

Topic: Arrays
"""