"""
LeetCode Problem #2930: Problem Statement

(Note: As of my knowledge cutoff in October 2023, LeetCode Problem #2930 does not exist. 
Instead, I will create a hypothetical problem statement for this question.)

Problem Statement:
You are given a list of integers `nums` and an integer `target`. Your task is to find all unique pairs of numbers 
in the list that sum up to the `target`. Each pair should be represented as a tuple `(a, b)` where `a <= b`. 
Return the list of pairs sorted in ascending order. If no such pairs exist, return an empty list.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 5
Output: [(1, 4), (2, 3)]

Constraints:
- The length of `nums` is between 0 and 10^4.
- Each element in `nums` is an integer between -10^6 and 10^6.
- The `target` is an integer between -10^6 and 10^6.
- Each pair must be unique, and the order of elements in the pair does not matter.
"""

# Python Solution
def find_pairs(nums, target):
    """
    Finds all unique pairs of numbers in the list that sum up to the target.

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
    print(find_pairs(nums, target))  # Expected Output: [(1, 4), (2, 3)]

    # Test Case 2
    nums = [0, -1, 2, -3, 1]
    target = -2
    print(find_pairs(nums, target))  # Expected Output: [(-3, 1)]

    # Test Case 3
    nums = [1, 1, 1, 1]
    target = 2
    print(find_pairs(nums, target))  # Expected Output: [(1, 1)]

    # Test Case 4
    nums = []
    target = 5
    print(find_pairs(nums, target))  # Expected Output: []

    # Test Case 5
    nums = [10, -10, 20, -20, 30]
    target = 0
    print(find_pairs(nums, target))  # Expected Output: [(-20, 20), (-10, 10)]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the list `nums` once, making the time complexity O(n), where n is the length of `nums`.
- The `sorted` function is applied to each pair before adding it to the `pairs` set, which is O(1) since pairs are of fixed size (2 elements).
- Sorting the final list of pairs takes O(k log k), where k is the number of unique pairs.

Overall time complexity: O(n + k log k).

Space Complexity:
- The `seen` set stores up to n elements, and the `pairs` set stores up to k pairs.
- The space complexity is O(n + k), where n is the length of `nums` and k is the number of unique pairs.

Overall space complexity: O(n + k).
"""

# Topic: Hashing