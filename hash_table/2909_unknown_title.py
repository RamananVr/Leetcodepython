"""
LeetCode Problem #2909: Problem Statement

(Note: As of my knowledge cutoff in October 2023, LeetCode problem #2909 does not exist. 
Instead, I will create a hypothetical problem statement for this question.)

Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to determine if there exists a pair of distinct indices `(i, j)` such that:
1. `nums[i] == nums[j]`
2. The absolute difference between `i` and `j` is at most `k`.

Return `True` if such a pair exists, otherwise return `False`.

Example:
Input: nums = [1, 2, 3, 1], k = 3
Output: True
Explanation: nums[0] == nums[3] and abs(0 - 3) <= 3.

Input: nums = [1, 0, 1, 1], k = 1
Output: True
Explanation: nums[2] == nums[3] and abs(2 - 3) <= 1.

Input: nums = [1, 2, 3, 1, 2, 3], k = 2
Output: False
Explanation: No such pair exists.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5
"""

# Python Solution
def containsNearbyDuplicate(nums, k):
    """
    Determines if there exists a pair of indices (i, j) such that:
    1. nums[i] == nums[j]
    2. abs(i - j) <= k

    :param nums: List[int] - List of integers
    :param k: int - Maximum allowed index difference
    :return: bool - True if such a pair exists, False otherwise
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
    # Test Case 1
    nums1 = [1, 2, 3, 1]
    k1 = 3
    print(containsNearbyDuplicate(nums1, k1))  # Output: True

    # Test Case 2
    nums2 = [1, 0, 1, 1]
    k2 = 1
    print(containsNearbyDuplicate(nums2, k2))  # Output: True

    # Test Case 3
    nums3 = [1, 2, 3, 1, 2, 3]
    k3 = 2
    print(containsNearbyDuplicate(nums3, k3))  # Output: False

    # Test Case 4
    nums4 = [99, 99]
    k4 = 2
    print(containsNearbyDuplicate(nums4, k4))  # Output: True

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5]
    k5 = 0
    print(containsNearbyDuplicate(nums5, k5))  # Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the list of numbers once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input list `nums`.

Space Complexity:
- The algorithm uses a dictionary to store the last seen index of each number. In the worst case, the dictionary could store up to n entries (if all numbers are unique).
- Therefore, the space complexity is O(n).
"""

# Topic: Hash Table