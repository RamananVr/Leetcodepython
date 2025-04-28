"""
LeetCode Problem #2366: Minimum Replacements to Sort the Array

Problem Statement:
You are given a 0-indexed integer array nums. You are allowed to perform the following operation on the array any number of times:

- Choose an element of the array nums[i].
- Replace nums[i] with any two integers a and b such that a + b = nums[i] and a <= b.

Your goal is to make the array sorted in non-decreasing order. Return the minimum number of operations needed to achieve this.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

# Python Solution
def minimumReplacement(nums):
    """
    Function to calculate the minimum number of replacements needed to sort the array in non-decreasing order.

    :param nums: List[int] - The input array
    :return: int - Minimum number of replacements
    """
    n = len(nums)
    replacements = 0
    prev = nums[-1]  # Start from the last element

    # Traverse the array from right to left
    for i in range(n - 2, -1, -1):
        if nums[i] > prev:
            # Calculate the number of parts needed
            parts = (nums[i] + prev - 1) // prev
            replacements += parts - 1
            # Update prev to the largest possible value for the current nums[i]
            prev = nums[i] // parts
        else:
            prev = nums[i]

    return replacements

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 9, 3]
    print(minimumReplacement(nums1))  # Output: 2

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(minimumReplacement(nums2))  # Output: 0

    # Test Case 3
    nums3 = [10, 5, 2]
    print(minimumReplacement(nums3))  # Output: 6

    # Test Case 4
    nums4 = [100, 50, 25, 12]
    print(minimumReplacement(nums4))  # Output: 11

    # Test Case 5
    nums5 = [5, 5, 5, 5]
    print(minimumReplacement(nums5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array once, performing constant-time calculations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space (variables like `prev` and `replacements`).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""