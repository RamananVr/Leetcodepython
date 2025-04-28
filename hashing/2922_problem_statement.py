"""
LeetCode Question #2922: Problem Statement

You are given a list of integers `nums` and an integer `target`. Your task is to determine if there exists a pair of numbers in the list that adds up to the target. If such a pair exists, return True; otherwise, return False.

Constraints:
- The list `nums` contains integers, and its length is between 1 and 10^5.
- The integer `target` can be any value within the range of a 32-bit signed integer.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: True
Explanation: The pair (2, 7) adds up to 9.

Input: nums = [1, 2, 3, 4], target = 8
Output: False
Explanation: No pair adds up to 8.

Your goal is to implement a function `has_pair_with_sum(nums, target)` that solves this problem efficiently.
"""

# Clean, Correct Python Solution
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
    print(has_pair_with_sum(nums1, target1))  # Expected Output: True

    # Test Case 2: Pair does not exist
    nums2 = [1, 2, 3, 4]
    target2 = 8
    print(has_pair_with_sum(nums2, target2))  # Expected Output: False

    # Test Case 3: Single element in the list
    nums3 = [5]
    target3 = 5
    print(has_pair_with_sum(nums3, target3))  # Expected Output: False

    # Test Case 4: Negative numbers
    nums4 = [-1, -2, -3, -4]
    target4 = -5
    print(has_pair_with_sum(nums4, target4))  # Expected Output: True

    # Test Case 5: Large list with no pair
    nums5 = list(range(1, 100000))
    target5 = 200000
    print(has_pair_with_sum(nums5, target5))  # Expected Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the list `nums` once, performing O(1) operations for each element (checking membership in a set and adding an element to the set).
- Therefore, the time complexity is O(n), where n is the length of the list.

Space Complexity:
- The space complexity is O(n) due to the `seen` set, which can store up to n elements in the worst case.
"""

# Topic: Hashing