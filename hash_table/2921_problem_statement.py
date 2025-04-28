"""
LeetCode Question #2921: Problem Statement

You are given a list of integers `nums` and an integer `target`. Your task is to determine whether there exist two distinct indices `i` and `j` in the list such that `nums[i] + nums[j] == target`.

Return `True` if such indices exist, otherwise return `False`.

Constraints:
- 2 <= len(nums) <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
"""

# Solution
def two_sum_exists(nums, target):
    """
    Determines if there exist two distinct indices i and j such that nums[i] + nums[j] == target.

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
    # Test Case 1: Positive case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(two_sum_exists(nums1, target1))  # Expected output: True

    # Test Case 2: Negative case
    nums2 = [1, 2, 3, 4]
    target2 = 10
    print(two_sum_exists(nums2, target2))  # Expected output: False

    # Test Case 3: Edge case with negative numbers
    nums3 = [-3, 4, 3, 90]
    target3 = 0
    print(two_sum_exists(nums3, target3))  # Expected output: True

    # Test Case 4: Edge case with large numbers
    nums4 = [10**9, -10**9, 0]
    target4 = 0
    print(two_sum_exists(nums4, target4))  # Expected output: True

    # Test Case 5: Edge case with minimum input size
    nums5 = [1, 2]
    target5 = 3
    print(two_sum_exists(nums5, target5))  # Expected output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the list once, performing O(1) operations for each element (checking membership in a set and adding to the set).
- Therefore, the time complexity is O(n), where n is the length of the input list `nums`.

Space Complexity:
- The space complexity is O(n) due to the `seen` set, which can store up to n elements in the worst case.
"""

# Topic: Hash Table