"""
LeetCode Problem #486: Predict the Winner

Problem Statement:
You are given an integer array `nums`. Two players are playing a game with this array: Player 1 and Player 2. 
Player 1 always goes first, and the two players take turns choosing a number from either end of the array. 
The player who has the larger sum of numbers at the end of the game wins. If the two players have the same 
sum, then Player 1 is still the winner.

You want to determine if Player 1 can win the game assuming both players play optimally.

Return `true` if Player 1 can win, or `false` otherwise.

Constraints:
- 1 <= nums.length <= 20
- 0 <= nums[i] <= 10^7
"""

def PredictTheWinner(nums):
    """
    Determines if Player 1 can win the game assuming both players play optimally.

    :param nums: List[int] - The array of integers representing the game.
    :return: bool - True if Player 1 can win, False otherwise.
    """
    def helper(start, end):
        # Base case: If there's only one number left, the player takes it.
        if start == end:
            return nums[start]
        
        # Recursive case: Choose the maximum score the current player can achieve.
        pick_start = nums[start] - helper(start + 1, end)
        pick_end = nums[end] - helper(start, end - 1)
        return max(pick_start, pick_end)
    
    # If Player 1's score is non-negative, they can win or tie.
    return helper(0, len(nums) - 1) >= 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 5, 2]
    print(PredictTheWinner(nums1))  # Output: False

    # Test Case 2
    nums2 = [1, 5, 233, 7]
    print(PredictTheWinner(nums2))  # Output: True

    # Test Case 3
    nums3 = [1, 1, 1]
    print(PredictTheWinner(nums3))  # Output: True

    # Test Case 4
    nums4 = [0]
    print(PredictTheWinner(nums4))  # Output: True

"""
Time Complexity Analysis:
- The helper function is called recursively for every possible subarray of `nums`.
- There are O(n^2) subarrays in total, and each subarray computation takes O(1) time.
- Therefore, the time complexity is O(n^2).

Space Complexity Analysis:
- The recursion depth is at most O(n), where `n` is the length of the array.
- Additionally, we use O(n^2) space for memoization (if implemented).
- Therefore, the space complexity is O(n^2).

Topic: Dynamic Programming
"""