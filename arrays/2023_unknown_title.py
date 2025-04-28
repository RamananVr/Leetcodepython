"""
LeetCode Problem #2023: Number of Pairs of Strings With Concatenation Equal to Target

Problem Statement:
Given an array of strings `nums` and a string `target`, return the number of pairs `(i, j)` 
such that `i != j` and the concatenation of `nums[i] + nums[j]` equals `target`.

Example:
Input: nums = ["a", "b", "ab"], target = "ab"
Output: 2
Explanation: The pairs are:
- (0, 1): "a" + "b" = "ab"
- (1, 0): "b" + "a" = "ab"

Constraints:
- 2 <= nums.length <= 100
- 1 <= nums[i].length, target.length <= 100
- nums[i] and target consist of lowercase English letters.
"""

# Python Solution
def numOfPairs(nums, target):
    """
    Function to calculate the number of pairs of strings in nums whose concatenation equals target.

    :param nums: List[str] - List of strings
    :param target: str - Target string
    :return: int - Number of valid pairs
    """
    count = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(n):
            if i != j and nums[i] + nums[j] == target:
                count += 1
                
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = ["a", "b", "ab"]
    target1 = "ab"
    print(numOfPairs(nums1, target1))  # Output: 2

    # Test Case 2
    nums2 = ["abc", "def", "abcd", "ef"]
    target2 = "abcdef"
    print(numOfPairs(nums2, target2))  # Output: 1

    # Test Case 3
    nums3 = ["x", "y", "xy", "yx"]
    target3 = "xy"
    print(numOfPairs(nums3, target3))  # Output: 2

    # Test Case 4
    nums4 = ["a", "a", "a"]
    target4 = "aa"
    print(numOfPairs(nums4, target4))  # Output: 6

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function uses two nested loops to iterate over all pairs of indices in nums.
- For a list of size n, this results in O(n^2) time complexity.

Space Complexity:
- The function uses a constant amount of extra space, so the space complexity is O(1).

Overall:
- Time Complexity: O(n^2)
- Space Complexity: O(1)
"""

# Topic: Arrays