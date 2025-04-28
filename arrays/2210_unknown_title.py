"""
LeetCode Problem #2210: Count Hills and Valleys in an Array

Problem Statement:
You are given a 0-indexed integer array `nums`. An index `i` is part of a hill in `nums` if the closest non-equal neighbors of `nums[i]` are smaller than `nums[i]`. Similarly, an index `i` is part of a valley in `nums` if the closest non-equal neighbors of `nums[i]` are larger than `nums[i]`. 

An index `i` is neither a hill nor a valley if `nums[i]` is equal to at least one of its closest non-equal neighbors.

Return the number of hills and valleys in `nums`.

Example 1:
Input: nums = [2,4,1,1,6,5]
Output: 3
Explanation:
- Index 1 forms a hill because nums[0] < nums[1] > nums[4].
- Index 4 forms a hill because nums[1] < nums[4] > nums[5].
- Index 5 forms a valley because nums[4] > nums[5] < nums[6] (out of bounds is treated as infinity).
There are 3 hills and valleys, so we return 3.

Example 2:
Input: nums = [6,6,5,5,4,1]
Output: 0
Explanation:
There are no hills or valleys in nums.

Constraints:
- 3 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

def countHillValley(nums):
    """
    Function to count the number of hills and valleys in the array.

    :param nums: List[int] - The input array of integers.
    :return: int - The number of hills and valleys in the array.
    """
    # Remove consecutive duplicates to simplify the problem
    filtered_nums = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            filtered_nums.append(nums[i])
    
    # Count hills and valleys
    count = 0
    for i in range(1, len(filtered_nums) - 1):
        if filtered_nums[i - 1] < filtered_nums[i] > filtered_nums[i + 1]:
            count += 1  # Hill
        elif filtered_nums[i - 1] > filtered_nums[i] < filtered_nums[i + 1]:
            count += 1  # Valley
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 4, 1, 1, 6, 5]
    print(f"Test Case 1: {countHillValley(nums1)}")  # Expected Output: 3

    # Test Case 2
    nums2 = [6, 6, 5, 5, 4, 1]
    print(f"Test Case 2: {countHillValley(nums2)}")  # Expected Output: 0

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(f"Test Case 3: {countHillValley(nums3)}")  # Expected Output: 0

    # Test Case 4
    nums4 = [5, 3, 5, 3, 5]
    print(f"Test Case 4: {countHillValley(nums4)}")  # Expected Output: 4

    # Test Case 5
    nums5 = [1, 2, 2, 3, 2, 2, 1]
    print(f"Test Case 5: {countHillValley(nums5)}")  # Expected Output: 2

"""
Time Complexity Analysis:
- Filtering the array to remove consecutive duplicates takes O(n), where n is the length of the input array.
- Counting hills and valleys involves a single pass through the filtered array, which also takes O(n) in the worst case.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The filtered array requires additional space proportional to the size of the input array in the worst case.
- Overall space complexity: O(n).

Topic: Arrays
"""