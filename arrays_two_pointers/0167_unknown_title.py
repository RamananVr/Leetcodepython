"""
LeetCode Problem #167: Two Sum II - Input Array Is Sorted

Problem Statement:
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers be 
`numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, as an integer array `[index1, index2]` 
of length 2.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore, index1 = 1, index2 = 3.

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore, index1 = 1, index2 = 2.

Constraints:
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution.
"""

# Clean, Correct Python Solution
def twoSum(numbers, target):
    """
    Finds two numbers in a sorted array that add up to the target and returns their 1-based indices.

    :param numbers: List[int] - A sorted list of integers.
    :param target: int - The target sum.
    :return: List[int] - A list containing the 1-based indices of the two numbers.
    """
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # Return 1-based indices
        elif current_sum < target:
            left += 1  # Move the left pointer to increase the sum
        else:
            right -= 1  # Move the right pointer to decrease the sum

    # The problem guarantees exactly one solution, so we should never reach here.
    raise ValueError("No solution exists for the given input.")

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    numbers = [2, 7, 11, 15]
    target = 9
    print(twoSum(numbers, target))  # Output: [1, 2]

    # Test Case 2
    numbers = [2, 3, 4]
    target = 6
    print(twoSum(numbers, target))  # Output: [1, 3]

    # Test Case 3
    numbers = [-1, 0]
    target = -1
    print(twoSum(numbers, target))  # Output: [1, 2]

    # Test Case 4
    numbers = [1, 2, 3, 4, 4, 9, 56, 90]
    target = 8
    print(twoSum(numbers, target))  # Output: [4, 5]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm uses a two-pointer approach, where each pointer moves at most `n` steps in total.
- Therefore, the time complexity is O(n), where `n` is the length of the input array.

Space Complexity:
- The algorithm uses a constant amount of extra space, as it only maintains two pointers and a few variables.
- Therefore, the space complexity is O(1).
"""

# Topic: Arrays, Two Pointers