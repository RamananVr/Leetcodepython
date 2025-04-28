"""
LeetCode Problem #2567: Minimum Score by Changing Two Elements

Problem Statement:
You are given a 0-indexed integer array nums.

- The score of nums is the difference between the maximum and minimum elements in nums.
- The score of an array of size 1 is 0.

You can change two elements of nums to any value you want (possibly the same value).

Return the minimum possible score after changing two elements.

Constraints:
- 2 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

def minimizeScore(nums):
    """
    Function to calculate the minimum possible score after changing two elements in the array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The minimum possible score.
    """
    # If the array has only two elements, the score is always 0 after changing both elements.
    if len(nums) <= 3:
        return 0

    # Sort the array to easily access the smallest and largest elements.
    nums.sort()

    # Consider the following cases:
    # 1. Change the two largest elements to the value of the third largest element.
    # 2. Change the two smallest elements to the value of the third smallest element.
    # 3. Change the largest and smallest elements to values close to the second largest and second smallest elements.
    # 4. Change the largest and second largest elements to values close to the smallest and second smallest elements.

    # Calculate the minimum score for all these cases.
    return min(
        nums[-1] - nums[2],  # Change the two smallest elements
        nums[-3] - nums[0]   # Change the two largest elements