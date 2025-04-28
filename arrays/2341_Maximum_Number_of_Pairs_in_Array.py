"""
LeetCode Problem #2341: Maximum Number of Pairs in Array

Problem Statement:
You are given a 0-indexed integer array `nums`. In one operation, you can select two equal integers from `nums` and remove them from the array. 
Formally, you select two indices `i` and `j` such that `i != j` and `nums[i] == nums[j]`, then remove the integers at indices `i` and `j` from `nums`.

Return a 0-indexed integer array `answer` of size 2 where:
- `answer[0]` is the number of pairs that you can remove from `nums`.
- `answer[1]` is the number of leftover integers in `nums` after performing all possible operations.

Example:
Input: nums = [1,3,2,1,3,2,2]
Output: [3,1]

Explanation:
- Remove the pair (1,1), then nums = [3,2,3,2,2].
- Remove the pair (3,3), then nums = [2,2,2].
- Remove the pair (2,2), then nums = [2].
- At the end, there are 3 pairs removed and 1 number left.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100
"""

# Python Solution
from collections import Counter

def numberOfPairs(nums):
    """
    Calculate the number of pairs that can be removed and the number of leftover integers.

    :param nums: List[int] - The input array of integers.
    :return: List[int] - A list containing the number of pairs removed and the number of leftover integers.
    """
    count = Counter(nums)
    pairs = 0
    leftovers = 0
    
    for freq in count.values():
        pairs += freq // 2
        leftovers += freq % 2
    
    return [pairs, leftovers]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 2, 1, 3, 2, 2]
    print(numberOfPairs(nums1))  # Output: [3, 1]

    # Test Case 2
    nums2 = [1, 1]
    print(numberOfPairs(nums2))  # Output: [1, 0]

    # Test Case 3
    nums3 = [0]
    print(numberOfPairs(nums3))  # Output: [0, 1]

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    print(numberOfPairs(nums4))  # Output: [0, 5]

    # Test Case 5
    nums5 = [1, 1, 1, 1, 1, 1]
    print(numberOfPairs(nums5))  # Output: [3, 0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting the frequency of elements in `nums` using `Counter` takes O(n), where n is the length of the array.
- Iterating through the frequency dictionary takes O(k), where k is the number of unique elements in `nums`.
- Since k <= n, the overall time complexity is O(n).

Space Complexity:
- The `Counter` object stores the frequency of each unique element, which requires O(k) space, where k is the number of unique elements.
- In the worst case, k = n (all elements are unique), so the space complexity is O(n).

Overall:
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Topic: Arrays