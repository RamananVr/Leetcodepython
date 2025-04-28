"""
LeetCode Problem #2656: Maximum Sum With Exactly K Elements

Problem Statement:
You are given a 0-indexed integer array `nums` and an integer `k`. Your task is to perform the following operation exactly `k` times in order to maximize your score:
- Pick the largest element in `nums` and add it to your score.
- Replace the picked element with `nums[i] + 1`.

Return the maximum score you can achieve after performing the operation exactly `k` times.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
- 1 <= k <= 1000
"""

# Solution
def maximizeSum(nums, k):
    """
    Function to calculate the maximum sum with exactly k operations.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The number of operations to perform.

    Returns:
    int: The maximum score achievable after k operations.
    """
    # Find the largest element in the array
    max_element = max(nums)
    
    # Calculate the sum of the largest element incremented k times
    # Using the formula for the sum of an arithmetic progression
    return k * max_element + k * (k - 1) // 2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [1, 2, 3, 4, 5]
    k = 3
    print(maximizeSum(nums, k))  # Expected Output: 18

    # Test Case 2
    nums = [5, 5, 5]
    k = 2
    print(maximizeSum(nums, k))  # Expected Output: 11

    # Test Case 3
    nums = [10, 20, 30]
    k = 4
    print(maximizeSum(nums, k))  # Expected Output: 134

    # Test Case 4
    nums = [1]
    k = 5
    print(maximizeSum(nums, k))  # Expected Output: 20

"""
Time and Space Complexity Analysis:

Time Complexity:
- Finding the maximum element in the array takes O(n), where n is the length of `nums`.
- The rest of the operations (arithmetic calculations) are O(1).
- Overall time complexity: O(n).

Space Complexity:
- The function uses a constant amount of extra space.
- Overall space complexity: O(1).

Topic: Arrays
"""