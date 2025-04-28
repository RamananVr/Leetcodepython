"""
LeetCode Problem #2966: Problem Statement

(Note: As of my knowledge cutoff in October 2023, LeetCode Problem #2966 does not exist. 
Instead, I will create a hypothetical problem statement for this question.)

Problem Statement:
You are given an array of integers `nums` and an integer `target`. Your task is to find all unique pairs of numbers in the array that sum up to the `target`. Each pair should be represented as a tuple `(a, b)` where `a <= b`. Return the list of pairs sorted in ascending order.

Constraints:
1. The input array `nums` can contain both positive and negative integers.
2. The input array `nums` may contain duplicate values.
3. The output should not contain duplicate pairs.
4. The length of `nums` is between 1 and 10^4.
5. The target is an integer between -10^5 and 10^5.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 5
Output: [(1, 4), (2, 3)]

Input: nums = [1, 1, 2, 3, 4], target = 5
Output: [(1, 4), (2, 3)]

Input: nums = [-1, 0, 1, 2, -1, -4], target = 0
Output: [(-1, 1), (-4, 4)]
"""

# Python Solution
def two_sum_pairs(nums, target):
    """
    Finds all unique pairs of numbers in the array that sum up to the target.

    Args:
    nums (List[int]): The input array of integers.
    target (int): The target sum.

    Returns:
    List[Tuple[int, int]]: A list of unique pairs sorted in ascending order.
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
    nums1 = [1, 2, 3, 4, 5]
    target1 = 5
    print(two_sum_pairs(nums1, target1))  # Expected Output: [(1, 4), (2, 3)]

    # Test Case 2
    nums2 = [1, 1, 2, 3, 4]
    target2 = 5
    print(two_sum_pairs(nums2, target2))  # Expected Output: [(1, 4), (2, 3)]

    # Test Case 3
    nums3 = [-1, 0, 1, 2, -1, -4]
    target3 = 0
    print(two_sum_pairs(nums3, target3))  # Expected Output: [(-1, 1), (-4, 4)]

    # Test Case 4
    nums4 = [0, 0, 0, 0]
    target4 = 0
    print(two_sum_pairs(nums4, target4))  # Expected Output: [(0, 0)]

    # Test Case 5
    nums5 = [10, -10, 20, -20, 30, -30]
    target5 = 0
    print(two_sum_pairs(nums5, target5))  # Expected Output: [(-30, 30), (-20, 20), (-10, 10)]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the array once, making it O(n).
- Sorting the pairs at the end is O(k log k), where k is the number of unique pairs.
- Overall complexity: O(n + k log k).

Space Complexity:
- The `seen` set stores up to n elements, making it O(n).
- The `pairs` set stores up to k pairs, making it O(k).
- Overall space complexity: O(n + k).

Topic: Arrays, Hashing
"""