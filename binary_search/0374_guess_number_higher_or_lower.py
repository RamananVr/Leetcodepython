"""
LeetCode Question #374: Guess Number Higher or Lower

Problem Statement:
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API `guess(int num)` which returns three possible results:
- -1: Your guess is higher than the number I picked (i.e., num > pick).
- 1: Your guess is lower than the number I picked (i.e., num < pick).
- 0: Your guess is equal to the number I picked (i.e., num == pick).

Write a function `guessNumber(n)` that returns the number I picked.

Constraints:
- 1 <= n <= 2^31 - 1
- 1 <= pick <= n
"""

# Clean and Correct Python Solution
def guessNumber(n: int) -> int:
    """
    This function uses binary search to efficiently find the number picked.
    """
    low, high = 1, n
    while low <= high:
        mid = low + (high - low) // 2
        result = guess(mid)
        if result == 0:
            return mid  # Found the number
        elif result == -1:
            high = mid - 1  # The picked number is lower
        else:
            low = mid + 1  # The picked number is higher
    return -1  # This line should never be reached

# Example Test Cases
# Note: The `guess` API is not implemented here. To test this function, you need to mock the `guess` API.
def guess(num: int) -> int:
    """
    Mock implementation of the guess API for testing purposes.
    Replace `pick` with the number you want to test against.
    """
    pick = 6  # Example: The number picked is 6
    if num < pick:
        return 1
    elif num > pick:
        return -1
    else:
        return 0

if __name__ == "__main__":
    # Test Case 1
    n = 10
    print(f"Test Case 1: n = {n}, pick = 6 -> Output: {guessNumber(n)}")  # Expected: 6

    # Test Case 2
    n = 1
    print(f"Test Case 2: n = {n}, pick = 1 -> Output: {guessNumber(n)}")  # Expected: 1

    # Test Case 3
    n = 100
    print(f"Test Case 3: n = {n}, pick = 50 -> Output: {guessNumber(n)}")  # Expected: 50

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm uses binary search, which has a time complexity of O(log n), where n is the input range.

Space Complexity:
- The algorithm uses constant space, so the space complexity is O(1).
"""

# Topic: Binary Search