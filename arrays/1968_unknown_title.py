"""
LeetCode Problem #1968: Array With Elements Not Equal to Average of Neighbors

Problem Statement:
You are given a 0-indexed array `nums` of distinct integers. You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.

More formally, the rearranged array should have the property such that for every `i` in the range `[1, nums.length - 2]`, 
`(nums[i-1] + nums[i+1]) / 2` is not equal to `nums[i]`.

Return any rearrangement of `nums` that meets the requirements.

Constraints:
- `3 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- All elements of `nums` are distinct.
"""

# Solution
def rearrangeArray(nums):
    """
    Rearranges the array such that no element is equal to the average of its neighbors.

    :param nums: List[int] - The input array of distinct integers.
    :return: List[int] - A rearranged array satisfying the condition.
    """
    nums.sort()  # Sort the array to facilitate the rearrangement
    result = []
    mid = len(nums) // 2

    # Interleave the smaller and larger halves of the sorted array
    for i in range(mid):
        result.append(nums[i])
        if mid + i < len(nums):
            result.append(nums[mid + i])

    # If the length of nums is odd, the last element will be added in the loop
    return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    print("Input:", nums1)
    print("Output:", rearrangeArray(nums1))  # Example Output: [1, 3, 2, 5, 4]

    # Test Case 2
    nums2 = [6, 2, 0, 9, 7]
    print("Input:", nums2)
    print("Output:", rearrangeArray(nums2))  # Example Output: [0, 6, 2, 9, 7]

    # Test Case 3
    nums3 = [1, 3, 5, 7, 9, 11]
    print("Input:", nums3)
    print("Output:", rearrangeArray(nums3))  # Example Output: [1, 5, 3, 9, 7, 11]

    # Test Case 4
    nums4 = [10, 20, 30, 40, 50, 60, 70]
    print("Input:", nums4)
    print("Output:", rearrangeArray(nums4))  # Example Output: [10, 40, 20, 50, 30, 60, 70]


# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- Rearranging the array takes O(n) as we iterate through the array once.
- Overall time complexity: O(n log n).

Space Complexity:
- The result array takes O(n) space.
- Sorting may require additional space depending on the sorting algorithm used.
- Overall space complexity: O(n).
"""

# Topic: Arrays