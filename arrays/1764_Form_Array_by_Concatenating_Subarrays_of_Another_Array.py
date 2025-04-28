"""
LeetCode Problem #1764: Form Array by Concatenating Subarrays of Another Array

Problem Statement:
You are given two arrays `groups` and `nums`. You are asked if you can choose some subarrays from `nums` and concatenate them in a way that it forms the array `groups`.

A subarray is a contiguous sequence of elements within an array.

Return `True` if you can do this, otherwise return `False`.

Example 1:
Input: groups = [[1, -1, -1], [3, -2, 0]], nums = [1, -1, -1, 3, -2, 0]
Output: True
Explanation: You can choose the subarrays [1, -1, -1] and [3, -2, 0] from nums.

Example 2:
Input: groups = [[10, -2], [1, 2, 3, 4]], nums = [1, 2, 3, 4, 10, -2]
Output: False
Explanation: You cannot choose any subarray from nums that matches the first group.

Example 3:
Input: groups = [[1, 2, 3], [3, 4]], nums = [7, 1, 2, 3, 4]
Output: False
Explanation: You can choose the subarray [1, 2, 3] but there is no subarray that matches [3, 4].

Constraints:
- `groups.length <= 10^3`
- `groups[i].length <= 10^3`
- `nums.length <= 10^3`
- `-10^7 <= groups[i][j], nums[k] <= 10^7`
"""

def canChoose(groups, nums):
    """
    Determines if the array `groups` can be formed by concatenating subarrays of `nums`.

    :param groups: List[List[int]] - List of groups to form.
    :param nums: List[int] - Array to extract subarrays from.
    :return: bool - True if `groups` can be formed, False otherwise.
    """
    i = 0  # Pointer for groups
    j = 0  # Pointer for nums

    while i < len(groups) and j < len(nums):
        # Check if the current group matches a subarray starting at index j
        if nums[j:j + len(groups[i])] == groups[i]:
            # Move the pointer in nums forward by the length of the matched group
            j += len(groups[i])
            # Move to the next group
            i += 1
        else:
            # Increment the pointer in nums to check the next subarray
            j += 1

    # If all groups are matched, return True
    return i == len(groups)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    groups = [[1, -1, -1], [3, -2, 0]]
    nums = [1, -1, -1, 3, -2, 0]
    print(canChoose(groups, nums))  # Output: True

    # Test Case 2
    groups = [[10, -2], [1, 2, 3, 4]]
    nums = [1, 2, 3, 4, 10, -2]
    print(canChoose(groups, nums))  # Output: False

    # Test Case 3
    groups = [[1, 2, 3], [3, 4]]
    nums = [7, 1, 2, 3, 4]
    print(canChoose(groups, nums))  # Output: False

    # Test Case 4
    groups = [[1, 2], [3, 4]]
    nums = [1, 2, 3, 4]
    print(canChoose(groups, nums))  # Output: True

    # Test Case 5
    groups = [[1, 2, 3], [4, 5]]
    nums = [1, 2, 3, 4, 5]
    print(canChoose(groups, nums))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- Let `g` be the total number of elements in `groups` and `n` be the number of elements in `nums`.
- For each group in `groups`, we may need to scan through `nums` to find a match.
- In the worst case, we scan through `nums` for each group, resulting in a time complexity of O(g * n).

Space Complexity:
- The algorithm uses constant space, as we are only using pointers and slicing operations.
- Space complexity is O(1).

Topic: Arrays
"""