"""
LeetCode Problem #1535: Find the Winner of an Array Game

Problem Statement:
Given an integer array `arr` of distinct integers and an integer `k`.

A game will be played between the first two elements of the array (arr[0] and arr[1]). In each round of the game, we compare `arr[0]` with `arr[1]`, the larger integer wins, and the winner remains at the first position of the array. The loser moves to the end of the array. The game ends when an integer wins `k` consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game within 10^7 rounds for the given constraints.

Constraints:
- 2 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^6
- arr contains distinct integers.
- 1 <= k <= arr.length
"""

# Python Solution
def getWinner(arr, k):
    """
    Function to find the winner of the array game.
    
    :param arr: List[int] - The array of distinct integers.
    :param k: int - The number of consecutive wins required to end the game.
    :return: int - The integer that wins the game.
    """
    current_winner = arr[0]
    consecutive_wins = 0

    for i in range(1, len(arr)):
        if arr[i] > current_winner:
            current_winner = arr[i]
            consecutive_wins = 1
        else:
            consecutive_wins += 1

        if consecutive_wins == k:
            return current_winner

    # If no winner is found after iterating through the array, the largest element is the winner
    return current_winner


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [2, 1, 3, 5, 4, 6, 7]
    k1 = 2
    print(getWinner(arr1, k1))  # Expected Output: 5

    # Test Case 2
    arr2 = [3, 2, 1]
    k2 = 10
    print(getWinner(arr2, k2))  # Expected Output: 3

    # Test Case 3
    arr3 = [1, 9, 8, 2, 3, 7, 6, 4, 5]
    k3 = 7
    print(getWinner(arr3, k3))  # Expected Output: 9

    # Test Case 4
    arr4 = [1, 11, 22, 33, 44, 55, 66, 77, 88, 99]
    k4 = 100
    print(getWinner(arr4, k4))  # Expected Output: 99


# Time and Space Complexity Analysis
"""
Time Complexity:
- The loop iterates through the array at most once, and each comparison takes O(1) time.
- In the worst case, the loop runs for all elements in the array, so the time complexity is O(n), 
  where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space (variables `current_winner` and `consecutive_wins`).
- Therefore, the space complexity is O(1).
"""

# Topic: Arrays