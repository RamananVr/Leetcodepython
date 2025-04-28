"""
LeetCode Question #1121: Divide Array Into Increasing Sequences

Problem Statement:
You are given an integer array nums and an integer k. Split the array into k non-empty subsets such that:
1. Each subset is strictly increasing.
2. The largest subset size is minimized.

Return true if it is possible to split the array into k subsets satisfying these conditions, otherwise return false.

Example:
Input: nums = [5, 6, 7, 8, 9], k = 2
Output: true
Explanation: We can split the array into subsets [5, 6, 7] and [8, 9].

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= nums.length
"""

# Python Solution
from collections import Counter

def canDivideIntoSubsequences(nums, k):
    """
    Determines if the array can be divided into k non-empty subsets such that
    each subset is strictly increasing and the largest subset size is minimized.

    :param nums: List[int] - The input array
    :param k: int - The number of subsets
    :return: bool - True if the division is possible, False otherwise
    """
    # Count the frequency of each number in the array
    freq = Counter(nums)
    
    # Find the maximum frequency of any number
    max_freq = max(freq.values())
    
    # Check if the array can be divided into k subsets
    return len(nums) >= k * max_freq

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [5, 6, 7, 8, 9]
    k1 = 2
    print(canDivideIntoSubsequences(nums1, k1))  # Output: True

    # Test Case 2
    nums2 = [1, 2, 2, 3, 3, 4, 4]
    k2 = 3
    print(canDivideIntoSubsequences(nums2, k2))  # Output: True

    # Test Case 3
    nums3 = [1, 2, 2, 3, 3, 4, 4]
    k3 = 4
    print(canDivideIntoSubsequences(nums3, k3))  # Output: False

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    k4 = 2
    print(canDivideIntoSubsequences(nums4, k4))  # Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting the frequency of elements in the array takes O(n), where n is the length of nums.
- Finding the maximum frequency in the frequency dictionary takes O(m), where m is the number of unique elements in nums.
- Overall, the time complexity is O(n + m), which is effectively O(n) since m <= n.

Space Complexity:
- The space complexity is O(m), where m is the number of unique elements in nums, due to the frequency dictionary.
- In the worst case, m = n (all elements are unique), so the space complexity is O(n).
"""

# Topic: Arrays