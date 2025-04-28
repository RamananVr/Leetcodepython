"""
LeetCode Problem #220: Contains Duplicate III

Problem Statement:
You are given an integer array `nums` and two integers `k` and `t`. 
Return true if there are two distinct indices `i` and `j` in the array such that:
- `abs(nums[i] - nums[j]) <= t`, and
- `abs(i - j) <= k`.

If no such indices exist, return false.

Constraints:
- 0 <= nums.length <= 2 * 10^4
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^4
- 0 <= t <= 2^31 - 1
"""

from sortedcontainers import SortedList

def containsNearbyAlmostDuplicate(nums, k, t):
    """
    Determines if there are two distinct indices i and j in the array such that:
    - abs(nums[i] - nums[j]) <= t
    - abs(i - j) <= k

    Args:
    nums (List[int]): The input array of integers.
    k (int): The maximum index difference.
    t (int): The maximum value difference.

    Returns:
    bool: True if such indices exist, False otherwise.
    """
    if t < 0 or k <= 0:
        return False

    sorted_list = SortedList()

    for i in range(len(nums)):
        # Check if there is a number in the sorted list within the range [nums[i] - t, nums[i] + t]
        if sorted_list:
            pos = sorted_list.bisect_left(nums[i] - t)
            if pos < len(sorted_list) and abs(sorted_list[pos] - nums[i]) <= t:
                return True

        # Add the current number to the sorted list
        sorted_list.add(nums[i])

        # Maintain the sliding window of size k
        if i >= k:
            sorted_list.remove(nums[i - k])

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 1]
    k1 = 3
    t1 = 0
    print(containsNearbyAlmostDuplicate(nums1, k1, t1))  # Expected: True

    # Test Case 2
    nums2 = [1, 0, 1, 1]
    k2 = 1
    t2 = 2
    print(containsNearbyAlmostDuplicate(nums2, k2, t2))  # Expected: True

    # Test Case 3
    nums3 = [1, 5, 9, 1, 5, 9]
    k3 = 2
    t3 = 3
    print(containsNearbyAlmostDuplicate(nums3, k3, t3))  # Expected: False

    # Test Case 4
    nums4 = []
    k4 = 0
    t4 = 0
    print(containsNearbyAlmostDuplicate(nums4, k4, t4))  # Expected: False

    # Test Case 5
    nums5 = [2, 2]
    k5 = 0
    t5 = 0
    print(containsNearbyAlmostDuplicate(nums5, k5, t5))  # Expected: False

"""
Time Complexity:
- The main loop iterates over the `nums` array, which has a length of `n`.
- For each iteration, we perform operations on a `SortedList`:
  - Adding an element: O(log k)
  - Removing an element: O(log k)
  - Searching for a range: O(log k)
  Since the size of the `SortedList` is limited to `k`, the overall complexity is O(n log k).

Space Complexity:
- The `SortedList` stores at most `k` elements, so the space complexity is O(k).

Topic: Arrays, Sliding Window, Sorted Data Structure
"""