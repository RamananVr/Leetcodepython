"""
LeetCode Question #2154: Keep Multiplying Found Values by Two

Problem Statement:
You are given an integer array `nums` and an integer `original`. You need to do the following:
- If `original` is found in `nums`, multiply it by two (i.e., set `original = original * 2`).
- Repeat this process as long as `original` is found in `nums`.

Return the final value of `original`.

Example:
Input: nums = [5, 3, 6, 1, 12], original = 3
Output: 24
Explanation:
- 3 is found in nums, so multiply it by 2 to get 6.
- 6 is found in nums, so multiply it by 2 to get 12.
- 12 is found in nums, so multiply it by 2 to get 24.
- 24 is not found in nums, so return 24.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i], original <= 1000
"""

# Python Solution
def findFinalValue(nums, original):
    """
    This function takes an array of integers `nums` and an integer `original`.
    It keeps multiplying `original` by 2 as long as `original` is found in `nums`.
    Returns the final value of `original`.

    :param nums: List[int] - The input array of integers
    :param original: int - The starting integer
    :return: int - The final value of `original`
    """
    # Convert nums to a set for O(1) lookup
    num_set = set(nums)
    
    # Keep multiplying original by 2 while it's found in the set
    while original in num_set:
        original *= 2
    
    return original

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [5, 3, 6, 1, 12]
    original1 = 3
    print(findFinalValue(nums1, original1))  # Output: 24

    # Test Case 2
    nums2 = [2, 7, 9]
    original2 = 4
    print(findFinalValue(nums2, original2))  # Output: 4

    # Test Case 3
    nums3 = [1, 2, 4, 8, 16]
    original3 = 1
    print(findFinalValue(nums3, original3))  # Output: 32

    # Test Case 4
    nums4 = [10, 20, 30, 40]
    original4 = 5
    print(findFinalValue(nums4, original4))  # Output: 5

    # Test Case 5
    nums5 = [1000]
    original5 = 1000
    print(findFinalValue(nums5, original5))  # Output: 2000

# Time and Space Complexity Analysis
"""
Time Complexity:
- Converting `nums` to a set takes O(n), where n is the length of `nums`.
- The while loop runs at most log(original_final / original_initial) iterations, 
  where original_final is the final value of `original` and original_initial is the starting value.
- Each lookup in the set takes O(1).
- Overall, the time complexity is O(n + log(original_final / original_initial)).

Space Complexity:
- The space complexity is O(n) due to the set created from `nums`.
"""

# Topic: Arrays