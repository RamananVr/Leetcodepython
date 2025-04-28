"""
LeetCode Problem #2229: Check if an Array is Consecutive

Problem Statement:
Given an integer array `nums`, return `true` if the array contains consecutive integers with no duplicates. 
Otherwise, return `false`.

An array is considered consecutive if it contains every number in the range `[min(nums), max(nums)]` (inclusive) 
and each number appears exactly once.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

def isConsecutive(nums):
    """
    Function to check if the array contains consecutive integers with no duplicates.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    bool: True if the array is consecutive, False otherwise.
    """
    # A set is used to remove duplicates and check for consecutive numbers
    nums_set = set(nums)
    return len(nums_set) == len(nums) and max(nums) - min(nums) + 1 == len(nums)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Consecutive numbers
    nums1 = [4, 2, 3, 5]
    print(isConsecutive(nums1))  # Expected output: True

    # Test Case 2: Non-consecutive numbers
    nums2 = [1, 3, 5, 7]
    print(isConsecutive(nums2))  # Expected output: False

    # Test Case 3: Duplicate numbers
    nums3 = [1, 2, 2, 3]
    print(isConsecutive(nums3))  # Expected output: False

    # Test Case 4: Single element
    nums4 = [10]
    print(isConsecutive(nums4))  # Expected output: True

    # Test Case 5: Negative numbers
    nums5 = [-3, -2, -1, 0]
    print(isConsecutive(nums5))  # Expected output: True

    # Test Case 6: Large range with missing numbers
    nums6 = [1000000000, 999999999, 999999998]
    print(isConsecutive(nums6))  # Expected output: True

    # Test Case 7: Large range with duplicates
    nums7 = [1000000000, 999999999, 999999999]
    print(isConsecutive(nums7))  # Expected output: False

"""
Time Complexity Analysis:
- The function uses the `set` data structure to remove duplicates, which takes O(n) time.
- Calculating `min(nums)` and `max(nums)` also takes O(n) time.
- Overall, the time complexity is O(n).

Space Complexity Analysis:
- The function uses a set to store the unique elements of the array, which requires O(n) space in the worst case.
- Overall, the space complexity is O(n).

Topic: Arrays
"""