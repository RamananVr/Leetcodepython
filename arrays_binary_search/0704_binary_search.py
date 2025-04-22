"""
LeetCode Question #704: Binary Search

Problem Statement:
------------------
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
----------
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4.

Example 2:
----------
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1.

Constraints:
------------
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i], target <= 10^4
- All the integers in `nums` are unique.
- `nums` is sorted in ascending order.
"""

# Solution
def search(nums, target):
    """
    Perform binary search to find the target in the sorted array nums.

    Args:
    nums (List[int]): A sorted list of integers.
    target (int): The integer to search for.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid potential overflow
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Target exists in the array
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(search(nums1, target1))  # Expected Output: 4

    # Test Case 2: Target does not exist in the array
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(search(nums2, target2))  # Expected Output: -1

    # Test Case 3: Single element array where target exists
    nums3 = [5]
    target3 = 5
    print(search(nums3, target3))  # Expected Output: 0

    # Test Case 4: Single element array where target does not exist
    nums4 = [5]
    target4 = 3
    print(search(nums4, target4))  # Expected Output: -1

    # Test Case 5: Large array with target at the beginning
    nums5 = list(range(1, 10001))
    target5 = 1
    print(search(nums5, target5))  # Expected Output: 0

    # Test Case 6: Large array with target at the end
    nums6 = list(range(1, 10001))
    target6 = 10000
    print(search(nums6, target6))  # Expected Output: 9999

# Time and Space Complexity Analysis
"""
Time Complexity:
----------------
The binary search algorithm divides the search space in half at each step. 
In the worst case, the number of steps required is proportional to log(n), 
where n is the size of the input array. Thus, the time complexity is O(log n).

Space Complexity:
-----------------
The algorithm uses a constant amount of space for variables (left, right, mid). 
No additional data structures are used, so the space complexity is O(1).
"""

# Topic: Arrays, Binary Search