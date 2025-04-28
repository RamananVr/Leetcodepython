"""
LeetCode Problem #448: Find All Numbers Disappeared in an Array

Problem Statement:
Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, 
return an array of all the integers in the range `[1, n]` that do not appear in `nums`.

Example:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Constraints:
- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`

Follow up:
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""

# Python Solution
def findDisappearedNumbers(nums):
    """
    Finds all numbers in the range [1, n] that do not appear in the input array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    List[int]: A list of integers that are missing from the range [1, n].
    """
    # Mark numbers as visited by negating the value at the corresponding index
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    
    # Collect all indices that are still positive (unvisited)
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
    print("Input:", nums1)
    print("Output:", findDisappearedNumbers(nums1))  # Expected: [5, 6]

    # Test Case 2
    nums2 = [1, 1]
    print("Input:", nums2)
    print("Output:", findDisappearedNumbers(nums2))  # Expected: [2]

    # Test Case 3
    nums3 = [2, 2]
    print("Input:", nums3)
    print("Output:", findDisappearedNumbers(nums3))  # Expected: [1]

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    print("Input:", nums4)
    print("Output:", findDisappearedNumbers(nums4))  # Expected: []

    # Test Case 5
    nums5 = [10, 2, 5, 10, 9, 1, 1, 4, 3, 7]
    print("Input:", nums5)
    print("Output:", findDisappearedNumbers(nums5))  # Expected: [6, 8]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array twice:
  1. Once to mark the visited indices (O(n)).
  2. Once to collect the missing numbers (O(n)).
- Overall time complexity: O(n).

Space Complexity:
- The algorithm modifies the input array in place and uses no additional data structures.
- The output list is not considered extra space as per the problem's follow-up requirement.
- Overall space complexity: O(1).
"""

# Topic: Arrays