"""
LeetCode Question #2916: Problem Statement

You are given a list of integers `nums` and an integer `target`. Your task is to determine if there exists a pair of integers in the list whose sum is equal to the `target`. If such a pair exists, return `True`. Otherwise, return `False`.

Constraints:
- The list `nums` can contain both positive and negative integers.
- The list `nums` may contain duplicate values.
- The length of `nums` is at least 2.
- The target is an integer.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: True
Explanation: The pair (2, 7) sums to 9.

Input: nums = [3, 2, 4], target = 6
Output: True
Explanation: The pair (2, 4) sums to 6.

Input: nums = [3, 3], target = 6
Output: True
Explanation: The pair (3, 3) sums to 6.

Input: nums = [1, 2, 3], target = 7
Output: False
Explanation: No pair sums to 7.
"""

# Python Solution
def has_pair_with_sum(nums, target):
    """
    Determines if there exists a pair of integers in the list `nums` whose sum equals `target`.

    Args:
    nums (List[int]): List of integers.
    target (int): Target sum.

    Returns:
    bool: True if a pair exists, False otherwise.
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
    target4 = 7
    print(has_pair_with_sum(nums4, target4))  # Expected Output: False

    # Test Case 5
    nums5 = [-1, -2, -3, -4, -5]
    target5 = -8
    print(has_pair_with_sum(nums5, target5))  # Expected Output: True

    # Test Case 6
    nums6 = [0, 0, 0]
    target6 = 0
    print(has_pair_with_sum(nums6, target6))  # Expected Output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the list `nums` once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the list.

Space Complexity:
- The function uses a set `seen` to store elements from the list. In the worst case, the set will contain all n elements.
- Therefore, the space complexity is O(n).
"""

# Topic: Hash Table