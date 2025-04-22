"""
LeetCode Question #219: Contains Duplicate II

Problem Statement:
Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5
"""

# Solution
def containsNearbyDuplicate(nums, k):
    """
    Determines if there are two distinct indices i and j in the array such that:
    nums[i] == nums[j] and abs(i - j) <= k.

    :param nums: List[int] - The input array of integers.
    :param k: int - The maximum allowed index difference.
    :return: bool - True if such indices exist, False otherwise.
    """
    # Dictionary to store the last seen index of each number
    index_map = {}
    
    for i, num in enumerate(nums):
        # Check if the number exists in the map and the difference is within k
        if num in index_map and i - index_map[num] <= k:
            return True
        # Update the last seen index of the number
        index_map[num] = i
    
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
- The function iterates through the `nums` array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the `nums` array.

Space Complexity:
- The function uses a dictionary (`index_map`) to store the last seen index of each number.
- In the worst case, the dictionary could store all unique numbers in `nums`.
- Therefore, the space complexity is O(min(n, u)), where u is the number of unique elements in `nums`.

Overall:
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Topic: Hash Table