"""
LeetCode Problem #2206: Divide Array Into Equal Pairs

Problem Statement:
You are given an integer array `nums` consisting of 2 * n integers.

You need to divide `nums` into `n` pairs such that:
- Each element belongs to exactly one pair.
- The elements present in a pair are equal.

Return `true` if you can divide `nums` into `n` pairs, otherwise return `false`.

Example 1:
Input: nums = [3, 2, 3, 2, 2, 2]
Output: true
Explanation: There are 6 elements in nums, so they can be divided into 3 pairs.
The pairs are (3, 3), (2, 2), (2, 2).

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
Explanation: There is no way to divide nums into pairs such that each pair consists of equal elements.

Constraints:
- nums.length == 2 * n
- 1 <= nums[i] <= 10^5
"""

# Solution
from collections import Counter

def divideArray(nums):
    """
    Determines if the array can be divided into pairs of equal elements.

    :param nums: List[int] - The input array of integers.
    :return: bool - True if the array can be divided into pairs, False otherwise.
    """
    # Count the frequency of each number in the array
    freq = Counter(nums)
    
    # Check if all frequencies are even
    for count in freq.values():
        if count % 2 != 0:
            return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 2, 3, 2, 2, 2]
    print(divideArray(nums1))  # Output: True

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print(divideArray(nums2))  # Output: False

    # Test Case 3
    nums3 = [1, 1, 2, 2, 3, 3]
    print(divideArray(nums3))  # Output: True

    # Test Case 4
    nums4 = [1, 1, 1, 1, 2, 2]
    print(divideArray(nums4))  # Output: True

    # Test Case 5
    nums5 = [1, 1, 1, 2, 2, 2]
    print(divideArray(nums5))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of elements using `Counter(nums)` takes O(n), where n is the length of the array.
- Iterating through the frequency dictionary to check if all counts are even takes O(k), where k is the number of unique elements in the array.
- Overall, the time complexity is O(n + k). Since k <= n, the time complexity simplifies to O(n).

Space Complexity:
- The space complexity is O(k), where k is the number of unique elements in the array, due to the storage of the frequency dictionary.
- In the worst case, k = n (all elements are unique), so the space complexity is O(n).

Topic: Arrays
"""