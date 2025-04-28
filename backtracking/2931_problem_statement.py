"""
LeetCode Question #2931: Problem Statement

(Note: As of my knowledge cutoff date in October 2023, LeetCode Question #2931 does not exist. 
However, I will create a hypothetical problem statement for this question and provide a solution accordingly.)

Problem Statement:
You are given a list of integers `nums` and an integer `target`. Your task is to find all unique combinations 
in `nums` where the numbers sum up to `target`. Each number in `nums` can be used an unlimited number of times. 
The solution set must not contain duplicate combinations.

Example:
Input: nums = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]

Constraints:
1. 1 <= nums.length <= 30
2. 1 <= nums[i] <= 200
3. 1 <= target <= 500
"""

# Solution
from typing import List

def combinationSum(nums: List[int], target: int) -> List[List[int]]:
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start, len(nums)):
            if nums[i] <= target:
                path.append(nums[i])
                backtrack(i, target - nums[i], path)
                path.pop()

    result = []
    nums.sort()  # Sorting helps avoid duplicates and optimizes the search
    backtrack(0, target, [])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [2, 3, 6, 7]
    target = 7
    print(combinationSum(nums, target))  # Expected Output: [[2, 2, 3], [7]]

    # Test Case 2
    nums = [2, 3, 5]
    target = 8
    print(combinationSum(nums, target))  # Expected Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    # Test Case 3
    nums = [1]
    target = 2
    print(combinationSum(nums, target))  # Expected Output: [[1, 1]]

    # Test Case 4
    nums = [4, 2, 8]
    target = 8
    print(combinationSum(nums, target))  # Expected Output: [[4, 4], [2, 2, 2, 2], [8]]

# Time and Space Complexity Analysis
"""
Time Complexity:
The time complexity of this solution is O(2^T), where T is the target value. This is because, in the worst case, 
we explore all possible combinations of numbers that sum up to the target. Sorting the array takes O(N log N), 
where N is the length of the input array.

Space Complexity:
The space complexity is O(T), where T is the target value. This is due to the recursion stack and the space 
used to store the current combination path.
"""

# Topic: Backtracking