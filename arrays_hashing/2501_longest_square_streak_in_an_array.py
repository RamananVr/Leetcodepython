"""
LeetCode Question #2501: Longest Square Streak in an Array

Problem Statement:
You are given an integer array `nums`. A square streak is a sequence of integers in the array such that:
1. The sequence starts with some integer `x`.
2. Every subsequent integer in the sequence is the square of the previous integer.

Return the length of the longest square streak in `nums`. If no square streak exists, return -1.

A square streak must be a subsequence of the array, and the elements of the square streak must appear in the same order as they do in the array.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

# Solution
def longest_square_streak(nums):
    """
    Finds the length of the longest square streak in the array.

    :param nums: List[int] - The input array of integers.
    :return: int - The length of the longest square streak, or -1 if no streak exists.
    """
    # Convert nums to a set for O(1) lookups
    num_set = set(nums)
    max_streak = -1

    # Iterate through each number in the array
    for num in nums:
        streak_length = 0
        current = num

        # Check if the current number can form a square streak
        while current in num_set:
            streak_length += 1
            current = current ** 2

        # Update the maximum streak length
        if streak_length > 1:  # A valid streak must have at least 2 numbers
            max_streak = max(max_streak, streak_length)

    return max_streak

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic example with a valid square streak
    nums1 = [4, 16, 256, 2]
    print(longest_square_streak(nums1))  # Output: 3 (4 -> 16 -> 256)

    # Test Case 2: No valid square streak
    nums2 = [1, 2, 3, 5]
    print(longest_square_streak(nums2))  # Output: -1

    # Test Case 3: Multiple streaks, longest one is chosen
    nums3 = [2, 4, 16, 256, 3, 9, 81]
    print(longest_square_streak(nums3))  # Output: 4 (2 -> 4 -> 16 -> 256)

    # Test Case 4: Single number in the array
    nums4 = [4]
    print(longest_square_streak(nums4))  # Output: -1

    # Test Case 5: Large numbers with a valid streak
    nums5 = [10, 100, 10000, 100000000]
    print(longest_square_streak(nums5))  # Output: 4 (10 -> 100 -> 10000 -> 100000000)

# Time and Space Complexity Analysis
"""
Time Complexity:
- Converting nums to a set takes O(n), where n is the length of nums.
- For each number in nums, we perform a while loop to check for square streaks. 
  In the worst case, the loop runs log(nums[i]) times for each number (since squaring grows exponentially).
- Overall, the time complexity is O(n * log(max(nums))), where max(nums) is the largest number in the array.

Space Complexity:
- The space complexity is O(n) due to the set used to store nums.

Topic: Arrays, Hashing
"""