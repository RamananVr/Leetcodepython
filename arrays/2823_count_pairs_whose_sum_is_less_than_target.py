"""
LeetCode Question #2823: Count Pairs Whose Sum is Less than Target

Problem Statement:
You are given a 0-indexed integer array `nums` of length `n` and an integer `target`.

Your task is to count the number of pairs `(i, j)` where `0 <= i < j < n` and `nums[i] + nums[j] < target`.

Return the number of such pairs.

Constraints:
- 2 <= nums.length <= 100
- -10^3 <= nums[i] <= 10^3
- -10^3 <= target <= 10^3
"""

def count_pairs(nums, target):
    """
    Function to count the number of pairs (i, j) where nums[i] + nums[j] < target.

    Args:
    nums (List[int]): The input array of integers.
    target (int): The target sum.

    Returns:
    int: The count of pairs satisfying the condition.
    """
    n = len(nums)
    count = 0

    # Iterate through all pairs (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] < target:
                count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    target1 = 5
    print(count_pairs(nums1, target1))  # Output: 4

    # Test Case 2
    nums2 = [-1, 0, 2, 3]
    target2 = 3
    print(count_pairs(nums2, target2))  # Output: 4

    # Test Case 3
    nums3 = [5, 1, 2, 3]
    target3 = 6
    print(count_pairs(nums3, target3))  # Output: 3

    # Test Case 4
    nums4 = [0, 0, 0]
    target4 = 1
    print(count_pairs(nums4, target4))  # Output: 3

    # Test Case 5
    nums5 = [10, 20, 30]
    target5 = 15
    print(count_pairs(nums5, target5))  # Output: 0

"""
Time Complexity Analysis:
- The function uses a nested loop to iterate through all pairs of indices (i, j) where i < j.
- The outer loop runs `n` times, and the inner loop runs approximately `n/2` times on average.
- Therefore, the time complexity is O(n^2), where n is the length of the input array `nums`.

Space Complexity Analysis:
- The function uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""