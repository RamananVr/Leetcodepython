"""
LeetCode Problem #2940: Valid Problem Statement

Problem Statement:
You are given a list of integers `nums` and an integer `target`. Your task is to determine if there exist two distinct indices `i` and `j` in the list such that `nums[i] + nums[j] == target`. If such indices exist, return `True`. Otherwise, return `False`.

Constraints:
- The length of `nums` is at least 2.
- Each element in `nums` is an integer.
- The `target` is an integer.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: True
Explanation: nums[0] + nums[1] = 2 + 7 = 9

Input: nums = [3, 2, 4], target = 6
Output: True
Explanation: nums[1] + nums[2] = 2 + 4 = 6

Input: nums = [3, 3], target = 6
Output: True
Explanation: nums[0] + nums[1] = 3 + 3 = 6

Input: nums = [1, 2, 3], target = 5
Output: False
Explanation: No two distinct indices satisfy the condition.

"""

# Solution
def has_pair_with_sum(nums, target):
    """
    Determines if there exist two distinct indices i and j in the list such that nums[i] + nums[j] == target.

    Args:
    nums (List[int]): List of integers.
    target (int): Target sum.

    Returns:
    bool: True if such indices exist, False otherwise.
    """
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(has_pair_with_sum(nums1, target1))  # Expected Output: True

    # Test Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(has_pair_with_sum(nums2, target2))  # Expected Output: True

    # Test Case 3
    nums3 = [3, 3]
    target3 = 6
    print(has_pair_with_sum(nums3, target3))  # Expected Output: True

    # Test Case 4
    nums4 = [1, 2, 3]
    target4 = 5
    print(has_pair_with_sum(nums4, target4))  # Expected Output: False

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5]
    target5 = 10
    print(has_pair_with_sum(nums5, target5))  # Expected Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the list of numbers once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input list `nums`.

Space Complexity:
- The function uses a set to store seen numbers, which in the worst case can contain all elements of `nums`.
- Therefore, the space complexity is O(n), where n is the length of the input list `nums`.

"""

# Topic: Hashing