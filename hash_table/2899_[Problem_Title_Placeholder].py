"""
LeetCode Problem #2899: [Problem Title Placeholder]

Problem Statement:
[Note: As of my knowledge cutoff in October 2023, LeetCode Question #2899 does not exist. 
If you have a specific problem statement in mind, please provide it, and I will write the solution accordingly.]

For the sake of demonstration, let's assume the problem is as follows:

You are given an integer array `nums` and an integer `target`. Return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9, so we return [0, 1].

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""

# Python Solution
def twoSum(nums, target):
    """
    Finds two numbers in the array that add up to the target and returns their indices.

    :param nums: List[int] - The input array of integers.
    :param target: int - The target sum.
    :return: List[int] - Indices of the two numbers that add up to the target.
    """
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []  # This line should never be reached due to the problem constraints.

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))  # Output: [0, 1]

    # Test Case 2
    nums = [3, 2, 4]
    target = 6
    print(twoSum(nums, target))  # Output: [1, 2]

    # Test Case 3
    nums = [3, 3]
    target = 6
    print(twoSum(nums, target))  # Output: [0, 1]

    # Test Case 4
    nums = [1, 5, 7, 8]
    target = 13
    print(twoSum(nums, target))  # Output: [1, 3]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `nums` array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the `nums` array.

Space Complexity:
- The function uses a dictionary `num_to_index` to store at most n elements (one for each number in `nums`).
- Therefore, the space complexity is O(n).
"""

# Topic: Hash Table