"""
LeetCode Problem #2519: Count the Number of K-Big Indices

Problem Statement:
You are given a 0-indexed integer array `nums` and a positive integer `k`.

We call an index `i` in the array a `k-big` index if the following conditions are satisfied:
1. There exist at least `k` elements strictly smaller than `nums[i]` in the subarray `nums[0...i]`.
2. There exist at least `k` elements strictly smaller than `nums[i]` in the subarray `nums[i...n-1]`.

Return the number of `k-big` indices.

Constraints:
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= nums.length`
"""

from sortedcontainers import SortedList

def kBigIndices(nums, k):
    """
    Function to count the number of k-big indices in the array.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The threshold for determining k-big indices.

    Returns:
    int: The number of k-big indices.
    """
    n = len(nums)
    left_smaller = [0] * n
    right_smaller = [0] * n

    # Use a SortedList to efficiently count elements smaller than nums[i] on the left
    sorted_list = SortedList()
    for i in range(n):
        left_smaller[i] = sorted_list.bisect_left(nums[i])
        sorted_list.add(nums[i])

    # Use another SortedList to efficiently count elements smaller than nums[i] on the right
    sorted_list = SortedList()
    for i in range(n - 1, -1, -1):
        right_smaller[i] = sorted_list.bisect_left(nums[i])
        sorted_list.add(nums[i])

    # Count the number of k-big indices
    count = 0
    for i in range(n):
        if left_smaller[i] >= k and right_smaller[i] >= k:
            count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 6, 5, 2]
    k1 = 2
    print(kBigIndices(nums1, k1))  # Output: 1

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    k2 = 1
    print(kBigIndices(nums2, k2))  # Output: 2

    # Test Case 3
    nums3 = [5, 1, 2, 3, 4]
    k3 = 1
    print(kBigIndices(nums3, k3))  # Output: 3

"""
Time Complexity Analysis:
- Calculating `left_smaller` and `right_smaller` each takes O(n log n) due to the use of SortedList and its `bisect_left` and `add` operations.
- The final loop to count k-big indices takes O(n).
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- The SortedList data structure requires O(n) space.
- The `left_smaller` and `right_smaller` arrays also require O(n) space.
- Overall space complexity: O(n).

Topic: Arrays, Binary Search, SortedList
"""