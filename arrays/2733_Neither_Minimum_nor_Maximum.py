"""
LeetCode Problem #2733: Neither Minimum nor Maximum

Problem Statement:
You are given a 0-indexed integer array nums containing distinct numbers. 
You need to find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if no such number exists.

Example 1:
Input: nums = [3, 1, 2]
Output: 2
Explanation: The minimum value is 1, the maximum value is 3, and either 2 is neither.

Example 2:
Input: nums = [1, 2]
Output: -1
Explanation: Since there are only two numbers, there is no number that is neither minimum nor maximum.

Example 3:
Input: nums = [2, 1, 3]
Output: 2
Explanation: The minimum value is 1, the maximum value is 3, and either 2 is neither.

Constraints:
- 3 <= nums.length <= 100
- 1 <= nums[i] <= 100
- All elements in nums are distinct.
"""

def findNonMinOrMax(nums):
    """
    Function to find any number in the array that is neither the minimum nor the maximum.
    If no such number exists, return -1.

    :param nums: List[int] - A list of distinct integers
    :return: int - A number that is neither the minimum nor the maximum, or -1
    """
    if len(nums) < 3:
        return -1

    # Find the minimum and maximum values
    min_val = min(nums)
    max_val = max(nums)

    # Return the first number that is neither minimum nor maximum
    for num in nums:
        if num != min_val and num != max_val:
            return num

    return -1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 1, 2]
    print(findNonMinOrMax(nums1))  # Output: 2

    # Test Case 2
    nums2 = [1, 2]
    print(findNonMinOrMax(nums2))  # Output: -1

    # Test Case 3
    nums3 = [2, 1, 3]
    print(findNonMinOrMax(nums3))  # Output: 2

    # Test Case 4
    nums4 = [10, 20, 30, 40, 50]
    print(findNonMinOrMax(nums4))  # Output: 20 (or any other valid number)

    # Test Case 5
    nums5 = [5, 1, 9, 3, 7]
    print(findNonMinOrMax(nums5))  # Output: 5 (or any other valid number)


"""
Time Complexity Analysis:
- Finding the minimum and maximum values in the array takes O(n) time.
- Iterating through the array to find a number that is neither minimum nor maximum also takes O(n) time.
- Therefore, the overall time complexity is O(n).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""