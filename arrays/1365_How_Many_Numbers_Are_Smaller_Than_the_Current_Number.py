"""
LeetCode Problem #1365: How Many Numbers Are Smaller Than the Current Number

Problem Statement:
Given the array `nums`, for each `nums[i]` find out how many numbers in the array are smaller than it. 
That is, for each `nums[i]` you have to count the number of valid `j`s such that `j != i` and `nums[j] < nums[i]`.

Return the answer in an array.

Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2, and 3). 
For nums[1]=1 no number is smaller than it.
For nums[2]=2 there is one smaller number than it (1). 
For nums[3]=2 there is one smaller number than it (1). 
For nums[4]=3 there are three smaller numbers than it (1, 2, and 2).

Example 2:
Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:
Input: nums = [7,7,7,7]
Output: [0,0,0,0]

Constraints:
- 2 <= nums.length <= 500
- 0 <= nums[i] <= 100
"""

# Python Solution
def smallerNumbersThanCurrent(nums):
    """
    This function returns an array where each element at index i represents
    the count of numbers in the input array that are smaller than nums[i].
    """
    # Create a sorted version of the array
    sorted_nums = sorted(nums)
    
    # Create a dictionary to store the rank (number of smaller elements) for each number
    rank = {}
    for i, num in enumerate(sorted_nums):
        # Only assign the rank if the number is not already in the dictionary
        if num not in rank:
            rank[num] = i
    
    # Use the rank dictionary to build the result array
    return [rank[num] for num in nums]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [8, 1, 2, 2, 3]
    print(smallerNumbersThanCurrent(nums1))  # Output: [4, 0, 1, 1, 3]

    # Test Case 2
    nums2 = [6, 5, 4, 8]
    print(smallerNumbersThanCurrent(nums2))  # Output: [2, 1, 0, 3]

    # Test Case 3
    nums3 = [7, 7, 7, 7]
    print(smallerNumbersThanCurrent(nums3))  # Output: [0, 0, 0, 0]

    # Test Case 4
    nums4 = [10, 20, 10, 30]
    print(smallerNumbersThanCurrent(nums4))  # Output: [0, 2, 0, 3]

    # Test Case 5
    nums5 = [0, 0, 0, 0]
    print(smallerNumbersThanCurrent(nums5))  # Output: [0, 0, 0, 0]

# Time Complexity Analysis:
# Sorting the array takes O(n log n), where n is the length of the input array.
# Creating the rank dictionary takes O(n) in the worst case.
# Building the result array also takes O(n).
# Overall time complexity: O(n log n).

# Space Complexity Analysis:
# The space complexity is O(n) due to the sorted array and the rank dictionary.
# Overall space complexity: O(n).

# Topic: Arrays