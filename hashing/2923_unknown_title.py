"""
LeetCode Problem #2923: [Problem Title Placeholder]
(Note: As of my knowledge cutoff in October 2023, LeetCode Problem #2923 does not exist. 
If this problem was added after my cutoff date, I cannot provide the exact problem statement. 
Instead, I will create a hypothetical problem for demonstration purposes.)

Problem Statement:
You are given an array of integers `nums` and an integer `target`. Your task is to find all unique pairs of numbers in the array that sum up to the `target`. 
Each pair should be represented as a tuple `(a, b)` where `a <= b`. Return the list of pairs sorted in ascending order.

Example:
Input: nums = [1, 2, 3, 4, 5], target = 5
Output: [(1, 4), (2, 3)]

Constraints:
- The array `nums` may contain duplicate numbers.
- The solution should not include duplicate pairs.
- The length of `nums` is between 1 and 10^4.
- Each number in `nums` is between -10^6 and 10^6.
"""

# Solution
def two_sum_pairs(nums, target):
    """
    Finds all unique pairs of numbers in the array that sum up to the target.

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
    nums = [1, 1, 2, 2, 3, 3]
    target = 4
    print(two_sum_pairs(nums, target))  # Expected Output: [(1, 3), (2, 2)]

    # Test Case 3
    nums = [-1, 0, 1, 2, -1, -4]
    target = 0
    print(two_sum_pairs(nums, target))  # Expected Output: [(-1, 1)]

    # Test Case 4
    nums = [5, 5, 5, 5]
    target = 10
    print(two_sum_pairs(nums, target))  # Expected Output: [(5, 5)]

    # Test Case 5
    nums = []
    target = 3
    print(two_sum_pairs(nums, target))  # Expected Output: []

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the array once, making it O(n).
- Sorting the pairs and adding them to the set is O(1) for each pair due to the fixed size of tuples.
- Overall, the time complexity is O(n).

Space Complexity:
- The `seen` set stores up to n elements, making its space complexity O(n).
- The `pairs` set stores unique pairs, which in the worst case is O(n/2) (if all pairs are unique).
- Overall, the space complexity is O(n).
"""

# Topic: Hashing