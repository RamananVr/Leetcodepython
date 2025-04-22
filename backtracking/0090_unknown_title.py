"""
LeetCode Problem #90: Subsets II

Problem Statement:
Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
"""

def subsetsWithDup(nums):
    """
    Generate all unique subsets of the given list of numbers, including duplicates.

    :param nums: List[int] - The input list of integers, which may contain duplicates.
    :return: List[List[int]] - A list of all unique subsets.
    """
    def backtrack(start, path):
        # Add the current subset to the result
        result.append(path[:])
        
        # Iterate through the numbers starting from the current index
        for i in range(start, len(nums)):
            # Skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue
            # Include nums[i] in the current subset and recurse
            path.append(nums[i])
            backtrack(i + 1, path)
            # Backtrack by removing the last element
            path.pop()
    
    # Sort the input to handle duplicates
    nums.sort()
    result = []
    backtrack(0, [])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 2]
    print("Input:", nums1)
    print("Output:", subsetsWithDup(nums1))
    # Expected Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

    # Test Case 2
    nums2 = [0]
    print("Input:", nums2)
    print("Output:", subsetsWithDup(nums2))
    # Expected Output: [[], [0]]

    # Test Case 3
    nums3 = [4, 4, 4, 1, 4]
    print("Input:", nums3)
    print("Output:", subsetsWithDup(nums3))
    # Expected Output: [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]

"""
Time Complexity:
- Sorting the input array takes O(n log n), where n is the length of the input array.
- The backtracking algorithm generates all subsets, which is O(2^n) in the worst case.
- For each subset, we spend O(n) time copying elements to the result.
- Overall time complexity: O(n log n + n * 2^n).

Space Complexity:
- The recursion stack can go as deep as O(n) in the worst case.
- The result list stores all subsets, which can be O(2^n) in size.
- Overall space complexity: O(n + 2^n).

Topic: Backtracking
"""