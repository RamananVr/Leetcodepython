"""
LeetCode Problem #1512: Number of Good Pairs

Problem Statement:
Given an array of integers `nums`, a pair `(i, j)` is called good if `nums[i] == nums[j]` and `i < j`.
Return the number of good pairs.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) (indexing starts from 0).

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array is a good pair.

Example 3:
Input: nums = [1,2,3]
Output: 0
Explanation: There are no good pairs.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

# Clean and Correct Python Solution
from collections import Counter

def numIdenticalPairs(nums):
    """
    Function to calculate the number of good pairs in the array.
    
    :param nums: List[int] - The input array of integers
    :return: int - The number of good pairs
    """
    count = Counter(nums)
    good_pairs = 0
    
    for freq in count.values():
        # If a number appears `freq` times, the number of good pairs is freq * (freq - 1) // 2
        good_pairs += (freq * (freq - 1)) // 2
    
    return good_pairs

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 1, 1, 3]
    print(numIdenticalPairs(nums1))  # Output: 4

    # Test Case 2
    nums2 = [1, 1, 1, 1]
    print(numIdenticalPairs(nums2))  # Output: 6

    # Test Case 3
    nums3 = [1, 2, 3]
    print(numIdenticalPairs(nums3))  # Output: 0

    # Test Case 4
    nums4 = [1]
    print(numIdenticalPairs(nums4))  # Output: 0

    # Test Case 5
    nums5 = [1, 2, 2, 3, 3, 3]
    print(numIdenticalPairs(nums5))  # Output: 4

"""
Time Complexity Analysis:
- Counting the frequency of elements in the array using `Counter` takes O(n), where n is the length of the array.
- Iterating through the frequency dictionary to calculate the number of good pairs takes O(k), where k is the number of unique elements in the array.
- In the worst case, k <= n, so the overall time complexity is O(n).

Space Complexity Analysis:
- The space complexity is O(k), where k is the number of unique elements in the array, as we store the frequency of each element in a dictionary.
- In the worst case, k <= n, so the space complexity is O(n).

Topic: Arrays
"""