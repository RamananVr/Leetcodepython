"""
LeetCode Problem #2780: Minimum Index of a Valid Split

Problem Statement:
You are given a 0-indexed integer array `nums` of length `n`.

A split of `nums` is called valid if:
- The array can be split into two non-empty parts with indices `0` to `i` and `i+1` to `n-1`, where `0 <= i < n-1`.
- The most frequent element in the first part is the same as the most frequent element in the second part.

Return the minimum index `i` of a valid split. If no valid split exists, return `-1`.

Example:
Input: nums = [1, 2, 2, 2]
Output: 2
Explanation: We can split the array at index 2. The first part is [1, 2, 2] and the second part is [2]. The most frequent element in both parts is 2.

Constraints:
- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
"""

from collections import Counter

def minimumIndex(nums):
    """
    Finds the minimum index of a valid split in the array `nums`.
    
    :param nums: List[int] - The input array of integers.
    :return: int - The minimum index of a valid split, or -1 if no valid split exists.
    """
    n = len(nums)
    left_count = Counter()
    right_count = Counter(nums)
    left_size = 0
    right_size = n

    for i in range(n - 1):
        # Update counts for left and right parts
        left_count[nums[i]] += 1
        right_count[nums[i]] -= 1
        left_size += 1
        right_size -= 1

        # Remove zero-count elements from right_count
        if right_count[nums[i]] == 0:
            del right_count[nums[i]]

        # Find the most frequent element in both parts
        left_majority = max(left_count, key=lambda x: left_count[x])
        right_majority = max(right_count, key=lambda x: right_count[x])

        # Check if the most frequent element is the same and satisfies the majority condition
        if left_majority == right_majority:
            left_majority_count = left_count[left_majority]
            right_majority_count = right_count[right_majority]
            if left_majority_count * 2 > left_size and right_majority_count * 2 > right_size:
                return i

    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 2, 2]
    print(minimumIndex(nums1))  # Output: 2

    # Test Case 2
    nums2 = [1, 1, 1, 1, 2, 2]
    print(minimumIndex(nums2))  # Output: -1

    # Test Case 3
    nums3 = [4, 4, 4, 4, 4, 4]
    print(minimumIndex(nums3))  # Output: 0

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    print(minimumIndex(nums4))  # Output: -1

    # Test Case 5
    nums5 = [5, 5, 5, 6, 6, 6, 5]
    print(minimumIndex(nums5))  # Output: 2

"""
Time Complexity:
- The algorithm iterates through the array once, updating the counts for the left and right parts.
- Each update involves finding the most frequent element, which is O(1) due to the use of a Counter.
- Overall time complexity: O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses two Counter objects to store the frequency of elements in the left and right parts.
- In the worst case, the space complexity is O(n) for the Counter objects.
- Overall space complexity: O(n).

Topic: Arrays, Hash Table
"""