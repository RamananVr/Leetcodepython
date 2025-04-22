"""
LeetCode Problem #747: Largest Number At Least Twice of Others

Problem Statement:
You are given an integer array `nums` where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. 
If it is, return the index of the largest element, or return -1 otherwise.

Example 1:
Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is at least twice as big as x. The index of value 6 is 1, so we return 1.

Example 2:
Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 is the largest number, but 4 is not at least twice as big as 3, so we return -1.

Example 3:
Input: nums = [1]
Output: 0
Explanation: 1 is trivially at least twice the value as any other number because there are no other numbers.

Constraints:
- 1 <= nums.length <= 50
- 0 <= nums[i] <= 100
- The largest element in nums is unique.
"""

def dominantIndex(nums):
    """
    Function to find the index of the largest number if it is at least twice as large as all other numbers.
    Otherwise, return -1.
    
    :param nums: List[int] - The input array of integers
    :return: int - The index of the largest number or -1
    """
    if len(nums) == 1:
        return 0  # If there's only one number, it is trivially the largest and satisfies the condition.

    # Find the largest and second largest numbers in the array
    max_num = max(nums)
    max_index = nums.index(max_num)
    
    # Check if the largest number is at least twice as large as all other numbers
    for num in nums:
        if num != max_num and max_num < 2 * num:
            return -1
    
    return max_index

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 6, 1, 0]
    print(dominantIndex(nums1))  # Output: 1

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print(dominantIndex(nums2))  # Output: -1

    # Test Case 3
    nums3 = [1]
    print(dominantIndex(nums3))  # Output: 0

    # Test Case 4
    nums4 = [0, 0, 3, 6]
    print(dominantIndex(nums4))  # Output: 3

    # Test Case 5
    nums5 = [10, 5, 2, 1]
    print(dominantIndex(nums5))  # Output: 0

"""
Time Complexity Analysis:
- Finding the maximum number in the array takes O(n) time.
- Checking if the largest number is at least twice as large as all other numbers also takes O(n) time.
- Therefore, the overall time complexity is O(n).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""