"""
LeetCode Question #2856: Minimum Array Length After Pair Removals

Problem Statement:
You are given a 0-indexed integer array nums. In one operation, you can remove any two adjacent elements of nums that are equal.

For example, if nums = [1,2,2,3,3,3], you can:
- Remove the pair of 2's at index 1 and 2, making nums = [1,2,3,3,3].
- Remove the pair of 3's at index 3 and 4, making nums = [1,2,3,3].

Your task is to return the minimum possible length of the array after performing any number of such operations.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
"""

# Solution
def minLengthAfterRemovals(nums):
    """
    This function calculates the minimum possible length of the array after performing
    any number of pair removal operations.

    :param nums: List[int] - The input array of integers
    :return: int - The minimum possible length of the array
    """
    from collections import Counter

    # Count the frequency of each number in the array
    freq = Counter(nums)

    # Find the maximum frequency of any number
    max_freq = max(freq.values())

    # Calculate the minimum length of the array
    n = len(nums)
    if max_freq > n // 2:
        return 2 * max_freq - n
    else:
        return n % 2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 2, 3, 3, 3]
    print(minLengthAfterRemovals(nums1))  # Output: 1

    # Test Case 2
    nums2 = [1, 1, 1, 1, 1, 1]
    print(minLengthAfterRemovals(nums2))  # Output: 6

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(minLengthAfterRemovals(nums3))  # Output: 1

    # Test Case 4
    nums4 = [1, 1, 2, 2, 3, 3]
    print(minLengthAfterRemovals(nums4))  # Output: 0

    # Test Case 5
    nums5 = [1]
    print(minLengthAfterRemovals(nums5))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of elements using `Counter(nums)` takes O(n), where n is the length of the array.
- Finding the maximum frequency using `max(freq.values())` takes O(k), where k is the number of unique elements in the array.
- Overall, the time complexity is O(n + k). Since k <= n, the time complexity simplifies to O(n).

Space Complexity:
- The `Counter` object stores the frequency of each unique element, which requires O(k) space, where k is the number of unique elements.
- In the worst case, k = n (all elements are unique), so the space complexity is O(n).

Topic: Arrays
"""