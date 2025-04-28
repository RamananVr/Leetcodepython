"""
LeetCode Question #2610: Convert an Array Into a 2D Array With Conditions

Problem Statement:
You are given an integer array `nums`. You need to convert it into a 2D array following these conditions:
1. Each subarray in the resulting 2D array must contain only unique elements.
2. The sum of the lengths of all subarrays must be equal to the length of `nums`.
3. If there are multiple valid answers, return any of them.

Return the resulting 2D array. It is guaranteed that the given input always has a valid answer.

Example:
Input: nums = [1, 3, 4, 1, 2, 3, 1]
Output: [[1, 3, 4, 2], [1, 3], [1]]

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100
"""

# Solution
from collections import defaultdict

def groupElements(nums):
    """
    Convert an array into a 2D array with conditions.

    Args:
    nums (List[int]): The input array.

    Returns:
    List[List[int]]: The resulting 2D array.
    """
    # Dictionary to track the frequency of each number
    freq = defaultdict(int)
    
    # Count the frequency of each number in nums
    for num in nums:
        freq[num] += 1
    
    # Create the 2D array
    result = []
    for _ in range(max(freq.values())):
        subarray = []
        for num in freq:
            if freq[num] > 0:
                subarray.append(num)
                freq[num] -= 1
        result.append(subarray)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 4, 1, 2, 3, 1]
    print(groupElements(nums1))  # Output: [[1, 3, 4, 2], [1, 3], [1]]

    # Test Case 2
    nums2 = [1, 1, 1, 1]
    print(groupElements(nums2))  # Output: [[1], [1], [1], [1]]

    # Test Case 3
    nums3 = [5, 5, 5, 6, 6, 7]
    print(groupElements(nums3))  # Output: [[5, 6, 7], [5, 6], [5]]

    # Test Case 4
    nums4 = [10]
    print(groupElements(nums4))  # Output: [[10]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting the frequency of elements in nums takes O(n), where n is the length of nums.
- Constructing the 2D array involves iterating over the frequency dictionary and reducing the count, which takes O(n) in total.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The frequency dictionary uses O(u) space, where u is the number of unique elements in nums.
- The result 2D array uses O(n) space in the worst case.
- Therefore, the overall space complexity is O(n).
"""

# Topic: Arrays