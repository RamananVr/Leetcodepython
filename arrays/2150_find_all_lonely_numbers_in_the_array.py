"""
LeetCode Question #2150: Find All Lonely Numbers in the Array

Problem Statement:
You are given an integer array `nums`. A number `x` is called lonely if it appears exactly once in the array, 
and none of its neighbors (`x + 1` and `x - 1`) appear in the array.

Return all lonely numbers in `nums`. You may return the answer in any order.

Example 1:
Input: nums = [10,6,5,8]
Output: [10,8]
Explanation:
- 10 is lonely because it appears exactly once and 9 and 11 are not in nums.
- 8 is lonely because it appears exactly once and 7 and 9 are not in nums.
- 5 and 6 are not lonely because they appear in nums.

Example 2:
Input: nums = [1,3,5,3]
Output: [1,5]
Explanation:
- 1 is lonely because it appears exactly once and 0 and 2 are not in nums.
- 5 is lonely because it appears exactly once and 4 and 6 are not in nums.
- 3 is not lonely because it appears twice.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^6
"""

# Python Solution
from collections import Counter

def findLonely(nums):
    """
    Finds all lonely numbers in the array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    List[int]: A list of lonely numbers.
    """
    count = Counter(nums)
    lonely_numbers = []
    
    for num in nums:
        if count[num] == 1 and count[num - 1] == 0 and count[num + 1] == 0:
            lonely_numbers.append(num)
    
    return lonely_numbers

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [10, 6, 5, 8]
    print(findLonely(nums1))  # Output: [10, 8]

    # Test Case 2
    nums2 = [1, 3, 5, 3]
    print(findLonely(nums2))  # Output: [1, 5]

    # Test Case 3
    nums3 = [7]
    print(findLonely(nums3))  # Output: [7]

    # Test Case 4
    nums4 = [4, 4, 4, 4]
    print(findLonely(nums4))  # Output: []

    # Test Case 5
    nums5 = [0, 2, 4, 6, 8]
    print(findLonely(nums5))  # Output: [0, 2, 4, 6, 8]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the Counter object takes O(n), where n is the length of the input array `nums`.
- Iterating through the array to check conditions takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- The Counter object uses O(u) space, where u is the number of unique elements in `nums`.
- In the worst case, u = n (all elements are unique), so space complexity is O(n).
- The output list `lonely_numbers` also uses O(k) space, where k is the number of lonely numbers.
- Overall space complexity: O(n).
"""

# Topic: Arrays