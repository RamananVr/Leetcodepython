"""
LeetCode Question #2537: Count the Number of Good Subarrays

Problem Statement:
You are given an integer array `nums` and an integer `k`. A subarray is called good if there are at least `k` pairs of indices `(i, j)` such that `i < j` and `nums[i] == nums[j]`.

Return the number of good subarrays of `nums`.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
- `1 <= nums.length <= 10^5`
- `1 <= nums[i], k <= 10^9`
"""

from collections import defaultdict

def countGood(nums, k):
    """
    Function to count the number of good subarrays in the given array.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The minimum number of pairs required for a subarray to be good.

    Returns:
    int: The number of good subarrays.
    """
    n = len(nums)
    count = defaultdict(int)
    left = 0
    total_pairs = 0
    result = 0

    for right in range(n):
        # Add the current number to the count
        total_pairs += count[nums[right]]
        count[nums[right]] += 1

        # Shrink the window from the left until the subarray is no longer good
        while total_pairs >= k:
            result += n - right
            count[nums[left]] -= 1
            total_pairs -= count[nums[left]]
            left += 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 1, 1]
    k1 = 6
    print(countGood(nums1, k1))  # Output: 1

    # Test Case 2
    nums2 = [3, 1, 4, 3, 2, 2, 4]
    k2 = 2
    print(countGood(nums2, k2))  # Output: 4

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    k3 = 1
    print(countGood(nums3, k3))  # Output: 0

"""
Time Complexity Analysis:
- The algorithm uses a sliding window approach, where the `right` pointer iterates through the array once, and the `left` pointer adjusts as needed.
- Each element is added and removed from the `count` dictionary at most once.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity Analysis:
- The space complexity is O(u), where u is the number of unique elements in the array `nums`, as we use a dictionary to store the counts of elements.

Topic: Sliding Window, Hash Table
"""