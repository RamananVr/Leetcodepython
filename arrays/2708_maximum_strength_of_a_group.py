"""
LeetCode Question #2708: Maximum Strength of a Group

Problem Statement:
You are given a 0-indexed integer array nums representing the strength of some group members. 
The strength of a group is defined as the product of all the numbers in the group. 
Return the maximum strength of a group.

A group can be formed by choosing any subset of the array nums. 
If the group is empty, the strength is considered to be 0.

Example 1:
Input: nums = [3, -1, -5, 2, 5, -9]
Output: 1350
Explanation: One of the optimal subsets is [3, -5, 2, 5, -9]. The product is 3 * (-5) * 2 * 5 * (-9) = 1350.

Example 2:
Input: nums = [-4, -5, -6]
Output: 30
Explanation: One of the optimal subsets is [-4, -5]. The product is (-4) * (-5) = 20. Note that [-4, -5, -6] is also an optimal subset.

Constraints:
- 1 <= nums.length <= 13
- -9 <= nums[i] <= 9
"""

# Python Solution
from functools import reduce

def maxStrength(nums):
    # Separate positive, negative, and zero values
    positives = [x for x in nums if x > 0]
    negatives = [x for x in nums if x < 0]
    zeros = [x for x in nums if x == 0]

    # Sort negatives to pair them optimally
    negatives.sort()

    # If there are an odd number of negatives, remove the smallest one
    if len(negatives) % 2 != 0:
        negatives.pop()

    # Combine positives and paired negatives
    combined = positives + negatives

    # If the combined list is empty, return 0 (empty subset strength)
    if not combined:
        return 0

    # Calculate the product of the combined list
    return reduce(lambda x, y: x * y, combined)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, -1, -5, 2, 5, -9]
    print(maxStrength(nums1))  # Output: 1350

    # Test Case 2
    nums2 = [-4, -5, -6]
    print(maxStrength(nums2))  # Output: 30

    # Test Case 3
    nums3 = [0, 0, 0]
    print(maxStrength(nums3))  # Output: 0

    # Test Case 4
    nums4 = [1, 2, 3, 4]
    print(maxStrength(nums4))  # Output: 24

    # Test Case 5
    nums5 = [-1, -2, -3, -4, -5]
    print(maxStrength(nums5))  # Output: 120

"""
Time and Space Complexity Analysis:

Time Complexity:
- Separating positives, negatives, and zeros: O(n), where n is the length of nums.
- Sorting the negatives: O(n log n).
- Calculating the product of the combined list: O(k), where k is the size of the combined list.
Overall: O(n log n).

Space Complexity:
- Storing positives, negatives, and zeros: O(n).
- Combined list storage: O(n).
Overall: O(n).

Topic: Arrays
"""