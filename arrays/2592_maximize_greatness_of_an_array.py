"""
LeetCode Question #2592: Maximize Greatness of an Array

Problem Statement:
You are given a 0-indexed integer array `nums`. You are allowed to permute `nums` into any order. 
Let `greatness` be defined as the number of indices `i` for which `nums[i] > nums[i - 1]` (for `i > 0`).

Return the maximum possible value of `greatness` that can be achieved after permuting `nums`.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

# Solution
def maximizeGreatness(nums):
    """
    Function to maximize the greatness of an array by permuting its elements.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The maximum possible greatness of the array.
    """
    nums.sort()
    n = len(nums)
    greatness = 0
    j = 0

    # Iterate through the array and count the number of elements that can be greater
    for i in range(n):
        if j < n and nums[j] > nums[i]:
            greatness += 1
            j += 1
        else:
            j += 1

    return greatness

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 5, 2, 4]
    print(maximizeGreatness(nums1))  # Expected Output: 4

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(maximizeGreatness(nums2))  # Expected Output: 4

    # Test Case 3
    nums3 = [5, 5, 5, 5]
    print(maximizeGreatness(nums3))  # Expected Output: 0

    # Test Case 4
    nums4 = [1]
    print(maximizeGreatness(nums4))  # Expected Output: 0

    # Test Case 5
    nums5 = [1, 2, 2, 3, 3, 4]
    print(maximizeGreatness(nums5))  # Expected Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The iteration through the array takes O(n).
- Therefore, the overall time complexity is O(n log n).

Space Complexity:
- The sorting operation is performed in-place, so the space complexity is O(1) (excluding the input array).
- No additional data structures are used, so the space complexity remains O(1).

Topic: Arrays
"""