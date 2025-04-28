"""
LeetCode Problem #287: Find the Duplicate Number

Problem Statement:
Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive, 
there is only one repeated number in `nums`. Return this repeated number.

You must solve the problem without modifying the array `nums` and use only constant extra space.

Constraints:
- 1 <= n <= 10^5
- nums.length == n + 1
- 1 <= nums[i] <= n
- All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow-up:
- Can you solve the problem in O(n) time complexity and constant space?

"""

# Solution
def findDuplicate(nums):
    """
    Finds the duplicate number in the array using Floyd's Tortoise and Hare (Cycle Detection) algorithm.

    Args:
    nums (List[int]): The input array containing n + 1 integers.

    Returns:
    int: The duplicate number.
    """
    # Phase 1: Detect the cycle using slow and fast pointers
    slow, fast = nums[0], nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Find the entrance to the cycle (duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 4, 2, 2]
    print(findDuplicate(nums1))  # Output: 2

    # Test Case 2
    nums2 = [3, 1, 3, 4, 2]
    print(findDuplicate(nums2))  # Output: 3

    # Test Case 3
    nums3 = [1, 1]
    print(findDuplicate(nums3))  # Output: 1

    # Test Case 4
    nums4 = [1, 2, 2, 3, 4]
    print(findDuplicate(nums4))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm runs in O(n) time because both the cycle detection phase and the cycle entrance finding phase 
  involve traversing the array with pointers, which takes linear time.

Space Complexity:
- The algorithm uses constant extra space, O(1), as it only uses a few pointers (slow and fast) and does not modify the input array.

Topic: Arrays, Cycle Detection
"""