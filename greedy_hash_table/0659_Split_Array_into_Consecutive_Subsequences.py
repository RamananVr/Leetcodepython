"""
LeetCode Problem #659: Split Array into Consecutive Subsequences

Problem Statement:
You are given an integer array `nums` sorted in ascending order. Return `true` if and only if you can split it into one or more subsequences such that both of the following conditions are true:
1. Each subsequence consists of consecutive integers and has a length of at least 3.
2. All integers in `nums` are used in exactly one subsequence.

Example 1:
Input: nums = [1,2,3,3,4,5]
Output: true
Explanation: nums can be split into the subsequences [1,2,3] and [3,4,5].

Example 2:
Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the subsequences [1,2,3,4,5] and [3,4,5].

Example 3:
Input: nums = [1,2,3,4,4,5]
Output: false
Explanation: It is impossible to split nums into consecutive subsequences of length at least 3.

Constraints:
- 1 <= nums.length <= 10^4
- -10^6 <= nums[i] <= 10^6
- nums is sorted in ascending order.
"""

from collections import Counter, defaultdict

def isPossible(nums):
    """
    Determines if the array can be split into one or more subsequences
    such that each subsequence consists of consecutive integers and has
    a length of at least 3.

    :param nums: List[int] - The input array of integers
    :return: bool - True if the array can be split as described, False otherwise
    """
    freq = Counter(nums)  # Count the frequency of each number
    append_freq = defaultdict(int)  # Tracks the end of subsequences

    for num in nums:
        if freq[num] == 0:  # If the number is already used, skip it
            continue

        # Try to append the number to an existing subsequence
        if append_freq[num] > 0:
            append_freq[num] -= 1
            append_freq[num + 1] += 1
        # Try to create a new subsequence starting with this number
        elif freq[num + 1] > 0 and freq[num + 2] > 0:
            freq[num + 1] -= 1
            freq[num + 2] -= 1
            append_freq[num + 3] += 1
        else:
            return False

        freq[num] -= 1  # Use the current number

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 3, 4, 5]
    print(isPossible(nums1))  # Output: True

    # Test Case 2
    nums2 = [1, 2, 3, 3, 4, 4, 5, 5]
    print(isPossible(nums2))  # Output: True

    # Test Case 3
    nums3 = [1, 2, 3, 4, 4, 5]
    print(isPossible(nums3))  # Output: False

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(isPossible(nums4))  # Output: True

    # Test Case 5
    nums5 = [1, 2, 3, 5, 6, 7]
    print(isPossible(nums5))  # Output: False

"""
Time Complexity Analysis:
- The algorithm iterates through the `nums` array once, and for each number, it performs constant-time operations (checking and updating counters).
- The overall time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The algorithm uses two additional data structures: `freq` (a Counter) and `append_freq` (a defaultdict).
- Both of these structures can store at most n keys in the worst case, where n is the number of unique elements in `nums`.
- The overall space complexity is O(n).

Topic: Greedy, Hash Table
"""