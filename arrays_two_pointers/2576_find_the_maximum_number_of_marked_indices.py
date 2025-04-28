"""
LeetCode Question #2576: Find the Maximum Number of Marked Indices

Problem Statement:
You are given a 0-indexed integer array nums. Initially, all of the indices are unmarked. You are allowed to make
pairs of indices (i, j) such that:
    - 0 <= i < j < nums.length
    - 2 * nums[i] <= nums[j]

A pair (i, j) is called a marked pair if both i and j are unmarked. You need to mark both indices i and j in a marked
pair. Note that an index can be marked at most once.

Return the maximum number of marked indices that you can obtain after marking pairs.

Constraints:
    - 1 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^9
"""

# Solution
def maxNumOfMarkedIndices(nums):
    """
    Finds the maximum number of marked indices in the array nums.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The maximum number of marked indices.
    """
    # Sort the array to facilitate pairing
    nums.sort()
    n = len(nums)
    marked_count = 0

    # Use two pointers to find valid pairs
    left, right = 0, n // 2
    while right < n:
        if 2 * nums[left] <= nums[right]:
            # Mark both indices
            marked_count += 2
            left += 1
        right += 1

    return marked_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 5, 2, 4]
    print(maxNumOfMarkedIndices(nums1))  # Expected Output: 2

    # Test Case 2
    nums2 = [9, 2, 5, 4]
    print(maxNumOfMarkedIndices(nums2))  # Expected Output: 4

    # Test Case 3
    nums3 = [7, 6, 8]
    print(maxNumOfMarkedIndices(nums3))  # Expected Output: 0

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    print(maxNumOfMarkedIndices(nums4))  # Expected Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The two-pointer approach iterates through the array once, which takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The algorithm uses O(1) additional space, as it operates directly on the input array and uses a few variables.
- Overall space complexity: O(1).

Topic: Arrays, Two Pointers
"""