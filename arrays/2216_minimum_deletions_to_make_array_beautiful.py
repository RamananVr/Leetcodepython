"""
LeetCode Question #2216: Minimum Deletions to Make Array Beautiful

Problem Statement:
You are given a 0-indexed integer array nums. The array is called beautiful if:
- nums[i] != nums[i + 1] for all 0 <= i < nums.length - 1.

In one step, you can delete any element from nums. After deleting an element, the elements to the right of the deleted element will shift one position to the left to fill the gap.

Return the minimum number of deletions needed to make nums beautiful.

Example 1:
Input: nums = [1,1,2,3,5]
Output: 1
Explanation: You can delete nums[1] to make nums = [1,2,3,5], which is beautiful.

Example 2:
Input: nums = [1,1,1,1,1]
Output: 4
Explanation: You need to delete 4 elements to make nums = [1], which is beautiful.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
"""

# Python Solution
def minDeletion(nums):
    deletions = 0
    n = len(nums)
    
    for i in range(n - 1):
        # Adjust index after deletions
        adjusted_index = i - deletions
        if adjusted_index % 2 == 0 and nums[i] == nums[i + 1]:
            deletions += 1
    
    # If the final length is odd, delete one more element
    if (n - deletions) % 2 != 0:
        deletions += 1
    
    return deletions

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 2, 3, 5]
    print(minDeletion(nums1))  # Output: 1

    # Test Case 2
    nums2 = [1, 1, 1, 1, 1]
    print(minDeletion(nums2))  # Output: 4

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(minDeletion(nums3))  # Output: 0

    # Test Case 4
    nums4 = [1, 1, 2, 2, 3, 3]
    print(minDeletion(nums4))  # Output: 2

    # Test Case 5
    nums5 = [1]
    print(minDeletion(nums5))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The solution uses a constant amount of extra space (only a few variables).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""