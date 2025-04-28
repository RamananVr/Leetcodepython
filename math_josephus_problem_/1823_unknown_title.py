"""
LeetCode Problem #1823: Find the Winner of the Circular Game

Problem Statement:
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. 
More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from 
the nth friend brings you to the 1st friend.

The rules of the game are as follows:
1. Start at the 1st friend.
2. Count the next k friends in the clockwise direction, including the friend you started at. The counting wraps around the circle 
   and may count some friends more than once.
3. The last friend you counted leaves the circle and loses the game.
4. If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the 
   friend who just lost and repeat.
5. Else, the last friend in the circle wins the game.

Given the number of friends, n, and an integer k, return the winner of the game.

Example 1:
Input: n = 5, k = 2
Output: 3
Explanation: Here is a step-by-step explanation of what happens during the game:
1. Start at friend 1. Count 2 friends clockwise, which are friends 1 and 2. Friend 2 leaves the circle. Next start is friend 3.
2. Start at friend 3. Count 2 friends clockwise, which are friends 3 and 4. Friend 4 leaves the circle. Next start is friend 5.
3. Start at friend 5. Count 2 friends clockwise, which are friends 5 and 1. Friend 1 leaves the circle. Next start is friend 3.
4. Start at friend 3. Count 2 friends clockwise, which are friends 3 and 5. Friend 5 leaves the circle. Friend 3 is the only one 
   remaining, so they are the winner.

Example 2:
Input: n = 6, k = 5
Output: 1

Constraints:
- 1 <= k <= n <= 500

Follow up:
Could you solve this problem in linear time with constant space?

"""

# Solution
def findTheWinner(n: int, k: int) -> int:
    # Using the Josephus problem formula
    winner = 0  # Base case: when there's only one person, they are the winner
    for i in range(2, n + 1):
        winner = (winner + k) % i
    return winner + 1  # Convert 0-based index to 1-based index

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, k1 = 5, 2
    print(findTheWinner(n1, k1))  # Expected Output: 3

    # Test Case 2
    n2, k2 = 6, 5
    print(findTheWinner(n2, k2))  # Expected Output: 1

    # Test Case 3
    n3, k3 = 1, 1
    print(findTheWinner(n3, k3))  # Expected Output: 1

    # Test Case 4
    n4, k4 = 10, 3
    print(findTheWinner(n4, k4))  # Expected Output: 4

    # Test Case 5
    n5, k5 = 7, 7
    print(findTheWinner(n5, k5))  # Expected Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution iterates from 2 to n, performing a constant-time operation (modulus and addition) in each iteration.
- Therefore, the time complexity is O(n).

Space Complexity:
- The solution uses only a constant amount of extra space (a single variable `winner`).
- Therefore, the space complexity is O(1).

Topic: Math (Josephus Problem)
"""