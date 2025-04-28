"""
LeetCode Question #2920: Problem Statement

You are given a list of integers `nums` and an integer `target`. Your task is to determine if there exists a pair of numbers in the list that adds up to the target. Return `True` if such a pair exists, otherwise return `False`.

Constraints:
- The list `nums` contains integers, and its length is between 1 and 10^5.
- The integer `target` can be positive, negative, or zero.
- Each number in `nums` can appear multiple times.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: True
Explanation: 2 + 7 = 9, so the pair exists.

Input: nums = [1, 2, 3, 4], target = 8
Output: False
Explanation: No pair of numbers adds up to 8.

"""

# Solution
def has_pair_with_sum(nums, target):
    """
    Determines if there exists a pair of numbers in the list that adds up to the target.

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
    # Test Case 1: Pair exists
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(has_pair_with_sum(nums1, target1))  # Expected output: True

    # Test Case 2: Pair does not exist
    nums2 = [1, 2, 3, 4]
    target2 = 8
    print(has_pair_with_sum(nums2, target2))  # Expected output: False

    # Test Case 3: Single element in the list
    nums3 = [5]
    target3 = 5
    print(has_pair_with_sum(nums3, target3))  # Expected output: False

    # Test Case 4: Negative numbers
    nums4 = [-1, -2, -3, -4]
    target4 = -5
    print(has_pair_with_sum(nums4, target4))  # Expected output: True

    # Test Case 5: Zero target
    nums5 = [0, 1, 2, 3]
    target5 = 0
    print(has_pair_with_sum(nums5, target5))  # Expected output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the list `nums` once, performing O(1) operations for each element (checking membership in a set and adding to the set).
- Therefore, the time complexity is O(n), where n is the length of the list.

Space Complexity:
- The space complexity is O(n) due to the `seen` set, which can store up to n elements in the worst case.
- Thus, the space complexity is O(n).

"""

# Topic: Hashing