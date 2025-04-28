"""
LeetCode Problem #1224: Maximum Equal Frequency

Problem Statement:
Given an array `nums` of positive integers, return the maximum possible value of `x` such that there is a prefix of `nums[0:x]` 
that satisfies the following conditions:
1. All the numbers in the prefix have the same frequency (e.g., [1,2,3,4] or [1,1,2,2,3,3]).
2. Or, if you remove one element from the prefix, all the remaining numbers will have the same frequency 
   (e.g., [1,1,1,2,2,2,3] or [1,1,2,2,3,3,3]).

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

def maxEqualFreq(nums):
    """
    Function to find the maximum possible value of x such that the prefix nums[0:x] satisfies the conditions.
    """
    from collections import Counter

    freq = Counter()  # Frequency of each number
    count = Counter()  # Count of frequencies
    max_len = 0

    for i, num in enumerate(nums):
        # Update frequency of the current number
        if freq[num] > 0:
            count[freq[num]] -= 1
            if count[freq[num]] == 0:
                del count[freq[num]]
        freq[num] += 1
        count[freq[num]] += 1

        # Check if the current prefix satisfies the conditions
        if len(count) == 1:
            # Case 1: All numbers have the same frequency
            freq_val = next(iter(count))
            if freq_val == 1 or count[freq_val] == 1:
                max_len = i + 1
        elif len(count) == 2:
            # Case 2: Two different frequencies
            freq1, freq2 = count.keys()
            if (freq1 == 1 and count[freq1] == 1) or (freq2 == 1 and count[freq2] == 1):
                max_len = i + 1
            elif abs(freq1 - freq2) == 1:
                if (freq1 > freq2 and count[freq1] == 1) or (freq2 > freq1 and count[freq2] == 1):
                    max_len = i + 1

    return max_len

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 2, 1, 1, 5, 3, 3, 5]
    print(maxEqualFreq(nums1))  # Expected Output: 7

    # Test Case 2
    nums2 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]
    print(maxEqualFreq(nums2))  # Expected Output: 13

    # Test Case 3
    nums3 = [10, 10, 10, 10, 10, 10, 10]
    print(maxEqualFreq(nums3))  # Expected Output: 7

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(maxEqualFreq(nums4))  # Expected Output: 9

    # Test Case 5
    nums5 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
    print(maxEqualFreq(nums5))  # Expected Output: 10

"""
Time Complexity:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Thus, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm uses two Counter objects to store frequencies and counts, which at most will have O(n) unique keys.
- Thus, the space complexity is O(n).

Topic: Arrays, Hash Table
"""