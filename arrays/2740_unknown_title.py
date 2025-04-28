"""
LeetCode Problem #2740: Find the Value of the Partition

Problem Statement:
You are given an integer array `nums` of length `n`. You need to partition the array into two non-empty parts such that:
- The left part contains `left` elements, and the right part contains `right` elements.
- Every element in the left part is less than or equal to every element in the right part.

The value of the partition is defined as:
    max(left) - min(right)

Return the minimum value of the partition.

Notes:
- The partition must be valid, meaning both the left and right parts must be non-empty.
- It is guaranteed that such a partition exists.

Constraints:
- 2 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
"""

def findValueOfPartition(nums):
    """
    Function to find the minimum value of the partition.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The minimum value of the partition.
    """
    # Sort the array to ensure the left part is <= right part
    nums.sort()
    
    # Initialize the minimum difference to a large value
    min_diff = float('inf')
    
    # Iterate through the sorted array to find the minimum difference
    for i in range(1, len(nums)):
        min_diff = min(min_diff, nums[i] - nums[i - 1])
    
    return min_diff

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 2, 4]
    print(findValueOfPartition(nums1))  # Output: 1

    # Test Case 2
    nums2 = [10, 100, 300, 200]
    print(findValueOfPartition(nums2))  # Output: 100

    # Test Case 3
    nums3 = [5, 8, 6, 3]
    print(findValueOfPartition(nums3))  # Output: 1

    # Test Case 4
    nums4 = [1, 2]
    print(findValueOfPartition(nums4))  # Output: 1

    # Test Case 5
    nums5 = [100, 200, 300, 400, 500]
    print(findValueOfPartition(nums5))  # Output: 100

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- Iterating through the sorted array to find the minimum difference takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- Sorting the array may require O(n) additional space depending on the sorting algorithm used.
- No additional data structures are used, so the space complexity is O(1) (excluding input storage).

Primary Topic: Arrays
"""