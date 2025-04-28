"""
LeetCode Problem #2190: Most Frequent Number Following Key In an Array

Problem Statement:
You are given a 0-indexed integer array `nums` and an integer `key`, which is present in `nums`.

For every unique integer `target` in `nums`, count the number of times `target` immediately follows an occurrence of `key` in `nums`. Return the `target` with the maximum count. The test cases are generated such that the `target` with the maximum count is unique.

Example 1:
Input: nums = [1, 100, 200, 1, 100], key = 1
Output: 100
Explanation: For key = 1, the targets are [100, 100]. The count for 100 is 2, which is the maximum.

Example 2:
Input: nums = [2, 2, 2, 2, 3], key = 2
Output: 2
Explanation: For key = 2, the targets are [2, 2, 2]. The count for 2 is 3, which is the maximum.

Constraints:
- 2 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
- The test cases are generated such that the answer is unique.
- key is present in nums.
"""

def mostFrequent(nums, key):
    """
    Finds the most frequent number that follows the given key in the array.

    :param nums: List[int] - The input array of integers.
    :param key: int - The key whose following numbers are to be analyzed.
    :return: int - The most frequent number following the key.
    """
    from collections import defaultdict

    # Dictionary to store the frequency of numbers following the key
    freq = defaultdict(int)

    # Iterate through the array to count occurrences
    for i in range(len(nums) - 1):
        if nums[i] == key:
            freq[nums[i + 1]] += 1

    # Find the number with the maximum frequency
    return max(freq, key=freq.get)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 100, 200, 1, 100]
    key1 = 1
    print(mostFrequent(nums1, key1))  # Output: 100

    # Test Case 2
    nums2 = [2, 2, 2, 2, 3]
    key2 = 2
    print(mostFrequent(nums2, key2))  # Output: 2

    # Test Case 3
    nums3 = [1, 2, 3, 1, 2, 3, 1, 3]
    key3 = 1
    print(mostFrequent(nums3, key3))  # Output: 2

    # Test Case 4
    nums4 = [4, 4, 4, 5, 6, 4, 5, 5]
    key4 = 4
    print(mostFrequent(nums4, key4))  # Output: 5


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array once, making it O(n), where n is the length of the array.
- The `max` function iterates over the dictionary keys, which is O(k), where k is the number of unique numbers following the key.
- In the worst case, k can be at most n, so the overall time complexity is O(n).

Space Complexity:
- The algorithm uses a dictionary to store the frequency of numbers following the key. In the worst case, the dictionary can have up to n entries (if all numbers are unique), so the space complexity is O(n).

Topic: Arrays
"""