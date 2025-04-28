"""
LeetCode Problem #2426: Number of Pairs Satisfying Inequality

Problem Statement:
You are given two 0-indexed integer arrays `nums1` and `nums2`, each of size `n`, and an integer `diff`. 
Find the number of pairs `(i, j)` where:
    - 0 <= i < j < n, and
    - nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.

Return the number of pairs that satisfy the conditions.

Constraints:
- `n == nums1.length == nums2.length`
- `2 <= n <= 10^5`
- `-10^4 <= nums1[i], nums2[i] <= 10^4`
- `-10^4 <= diff <= 10^4`
"""

from sortedcontainers import SortedList

def numberOfPairs(nums1, nums2, diff):
    """
    Function to calculate the number of pairs (i, j) satisfying the given inequality.

    Args:
    nums1 (List[int]): First list of integers.
    nums2 (List[int]): Second list of integers.
    diff (int): The difference value.

    Returns:
    int: The number of pairs satisfying the inequality.
    """
    n = len(nums1)
    sl = SortedList()
    count = 0

    for i in range(n):
        # Calculate the value to search for in the sorted list
        target = nums1[i] - nums2[i] + diff
        # Count the number of elements in the sorted list <= target
        count += sl.bisect_right(target)
        # Add the current value to the sorted list
        sl.add(nums1[i] - nums2[i])

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 2, 5]
    nums2 = [2, 2, 1]
    diff = 1
    print(numberOfPairs(nums1, nums2, diff))  # Output: 3

    # Test Case 2
    nums1 = [1, 4, 2, 3]
    nums2 = [2, 1, 4, 1]
    diff = 2
    print(numberOfPairs(nums1, nums2, diff))  # Output: 4

    # Test Case 3
    nums1 = [1, 2]
    nums2 = [2, 1]
    diff = 0
    print(numberOfPairs(nums1, nums2, diff))  # Output: 1

"""
Time Complexity Analysis:
- The loop iterates over the `nums1` and `nums2` arrays, which takes O(n) time.
- For each iteration, the `bisect_right` operation and the `add` operation on the SortedList take O(log n) time.
- Therefore, the overall time complexity is O(n log n).

Space Complexity Analysis:
- The SortedList data structure is used to store up to `n` elements, which requires O(n) space.
- Thus, the space complexity is O(n).

Topic: Arrays, Binary Search, SortedList
"""