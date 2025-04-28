"""
LeetCode Question #2161: Partition Array According to Given Pivot

Problem Statement:
You are given a 0-indexed integer array `nums` and an integer `pivot`. 
Rearrange `nums` such that the following conditions are satisfied:
1. Every element less than `pivot` appears before every element equal to `pivot`.
2. Every element equal to `pivot` appears before every element greater than `pivot`.
3. The relative order of the elements less than `pivot`, equal to `pivot`, and greater than `pivot` should be preserved.

Return the rearranged array.

Example 1:
Input: nums = [9, 12, 5, 10, 14, 3, 10], pivot = 10
Output: [9, 5, 3, 10, 10, 12, 14]
Explanation: 
- Elements less than pivot: [9, 5, 3]
- Elements equal to pivot: [10, 10]
- Elements greater than pivot: [12, 14]
The elements in each group remain in their original order.

Example 2:
Input: nums = [-3, 4, 3, 2], pivot = 2
Output: [-3, 2, 4, 3]
Explanation: 
- Elements less than pivot: [-3]
- Elements equal to pivot: [2]
- Elements greater than pivot: [4, 3]
The elements in each group remain in their original order.

Constraints:
- 1 <= nums.length <= 10^5
- -10^6 <= nums[i], pivot <= 10^6
"""

# Python Solution
def pivotArray(nums, pivot):
    """
    Rearranges the array according to the given pivot.

    :param nums: List[int] - The input array of integers.
    :param pivot: int - The pivot value.
    :return: List[int] - The rearranged array.
    """
    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []

    for num in nums:
        if num < pivot:
            less_than_pivot.append(num)
        elif num == pivot:
            equal_to_pivot.append(num)
        else:
            greater_than_pivot.append(num)

    return less_than_pivot + equal_to_pivot + greater_than_pivot


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [9, 12, 5, 10, 14, 3, 10]
    pivot1 = 10
    print(pivotArray(nums1, pivot1))  # Output: [9, 5, 3, 10, 10, 12, 14]

    # Test Case 2
    nums2 = [-3, 4, 3, 2]
    pivot2 = 2
    print(pivotArray(nums2, pivot2))  # Output: [-3, 2, 4, 3]

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    pivot3 = 3
    print(pivotArray(nums3, pivot3))  # Output: [1, 2, 3, 4, 5]

    # Test Case 4
    nums4 = [5, 5, 5, 5]
    pivot4 = 5
    print(pivotArray(nums4, pivot4))  # Output: [5, 5, 5, 5]

    # Test Case 5
    nums5 = [10, -10, 0, 10, -5, 10]
    pivot5 = 10
    print(pivotArray(nums5, pivot5))  # Output: [-10, 0, -5, 10, 10, 10]


# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `nums` array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the `nums` array.

Space Complexity:
- Three additional lists (`less_than_pivot`, `equal_to_pivot`, `greater_than_pivot`) are created to store elements based on their relation to the pivot.
- In the worst case, the combined size of these lists is equal to the size of the input array `nums`.
- Therefore, the space complexity is O(n).
"""

# Topic: Arrays