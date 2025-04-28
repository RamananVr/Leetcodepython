"""
LeetCode Problem #324: Wiggle Sort II

Problem Statement:
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
You may assume the input array always has a valid answer.

Example 1:
Input: nums = [1, 5, 1, 1, 6, 4]
Output: [1, 6, 1, 5, 1, 4]
Explanation: [1, 6, 1, 5, 1, 4] is a valid answer. Other valid answers include [1, 6, 1, 4, 1, 5].

Example 2:
Input: nums = [1, 3, 2, 2, 3, 1]
Output: [2, 3, 1, 3, 1, 2]

Constraints:
- 1 <= nums.length <= 5 * 10^4
- 0 <= nums[i] <= 5000
- It is guaranteed that there will be an answer for the given input nums.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""

# Solution
def wiggleSort(nums):
    """
    Reorders the array nums in-place to satisfy the wiggle sort condition:
    nums[0] < nums[1] > nums[2] < nums[3]...

    Args:
    nums (List[int]): The input array.

    Returns:
    None: The function modifies nums in-place.
    """
    # Step 1: Sort the array
    nums.sort()

    # Step 2: Split the sorted array into two halves
    n = len(nums)
    mid = (n + 1) // 2  # Midpoint for the left half
    left = nums[:mid]   # Smaller half
    right = nums[mid:]  # Larger half

    # Step 3: Interleave the two halves in reverse order
    # Reverse both halves to ensure the largest elements are placed first
    left.reverse()
    right.reverse()

    # Step 4: Merge the two halves into the original array
    nums[::2] = left  # Fill even indices with the left half
    nums[1::2] = right  # Fill odd indices with the right half

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 5, 1, 1, 6, 4]
    wiggleSort(nums1)
    print(nums1)  # Output: [1, 6, 1, 5, 1, 4] (or other valid wiggle sort)

    # Test Case 2
    nums2 = [1, 3, 2, 2, 3, 1]
    wiggleSort(nums2)
    print(nums2)  # Output: [2, 3, 1, 3, 1, 2] (or other valid wiggle sort)

    # Test Case 3
    nums3 = [4, 5, 5, 6]
    wiggleSort(nums3)
    print(nums3)  # Output: [5, 6, 4, 5] (or other valid wiggle sort)

    # Test Case 4
    nums4 = [1, 1, 2, 2, 3, 3]
    wiggleSort(nums4)
    print(nums4)  # Output: [2, 3, 1, 3, 1, 2] (or other valid wiggle sort)

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n).
- Splitting the array and reversing the halves each take O(n).
- Merging the two halves into the original array takes O(n).
Overall, the time complexity is O(n log n).

Space Complexity:
- The function uses O(n) extra space to store the two halves (left and right).
- The in-place modification of the original array does not require additional space.
Overall, the space complexity is O(n).
"""

# Topic: Arrays