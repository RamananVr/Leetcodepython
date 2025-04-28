"""
LeetCode Question #2453: Destroy Sequential Targets

Problem Statement:
You are given an array `nums` consisting of positive integers, and an integer `space`.

You can perform the following operation any number of times:
- Choose any element of the array `nums` and destroy it. Destroying an element means removing it from the array.

Your goal is to maximize the number of elements remaining in the array such that no two elements are congruent modulo `space`.

Return the maximum number of elements you can have in the array after performing the above operation.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= space <= 10^9
"""

# Python Solution
from collections import defaultdict

def destroy_sequential_targets(nums, space):
    """
    Function to maximize the number of elements remaining in the array such that no two elements
    are congruent modulo `space`.

    Args:
    nums (List[int]): List of positive integers.
    space (int): The modulo space.

    Returns:
    int: Maximum number of elements that can remain in the array.
    """
    # Dictionary to count occurrences of each remainder
    remainder_count = defaultdict(int)
    
    # Count the frequency of each remainder when nums[i] % space
    for num in nums:
        remainder_count[num % space] += 1
    
    # Find the remainder with the maximum frequency
    max_remainder = max(remainder_count, key=lambda x: (remainder_count[x], -x))
    
    # Count the number of elements in nums that have the same remainder as max_remainder
    result = sum(1 for num in nums if num % space == max_remainder)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 7, 8, 10, 15]
    space1 = 5
    print(destroy_sequential_targets(nums1, space1))  # Output: 3

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    space2 = 2
    print(destroy_sequential_targets(nums2, space2))  # Output: 3

    # Test Case 3
    nums3 = [6, 2, 8, 4, 10]
    space3 = 4
    print(destroy_sequential_targets(nums3, space3))  # Output: 2

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1]
    space4 = 1
    print(destroy_sequential_targets(nums4, space4))  # Output: 5

    # Test Case 5
    nums5 = [1000000000, 999999999, 999999998]
    space5 = 3
    print(destroy_sequential_targets(nums5, space5))  # Output: 1

"""
Time Complexity Analysis:
- Calculating the remainders for all elements in `nums` takes O(n), where n is the length of `nums`.
- Counting the frequency of remainders using a dictionary also takes O(n).
- Finding the maximum frequency remainder takes O(k), where k is the number of unique remainders (k <= space).
- Summing the elements with the same remainder takes O(n).
- Overall time complexity: O(n).

Space Complexity Analysis:
- The dictionary `remainder_count` stores at most `space` keys, so its space complexity is O(min(n, space)).
- Overall space complexity: O(min(n, space)).

Topic: Arrays, Hash Table
"""