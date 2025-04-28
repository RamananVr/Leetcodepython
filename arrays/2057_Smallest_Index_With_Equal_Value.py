"""
LeetCode Problem #2057: Smallest Index With Equal Value

Problem Statement:
Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if no such index exists.

x mod y denotes the remainder when x is divided by y.

Example:
- For nums = [0, 1, 2], the result is 0 because 0 mod 10 == nums[0].
- For nums = [4, 3, 2, 1], the result is 2 because 2 mod 10 == nums[2].
- For nums = [1, 2, 3, 4], the result is -1 because no index satisfies the condition.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 9
"""

def smallestEqual(nums):
    """
    Finds the smallest index i such that i mod 10 == nums[i].

    :param nums: List[int] - A list of integers.
    :return: int - The smallest index satisfying the condition, or -1 if no such index exists.
    """
    for i in range(len(nums)):
        if i % 10 == nums[i]:
            return i
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Expected output is 0
    print(smallestEqual([0, 1, 2]))  # Output: 0

    # Test Case 2: Expected output is 2
    print(smallestEqual([4, 3, 2, 1]))  # Output: 2

    # Test Case 3: Expected output is -1
    print(smallestEqual([1, 2, 3, 4]))  # Output: -1

    # Test Case 4: Expected output is 1
    print(smallestEqual([9, 1, 5, 6]))  # Output: 1

    # Test Case 5: Expected output is -1
    print(smallestEqual([9, 9, 9, 9]))  # Output: -1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the list `nums` once, checking the condition for each index.
- Let n be the length of the array. The time complexity is O(n).

Space Complexity:
- The function uses a constant amount of space for variables and does not use any additional data structures.
- The space complexity is O(1).

Topic: Arrays
"""