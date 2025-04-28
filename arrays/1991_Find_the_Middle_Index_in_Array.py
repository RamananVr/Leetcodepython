"""
LeetCode Problem #1991: Find the Middle Index in Array

Problem Statement:
Given a 0-indexed integer array `nums`, find the **middle index** (if it exists) of the array.

The middle index is an index where the sum of the elements to the left of the index is equal to the sum of the elements to the right of the index. If the index is on the left edge of the array, then the left sum is considered to be 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the **leftmost middle index** that satisfies the condition, or -1 if there is no such index.

Example 1:
Input: nums = [2, 3, -1, 8, 4]
Output: 3
Explanation:
The sum of the elements to the left of index 3 is (2 + 3 + -1) = 4.
The sum of the elements to the right of index 3 is (4) = 4.

Example 2:
Input: nums = [1, -1, 4]
Output: 2
Explanation:
The sum of the elements to the left of index 2 is (1 + -1) = 0.
The sum of the elements to the right of index 2 is (0) = 0.

Example 3:
Input: nums = [2, 5]
Output: -1
Explanation:
There is no valid middle index.

Constraints:
- 1 <= nums.length <= 100
- -1000 <= nums[i] <= 1000
"""

def findMiddleIndex(nums):
    """
    Finds the leftmost middle index in the array where the sum of elements
    to the left equals the sum of elements to the right.

    :param nums: List[int] - The input array of integers
    :return: int - The leftmost middle index, or -1 if no such index exists
    """
    total_sum = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
        # Calculate the right sum as total_sum - left_sum - num
        right_sum = total_sum - left_sum - num
        if left_sum == right_sum:
            return i
        left_sum += num

    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, -1, 8, 4]
    print(findMiddleIndex(nums1))  # Output: 3

    # Test Case 2
    nums2 = [1, -1, 4]
    print(findMiddleIndex(nums2))  # Output: 2

    # Test Case 3
    nums3 = [2, 5]
    print(findMiddleIndex(nums3))  # Output: -1

    # Test Case 4
    nums4 = [1, 7, 3, 6, 5, 6]
    print(findMiddleIndex(nums4))  # Output: 3

    # Test Case 5
    nums5 = [1, 2, 3]
    print(findMiddleIndex(nums5))  # Output: -1

"""
Time Complexity Analysis:
- Calculating the total sum of the array takes O(n) time.
- Iterating through the array to find the middle index takes O(n) time.
- Thus, the overall time complexity is O(n).

Space Complexity Analysis:
- We use a constant amount of extra space for variables like `total_sum` and `left_sum`.
- Thus, the space complexity is O(1).

Topic: Arrays
"""