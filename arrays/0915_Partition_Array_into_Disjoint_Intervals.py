"""
LeetCode Problem #915: Partition Array into Disjoint Intervals

Problem Statement:
Given an integer array `nums`, partition it into two (contiguous) subarrays left and right so that:
1. Every element in left is less than or equal to every element in right.
2. left and right are non-empty.
3. left has the smallest possible size.

Return the length of left after such a partitioning.

Test cases are generated such that there is at least one valid answer.

Constraints:
- 2 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^6

Example 1:
Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]

Example 2:
Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
"""

def partitionDisjoint(nums):
    """
    Function to partition the array into disjoint intervals.
    
    Args:
    nums (List[int]): The input array of integers.
    
    Returns:
    int: The length of the left subarray.
    """
    n = len(nums)
    max_left = [0] * n
    min_right = [0] * n

    # Fill max_left array
    max_left[0] = nums[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], nums[i])

    # Fill min_right array
    min_right[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], nums[i])

    # Find the partition point
    for i in range(1, n):
        if max_left[i - 1] <= min_right[i]:
            return i

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [5, 0, 3, 8, 6]
    print(partitionDisjoint(nums1))  # Output: 3

    # Test Case 2
    nums2 = [1, 1, 1, 0, 6, 12]
    print(partitionDisjoint(nums2))  # Output: 4

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(partitionDisjoint(nums3))  # Output: 1

    # Test Case 4
    nums4 = [10, 5, 0, 3, 8, 6]
    print(partitionDisjoint(nums4))  # Output: 5

"""
Time Complexity Analysis:
- Filling the `max_left` array takes O(n) time.
- Filling the `min_right` array takes O(n) time.
- The final loop to find the partition point takes O(n) time.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The `max_left` and `min_right` arrays each take O(n) space.
- Overall space complexity: O(n).

Topic: Arrays
"""