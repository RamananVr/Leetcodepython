"""
LeetCode Question #2958: Full Problem Statement

Problem:
You are given a list of integers `nums` and an integer `target`. Your task is to find all unique pairs of integers in `nums` that sum up to `target`. Each pair should be represented as a tuple `(a, b)` where `a <= b`. The result should be a list of tuples sorted in ascending order.

Constraints:
1. The input list `nums` can contain duplicate integers.
2. The input list `nums` can have a length of up to 10^5.
3. The target integer can be any value within the range of -10^9 to 10^9.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 5
Output: [(1, 4), (2, 3)]

Input: nums = [1, 1, 2, 3, 4], target = 4
Output: [(1, 3)]

Input: nums = [1, 2, 3, 4, 5], target = 10
Output: []

Your solution should be efficient and handle large inputs within the constraints.
"""

# Solution
def two_sum_pairs(nums, target):
    """
    Finds all unique pairs of integers in `nums` that sum up to `target`.

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
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)

    return sorted(pairs)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [1, 2, 3, 4, 5]
    target = 5
    print(two_sum_pairs(nums, target))  # Expected Output: [(1, 4), (2, 3)]

    # Test Case 2
    nums = [1, 1, 2, 3, 4]
    target = 4
    print(two_sum_pairs(nums, target))  # Expected Output: [(1, 3)]

    # Test Case 3
    nums = [1, 2, 3, 4, 5]
    target = 10
    print(two_sum_pairs(nums, target))  # Expected Output: []

    # Test Case 4
    nums = [-1, 0, 1, 2, -1, -4]
    target = 0
    print(two_sum_pairs(nums, target))  # Expected Output: [(-1, 1)]

    # Test Case 5
    nums = [0, 0, 0, 0]
    target = 0
    print(two_sum_pairs(nums, target))  # Expected Output: [(0, 0)]

"""
Time and Space Complexity Analysis

Time Complexity:
- The function iterates through the list `nums` once, making the time complexity O(n), where n is the length of `nums`.
- Sorting the pairs at the end has a complexity of O(k log k), where k is the number of unique pairs. In the worst case, k <= n.

Overall time complexity: O(n + k log k), which simplifies to O(n) for large inputs since k is typically much smaller than n.

Space Complexity:
- The `seen` set stores up to n elements, and the `pairs` set stores up to n/2 pairs in the worst case.
- Space complexity is O(n).

Topic: Hashing
"""