"""
LeetCode Problem #2917: Full Problem Statement

Problem Statement:
You are given a list of integers `nums` and an integer `target`. Your task is to determine if there exists a pair of numbers in the list that adds up to the target. If such a pair exists, return True; otherwise, return False.

Constraints:
- The list `nums` contains integers, and its length is between 1 and 10^5.
- The integer `target` can be any value within the range of a 32-bit signed integer.
- You must solve the problem with a time complexity better than O(n^2).

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: True
Explanation: 2 + 7 = 9, so the pair exists.

Input: nums = [3, 2, 4], target = 6
Output: True
Explanation: 2 + 4 = 6, so the pair exists.

Input: nums = [3, 3], target = 6
Output: True
Explanation: 3 + 3 = 6, so the pair exists.

Input: nums = [1, 2, 3], target = 7
Output: False
Explanation: No pair adds up to 7.

"""

# Python Solution
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
    nums5 = []
    target5 = 5
    print(has_pair_with_sum(nums5, target5))  # Expected Output: False

    # Test Case 6
    nums6 = [1]
    target6 = 2
    print(has_pair_with_sum(nums6, target6))  # Expected Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the list `nums` once, performing O(1) operations for each element (checking membership in a set and adding an element to the set).
- Therefore, the time complexity is O(n), where n is the length of the list.

Space Complexity:
- The space complexity is O(n) because, in the worst case, we store all elements of `nums` in the `seen` set.
"""

# Topic: Hash Table