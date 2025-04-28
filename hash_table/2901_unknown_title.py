"""
LeetCode Problem #2901: Problem Statement

Given a list of integers `nums` and an integer `k`, your task is to determine if there exists a pair of distinct indices `i` and `j` in the array such that:
1. `nums[i] == nums[j]`, and
2. The absolute difference between `i` and `j` is at most `k`.

Return `True` if such a pair exists, otherwise return `False`.

Constraints:
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`
"""

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    """
    Determines if there exists a pair of indices i and j such that:
    1. nums[i] == nums[j]
    2. abs(i - j) <= k

    Args:
    nums (list[int]): List of integers.
    k (int): Maximum allowed index difference.

    Returns:
    bool: True if such a pair exists, False otherwise.
    """
    # Dictionary to store the last seen index of each number
    last_seen = {}

    for i, num in enumerate(nums):
        # Check if the number has been seen before and the index difference is within k
        if num in last_seen and i - last_seen[num] <= k:
            return True
        # Update the last seen index of the current number
        last_seen[num] = i

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Pair exists within k distance
    nums1 = [1, 2, 3, 1]
    k1 = 3
    print(containsNearbyDuplicate(nums1, k1))  # Expected: True

    # Test Case 2: Pair exists but exceeds k distance
    nums2 = [1, 0, 1, 1]
    k2 = 1
    print(containsNearbyDuplicate(nums2, k2))  # Expected: True

    # Test Case 3: No duplicate pair exists
    nums3 = [1, 2, 3, 4, 5]
    k3 = 2
    print(containsNearbyDuplicate(nums3, k3))  # Expected: False

    # Test Case 4: Edge case with k = 0
    nums4 = [1, 2, 3, 1]
    k4 = 0
    print(containsNearbyDuplicate(nums4, k4))  # Expected: False

    # Test Case 5: Large k value
    nums5 = [1, 2, 3, 1, 2, 3]
    k5 = 2
    print(containsNearbyDuplicate(nums5, k5))  # Expected: False

"""
Time Complexity Analysis:
- The algorithm iterates through the list of numbers once, performing O(1) operations for each element (dictionary lookup and update).
- Therefore, the time complexity is O(n), where n is the length of the input list `nums`.

Space Complexity Analysis:
- The algorithm uses a dictionary to store the last seen index of each number. In the worst case, the dictionary could store up to n entries (if all numbers are unique).
- Therefore, the space complexity is O(n).

Topic: Hash Table
"""