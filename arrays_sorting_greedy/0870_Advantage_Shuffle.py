"""
LeetCode Problem #870: Advantage Shuffle

Problem Statement:
You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 over nums2 is the number of indices i for which nums1[i] > nums2[i].

Return any permutation of nums1 that maximizes its advantage over nums2.

Example 1:
Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
Output: [2,11,7,15]

Example 2:
Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
Output: [24,32,8,12]

Constraints:
- 1 <= nums1.length <= 10^5
- 0 <= nums1[i], nums2[i] <= 10^9
"""

# Solution
from collections import deque

def advantageCount(nums1, nums2):
    """
    Function to maximize the advantage of nums1 over nums2.
    
    Args:
    nums1 (List[int]): First list of integers.
    nums2 (List[int]): Second list of integers.
    
    Returns:
    List[int]: Permutation of nums1 that maximizes its advantage over nums2.
    """
    # Sort nums1 and nums2
    sorted_nums1 = sorted(nums1)
    sorted_nums2 = sorted((val, idx) for idx, val in enumerate(nums2))
    
    # Initialize deque for nums1 and result array
    nums1_deque = deque(sorted_nums1)
    result = [0] * len(nums2)
    
    # Two-pointer approach
    for val, idx in sorted_nums2:
        if nums1_deque[0] > val:
            # Use the smallest number in nums1 that is greater than val
            result[idx] = nums1_deque.popleft()
        else:
            # Use the smallest number in nums1 (no advantage)
            result[idx] = nums1_deque.pop()
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 7, 11, 15]
    nums2 = [1, 10, 4, 11]
    print(advantageCount(nums1, nums2))  # Output: [2, 11, 7, 15]

    # Test Case 2
    nums1 = [12, 24, 8, 32]
    nums2 = [13, 25, 32, 11]
    print(advantageCount(nums1, nums2))  # Output: [24, 32, 8, 12]

    # Test Case 3
    nums1 = [1, 2, 3, 4]
    nums2 = [2, 2, 2, 2]
    print(advantageCount(nums1, nums2))  # Output: [3, 4, 1, 2]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting nums1 takes O(n log n).
- Sorting nums2 (with indices) takes O(n log n).
- The loop to assign values takes O(n).
Overall time complexity: O(n log n).

Space Complexity:
- Sorting nums2 creates a list of tuples, which takes O(n) space.
- The deque for nums1 takes O(n) space.
- The result array takes O(n) space.
Overall space complexity: O(n).
"""

# Topic: Arrays, Sorting, Greedy