"""
LeetCode Problem #2990: Problem Statement

(Note: As of my knowledge cutoff in October 2023, LeetCode Problem #2990 does not exist. 
Instead, I will create a hypothetical problem statement for this question.)

Problem Statement:
You are given a list of integers `nums` and an integer `target`. Your task is to find all unique pairs of integers in `nums` that sum up to `target`. Each pair should be represented as a tuple `(a, b)` where `a <= b`. Return the list of pairs sorted in ascending order.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 5
Output: [(1, 4), (2, 3)]

Constraints:
1. 2 <= len(nums) <= 10^4
2. -10^6 <= nums[i] <= 10^6
3. -10^6 <= target <= 10^6
4. Each pair must be unique.
"""

# Python Solution
def two_sum_pairs(nums, target):
    """
    Finds all unique pairs of integers in nums that sum up to target.

    Args:
    nums (List[int]): List of integers.
    target (int): Target sum.

    Returns:
    List[Tuple[int, int]]: List of unique pairs sorted in ascending order.
    """
    seen = set()
    pairs = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)

    return sorted(pairs)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [1, 2, 3, 4, 5]
    target = 5
    print(two_sum_pairs(nums, target))  # Output: [(1, 4), (2, 3)]

    # Test Case 2
    nums = [0, -1, 2, -3, 1]
    target = -1
    print(two_sum_pairs(nums, target))  # Output: [(-3, 2), (-1, 0)]

    # Test Case 3
    nums = [1, 1, 1, 1]
    target = 2
    print(two_sum_pairs(nums, target))  # Output: [(1, 1)]

    # Test Case 4
    nums = [5, 5, 5, 5]
    target = 10
    print(two_sum_pairs(nums, target))  # Output: [(5, 5)]

    # Test Case 5
    nums = []
    target = 0
    print(two_sum_pairs(nums, target))  # Output: []

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the list `nums` once, making the time complexity O(n), where n is the length of `nums`.
- The operations on sets (add, check membership) are O(1) on average.

Space Complexity:
- The space complexity is O(n) due to the `seen` set, which stores up to n elements.
- The `pairs` set also uses space proportional to the number of unique pairs, which is at most O(n) in the worst case.

Overall:
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Topic: Hashing